<template>
    <div class="kontact-wrapper">
        <div class="kontact-container">
            <div class="kontact-header">
                <div class='kontact-title'>
                    <h2>Kontacts</h2>
                </div>
                <div class='kontact-add'>
                    +
                </div>
            </div>
            <hr>
            <div class='kontact-filter-container'>
                
            </div>
            <div class="kontact-body-container">
                {{msg}}
            </div>
        </div>
    </div>
</template>

<style>
    .kontact-wrapper{
        border: 1px solid black;
        max-width:1000px;
        height:auto;
        margin:0 auto 0 auto;
    }

    .kontact-header{
        display: flex;
        justify-content: space-between;
    }

    .kontact-title{
        
    }

    .kontact-add{
        border: 1px solid #aaa;
        box-shadow:2px 2px 2px #888; 
    }
</style>

<script>
    class App {
        data() {
            return {
                msg : "Test"
            }
        }
    }

    module.exports = new App();
</script>