<script setup>

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
                        <tr>
                          <td>1</td>
                          <td>Nom1</td>
                          <td>Description1</td>
                          <td class="text-warning">Non-disponible</td>
                          <td>
                            <button type="button" class="btn btn-danger btn-rounded btn-icon m-2">
                              <i class="ti-eraser"></i>
                            </button>
                            <button type="button" class="btn btn-warning btn-rounded btn-icon">
                              <i class="ti-pencil-alt"></i>
                            </button>
                          </td>
                        </tr>
                        <tr>
                          <td>2</td>
                          <td>Nom2</td>
                          <td>Description2</td>
                          <td class="text-success">Disponible</td>
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
