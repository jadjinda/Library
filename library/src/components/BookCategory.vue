<script>
import axios from "axios";
export default {
  data(){
    return{
      category: {
        nom : '',
        description: '',
        statut: ''
      },
      categories: []
    }
  },
  name: "Categories",
  mounted() {

  },
  methods:{
    async addCategory(){
      await axios
          .post("http://127.0.0.1:5000/library/category", this.category)
          .then(response=>{
            console.log("response", response.data);
            this.category={
              nom : '',
              description: '',
              statut: ''
            }
            this.$router.push('/categoryList')
          }).catch((error)=>{
            console.log(error)
          })
    }
  }
}
</script>

<template>
  <div class="main-panel">
        <div class="content-wrapper">
          <div class="row">
            <div class="col-12 grid-margin">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Créer une catégorie</h4>
                  <form class="form-sample" @submit.prevent="addCategory">
                    <div class="row">
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Nom</label>
                          <div class="col-sm-9">
                            <input type="text" class="form-control" id="nom" v-model="category.nom"/>
                          </div>
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Description</label>
                          <div class="col-sm-9">
                            <textarea class="form-control" id="description" v-model="category.description"></textarea>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Statut :</label>
                          <div class="col-sm-4">
                            <div class="form-check form-check-success">
                              <label class="form-check-label">
                                <input type="radio" class="form-check-input" name="statut" id="disponible" value="disponible" v-model="category.statut" checked="checked"> Disponible
                              </label>
                            </div>
                          </div>
                          <div class="col-sm-4">
                            <div class="form-check form-check-warning">
                              <label class="form-check-label">
                                <input type="radio" class="form-check-input" name="statut" id="non-disponible" value="non-disponible" v-model="category.statut"> Non-Disponible
                              </label>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <button type="submit" class="btn btn-primary btn-rounded btn-fw m-2">Valider</button>
                    <button type="reset" class="btn btn-danger btn-rounded btn-fw">Annuler</button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- content-wrapper ends -->
        <!-- partial:../../partials/_footer.html -->
        <footer class="footer">
          <div class="d-sm-flex justify-content-center justify-content-sm-between">
            <span class="text-muted text-center text-sm-left d-block d-sm-inline-block">Copyright © <a href="https://www.bootstrapdash.com/" target="_blank">bootstrapdash.com </a>2021</span>
            <span class="float-none float-sm-right d-block mt-1 mt-sm-0 text-center">Only the best <a href="https://www.bootstrapdash.com/" target="_blank"> Bootstrap dashboard </a> templates</span>
          </div>
        </footer>
        <!-- partial -->
      </div>
</template>
