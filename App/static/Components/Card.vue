<script>

    module.exports = {
        props : ['kontact'],
        methods : {
            /**
            * A card has been clicked to be investigated, set it and change the view to the Modify.vue component
            * @param {object} oKontact - kontact record to be possibly modified
            */
            ClickCard(oKontact)
            {
                this.$store.commit('SetKontactToUpdate', oKontact);
                this.$router.push({path : "/modify"});
            },

            /**
            * Ensures a media url link contains 'http' as the prefix 
            * @param {string} sLink - link to validate
            * @return {string} string  - valid link
            */
            EnsureValidLink(sLink)
            {
                if(sLink.indexOf("http") > -1)
                    return sLink;
                else
                    return "http://" + sLink;
            }
        }
    };
</script>

<template>
    <div class="kontact-card-template">
        <div class="kontact-card-img-container" @click="ClickCard(kontact)">
            <!-- <img src="./static/img/person.jpg" alt="">-->
            <img v-bind:src="kontact.face" alt="">
        </div>
        <div class="kontact-card-title-container">
            {{kontact.firstname + ' ' + kontact.lastname}}
        </div>
        <div class="kontact-card-media-container">
            <a class="kontact-card-media-link" v-for="media in kontact.media" v-show="media.link != ''" v-bind:href="EnsureValidLink(media.link)" target="_blank">
                <img v-bind:src="media.icon" alt="alt"> 
            </a>
        </div>
    </div>
</template> 


<style>
    .kontact-card-img-container{
        width:118px;
        height:118px;
        border-radius:50%;
        overflow:hidden;
        cursor:pointer;
        margin: 10px auto 0 auto;
    }.kontact-card-img-container > img{
        width:inherit;
        height:inherit;
    }
    .kontact-card-title-container{
        width:100%;
        text-align:center;
        font-size:20px;
        margin:30px 0 3.5px 0;
        background-color:#4bb;
        color:white;
    }
    .kontact-card-media-container{
        margin-left:100%;
        width:100%;
        transition:margin .8s ease;
        text-align:center;
        margin-bottom:5px;
    }
    .kontact-card-media-link{
        margin:10px;
    }.kontact-card-media-link > img{
        width:35px;
        height:35px;
        cursor:pointer;
    }
</style>