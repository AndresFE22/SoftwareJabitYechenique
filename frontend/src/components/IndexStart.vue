<template>
  <div class="background">
    <div class="grid-container">
      <div class="grid-item">
        <img src="@/assets/LogoLIEMAV.png" alt="Logo LIEMAV" class="liemav" />
      </div>
      <div class="grid-item">
        <img src="@/assets/icon.png" alt="Logo Icon" class="centered" />
      </div>
      <div class="grid-item">
        <img src="@/assets/LogosUNICOR.png" alt="Logo UNICOR" />
      </div>  
      <div class="grid-item"></div>
      <div class="grid-item">
        <h2>Modelo de Predicción del Rendimiento Académico</h2>
      </div>
      <div class="grid-item"></div>  
      <div class="grid-item"></div>
      <div class="grid-item"> 
        <v-btn @click="predecirRendimiento" color="rgb(0, 195, 255)" style="color: white;">Predecir Rendimiento</v-btn>
        <v-btn @click="entrenarModelo" color="success">Entrenar Modelo</v-btn> 
      </div>
      <div class="grid-item">
        <img src="@/assets/logoActualizado.jpg" alt="Logo UNICOR" />
      </div>  
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    predecirRendimiento() {
      this.$router.push('/prediction')
    },
    entrenarModelo() {
      // Implementa tu lógica aquí
    }
  }
}
</script>

<style scoped>
.background {
  display: grid;
  place-items: center;
  min-height: 100vh;
  background-image: url('@/assets/manofondo.jpg');
  background-size: cover;
}

.grid-container {
  width: 70%;
  display: grid;
  grid-template-columns: auto auto auto;
  padding: 10px;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  /* background-image: url('../assets/15518081_5594021.jpg'); */
  background-size: cover;
  background-color: white;
  border: 0.5px solid rgba(0, 195, 255, 0.377);
  box-shadow: 5px 2px 10px rgba(2, 203, 253, 0.24);
}

.grid-item {
  padding: 0px;
  font-size: 30px;
  text-align: center;
}

.grid-item h2 {
  font-size: 2.0rem;
  margin-bottom: 20px;
  color: #333333;
}

.v-btn {
  margin: 5px;
  font-size: 1rem;
  padding: 10px 20px;
  border-radius: 5px;
  transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
}


.v-btn.primary:hover {
  background-color: #0056b3;
}

.v-btn.success {
  background-color: #28a745;
  color: #ffffff;
}

.v-btn.success:hover {
  background-color: #218838;
}

@media screen and (max-width: 768px) {
  .grid-container {
    width: 90%;
  }
}

img {
  width: 150px;
}

.liemav {
  width: 200px;
} 

.centered {
  width: 200px;
  margin-bottom: 10%;
} 

</style>
