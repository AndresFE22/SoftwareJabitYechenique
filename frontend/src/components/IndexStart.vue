<template>
    <div class="background">
      <v-container class="d-flex justify-center align-center pa-5">
        <v-card class="pa-5 text-center">
          <div class="img">
            <table>
              <tr>
                <td class="corner">
                  <img src="../assets/LogoLIEMAV.png" alt="Logo LIEMAV" class="liemav" />
                </td>
                <td></td>
                <td class="corner">
                  <img src="../assets/LogosUNICOR.png" alt="Logo UNICOR" />
                </td>
              </tr>
              <tr>
                <td></td>
                <td rowspan="2">
                  <img src="../assets/icon.png" alt="Logo Icon" class="centered" />
                </td>
                <td></td>
              </tr>
              <tr>
                <td class="corner">
                  <img src="../assets/logoActualizado.jpg" alt="Logo UNICOR" />
                </td>
                <td class="corner"></td>
              </tr>
            </table>
          </div>
          <h2>Modelo de Predicción del Rendimiento Académico</h2>
          <v-btn @click="predecirRendimiento" color="primary">Predecir Rendimiento</v-btn>
          <v-btn @click="entrenarModelo" color="success">Entrenar Modelo</v-btn>
        </v-card>
      </v-container>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      predecirRendimiento() {
        this.$router.push('/prediction')
    },
      entrenarModelo() {
        // Lógica para entrenar modelo aquí
      }
    }
  }
  </script>
  
  <style scoped>
 .background {
    background-image: url('../assets/fondo.jpg');
    height: 100vh;
  } 

  .img {
  text-align: center;
}

img {
    width: 200px;
}
.centered {
  display: block;
  margin: 0 auto;
}
.corner {
    width: 100px;
    height: 100px;
  }
  </style>
  