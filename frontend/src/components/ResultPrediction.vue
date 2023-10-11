<template>
  <div class="custom-container">
    <v-container>
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card class="custom-card">
          <!-- Imagen en la parte superior -->
          <v-img
            src="../assets/result.jpg"
            aspect-ratio="2.75"
            class="custom-img"
          ></v-img>

          <!-- Contenido del v-card -->
          <v-card-text class="text-center custom-text">
            <div>
              <h2 class="custom-heading">Resultado de la Predicción</h2>
              <p class="custom-p">El resultado de esta predicción es: <strong>{{ result.prediction }}</strong></p>
              <p class="custom-p">Precisión del: <strong>{{ result.accuracy }}</strong></p>
            </div>
            <!-- Botón para el router push -->
            <v-btn @click="redirigir" color="secondary">Nueva predicción</v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
  </div>
</template>
  
  <script>
  import axios from 'axios'

  export default {
    data(){
      return {
        result: {}
      }

    },
    mounted() {
     this.predecirRendimiento()
    },
    methods: {
      predecirRendimiento() {
        const id_student = this.$store.state.userId
        console.log(id_student)
        axios.get(`http://127.0.0.1:5000/prediction/${id_student}`)
        .then(response => {
        console.log(response.data);
        this.result = response.data
      }) 
      .catch(error => {
        console.log(error, 'Error al capturar')
      })
      },

      redirigir() {
    localStorage.removeItem('userId') 
    this.$store.commit('clearUserId')
    this.$router.push('/prediction')
}


    },

  }
  </script>
  
  <style scoped>


  .custom-container {
  background-image: url('../assets/resultfondo.jpg'); /* Reemplaza 'tu-imagen.jpg' con el nombre de tu imagen */
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  min-height: 100vh; /* Ajusta el alto según tus necesidades */
}
.custom-card {
  background-color: #f8f8f8;
}

.custom-img {
  max-height: 400px; 
}

.custom-text {
  color: #333333; 
}

.custom-heading {
  font-size: 2em;
  margin-bottom: 40px;
  margin-top: 20px;
  color: rgba(0, 68, 255, 0.678);
}

.custom-p {
  margin-bottom: 40px;
  font-size: 15pt;
} </style>
  