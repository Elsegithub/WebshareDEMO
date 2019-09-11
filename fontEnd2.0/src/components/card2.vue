<template>
    <Card>
        <Button size='large' type="primary" @click="backHome">
                <Icon type="ios-arrow-back" />
                Backward
        </Button>
        <Card>
            <p slot="title">
                <Icon type="ios-film-outline"></Icon>
                {{sendPage.title}}
            </p>
            <a href="#" slot="extra" >
                <Icon type="ios-loop-strong"></Icon>
                {{sendPage.msg}}
            </a>
            <p class="text-wrapper">{{sendPage.txt}}</p>
            <img class="imgtest" src="/upload/upload/do.jpg"/>
        </Card>
    </Card>
</template>
<script>
export default {
    props: ['sendPage'],
    methods:{
        backHome(){
            console.log(1231);
            let pagemsg = {
                page: "cardtest",
            }
            this.$emit("changePage", pagemsg);
        }
    }
}
</script>
<style scoped>
    .text-wrapper{
        white-space: pre-wrap;
    }
    .imgtest{
        width: 100%;
        height: auto;
    }
</style>