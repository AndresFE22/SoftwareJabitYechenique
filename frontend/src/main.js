import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueRouter from 'vue-router'


import index from './components/IndexStart.vue'
import form from './components/FormPrediction.vue'
import result from './components/ResultPrediction.vue'



Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: index
},
{
  path: '/prediction',
  name: 'index',
  component: form
},
{
  path: '/result',
  name: 'index',
  component: result
},

]

const router = new VueRouter({
  routes,
  mode: 'history' 
})



new Vue({
  vuetify,
  router ,
  render: h => h(App)
}).$mount('#app')
