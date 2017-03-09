var Vue = require('vue');
var App = require('./Components/App.vue');
var Modify = require("./Components/Modify.vue");
var VueRouter = require("vue-router");
var RouterView = require("./Components/RouterView.vue");

//register router
Vue.use(VueRouter);


const router = new VueRouter({
  routes : [
      {path: '/', component: App},
      {path: '/modify', component: Modify}
  ]
});

const vueApp = new Vue({
  el : "#app",
  router,
  render: h => h(RouterView)
}); 