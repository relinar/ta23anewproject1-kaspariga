import './style.scss';
import { createApp } from 'vue';
import { createWebHashHistory, createWebHistory, createMemoryHistory, createRouter } from 'vue-router'
 
 
import App from './App.vue';
 
import Modals from './pages/Modals.vue';
import ToDo from './pages/ToDo.vue';
import Chuck from './pages/Chuck.vue';
import RickAndMorty from './pages/RickAndMorty.vue';

 
const routes = [
  { path: '/', component: ToDo, name: 'ToDo' },
  { path: '/about', component: Modals, name: 'Modals' },
  { path: '/chuck', component: Chuck, name: 'Chuck Norris' },
  { path: '/rickandmorty', component: RickAndMorty, name: 'Rick and Morty' },


]
 
const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
 
 
const app = createApp(App);
app.use(router);
app.mount('#app');