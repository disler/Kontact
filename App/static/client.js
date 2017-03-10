var Vue = require('vue');
var RouterView = require("./Components/RouterView.vue");
var store = require("./store");
var router = require("./router");

const vueApp = new Vue({
  el : "#app",
  router,
  store,
  render: _app => _app(RouterView)
}); 