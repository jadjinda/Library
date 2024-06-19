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
import Admin from "@/Admin.vue";

const route = createRouter({
  history: createWebHistory(),
  routes: [
      {
        path:'',
        name: 'login',
        component: Login
      },
      {
          path: '/register',
          name: 'register',
          component: Register
      },
      {
          path: '/acceuil',
          name: 'acceuil',
          component: Admin,
          children : [
              {
                  path: '',
                  name: 'Home',
                  component: Home
              },
              {
                  path: '/book',
                  name: 'book',
                  component: Book
              },
              {
                  path: '/bookCategory',
                  name: 'bookCategory',
                  component: BookCategory
              },
              {
                  path:'/bookList',
                  name: 'bookList',
                  component: BookList
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
      }
  ]
})

export default route
