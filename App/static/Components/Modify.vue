<script>
    const Util = require("../util");
    const randomcolor = require("randomcolor");

    const Notification = require("./Notification.vue");
    const Vue = require("vue");
    Vue.component('Notification', Notification);


    module.exports = {
        created(){
            const bCreateNotUpdate = this.$store.getters.CreateNotUpdate;
            if(bCreateNotUpdate === false)
            {
                this.bCreateNotUpdate = false;
                const oKontactToUpdate = this.$store.getters.KontactToUpdate;
                this.SetKontactToUpdate(oKontactToUpdate);
            }
            else
            {
                this.bCreateNotUpdate = true;
            }
        },
        data(){
            return {
                bNotify : false,
                sNotifyMessage : "",
                bDeleteConfirmDisplay : false,
                bCreateNotUpdate : true,
                oKontact : {
                    id : -1,
                    face : "/static/img/heads/head0.jpg",
                    color : this.RandomColor(),
                    firstname : "",
                    lastname : "",
                    "date of birth" : "",
                    "zip-code" : "",
                    media : {
                        "facebook" : {
                            icon : "./static/img/facebook.png",
                            name : "facebook",
                            link : ""
                        },
                        "twitter" : {
                            icon : "./static/img/twitter.png",
                            name : "twitter",
                            link : ""
                        },
                        "linkedin" : {
                            icon : "./static/img/linkedin.png",
                            name : "linkedin",
                            link : ""
                        },
                        "youtube" : {
                            icon : "./static/img/youtube.png",
                            name : "youtube",
                            link : ""
                        },
                        "whatsapp" : {
                            icon : "./static/img/whatsapp.png",
                            name : "whatsapp",
                            link : ""
                        },
                    }
                },
            }
        },
        computed: {
            FullName()
            {
                return this.oKontact.firstname + ' ' + this.oKontact.lastname; 
            }
        },
        methods: {
            RandomColor(hue="", luminosity="light")
            {
                return randomcolor({  hue, luminosity  });
            },
            SetKontactToUpdate(oKontact)
            {
                this.oKontact = Util.DeepMerge({}, this.oKontact, oKontact);
            },
            Done()
            {
                this.$store.commit("ClearKontactReference");
                this.$router.push({path : "/"});
            },
            Save()
            {
                let oKontactToSave = this.oKontact;

                if(this.Validate(oKontactToSave))
                {
                    //create
                    if(this.bCreateNotUpdate === true)
                    {
                        this.$store.dispatch("CreateKontact", oKontactToSave).then( (success) => {
                            this.Notify("Successfully Saved", 3000, "success");
                        }, (error) => {
                            console.error("error Creating kontact", error);
                        });
                    }
                    //update
                    else
                    {
                        this.$store.dispatch("UpdateKontact", oKontactToSave).then( (success) => {
                            this.Notify("Successfully Updated", 3000, "success");
                        }, (error) => {
                            console.error("error updating kontact", error);
                        });
                    }
                }
            },
            Delete()
            {
                let oKontactToDelete = this.oKontact;
                this.$store.dispatch("DeleteKontact", oKontactToDelete).then( (success) =>{
                    this.$store.commit("SetJustDeletedRecord", true);
                    this.$router.push({path : "/"});
                }, (error) =>{
                    console.error("error deleting kontact", error);
                });

            },
            Validate(oKontactToValidate)
            {
                if(!oKontactToValidate.firstname || !oKontactToValidate.lastname)
                {
                    this.Notify("First Name and Last Name are required", 5000, "error");
                    return false;
                }
                if( oKontactToValidate["date of birth"] )
                {
                    if( false == (/^\d{2}\/\d{2}\/\d{4}$/).test(oKontactToValidate["date of birth"]))
                    {
                        this.Notify("Date of Birth must be in format dd/mm/yyyy", 5000, "error");
                        return false;
                    }
                }

                const bValidMedia = Object.values(oKontactToValidate.media).every(_media => {
                    if(_media.link && _media.link.length > 0)
                    {
                        if( false == (/[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi).test(_media.link))
                        {
                            this.Notify(`The ${_media.name} url is invalid`, 5000, "error");
                            return false;
                        }
                        else
                            return true;
                    }

                    return true;
                })

                if(false === bValidMedia)
                    return false;
                


                return true;
            },
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
        }
    }
</script>

<template>
    <div class="modify-template">

        <Notification v-bind:bShow="bNotify" v-bind:sMessage="sNotifyMessage" v-bind:sType="sNotifyType"></Notification>

        <div class="modify-wrapper">
            <div class="modify-container">
                <div class="modify-header-container">
                    Kontacts
                </div>
                <hr>

                <div class="modify-user-container" v-bind:style="{backgroundColor:oKontact.color}">
                    <div class="modify-user-img-container">
                        <img v-bind:src="oKontact.face" alt="">
                    </div>
                    <div class="modify-user-name-container">
                        {{FullName}}
                    </div>

                </div>

                <div class="modify-content-container">
                    <div class="modify-input-container">
                        <label for="firstname">*First Name</label>
                        <input id="firstname" type="text" placeholder="First Name" v-model="oKontact.firstname">
                    </div>
                    <div class="modify-input-container">
                        <label for="lastname">*Last Name</label>
                        <input id="lastname" type="text" placeholder="Last Name" v-model="oKontact.lastname">
                    </div>
                    <div class="modify-input-container">
                        <label for="dateofbirth">Date of Birth</label>
                        <input id="dateofbirth" type="text" placeholder="Date Of Birth mm/dd/yyyy" v-model="oKontact['date of birth']">
                    </div>
                    <div class="modify-input-container">
                        <label for="zipcode">Zip Code</label>
                        <input id="zipcode" type="text" placeholder="Zip Code" v-model="oKontact['zip-code']">
                    </div>
                    <div class="modify-input-container">
                        <label for="facebook">Facebook</label>
                        <input id="facebook" type="text" placeholder="Facebook" v-model="oKontact.media.facebook.link">
                    </div>
                    <div class="modify-input-container">
                        <label for="twitter">Twitter</label>
                        <input id="twitter" type="text" placeholder="Twitter" v-model="oKontact.media.twitter.link">
                    </div>
                    <div class="modify-input-container">
                        <label for="linkedin">LinkedIn</label>
                        <input id="linkedin" type="text" placeholder="LinkedIn" v-model="oKontact.media.linkedin.link">
                    </div>
                    <div class="modify-input-container">
                        <label for="youtube">Youtube</label>
                        <input id="youtube" type="text" placeholder="Youtube" v-model="oKontact.media.youtube.link">
                    </div>
                    <div class="modify-input-container">
                        <label for="whatsapp">WhatsApp</label>
                        <input id="whatsapp" type="text" placeholder="WhatsApp" v-model="oKontact.media.whatsapp.link">
                    </div>
                </div>

                <div class="modify-action-container">
                    <div class="modify-action-left-container">
                        <div class="modify-action-left-inner" v-show="bCreateNotUpdate === false">
                            <div v-show="bDeleteConfirmDisplay===false">
                                <button class="btn red"  @click="bDeleteConfirmDisplay = true">Delete</button>
                            </div>
                            <div v-show="bDeleteConfirmDisplay===true">
                                <span class="text-big">Are you sure?</span>
                                <span>
                                    <button class="btn red" @click="Delete()">Delete</button>
                                </span>
                                <span>
                                    <button class="btn grey" @click="bDeleteConfirmDisplay = false">No</button>
                                </span>
                            </div>
                        </div>
                    </div>
                    <div class="modify-action-right-container">
                        <button class="btn green" @click="Save()">Save</button>
                        <button class="btn grey" @click="Done()">Done</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
    .modify-wrapper{
        max-width:1000px;
        height:auto;
        margin:0 auto 25px auto;
    }

    .modify-header-container{
        font-size:50px;
        margin:5px;
    }
    .modify-content-container{
        width:100%;
        display:flex;
        justify-content:space-between;
        flex-wrap:wrap;
    }
    .modify-input-container{
        width:49%;
    }.modify-input-container > input{
        margin:0 0 25px 0;
        width:100%;
        height:50px;
        font-size:24px;
        border-radius:5px;
        border:none;
        border-bottom:1px solid #aaa;
        border-left:1px solid #aaa;
        padding:15px;
    }
    .modify-action-container{
        display:flex;
        justify-content:space-between;
    }

    .modify-user-container{
        border-radius:10px;
        width:200px;
        min-height:200px;
        margin: 10px auto 10px auto;
        padding:10px 0 10px 0;
        transition:1s all ease;
    }

    .modify-user-img-container{
        width:118px;
        height:118px;
        border-radius:50%;
        overflow:hidden;
        cursor:pointer;
        margin: 10px auto 0 auto;
    }
    .modify-user-img-container > img{
        width:inherit;
        height:inherit;

    }
    .modify-user-name-container{
        margin: 10px auto 0 auto;
        font-size:22px;
        text-align:center;
        background-color:#4bb;
        color:white;
    }

    input, label{
        display:block;
    }
</style>