<template>
    <v-container class="d-flex justify-center align-center pa-5 background">
      <v-card class="pa-5 text-center">
        <!-- <img src="@/assetss/tu-logo.png" alt="Logo" class="mb-4" /> -->
        <h2>Modelo de Predicción del Rendimiento Académico</h2>
        <v-btn @click="predecirRendimiento" color="primary">Predecir Rendimiento</v-btn>
        <v-btn @click="entrenarModelo" color="success">Entrenar Modelo</v-btn>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    methods: {
      predecirRendimiento() {
        // Lógica para predecir rendimiento aquí
      },
      entrenarModelo() {
        // Lógica para entrenar modelo aquí
      }
    }
  }
  </script>
  
  <style scoped>
 .background {
    background-image: linear-gradient(to bottom, #FFD700, #FF8C00);
    height: 100vh; /* Ajusta la altura según sea necesario */
  }  </style>
  