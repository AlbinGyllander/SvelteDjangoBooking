from distutils.log import error
import json
from django.contrib.auth import get_user_model
import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

@require_POST
def login_view(request):
    data = json.loads(request.body)
    print(data)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

        
    user = authenticate(username=username, password=password)
    print(user)
    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

    login(request, user)
    return JsonResponse({'detail': 'Successfully logged in.'})


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})

@require_POST
def registration_view(request):
    data = json.loads(request.body)
    username = str(data.get('username'))
    email = str(data.get('email'))
    password = str(data.get('password'))
    passwordRepeat =str( data.get('passwordRepeat'))
    firstName = str(data.get('firstName'))
    lastName = str(data.get('lastName'))
    tennisClub = str(data.get('tennisClub'))
    experience = str(data.get('experience'))
    errorFieldList =[] 



    if len(username) == 0 :
        errorFieldList.append('usernameIsInvalid')

    validUsernameChars = "/^[A-Za-z0-9_]*$/"
    if  bool(re.match(validUsernameChars,username)) == True:
        errorFieldList.append('InvalidUsernameChars')

    if len(password) == 0 :
        errorFieldList.append('password')
   
    if len(passwordRepeat) == 0:
        errorFieldList.append('passwordRepeat')
   
    if len(email) == 0:
        errorFieldList.append('emailIsNotValid')

    if User.objects.filter(username=username).exists():
        errorFieldList.append('usernameAlreadyExists') 
    
    if User.objects.filter(email=email).exists():
        errorFieldList.append('emailAlreadyExists') 
   
    try:
        validate_email(email)
    except ValidationError as e:
        errorFieldList.append('emailIsNotValid') 
    
    if password != passwordRepeat:
        errorFieldList.append('passwordRepeat') 

    json_file = {}

    
    json_file['errorFields'] = list(set(errorFieldList))
   
    print('file:',json_file)
    
    if len(errorFieldList) > 0:
        return JsonResponse(json_file,status=400)
    else:
        logout(request)
        user = User.objects.create_user(username, email, password)
        user.last_name = lastName
        user.first_name = firstName
        user.profile.tennisClub = tennisClub
        user.profile.experienceStatus = experience
        user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
        user.save()

        user = authenticate(username=username, password=password)
        login(request, user)
        return JsonResponse({'details':'User successfully created. You are now logged in.'},status=200)


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'isAuthenticated': True})


@ensure_csrf_cookie
def isAuthenticad(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})
    print(request.user.username)
    return JsonResponse({'isAuthenticated': True,'user': request.user.username})

@require_POST
def getUserDataGeneral(request):
    data = json.loads(request.body)
    userID = data.get('userID')
    try:
        user = get_user_model().objects.get(username = userID) 
        
        return JsonResponse({
            'username': user.username,
            'email': user.email,
            'bio':user.profile.bio
        })
    except:
       
        return JsonResponse({'error':'The requested user was not found.'},status=500)
    
