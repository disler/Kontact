<script>
    const randomcolor = require("randomcolor");

    //register card component
    const Card = require("./Card.vue");
    var Vue = require('vue');
    Vue.component('Card', Card);

    module.exports = {
        created(){
            this.$store.dispatch("FetchKontacts").then( (lstKontacts) =>
            {
                this.lstKontact = this.$store.state.lstKontact;
                this.lstKontact = this.DecorateKontacts(this.lstKontact) 
            });
        },
        data() {
            return {
                lstKontact : [],
                sFilter : ""
            }
        },
        methods : {
            DecorateKontacts(lstKontact)
            {
                let lstDecoratedKontacts = [];
                lstDecoratedKontacts = this.lstKontact.map(_kontact => {
                    _kontact.color = this.RandomColor();
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
    
</style>
