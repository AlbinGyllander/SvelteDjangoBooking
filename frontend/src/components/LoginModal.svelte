<script>
    import { Button,Dropdown,Grid, Row, Column, Form,ProgressIndicator, ProgressStep,FormGroup,TextInput,PasswordInput, InlineNotification,Tile,Modal} from "carbon-components-svelte";
    import {Login,Logout,User} from "carbon-icons-svelte";
    let openLogin = false;
    let openRegister = false;
    let username;
	let password;

    let usernameRegistration;
	let passwordRegistration;
    let emailRegistration;
    let passwordRegistrationRepeat;

    //registration
    let emailRegistrationInvalid = false;
    let passwordRegistrationInvalid = false;
    let passwordRegistrationMessage = new Array;
    let passwordRegistrationRepeatInvalid = false
    let usernameRegistrationInvalid = false
    let usernameRegistrationInvalidMessage;
    let emailRegistrationInvalidMessage;
    let registrationError;
    let firstNameRegistration;
    let lastNameRegistration;
    let selectedTennisClub="0";
    let experienceLevel = "0";


	let error = null;
    let error_message = null;
    let registration_error_fields = []

    export let isAuthenticated;
    export let user;

    let currentIndex = 0;
    let registerPrimaryButtonText = "Next";
    let firstStep = false
    let secondStep = false
    let thirdStep = false
    let lastStep = false
    let registerPrimaryButtonDisallowed = false;
    let invalidPassStep;

    
    $:{
        if(passwordRegistrationRepeatInvalid == true || passwordRegistrationInvalid == true) {
            invalidPassStep = true
        }else{
            invalidPassStep = false
        }
        console.log(invalidPassStep)
    }

    $:{
        console.log(passwordRegistrationRepeatInvalid)
    }
    function setSteps(num,value){
        if( num == 0) firstStep = value
        if( num == 1) secondStep = value
        if( num == 2) thirdStep = value
        if( num == 3) lastStep = value        
    }
    
    
    let cookie
    function updateCookie(){
        cookie = getCookie('csrftoken')
    }
    updateCookie()
    
    
    function getCookie(name) {
		// Split cookie string and get all individual name=value pairs in an array
		var cookieArr = document.cookie.split(";");
		
		// Loop through the array elements
		for(var i = 0; i < cookieArr.length; i++) {
			var cookiePair = cookieArr[i].split("=");
			
			/* Removing whitespace at the beginning of the cookie name
			and compare it with the given string */
			if(name == cookiePair[0].trim()) {
				// Decode the cookie value and return
				return decodeURIComponent(cookiePair[1]);
			}
		}
		
		// Return null if not found
		return null;
	}
	
    function logout(){
        updateCookie()
        fetch("/api/logout/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken":cookie,
            },
            credentials: "same-origin",
            })
     .then(async response => {
         const isJson = response.headers.get('content-type')?.includes('application/json');
         console.log(response)
         const data = isJson ? await response.json() : null;

         // check for error response
         if (!response.ok) {
             // get error message from body or default to response status
             error = 'error'
             error_message = data.detail|| response.status
             
             return Promise.reject(error);
         }
         else{

             error= 'success'
             error_message = data.detail|| response.status
             updateCookie()
             
         }
         
         isAuthenticated = false
         window.location.replace('/');
     })
    }
    
    function login(){
        updateCookie()
     
		fetch("/api/login/", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"X-CSRFToken":cookie,
			},
			credentials: "same-origin",
			body: JSON.stringify({username: username, password: password}),
			})
		.then(async response => {
			const isJson = response.headers.get('content-type')?.includes('application/json');
			const data = isJson ? await response.json() : null;

			// check for error response
			if (!response.ok) {
				// get error message from body or default to response status
				error = 'error'
                error_message = data.detail|| response.status
				isAuthenticated=false
				return Promise.reject(error);
			}
            else{

                error= 'success'
                error_message = data.detail|| response.status
                openLogin = false
                isAuthenticated= true
                password=''
                username=''
                updateCookie()
                
            }
            
            window.location.replace('/');
		}).catch(error => {
            
        });

	}
    function register(){

        fetch("/api/registerUser/", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"X-CSRFToken":cookie,
			},
			credentials: "same-origin",
			body: JSON.stringify({
                    username: usernameRegistration, 
                    password: passwordRegistration,
                    passwordRepeat: passwordRegistrationRepeat, 
                    email:emailRegistration,
                    firstName: firstNameRegistration,
                    lastName : lastNameRegistration,
                    tennisClub: selectedTennisClub,
                    experience:experienceLevel,

                }),
			})
		.then(async response => {
			const isJson = response.headers.get('content-type')?.includes('application/json');
			const data = isJson ? await response.json() : null;
			// check for error response
			if (response.ok == false) {
                // get error message from body or default to response status
				registrationError = 'error'
                                
                registration_error_fields = data.errorFields || []
                                
                if (registration_error_fields.includes("usernameAlreadyExists")){
                    usernameRegistrationInvalid = true
                    usernameRegistration=''
                    usernameRegistrationInvalidMessage = 'This username already exists.'
                    
                }

                if (registration_error_fields.includes("InvalidUsernameChars")){
                    usernameRegistrationInvalid = true
                    usernameRegistration=''
                    usernameRegistrationInvalidMessage = 'Username contains invalid characters. Use only letters and numbers.'
                    
                }

                if (registration_error_fields.includes("usernameIsInvalid")){
                    usernameRegistrationInvalid = true
                    usernameRegistration=''
                    usernameRegistrationInvalidMessage = 'This field is required.'
                    
                }
                if (registration_error_fields.includes("emailIsNotValid")){
                    emailRegistrationInvalid = true
                    emailRegistration=''
                    emailRegistrationInvalidMessage = 'This email is not valid.'
                }
                if (registration_error_fields.includes("emailAlreadyExists")){
                    emailRegistrationInvalid = true
                    emailRegistration=''
                    emailRegistrationInvalidMessage = 'This email already exists.'
                }

                if (registration_error_fields.includes("password")){
                    passwordRegistrationInvalid = true
                    passwordRegistration=''
                    
                }
                if (registration_error_fields.includes("passwordRepeat")){
                    passwordRegistrationRepeatInvalid = true
                    passwordRegistrationRepeat=''
                    
                }
                
                
                
                
				isAuthenticated=false
                

				return Promise.reject(error);
			}
            else{

                firstStep = false
                secondStep = false
                thirdStep = false
                lastStep = false
                registrationError = 'success'
                openRegister = false
                isAuthenticated= true
                passwordRegistration=''
                
                passwordRegistrationRepeat=''
                emailRegistration=''
                passwordRegistrationRepeatInvalid = false
                usernameRegistrationInvalid = false
                emailRegistrationInvalid = false
                passwordRegistrationInvalid = false
                currentIndex =0
                updateCookie()
                window.location.replace(`/user/${usernameRegistration}`);
                console.log(usernameRegistration)
                usernameRegistration=''
                
            }
            

		}).catch(error => {
            
        });

	}
    //this makes sure that the entire CSS and page content has loaded before it allows to modal to show.
    //without it the modal loads in for around 200ms before disappearing because the page loads the modal element before realising it should be hidden.
    window.addEventListener('load', (event) => {
        document.getElementById('loginModal').removeAttribute('hidden')
        document.getElementById('registerModal').removeAttribute('hidden')
    });
    function checkEmailInvalid(){     
        var re = /\S+@\S+\.\S+/;
        if (re.test(emailRegistration) == false){
            emailRegistrationInvalid = true
            return true
        }else{
            emailRegistrationInvalid = false
            return false
        }
    
    }
    function checkUsernameValidity(){
        if(usernameRegistration == '' || /^[A-Za-z0-9_]*$/.test(usernameRegistration) == false){
            usernameRegistrationInvalid = true
            usernameRegistrationInvalidMessage = 'Invalid username. Can only contain letters and numbers.'
            return true
        } else{
            usernameRegistrationInvalid = false
            return false
        }
    }

    function checkPasswordValidity(){
        let passwordRegistrationMessages = new Array
        passwordRegistrationMessage= new Array
        if (/\d/.test(passwordRegistration) == false){
            passwordRegistrationInvalid = true
            passwordRegistrationMessages.push('Password must include a number.')

        }else{
            passwordRegistrationInvalid = false
            
        }
        if(passwordRegistration.length < 8){
            passwordRegistrationInvalid = true
            passwordRegistrationMessages.push('Password need to be minimum 8 characters long.')
        }else {
            passwordRegistrationInvalid = false
           
        }
        if(passwordRegistrationMessages.length > 1){
            passwordRegistrationMessage = passwordRegistrationMessages[0] + ' ' + passwordRegistrationMessages[1]
            return true
        } else{
            passwordRegistrationMessage = passwordRegistrationMessages[0]
            return false
        }  
        
    }
    function checkPasswordRepeatValidity(){
        if(passwordRegistrationRepeat == passwordRegistration){
            passwordRegistrationRepeatInvalid = false
            return false
        }else{
            passwordRegistrationRepeatInvalid = true
            return true
        }
    }
    
    $:{
        if (currentIndex == 3){
            registerPrimaryButtonText= "Register"
        }else{
            registerPrimaryButtonText = "Next"
        }
    }
    function changeRegisterSlide(dir='Forward'){
        if(dir == 'Back'){
            setSteps(currentIndex,false)
            currentIndex -=1
        }else{
            setSteps(currentIndex,true)
            currentIndex += 1     
        }
    }

</script>


<style>
    p{
        margin-bottom: 1rem;
    }


  
</style>
{#if isAuthenticated ===false}

    
        <Button size="field" icon={Login} iconDescription="Login" kind="tertiary" on:click={() => {
            (openLogin = true)
            document.getElementById('loginModal').removeAttribute('hidden')
        }}>Login</Button>
        <span style="margin-right: 0.5rem;"> </span>
        <Button size="field" kind="primary"  on:click={() => {
            (openRegister = true)
            document.getElementById('registerModal').removeAttribute('hidden')
        }}>Register</Button>    
     



<div id="loginModal" hidden>
    <Modal 
    bind:open={openLogin}
    bind:primaryButtonDisabled={isAuthenticated}
    modalHeading="Login"
    primaryButtonText="Login"
    secondaryButtonText="Cancel"
    on:click:button--secondary={() => (openLogin = false)}
    on:open
    on:close
    on:click:button--primary={() => {
        // if(valid()==true){
        //     login()
        // }
        login()
        
    }}
    hasScrollingContent={false}
    hasForm
    shouldSubmitOnEnter
    >
        {#if isAuthenticated == false}
            <p>Login in with your username and password.</p>
            {#if error =='error' }
            <InlineNotification
                kind='error'
                title="Error with login."
                subtitle={error_message}
                hideCloseButton
            />
            {:else if error=='success'}
            <!-- <InlineNotification
                kind='success'
                title="Successful login."
                subtitle=" "
                hideCloseButton
            /> -->
            {/if}

            <Form  >
            <FormGroup>
                <TextInput 

                    bind:value={username} 
                    labelText="Username" 
                    placeholder="Enter user name..." 
                    required 
                />    
            </FormGroup>
            <FormGroup>
                <PasswordInput
               
                required
                type="password"
                labelText="Password"
                placeholder="Enter password..."
                bind:value={password}
                />    
            </FormGroup>
            
            
        </Form>
        {:else}
            <p>You are already logged in.</p>
        {/if}
    </Modal>    
</div>

<div id="registerModal" hidden >
    <Modal 
    hasform
    hasScrollingContent=true
    size="lg"
    bind:open={openRegister}
    bind:primaryButtonDisabled={registerPrimaryButtonDisallowed}
    modalHeading="Register"
    bind:primaryButtonText={registerPrimaryButtonText}
    secondaryButtons={[{ text: "Cancel" }, { text: "Back" }]}
    on:click:button--secondary={({ detail }) => {
        if (detail.text === "Cancel") openRegister = false, console.log('close');
        if (detail.text === "Back") {
            
            if(currentIndex !=0 ){
                changeRegisterSlide('Back')};
            }
            
    }}
    on:open
    on:close
    on:click:button--primary={() => {

        if(currentIndex == 1 && usernameRegistration == ''){
            usernameRegistrationInvalid = true
            return
        }
        if(currentIndex == 2 && checkEmailInvalid()== true){
            return
        }
        
        if (currentIndex == 3 && (checkPasswordRepeatValidity()== true ||  checkPasswordValidity() == true ||  usernameRegistration == '' || checkEmailInvalid()== true)){
            return
        }else if( currentIndex == 3){
            register()
            return
        }
        changeRegisterSlide()
        
        
        
    }}

    shouldSubmitOnEnter
    >
        {#if isAuthenticated == false}
            <p>Register with a username, email and a password.</p>
            
            <ProgressIndicator spaceEqually bind:currentIndex>
                <ProgressStep
                  complete ={true}
                  label="Step 1"
                  description="The progress indicator will listen for clicks on the steps"
                  
                />
                <ProgressStep
                  bind:complete={secondStep}
                  label="Step 2"
                  description="The progress indicator will listen for clicks on the steps"
                  bind:invalid={usernameRegistrationInvalid}
                />
                <ProgressStep
                  bind:complete={thirdStep}
                  label="Step 3"
                  description="The progress indicator will listen for clicks on the steps"
                  bind:invalid={emailRegistrationInvalid}
                />
                <ProgressStep
                  bind:complete={lastStep}
                  label="Step 4"
                  bind:invalid={invalidPassStep}
                  
                />
              </ProgressIndicator>
            
            <!-- {#if registrationError =='error' }
                {#each registration_error_messages as message}
                    <InlineNotification
                        kind='error'
                        title="Error with registration."
                        subtitle={message}
                        hideCloseButton
                    />
                {/each}
            {/if} -->
            <Tile>
            <Form  >
            {#if currentIndex == 0}
            <p>This is the first step. Press next to begin.</p>
            {:else if currentIndex == 1}
            <FormGroup>
                <Grid noGutter=true fullWidth>
                    <Row>
                      <Column>
                        <TextInput 
                            bind:value={firstNameRegistration} 
                            labelText="First Name" 
                            placeholder="Enter First name..." 
                            required 
                        />
                      </Column>
                      <Column >
                        <TextInput 
                            bind:value={lastNameRegistration} 
                            labelText="Last Name" 
                            placeholder="Enter Last name..." 
                            required 
                        /> 
                      </Column>
                    </Row>
                </Grid>
                 
                
                <TextInput 
                    bind:value={usernameRegistration} 
                    labelText="Username" 
                    placeholder="Enter user name..." 
                    required 
                    bind:invalid={usernameRegistrationInvalid}
                    bind:invalidText={usernameRegistrationInvalidMessage}
                    on:blur={() => {checkUsernameValidity()}}
                />    
            </FormGroup>
            {:else if currentIndex == 2}
            <FormGroup>
                <TextInput 
                    bind:value={emailRegistration} 
                    labelText="Email" 
                    type="email"
                    placeholder="Enter email.." 
                    required 
                    bind:invalid={emailRegistrationInvalid}
                    bind:invalidText={emailRegistrationInvalidMessage}
                    on:blur={() => {checkEmailInvalid()}}
                />
                <Grid noGutter=true fullWidth>
                    <Row>
                      <Column>
                        <Dropdown
                            direction="top"
                            size="sm"
                            inline=true
                            titleText="Your preffered tennis club."
                            bind:selectedId={selectedTennisClub}
                            items={[
                                { id: "0", text: "SALK" },
                                { id: "1", text: "Kungliga Tennis Planen" },
                                { id: "2", text: "Solna Tennis Klubb" },
                            ]}
                        /> 
                     </Column>
                      <Column>
                        <Dropdown
                            direction="top"
                            inline=true
                            size="sm"
                            titleText="Your experience level."
                            bind:selectedId={experienceLevel}
                            items={[
                                { id: "0", text: "Beginner" },
                                { id: "1", text: "Intermidiate" },
                                { id: "2", text: "Advanced" },
                                { id: "3", text: "Trainer" },
                            ]}
                        /> 
                      </Column>
                    </Row>
                </Grid>
                
                   
            </FormGroup>
            {:else if currentIndex == 3}
            <FormGroup>
                <PasswordInput
                required
                type="password"
                labelText="Password"
                placeholder="Enter password..."
                bind:value={passwordRegistration}
                bind:invalid={passwordRegistrationInvalid}
                bind:invalidText={passwordRegistrationMessage}
                on:blur={() => {checkPasswordValidity()}}
                />  
                <PasswordInput
                required
                type="password"
                labelText="Repeat password"
                placeholder="Enter password again..."
                bind:value={passwordRegistrationRepeat}
                bind:invalid={passwordRegistrationRepeatInvalid}
                invalidText="Passwords need to be identical. Please try again."
                on:blur={() => {checkPasswordRepeatValidity()}}
                />    
            </FormGroup>
            
            {/if}
            
            
        </Form>
        </Tile>
        {:else}
            <p>You are already logged in.</p>
        {/if}
    </Modal>    
</div>
{:else}
<Button size="field" kind="tertiary" icon={User} on:click={() => (window.location.replace(`/user/${user}`))} iconDescription="Your account"></Button>
<span style="margin-right: 0.5rem;"> </span>
<Button icon={Logout} size="field" kind="secondary" on:click={() => (logout())}>Log out</Button>
{/if}

