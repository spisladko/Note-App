import Vue from 'vue'
import VueRouter from 'vue-router'

// импортируем все представления, по
// которым будем навигировать пользователя
import Login from '@/views/Login.vue'
import Notes from '@/views/Notes.vue'
import Register from '@/views/Register.vue'
import CreateNote from '@/views/CreateNote.vue'

Vue.use(VueRouter)

// заводим массив с роутами
const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/notes',
    name: 'Notes',
    component: Notes
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/create',
    name: 'CreateNote',
    component: CreateNote
  }
]

// создаём новый экземпляр класса
// VueRouter, с необходимыми параметрами
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// экспортируем сконфигурированный роутер
export default router
