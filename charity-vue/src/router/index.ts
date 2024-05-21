import { createRouter, createWebHistory } from 'vue-router';
// import HomeView from '../views/HomeView.vue';
import Home from "../components/Home.vue";
import HelloWorld from "../components/HelloWorld.vue";
import Categorie from '@/components/Categorie.vue';
import Projet from '@/components/Projet.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   redirect: '/home' // Redirection vers la route '/home'
    // },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    // {
    //   path: '/hello',
    //   name: 'hello',
    //   component: HelloWorld
    // },
    {
      path: '/',
      name: 'hello',
      component: HelloWorld
    },
    {
      path: '/projets',
      name: 'projets',
      component: Projet
    },
    {
      path: '/categories',
      name: 'categories',
      component: Categorie
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
  ]
});

export default router;