<script>

    module.exports = {
        props : ['kontact'],
        methods : {
            ClickCard(oKontact)
            {
                this.$store.commit('SetKontactToUpdate', oKontact);
                this.$router.push({path : "/modify"});
            }
        }
    };
</script>

<template>
    <div class="kontact-card-template">
        <div class="kontact-card-img-container" @click="ClickCard(kontact)">
            <img src="./static/img/person.jpg" alt="">
        </div>
        <div class="kontact-card-title-container">
            {{kontact.firstname + ' ' + kontact.lastname}}
        </div>
        <div class="kontact-card-media-container">
            <a class="kontact-card-media-link" v-for="media in kontact.media" v-bind:href="media.link" >
                <img v-bind:src="media.name" alt="alt"> 
            </a>
        </div>
    </div>
</template> 


<style>
    .kontact-card-img-container{
        width:100px;
        height:100px;
        border-radius:50%;
        overflow:hidden;
        cursor:pointer;
        margin: 10px auto 50px auto;
    }.kontact-card-img-container > img{
        width:inherit;
        height:inherit;
    }
    .kontact-card-title-container{
        width:100%;
        text-align:center;
        font-size:20px;
        margin:10px 0 10px 0;
        background-color:#4bb;
        color:white;
    }
    .kontact-card-media-container{
        margin-left:100%;
        width:100%;
        transition:margin .8s ease;
        text-align:center;
    }
    .kontact-card-media-link{
        margin:10px;
    }.kontact-card-media-link > img{
        width:35px;
        height:35px;
        cursor:pointer;
    }
</style>