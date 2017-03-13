<script>

    //register card component
    const Card = require("./Card.vue");
    var Vue = require('vue');
    Vue.component('Card', Card);

    //Register Notification.vue component
    const Notification = require("./Notification.vue");
    var Vue = require('vue');
    Vue.component('Notification', Notification);

    module.exports = {
        created()
        {
            //call store to fetch kontacts and set locally
            this.$store.dispatch("FetchKontacts").then( (lstKontacts) =>
            {
                this.lstKontact = this.$store.getters.Kontacts;
            });
            
            //call store to determine if a record was just deleted
            const bDidJustDeleteRecord = this.$store.getters.JustDeletedRecord;

            //if a record was deleted 
            if(bDidJustDeleteRecord)
            {
                //reset the 'was just deleted' store value to false since we've acknowledged it's value
                this.$store.commit("SetJustDeletedRecord", false);

                //create successfully deleted notification
                this.Notify("Successfully Deleted", 3000, "success");
            }
        },
        data() 
        {
            return {
                //list of kontacts to display
                lstKontact : [],

                //name filter to filter 'lstKontact' by
                sFilter : "",

                //notification message
                sNotifyMessage : "",

                //if we should display the notification panel
                bNotify : false,

                //the type of notification
                sNotifyType : ""
            }
        },
        methods : {

            /**
            * Change views to create a new kontact
            */
            Create()
            {
                //clear the current kontact reference oncase one was previously set, we need the Modify.vue component to create not update
                this.$store.commit("ClearKontactReference");

                //let the Modify.vue view know we're creating a record not updating it
                this.$store.commit("SetCreateNotUpdate", true);

                //change views to the Modify.vue component
                this.$router.push({path : "/modify"});
            },

            /**
            * Pop up the notification UI to notify the user of something
            * @param {string} sMessage - the message the client should see
            * @param {number} iDurationInMS - the duration the modal should exist in Milliseconds
            * @param {string} sNotifyType - the type of notification (success, warning, error)
            */
            Notify(sMessage, iDurationInMS, sNotifyType)
            {
                this.sNotifyMessage = sMessage;
                this.bNotify = true;
                this.sNotifyType = sNotifyType;
                setTimeout( () =>
                {
                    this.bNotify = false;
                }, iDurationInMS)
            }
        },
        computed : {

            /**
            * Run the kontacts through the 'sFilter' variable and filter accordingly if a filter exists
            */
            Kontacts(){

                //creates a full name by concatenating the first and last name with a space.
                const funcFullName = (_record) => _record.firstname.toLowerCase() + ' ' + _record.lastname.toLowerCase();

                //if we have a search filter filter the reocrds based on the 'sFilter' string
                if(this.sFilter)
                    return this.lstKontact.filter(_record => funcFullName(_record).includes(this.sFilter.toLowerCase()) );

                //return just the list of kontacts
                else
                    return this.lstKontact;
            }
        }
        
    }

</script>

<template>
    <div class="kontact-wrapper">

        <Notification v-bind:bShow="bNotify" v-bind:sMessage="sNotifyMessage" v-bind:sType="sNotifyType"></Notification>

        <div class="kontact-container">
            <div class="kontact-header">
                <div class='kontact-title'>
                    Kontact
                </div>
                <div class='kontact-add' @click="Create()">
                    +
                </div>
            </div>
            <hr>
            <div class='kontact-filter-container'>
                <input id="filter" v-model="sFilter" placeholder="Filter Kontacts">
            </div>
            <div class="kontact-body-container">
                <div class="kontact-card"   v-for="kontact in Kontacts" v-bind:style="{backgroundColor:kontact.color}">
                    <Card v-bind:kontact="kontact" />
                </div>
            </div>
        </div>
    </div>
</template>

<style>
    .kontact-wrapper{
        max-width:1000px;
        height:auto;
        margin:0 auto 0 auto;
    }

    .kontact-header{
        display: flex;
        justify-content: space-between;
    }

    .kontact-title{
        font-size:50px;
        margin:5px;
    }

    .kontact-add{
        border: 1px solid #eee;
        box-shadow:2px 2px 7px #aaa; 
        width:50px; 
        height:50px;
        font-size:30px;
        text-align:center;
        margin:15px;
        cursor:pointer;
    }
    .kontact-filter-container{
        width:100%;
    }.kontact-filter-container > input{
        width:100%;
        height:45px;
        font-size:25px;
        text-align:center;
        border-radius:10px;
        background-color: #ddd;
        border:none;
        transition: all .8s ease;
    }.kontact-filter-container > input:focus{
        box-shadow: 2px 2px 2px #aaa ;
    }
    .kontact-body-container{
        width: 100%;
        display:flex;
        justify-content:space-around;
        flex-wrap:wrap;
    }
        .kontact-card{
            width:200px;
            min-height:250px;
            margin:25px;
            border-radius:10px;
            box-shadow:2px 4px 10px #ccc;
            overflow-x:hidden;
            transition:.75s box-shadow ease, .75s opacity ease;
        }.kontact-card:hover{
            opacity:.75;
            box-shadow:4px 6px 10px #aaa;
        }.kontact-card:hover .kontact-card-media-container{
            margin-left:0;
        }
    
</style>
