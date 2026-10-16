import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DashboardView from '../views/DashboardView.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
  { path: '/', name: 'Home', component: HomeView, meta: { layout: 'PublicLayout' } },
  { path: '/login', name: 'Login', component: LoginView, meta: { layout: 'PublicLayout' } },
  { path: '/dashboard', name: 'Dashboard', component: DashboardView, meta: { layout: 'PrivateLayout', requiresAuth: true } },
  { path: '/:pathMatch(.*)*', redirect: '/' }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
