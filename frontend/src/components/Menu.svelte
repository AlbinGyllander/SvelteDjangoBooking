<script>
    import LoginModal from "./LoginModal.svelte";
    import { link } from "svelte-routing";
    import { Button} from "carbon-components-svelte";

    import {Menu} from "carbon-icons-svelte"
    export let isAuthenticated
    export let user
  </script>
  <!-- <Tile>
      <div style="display:flex; justify-content:space-around; align-items:center;">
        <p>Hello this is the logo</p>
        <div>
           
        </div>
           
      </div>

    
  </Tile> -->
  
  <nav class="navbar navbar-expand-lg sticky-top navbar-light bg-light  ">
    <div class="container-fluid">
      <a class="navbar-brand mb-0 h1" href="#">SetMatch</a>

      <div style="border:none!important;" class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <Button size="field" kind="tertiary" iconDescription="More" icon={Menu} >

        </Button>
      </div>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/" use:link>Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/blog" use:link>Blog</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="/about" use:link>Blog</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
          </li>
        </ul>
        <LoginModal bind:user={user} bind:isAuthenticated={isAuthenticated}></LoginModal>        
      </div>
    </div>
  </nav>




