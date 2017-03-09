var Vue = require('vue')
var App = require('./Components/App.vue')
new Vue({
  el: '#app',
  render: function (createElement) {
    return createElement(App) 
  }
}) 