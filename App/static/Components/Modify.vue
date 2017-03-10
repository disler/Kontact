<script>
    const Util = require("../util");

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
                bCreateNotUpdate : true,
                oKontact : {
                    id : -1,
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
        methods: {
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

                //create
                if(this.bCreateNotUpdate === true)
                {
                    this.$store.dispatch("CreateKontact", oKontactToSave).then( (success) => {
                        console.log("Successfully saved");
                    }, (error) => {
                        console.error("error Creating kontact", error);
                    });
                }
                //update
                else
                {
                    this.$store.dispatch("UpdateKontact", oKontactToSave).then( (success) => {
                        console.log("Successfully saved");
                    }, (error) => {
                        console.error("error updating kontact", error);
                    });
                }
            },
            Delete()
            {
                let oKontactToDelete = this.oKontact;
                this.$store.dispatch("DeleteKontact", oKontactToDelete).then( (success) =>{
                    console.log("Successfully Deleted");
                }, (error) =>{
                    console.error("error deleting kontact", error);
                });
            }
        }
    }
</script>

<template>
    <div class="modify-template">
        <div class="modify-wrapper">
            <div class="modify-container">
                <div class="modify-header-container">
                    Kontacts
                </div>
                <hr>

                <div class="modify-content-container">
                    <div class="modify-input-container">
                        <label for="firstname">First Name</label>
                        <input id="firstname" type="text" placeholder="First Name" v-model="oKontact.firstname">
                    </div>
                    <div class="modify-input-container">
                        <label for="lastname">Last Name</label>
                        <input id="lastname" type="text" placeholder="Last Name" v-model="oKontact.lastname">
                    </div>
                    <div class="modify-input-container">
                        <label for="dateofbirth">Date of Birth</label>
                        <input id="dateofbirth" type="text" placeholder="Date Of Birth" v-model="oKontact['date of birth']">
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
                        <button class="btn red" v-show="bCreateNotUpdate === false" @click="Delete()">Delete</button>
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
        margin:0 auto 0 auto;
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

    input, label{
        display:block;
    }
</style>