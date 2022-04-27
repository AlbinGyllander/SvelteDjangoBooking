<script>
    import { Button ,Grid, Row, Column,Accordion, AccordionItem} from "carbon-components-svelte";
    export let user
    let email;
    let bio;
    let username;
    let error = false;
    let errorMsg = ''
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


    
    function getUser(){
        updateCookie()
     
		fetch("/api/getUserDataGeneral/", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"X-CSRFToken":cookie,
			},
			credentials: "same-origin",
			body: JSON.stringify({userID: user}),
			})
		.then(async response => {
			const isJson = response.headers.get('content-type')?.includes('application/json');
			const data = isJson ? await response.json() : null;

			// check for error response
			if (!response.ok) {
				error = true
                errorMsg = data.error || null
                console.log(error)
			}
            else{
                error=false
                username = data.username
                email = data.email
                bio = data.bio
                updateCookie()
                
            }
            
		}).catch(error => {
            
        });

	}
    getUser()




</script>
{#if error == true}
<p>{errorMsg}</p>
{:else}
<div>
   
    <div class="bg-white  text-lg-start mt-5">
        <div  class="container py-5 " style="align-items: flex-start!important">
            
           
            <div class="row" style="justify-content: center!important">
                <div class="col-lg-4 col-md-6 mb-4 mb-md-0" style="position:sticky; top:120px;">
                    <img src="https://media.playyourcourt.com/media/pro/avatar-310404-1619632414.4840422.JPG.250x250_q85_box-319%2C0%2C1286%2C967.jpg" alt="ProfileImg">
                    <h4>Albin Gyllander</h4>
                    <p>5/5</p>
                    <a>See all reviews.</a>
                    <br>
                    <Button kind="primary">Book Now</Button>
                    <h4>Need help?</h4>
                    <p>Call us at:</p>
                    <a>0725555054</a>
                </div>
        
                <div class="col-lg-6 col-md-6 mb-4 mb-md-0 " style="margin-bottom: 600px !important; ">
                    <h2 class="mb-2">About me</h2>
                    <p>{bio}</p>
                    <div class="mt-5">
                        <h3 class="mb-2">Do you have any questions?</h3>
                        <Accordion>
                            <AccordionItem title="Natural Language Classifier">
                            <p>
                                Natural Language Classifier uses advanced natural language processing and
                                machine learning techniques to create custom classification models. Users
                                train their data and the service predicts the appropriate category for the
                                inputted text.
                            </p>
                            </AccordionItem>
                            <AccordionItem title="Natural Language Understanding">
                            <p>
                                Analyze text to extract meta-data from content such as concepts, entities,
                                emotion, relations, sentiment and more.
                            </p>
                            </AccordionItem>
                            <AccordionItem title="Language Translator">
                            <p>
                                Translate text, documents, and websites from one language to another.
                                Create industry or region-specific translations via the service's
                                customization capability.
                            </p>
                            </AccordionItem>
                        </Accordion>    
                    </div>
                    
                </div>
        
   
            </div>
    
        </div>    
    </div>
</div>
{/if}
