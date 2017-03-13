var Vue = require('vue');
var Vuex = require("vuex");
Vue.use(Vuex);


//configure state management
const store = new Vuex.Store({
    
    state: {
        lstKontact : [],
        oKontactToUpdate : {},
        bCreateNotUpdate : undefined,
        bJustDeletedRecord : false
    },
    getters: {
        /**
        * Retrieve the list of kontacts from state 
        * @param {object} state - Vuex state object 
        * @return {array} - list of kontact objects
        */
        Kontacts(state){
            return state.lstKontact;
        },

        /**
        * Retrieve the a boolean that determines if the kontact within the Modify.vue component should be updated or created 
        * @param {object} state - Vuex state object 
        * @return {boolean} - should be created or not
        */
        CreateNotUpdate(state){
            return state.bCreateNotUpdate;
        },
        
        /**
        * Retrieve the kontact that should be updated within the Modify.vue component
        * @param {object} state - Vuex state object 
        * @return {oKontact} - the kontact that should be updated
        */
        KontactToUpdate(state){
            return state.oKontactToUpdate;
        },

        /**
        * If a record has just been deleted, for the primary view for messaging
        * @param {object} state - Vuex state object 
        * @return {boolean}  - true if a record has just been deleted
        */
        JustDeletedRecord(state)
        {
            return state.bJustDeletedRecord;
        }
    },
    //sync
    mutations : {
        /**
        * Set the boolean that identifies if a record has just been deleted
        * @param {object} state - Vuex state object 
        * @param {boolean} bDeleted - if the record has been deleted
        */
        SetJustDeletedRecord(state, bDeleted)
        {
            state.bJustDeletedRecord = bDeleted;
        },

        /**
        * Set the list of kontacts
        * @param {object} state - Vuex state object 
        * @param {array} lstKontact - list of kontacts
        */
        SetKontacts(state, lstKontact)
        {
            state.lstKontact = lstKontact;
        },
        
        /**
        * Set the bool to identify if the Modify.vue component has handling a record that is to be updated or created
        * @param {object} state - Vuex state object 
        * @param {boolean} bCreateNotUpdate - boolean to know if a record is being created or updated
        */
        SetCreateNotUpdate(state, bCreateNotUpdate)
        {
            state.bCreateNotUpdate = bCreateNotUpdate;
        },
        
        /**
        * Set the kontact that is being updated
        * @param {object} state - Vuex state object 
        * @param {object} oKontactToUpdate - kontact object that's being updated
        */
        SetKontactToUpdate(state, oKontactToUpdate)
        {
            state.bCreateNotUpdate = false;
            state.oKontactToUpdate = oKontactToUpdate;
        },
        
        /**
        * Clear the kontact object for the next create/modify call to the Modify.vue component
        * @param {object} state - Vuex state object 
        */
        ClearKontactReference(state)
        {
            state.bCreateNotUpdate = undefined;
            state.oKontactToUpdate = {};
        }
    },
    actions : {

        /**
        * Fetch kontacts from server
        * @param {Vuex.Commit?} commit  - reference to commit resource
        */
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
        
        /**
        * Update kontact call to the server
        * @param {Vuex.Commit?} commit  - reference to commit resource
        * @param {object} oKontact  - kontact object to update
        */
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

        /**
        * Request kontact deletion from the server
        * @param {Vuex.Commit?} commit  - reference to commit resource
        * @param {object} oKontact  - object to delete
        */
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

        /**
        * Request kontact creation from the server
        * @param {}  - 
        * @return {}  - 
        */
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
});

module.exports = store;