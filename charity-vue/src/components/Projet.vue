<template>
  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
    Launch demo modal
</button>
  <h1>Je suis la page de Projet</h1>
  <div class="row">
    <div v-for="projet in projets" :key="projet.libelle" class="col-md-4 mb-4">
      <div class="card h-100">
        <img :src="getImageUrl(projet.image)" :alt="projet.libelle" class="card-img-top" style="object-fit: contain; height: 200px;" />
        <div class="card-body">
          <h5 class="card-title">{{ projet.libelle }}</h5>
          <p class="card-text">{{ projet.description }}</p>
        </div>
        <div class="card-footer">
          <small class="text-muted">{{ projet.categorie }}</small>
        </div>
      </div>
    </div>
  </div>
  <!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';
import {API_URL} from '@/utils/constants.js'

export default {
  name: 'App',
  data() {
    return {
      projets: [],
    };
  },
  methods: {
    fetchProjets() {
      axios.get(API_URL +'/api/blogpost')
        .then((response) => {
          this.projets = response.data;
        })
        .catch((error) => {
          console.error('Erreur lors de la récupération des projets:', error);
        });
    },
    getImageUrl(image) {
      // Utilisation de new URL en conjonction avec import.meta.url pour générer un chemin d'accès aux images
      return API_URL +"/uploads/"+image;
      // return `http://localhost:5000/charity/blog_posts/static/uploads/${imageName}`;
      
    },
    handleImageError(event) {
      console.error('Erreur lors du chargement de l\'image:', event.target.src);
    },
  },
  created() {
    this.fetchProjets();
  },
};
</script>