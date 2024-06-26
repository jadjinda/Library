<script>
import axios from "axios";

export default {
  data(){
    return{
      user: {
        email :'',
        password :''
      },
      users: []
    }
  },
  name: "Login",
  mounted() {},
  methods:{
    async login() {
      await axios
          .post("http://127.0.0.1:5000/auth/login", this.user)
          .then(response => {
            console.log("response", response.data);
            localStorage.setItem('access_token', response.data.access_token);
            this.user={
              email :'',
              password :''
            }
            this.$router.push('/acceuil')
          }).catch((error) => {
            console.log(error)
          })
    }
  },
  props: {}
}
</script>

<template>
<div class="container-scroller">
    <div class="container-fluid page-body-wrapper full-page-wrapper">
      <div class="content-wrapper d-flex align-items-center auth px-0">
        <div class="row w-100 mx-0">
          <div class="col-lg-4 mx-auto">
            <div class="auth-form-light text-left py-5 px-4 px-sm-5">
              <!--<div class="brand-logo">
                <img :src="logo" alt="logo">
              </div>-->
              <h4>Bienvenue!</h4>
              <h6 class="font-weight-light">Connectez-vous</h6>
              <form class="pt-3">
                <div class="form-group">
                  <input type="email" class="form-control form-control-lg" id="email" v-model="user.email" placeholder="Username">
                </div>
                <div class="form-group">
                  <input type="password" class="form-control form-control-lg" id="password" v-model="user.password" placeholder="Password">
                </div>
                <div class="mt-3">
                  <a class="btn btn-block btn-primary btn-lg font-weight-medium auth-form-btn" v-on:click="login">Se connecter</a>
                </div>
                <div class="my-2 d-flex justify-content-between align-items-center">
                  <div class="form-check">
                    <label class="form-check-label text-muted">
                      <input type="checkbox" class="form-check-input">
                      Se souvenir
                    </label>
                  </div>
                  <a href="#" class="auth-link text-black">Mot de passe oubliée?</a>
                </div>
                <div class="mb-2">
                  <button type="button" class="btn btn-block btn-facebook auth-form-btn">
                    <i class="ti-facebook me-2"></i>Se connecter avec Facebook
                  </button>
                </div>
                <div class="text-center mt-4 font-weight-light">
                  Vous n'avez pas de compte? <a href="/register" class="text-primary">S'inscrire</a>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <!-- content-wrapper ends -->
    </div>
    <!-- page-body-wrapper ends -->
  </div>
  <!-- container-scroller -->
</template>

<style scoped>

</style>