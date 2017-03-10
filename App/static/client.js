var Vue = require('vue');
var Vuex = require("vuex");
var VueRouter = require("vue-router");

var App = require('./Components/App.vue');
var Modify = require("./Components/Modify.vue");
var RouterView = require("./Components/RouterView.vue");

//register router, register vuex state management
Vue.use(VueRouter);
Vue.use(Vuex);


//configure router
const router = new VueRouter({
  routes : [
      {path: '/', component: App},
      {path: '/modify', component: Modify}
  ]
});

//configure state management
const store = new Vuex.Store({
  state: {
    lstKontact : [],
    oKontactToUpdate : {},
    bCreateNotUpdate : undefined
  },
  mutations : {
    SetKontacts(state, lstKontact)
    {
      state.lstKontact = lstKontact;
    },
    CreateNotUpdate(state, bCreateNotUpdate)
    {
      state.bCreateNotUpdate = bCreateNotUpdate;
    },
    SetKontactToUpdate(state, oKontactToUpdate)
    {
      state.bCreateNotUpdate = false;
      state.oKontactToUpdate = oKontactToUpdate;
    },
    ClearKontactReference(state)
    {
      state.bCreateNotUpdate = undefined;
      state.oKontactToUpdate = {};
    }
  },
  actions : {
    FetchKontacts({commit})
    {
      return new Promise( (resolve, reject) => {
        fetch("/kontacts", {method:"get"}).then( (response) =>
        {
          response.json().then((json) => {
            commit("SetKontacts", json);
            resolve(json);
          });
        }, (error) => {
          console.error('error', error);
          reject(error);
        });
      })
    }
  }
})

const vueApp = new Vue({
  el : "#app",
  router,
  store,
  render: h => h(RouterView)
}); 