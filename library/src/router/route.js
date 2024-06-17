import { createRouter, createWebHistory } from 'vue-router'
import Book from '@/components/Book.vue'
import BookCategory from '@/components/BookCategory.vue'
import Home from "@/components/Home.vue";
import BookCategoryList from "@/components/BookCategoryList.vue";
import Genre from "@/components/Genre.vue"
import BookList from "@/components/BookList.vue";
import Emprunt from "@/components/Emprunt.vue"
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";

const route = createRouter({
  history: createWebHistory(),
  routes: [
      {
        path:'/',
        name: 'home',
        component: Home
      },
      {
          path: '/login',
          name: 'login',
          component: Login
      },
      {
          path: '/register',
          name: 'register',
          component: Register
      },
      {
      path: '/book',
      name: 'book',
      component: Book
      },
      {
        path:'/bookList',
        name: 'bookList',
        component: BookList
      },
      {
      path: '/bookCategory',
      name: 'bookCategory',
      component: BookCategory
      },
      {
          path: '/categoryList',
          name: 'categoryList',
          component: BookCategoryList
      },
      {
          path: '/genre',
          name: 'genre',
          component: Genre
      },
      {
          path: '/emprunt',
          name: 'emprunt',
          component: Emprunt
      }
  ]
})

export default route
