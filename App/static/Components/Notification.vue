<template>

    <transition name="slide-fade">
        <div class="notification-wrapper" v-bind:class="[sType]"  v-show="bShow">
            <div class="notification-container">
                {{sMessage}}
            </div>
        </div>
    </transition>
    
</template>

<script>
    module.exports = {
        props : ["bShow", "sMessage", "sType"]
    };
</script>

<style>
    .notification-wrapper{
        position:absolute;
        top:20px;
        right:20px;
        box-shadow: 2px 2px 8px #999;
        padding:18px;
        font-size:22px;
        color:white;
    }

    .success{
        background-color:#3a5;
    }

    .warning{
        background-color:#aa4;
    }

    .error{
        background-color:#f35;

    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s;
    }
    .fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
        opacity: 0;
    }

    .slide-fade-enter-active {
        transition: all .3s ease;
    }
    .slide-fade-leave-active {
        transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
    }
    .slide-fade-enter, .slide-fade-leave-to{
        transform: translateX(10px);
        opacity: 0;
    }
</style>