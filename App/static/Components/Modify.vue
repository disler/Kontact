<script>
    module.exports = {
        create(){
            alert("CREATE");
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
                        <input id="firstname" type="text" placeholder="First Name">
                    </div>
                    <div class="modify-input-container">
                        <label for="lastname">Last Name</label>
                        <input id="lastname" type="text" placeholder="Last Name">
                    </div>
                    <div class="modify-input-container">
                        <label for="dateofbirth">Date of Birth</label>
                        <input id="dateofbirth" type="text" placeholder="Date Of Birth">
                    </div>
                    <div class="modify-input-container">
                        <label for="zipcode">Zip Code</label>
                        <input id="zipcode" type="text" placeholder="Zip Code">
                    </div>
                    <div class="modify-input-container">
                        <label for="facebook">Facebook</label>
                        <input id="facebook" type="text" placeholder="Facebook">
                    </div>
                    <div class="modify-input-container">
                        <label for="twitter">Twitter</label>
                        <input id="twitter" type="text" placeholder="Twitter">
                    </div>
                    <div class="modify-input-container">
                        <label for="linkedin">LinkedIn</label>
                        <input id="linkedin" type="text" placeholder="LinkedIn">
                    </div>
                    <div class="modify-input-container">
                        <label for="youtube">Youtube</label>
                        <input id="youtube" type="text" placeholder="Youtube">
                    </div>
                    <div class="modify-input-container">
                        <label for="whatsapp">WhatsApp</label>
                        <input id="whatsapp" type="text" placeholder="WhatsApp">
                    </div>
                </div>

                <div class="modify-action-container">
                    <div class="modify-action-left-container">
                        <button class="btn red">Delete</button>
                    </div>
                    <div class="modify-action-right-container">
                        <button class="btn green">Save</button>
                        <router-link to="/"><button class="btn grey">Done</button></router-link>
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