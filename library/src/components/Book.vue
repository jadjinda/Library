<script>
import axios from "axios";
export default {
  data(){
    return{
      book: {},
      bookCategory: [],
      bookGenre: [],
      books: []
    }
  },
  name: "Books",
  mounted() {
    this.allCategorie(),
    this.allGenre()
  },
  methods:{
    onImageChange(event){
     this.book.imageCouverture = event.target.files[0]
   },
    async allCategorie(){
      await axios
          .get('http://127.0.0.1:5000/library/listCategory')
          .then(value => {
            this.bookCategory = value.data
            console.log(value.data)
          })
          .catch(error => {
            console.log(error)
          })
    },
    async allGenre(){
      await axios
          .get('http://127.0.0.1:5000/library/listGenre')
          .then(value => {
            this.bookGenre = value.data
            console.log(value.data)
          })
          .catch(error => {
            console.log(error)
          })
    },
    addBook(){
     const formData = new FormData();
     formData.append('titre', this.book.titre)
      formData.append('auteur', this.book.auteur)
       formData.append('codeISBN', this.book.codeISBN)
       formData.append('datePublication', this.book.datePublication)
       formData.append('nombreExemplaires', this.book.nombreExemplaires)
       formData.append('imageCouverture', this.book.imageCouverture)
       formData.append('genre_id', this.book.genre_id)
      formData.append('category_id', this.book.category_id)
      axios.post('http://127.0.0.1:5000/library/book', formData,{
        headers:{'Contents-Type':'multipart/form-data'}
      }).then(response => {
        this.book = {}
        this.$router.push('/bookList')
      }).catch(error => {
        console.log('Error:', error);
      })
    }
  },
  props: {}
}
</script>
<template>
<div class="main-panel">
  <div class="content-wrapper">
          <div class="row">
            <div class="col-12 grid-margin">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Créer un Livre</h4>
                  <form class="form-sample" @submit.prevent="addBook">
                    <div class="row">
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Titre</label>
                          <div class="col-sm-9">
                            <input type="text" id="titre" name="titre" v-model="book.titre" class="form-control" />
                          </div>
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Auteur</label>
                          <div class="col-sm-9">
                            <input type="text" id="auteur" name="auteur" v-model="book.auteur" class="form-control" />
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Code ISBN</label>
                          <div class="col-sm-9">
                            <input type="text" id="codeISBN" name="codeISBN" v-model="book.codeISBN" class="form-control" />
                          </div>
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Date de publication</label>
                          <div class="col-sm-9">
                             <input type="text" id="datePublication" name="datePublication" v-model="book.datePublication" class="form-control" />
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Nombre d'exemplaires</label>
                          <div class="col-sm-9">
                            <input type="text" id="nombreExemplaires" name="nombreExemplaires" v-model="book.nombreExemplaires" class="form-control" />
                          </div>
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Image de Couverture</label>
                          <div class="col-sm-9">
                            <input type="file" class="form-control" id="imageCouverture" @change="onImageChange" accept="image/*" required/>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Genre</label>
                          <div class="col-sm-9">
                            <select class="form-control" v-model="book.genre_id">
                              <option v-for="genre in bookGenre" :key="genre.id">{{ genre.nom }}</option>
                            </select>
                          </div>
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Catégorie</label>
                          <div class="col-sm-9">
                            <select class="form-control" v-model="book.category_id">
                              <option v-for="category in bookCategory" :key="category.id">{{ category.nom }}</option>
                            </select>
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

