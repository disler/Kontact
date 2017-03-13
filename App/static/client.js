var Vue = require('vue');
var RouterView = require("./Components/RouterView.vue");
var store = require("./store");
var router = require("./router");

//create application with the addition of the router and store. Set up on 'RouterView' component for view swapping.
const vueApp = new Vue({
  el : "#app",
  router,
  store,
  render: _app => _app(RouterView)
}); 