<template>
    <div>
        <div class="title1" v-bind:style="{backgroundImage:'url('+getImg+')'}">
            <!-- <div class="title2">{{getData}}</div> -->
            <Button class="title2" type="default" :loading="loading" @click="toLoading" ghost>
                <span v-if="!loading" :v-model="getData">{{getData}}</span>
                <span v-else>loading</span>
            </Button>
            <!-- <Button class="title2" type="default" loading>{{getData}}</!--> 
        </div>
        <!-- <img class="img" src="../assets/logo.png"/> -->
    </div>
</template>

<script>
import logoimg from '@/assets/logo.png'
import doimg from '@/assets/do.jpg'
export default {
    props : ['getData','getImg', 'getTxt'],
    data() {
        return{
            logo: '../../../static/image/do.jpg',
            loading: false,
        }
    },
    // mounted() {
    //         let regs = new RegExp("\r", "g");
    //         let reg = new RegExp("\n", "g");
    //         let regSpace = new RegExp(" ", "g");
    //         this.getTxt = this.getTxt.replace(reg, "<br/>");
    //         this.getTxt = this.getTxt.replace(regs, "<br/>");
    //         this.getTxt = this.getTxt.replace(regSpace, "&nbsp;");
    // },
    methods:{
        toLoading(){
            this.loading = true;
            let pagemsg = {
                page: "cardtest2",
                title: this.getData,
                msg: "Test msg",
                txt: this.getTxt
            }
            this.$emit('childFn', pagemsg);
            console.log(this.getData);
        }
    }
}
</script>

<style scoped>
    .card{
        width: auto;
        height: auto;
    }
    .title1{
        /* background-image:url('../assets/logo.png');  */
        text-align: center;
        background-size: cover;
        width:100%;height:300px;
        background-repeat: no-repeat;
        background-attachment:fixed;
        /* filter:alpha(opacity=50);  
        -moz-opacity:0.5;  
        -khtml-opacity: 0.5;  
        opacity: 0.5; */
    }
    .title2{
        /* text-align: center; */
        position: relative;
        top: 40%;
        width: 30%;
        font-size: 30px;
        /* font-family: 'Times New Roman', Times, serif; */
    }
    .img{
        width: 100%;
        height: 200px;
        background-size: cover;
    }
</style>