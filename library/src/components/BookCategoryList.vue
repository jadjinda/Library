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
    this.allCategorie();
  },
  methods:{
    async allCategorie(){
      await axios
          .get('http://127.0.0.1:5000/library/listCategory')
          .then(value => {
            this.categories = value.data
            console.log(value.data)
          })
          .catch(error => {
            console.log(error)
          })
    },
    async deleteCategorie(categorie){
      await axios
          .delete("http://127.0.0.1:5000/library/deleteCategory/"+categorie.id)
          .then(response=>{
            console.log("response",response.data);
            this.allCategorie();
          }).catch((error)=>{
            console.log(error)})
    },
  }
}
</script>

<template>
  <div class="main-panel">
    <div class="content-wrapper">
      <div class="row">
        <div class="col-lg-12 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Liste des Catégories</h4>
                  <div class="table-responsive pt-3">
                    <table class="table table-bordered">
                      <thead>
                        <tr>
                          <th>#</th>
                          <th>Nom</th>
                          <th>Description</th>
                          <th>Statut</th>
                          <th>Option</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(item, index) in categories">
                          <td>{{index+1}}</td>
                          <td>{{ item.nom }}</td>
                          <td>{{ item.description }}</td>
                          <td :class="item.statut === 'non-disponible' ? 'text-warning' : 'text-success'">
                            {{ item.statut }}
                          </td>
                          <td>
                            <button type="button" v-on:click="deleteCategorie(item)" class="btn btn-danger btn-rounded btn-icon m-2">
                              <i class="ti-eraser"></i>
                            </button>
                            <button type="button" class="btn btn-warning btn-rounded btn-icon">
                              <i class="ti-pencil-alt"></i>
                            </button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
      </div>
    </div>
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

<style scoped>

</style>
