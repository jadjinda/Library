<script>
import logo from "../assets/images/logo.svg"
import axios from "axios";
export default {
  data(){
    return{
      user: {
        firstname : '',
        username : '',
        email :'',
        password :''
      },
      users: []
    }
  },
  name: "Register",
  mounted() {},
  methods:{
    async register() {
      await axios
          .post("http://127.0.0.1:5000/auth/register", this.user)
          .then(response => {
            console.log("response", response.data);
            this.user={
              firstname : '',
              username : '',
              email :'',
              password :''
            }
            this.$router.push('/')
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
                <img :src="logo" alt="">
              </div>-->
              <h4>Vous n'avez pas de compte?</h4>
              <h6 class="font-weight-light">Veuillez vous inscrire!</h6>
              <form class="pt-3">
                <div class="form-group">
                  <input type="text" class="form-control form-control-lg" id="firstname" v-model="user.firstname" placeholder="First Name">
                </div>
                <div class="form-group">
                  <input type="text" class="form-control form-control-lg" id="username" v-model="user.username" placeholder="Username">
                </div>
                <div class="form-group">
                  <input type="email" class="form-control form-control-lg" id="email" v-model="user.email" placeholder="Email">
                </div>
                <div class="form-group">
                  <input type="password" class="form-control form-control-lg" id="password" v-model="user.password" placeholder="Password">
                </div>
                <div class="mb-4">
                  <div class="form-check">
                    <label class="form-check-label text-muted">
                      <input type="checkbox" class="form-check-input">
                      J'accepte toute les Termes & Conditions
                    </label>
                  </div>
                </div>
                <div class="mt-3">
                  <a class="btn btn-block btn-primary btn-lg font-weight-medium auth-form-btn" v-on:click="register">S'inscrire</a>
                </div>
                <div class="text-center mt-4 font-weight-light">
                  Vous-avez déjà un compte? <a href="/" class="text-primary">Se connecter</a>
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
</template>

<style scoped>

</style>