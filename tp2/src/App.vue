<template>
  <div>
    <div v-for="projet in projets" :key="projet.libelle">
      <h2>{{ projet.libelle }}</h2>
      <p>{{ projet.description }}</p>
      <p>{{ projet.categorie }}</p>
      <!-- Utilisation de :src pour lier dynamiquement l'URL de l'image -->
      <img :src="getImageUrl(projet.image)" :alt="projet.libelle" />
      <!-- <img :src="'../static/charity_img/' + projet.image" :alt="projet.libelle" /> -->
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
      axios.get(API_URL +'/charity/api/list')
        .then((response) => {
          this.projets = response.data;
        })
        .catch((error) => {
          console.error('Erreur lors de la récupération des projets:', error);
        });
    },
    getImageUrl(imageName) {
      // Utilisation de new URL en conjonction avec import.meta.url pour générer un chemin d'accès aux images
      return API_URL +"/charity/static/charity_img/"+imageName;
    },
  },
  created() {
    this.fetchProjets();
  },
};
</script>
