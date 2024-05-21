<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
        <a class="navbar-brand" >Charity</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link "  ><router-link to="/categories">categorie</router-link></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" ><router-link to="/projets">projet</router-link></a>
            </li>
          </ul>
          <nav class="navbar navbar-light bg-light">
            <div class="container-fluid">
              <form class="d-flex">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Search</button>
              </form>
            </div>
          </nav>
        </div>
      </div>
    </nav>
  </header>
  <div id="app" class="container">
  <router-view></router-view>

</div>
</template>


<script>
import router from './router';


export default {
  name: 'App',
  router,
}
</script>


