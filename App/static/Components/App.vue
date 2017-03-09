<script>
    const randomcolor = require("randomcolor");

    module.exports = {
        created(){
            this.lstKontact = this.DecorateKontacts(this.lstKontact)
            
        },
        data() {
            return {
                lstKontact : [
                {
                    name : "steve",
                },{
                    name : "max"
                },{
                    name : "yaner"
                },{
                    name : "jacob"
                },{
                    name : "altho"
                },
                {
                    name : "johanna"
                }],
                sFilter : ""
            }
        },
        methods : {
            DecorateKontacts(lstKontact)
            {
                let lstDecoratedKontacts = [];
                lstDecoratedKontacts = this.lstKontact.map(_kontact => {
                    _kontact.color = this.RandomColor();
                    _kontact.media = [
                        {
                            "name" : "/static/img/facebook.png",
                            "link" : "http://facebook.com"
                        },{
                            "name" : "/static/img/twitter.png",
                            "link" : "http://twitter.com"
                        },
                    ]
                    return _kontact;
                });
                return lstDecoratedKontacts;
            },
            RandomColor(hue="", luminosity="light")
            {
                return randomcolor({  hue, luminosity  });
            },
        },
        computed : {
            Kontacts(){
                if(this.sFilter)
                    return this.lstKontact.filter(_record => _record.name.includes(this.sFilter));
                else
                    return this.lstKontact;
            }
        }
        
    }

</script>

<template>
    <div class="kontact-wrapper">
        <div class="kontact-container">
            <div class="kontact-header">
                <div class='kontact-title'>
                    Kontacts
                </div>
                <div class='kontact-add'>
                    +
                </div>
            </div>
            <hr>
            <div class='kontact-filter-container'>
                <input id="filter" v-model="sFilter" placeholder="Filter Kontacts">
                <!--<label for="filter">Filter...</label>-->
            </div>
            <div class="kontact-body-container">
                <div class="kontact-card"  v-for="kontact in Kontacts" v-bind:style="{backgroundColor:kontact.color}">
                    <div class="kontact-card-img-container">
                        <img src="./static/img/person.jpg" alt="">
                    </div>
                    <div class="kontact-card-title-container">
                        {{kontact.name}}
                    </div>
                    <div class="kontact-card-media-container">
                        <a class="kontact-card-media-link" v-for="media in kontact.media" v-bind:href="media.link" >
                            <img v-bind:src="media.name" alt=""> 
                        </a>
                    </div>
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
    }
    .kontact-body-container{
        width: 100%;
        display:flex;
        justify-content:space-around;
        flex-wrap:wrap;
    }
        .kontact-card{
            width:200px;
            height:250px;
            margin:25px;
            border-radius:10px;
            box-shadow:2px 4px 10px #ccc;
            overflow:hidden;
            transition:.75s all ease;
        }.kontact-card:hover{
            opacity:.85;
            margin-top:10px;
        }.kontact-card:hover .kontact-card-media-container{
            margin-left:0;
        }
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
                background-color:#4aa;
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
