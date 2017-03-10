var Vue = require('vue');
var VueRouter = require("vue-router");

//register router
Vue.use(VueRouter);

//get routable components
var App = require('./Components/App.vue');
var Modify = require("./Components/Modify.vue");

//configure router
const router = new VueRouter({
  routes : [
      {path: '/', component: App},
      {path: '/modify', component: Modify}
  ]
});

module.exports = router;