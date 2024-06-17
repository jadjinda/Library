<script>

</script>

<template>
<div class="main-panel">
  <div class="content-wrapper">
          <div class="row">
            <div class="col-12 grid-margin">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Emprunt</h4>
                  <form class="form-sample">
                    <div class="row">
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Nom</label>
                          <div class="col-sm-9">
                            <input type="text" class="form-control" />
                          </div>
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Date d'emprunt</label>
                          <div class="col-sm-9">
                            <input type="date" class="form-control" />
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Date de retour</label>
                          <div class="col-sm-9">
                            <input type="date" class="form-control" />
                          </div>
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Observation</label>
                          <div class="col-sm-9">
                            <textarea class="form-control"></textarea>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-md-6">
                        <div class="form-group row">
                          <label class="col-sm-3 col-form-label">Livre</label>
                          <div class="col-sm-9">
                            <select class="form-control">
                              <option>Livre1</option>
                              <option>Livre2</option>
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
            <div class="col-lg-12 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Liste des emprunts</h4>
                  <div class="table-responsive pt-3">
                    <table class="table table-bordered">
                      <thead>
                        <tr>
                          <th>#</th>
                          <th>Nom</th>
                          <th>Délais</th>
                          <th>Livre</th>
                          <th>Observation</th>
                          <th>Option</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>1</td>
                          <td>Herman Beck</td>
                          <td>08/05/2024 à 10/10/2024</td>
                          <td>L'enfant noir</td>
                          <td>Sans objet</td>
                          <td>
                            <button type="button" class="btn btn-danger btn-rounded btn-icon m-2">
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