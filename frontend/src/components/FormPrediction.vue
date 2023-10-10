<template>
  <div>
    <v-container>
    <v-form>
      <v-row v-for="(field, index) in fields" :key="index">
        <v-col cols="12" md="6">
          <v-text-field
            v-if="field.type === 'text'"
            v-model="field.value"
            :label="field.label"
            outlined
            required
          ></v-text-field>
          <v-select
            v-if="field.type === 'select'"
            v-model="field.value"
            :items="Object.keys(field.options)"
            :label="field.label"
            outlined
            required
          ></v-select>
        </v-col>
      </v-row>
      <v-btn color="primary" @click="modal">Enviar</v-btn>
    </v-form>
  </v-container>
  <v-dialog v-model="dialog" max-width="400px">
    <v-card class="card">
      <v-card-title>
        <span class="headline" v-if="loading">Realizando la predicción...</span>
      </v-card-title>
      <v-card-title>
        <span class="headline" v-if="!loading">Prediccion realizada<br>¿Ver resultados?</span>
      </v-card-title>
      <v-card-actions>
        <v-progress-circular
          v-if="loading"
          indeterminate
          color="primary"
        ></v-progress-circular>
      </v-card-actions>
      <v-divider></v-divider>
      <v-card-actions v-if="!loading">
        <v-btn @click="verResultado" color="primary">Ver resultado</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data() {
    return {
      fields: [
    { type: 'text', label: 'Nombre completo', value: '' },
    { type: 'select', label: 'Semestre académico', value: null, options: { '6': 6, '7': 7, '8': 8, '9': 9, '10': 10 } },
    { type: 'select', label: '¿Diste esta asignatura el semestre anterior?', value: null, options: { 'Si': 0, 'No': 1 } },
    { type: 'select', label: '¿Por qué motivo tuviste bajo rendimiento?', value: null, options: { 'Inasistencia': 0, 'Metodologia': 1, 'Dinero': 2, 'Ninguna de las anteriores': 3 } },
    { type: 'select', label: 'Satisfacción con la calidad de la enseñanza', value: null, options: { 'Muy satisfecho': 0, 'Regular': 1, 'Insatisfecho': 2 } },
    { type: 'select', label: 'Satisfacción con los conocimientos de la materia', value: null, options: { 'Muy satisfecho': 0, 'Regular': 1, 'Insatisfecho': 2 } },
    { type: 'select', label: '¿El docente realiza el seguimiento del desarrollo de la asignatura y actividades?', value: null, options: { 'Si': 0, 'No': 1 } },
    { type: 'select', label: '¿Sentiste apoyo por parte del docente a la hora de resolver las dudas que tuviste?', value: null, options: { 'Si': 0, 'No': 1 } },
    { type: 'select', label: '¿Qué tan útil fue el material que se te proporcionó en clase?', value: null, options: { 'Muy Util': 0, 'Algo Util': 1, 'No tan util': 2 } },
    { type: 'select', label: '¿Que tan difícil son las clases?', value: null, options: { 'Dificil': 0, 'Regular': 1, 'Facil': 2 } },
    { type: 'select', label: '¿Con qué frecuencia fuiste evaluado en el curso de tu clase?', value: null, options: { 'Siempre': 0, 'A veces': 1, 'Nunca': 2 } },
    { type: 'select', label: 'El profesor fue motivador y entusiasta', value: null, options: { 'Totalmente en desacuerdo': 0, 'Neutral': 1, 'Totalmente de acuerdo': 2 } },
    { type: 'select', label: '¿Crees que la clase proporcionó la cantidad adecuada de teoría y práctica?', value: null, options: { 'Si': 0, 'No': 1 } },
    { type: 'select', label: 'La clase estaba muy bien organizada', value: null, options: { 'Totalmente en desacuerdo': 0, 'Neutral': 1, 'Totalmente de acuerdo': 2 } },
    { type: 'select', label: 'El profesor estaba muy bien informado sobre el tema que se te enseñó', value: null, options: { 'Totalmente en desacuerdo': 0, 'Neutral': 1, 'Totalmente de acuerdo': 2 } },
    { type: 'select', label: '¿Crees que las enseñanzas de la clase serán útiles para el crecimiento de tu carrera?', value: null, options: { 'Si': 0, 'No': 1 } },
    { type: 'select', label: 'Rango del rendiemiento que tuviste por corte', value: null, options: { 'Alto': 0, 'Medio': 1, 'Bajo': 2 } }
],
dialog: false,
loading: true,
id: null


    };
  },
  methods: {
  submitForm() {
    const numericValues = this.fields.map(field => {
      if (field.type === 'select') {
        return field.value !== null ? field.options[field.value] : null;
      } else {
        return field.value;
      }
    });

    axios.post('http://127.0.0.1:5000/prediction', { field: numericValues })
      .then(response => {
        console.log(response.data);
        const userId = response.data.id
        console.log(userId);

        this.resetForm()
      })
      .catch(error => {
        console.log(error, 'Error al enviar')
      })
      this.dialog = true
    setTimeout(() => {
      this.loading = false;
      // this.ejecutarFuncion(); // Ejecutar la función cuando loading es false
 // Oculta la bolita de carga
    }, 3000);
  },

  resetForm() {
    this.fields.forEach(field => {
      if (field.type === 'select') {
        field.value = null;
      } else {
        field.value = '';
      }
    });
},

    verResultado() {
      this.$router.push('/result')
    },

    modal(){
    this.dialog = true
    this.submitForm();

    setTimeout(() => {
      this.loading = false; // Oculta la bolita de carga
    }, 3000);
  },

    cerrarDialog() {
      this.dialog = false;
    }
}
}

</script>

<style scoped>

.card {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
  border: 1px solid rgba(0, 195, 255, 0.582);

}

</style>
