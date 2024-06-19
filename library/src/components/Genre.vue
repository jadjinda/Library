<script>
import axios from "axios";
export default {
  data(){
    return{
      genre: {
        nom : '',
        statut: ''
      },
      genres: []
    }
  },
  name: "Genres",
  mounted() {
    this.allGenre()
  },
  methods:{
    async addGenre(){
      await axios
          .post("http://127.0.0.1:5000/library/genre", this.genre)
          .then(response=>{
            console.log("response", response.data);
            this.genre={
              nom : '',
              statut: ''
            }
            this.allGenre();
          }).catch((error)=>{
            console.log(error)
          })
    },
    async allGenre(){
      await axios
          .get('http://127.0.0.1:5000/library/listGenre')
          .then(value => {
            this.genres = value.data
            console.log(value.data)
          })
          .catch(error => {
            console.log(error)
          })
    },
    async deleteGenre(genre){
      await axios
          .delete("http://127.0.0.1:5000/library/deleteGenre/"+genre.id)
          .then(response=>{
            console.log("response",response.data);
            this.allGenre();
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
      <div class="col-12 grid-margin">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Créer un genre</h4>
            <form class="form-sample" @submit.prevent="addGenre">
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Nom</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" v-model="genre.nom"/>
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Statut :</label>
                    <div class="col-sm-4">
                      <div class="form-check form-check-success">
                        <label class="form-check-label">
                          <input type="radio" class="form-check-input" name="statut" id="disponible" value="disponible" checked="checked" v-model="genre.statut"> Disponible
                        </label>
                      </div>
                    </div>
                    <div class="col-sm-4">
                      <div class="form-check form-check-warning">
                        <label class="form-check-label">
                          <input type="radio" class="form-check-input" name="statut" id="non-disponible" value="non-disponible" v-model="genre.statut"> Non-Disponible
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
      <div class="col-lg-12 grid-margin stretch-card">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Liste des Genres</h4>
            <div class="table-responsive pt-3">
              <table class="table table-bordered">
                <thead>
                <tr>
                  <th>#</th>
                  <th>Nom</th>
                  <th>Statut</th>
                  <th>Option</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(item, index) in genres">
                  <td>{{ index+1 }}</td>
                  <td>{{ item.nom }}</td>
                  <td :class="item.statut === 'non-disponible' ? 'text-warning' : 'text-success'">
                    {{ item.statut }}
                  </td>
                  <td>
                    <button type="button" v-on:click="deleteGenre(item)" class="btn btn-danger btn-rounded btn-icon m-2">
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