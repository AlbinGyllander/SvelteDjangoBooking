<script>
	import { Router, Link, Route } from "svelte-routing";
	import Menu from "./components/Menu.svelte";
	import UserProfilePage from "./components/UserProfilePage.svelte";
	import IndexInfoPage from "./components/IndexInfoPage.svelte"
	import Footer from "./components/Footer.svelte"
	let isAuthenticated= null
	let currentUser= null;
	
	const who = () =>{
		fetch('http://127.0.0.1:8000/api/isAuthenticated')
		.then(response => response.json())
		.then(data => {
            
			isAuthenticated=data.isAuthenticated;
			currentUser = data.user ||null
			console.log(currentUser)
            
        })
	}
    who()

	
	

	export let url = "";
	
</script>

	<main>

		<Menu bind:user={currentUser} bind:isAuthenticated={isAuthenticated}></Menu>
  
		
	</main>	
	<Router url="{url}">

		<div>
		  <Route path="blog/:id"  />
		  <Route path="blog"  >
			  <p>Hello this is the blog.</p>
		  </Route>
		  <Route path="about" />
		  <Route path="/">
				
				<p>this is the home page</p>
				<IndexInfoPage/>

		</Route>
		<Route path="/user/:user" let:params>
				
			<p>this is the user page</p>
			
			<UserProfilePage user={params.user}></UserProfilePage>
		</Route>
		</div>
	  </Router>

	  <Footer></Footer>

<style>
	/* main {
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	} */
</style>