var Vue = require('vue');
var Vuex = require("vuex");
Vue.use(Vuex);


//configure state management
const store = new Vuex.Store({
    
    //expected state
    state: {
        lstKontact : [],
        oKontactToUpdate : {},
        bCreateNotUpdate : undefined
    },
    //standard getter interface
    getters: {
        Kontacts(state){
            return state.lstKontact;
        },
        CreateNotUpdate(state){
            return state.bCreateNotUpdate;
        },
        KontactToUpdate(state){
            return state.oKontactToUpdate;
        }
    },
    //sync
    mutations : {
        SetKontacts(state, lstKontact)
        {
            state.lstKontact = lstKontact;
        },
        SetCreateNotUpdate(state, bCreateNotUpdate)
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
    //async
    actions : {
    FetchKontacts({commit})
    {
        return new Promise( (resolve, reject) => 
        {
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
    },
    UpdateKontact({commit}, oKontact)
    {
        return new Promise( (resolve, reject) =>
        {
            fetch(`/kontacts/${oKontact.id}`, {
                method : "PUT", 
                body : JSON.stringify(oKontact) 
            }).then( (response) => {
                resolve(true);
            }, (error) => {
                console.error("error ", error);
                reject(error);
            });
        });
    },
    DeleteKontact({commit}, oKontact)
    {
        return new Promise( (resolve, reject) =>
        {
            fetch(`/kontacts/${oKontact.id}`, {
                method : "DELETE", 
                body : JSON.stringify(oKontact) 
            }).then( (response) => {
                resolve(true);
            }, (error) => {
                console.error("error ", error);
                reject(error);
            });
        });
    },
    CreateKontact({commit}, oKontact)
    {
        return new Promise( (resolve, reject) =>
        {
            fetch(`/kontacts`, {
                method : "POST", 
                body : JSON.stringify(oKontact) 
            }).then( (response) => {
                resolve(true);
            }, (error) => {
                console.error("error ", error);
                reject(error);
            });
        }); 
    }
  }
})

module.exports = store;