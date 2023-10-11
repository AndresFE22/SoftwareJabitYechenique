import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userId: localStorage.getItem('userId') || null,
  },
  mutations: {
    setUserId(state, userId) {
      state.userId = userId
      localStorage.setItem('userId', userId)
    },
    clearUserId(state) {
      state.userId = null
      localStorage.removeItem('userId')
    },
  },

});
