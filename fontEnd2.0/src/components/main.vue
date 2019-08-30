<style scoped>
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
    }
    .layout-logo{
        width: auto;
        height: auto;
        /* background-image: url('../assets/logo.png'); */
        border-radius: 3px;
        float: left;
        position: relative;
        /* top: 5px; */
        left: 20%;
    }
    .layout-header{
        height: 60px;
        background: #fff;
        box-shadow: 0 1px 1px rgba(252, 250, 250, 0.1);
    }
    .layout-copy{
        text-align: center;
        padding: 10px 0 20px;
        color: #9ea7b4;
    }
    .layout-ceiling{
        background: #464c5b;
        padding: 10px 0;
        overflow: hidden;
    }
    .layout-ceiling-main{
        float: right;
        margin-right: 15px;
    }
    .layout-ceiling-main a{
        color: #9ba7b5;
    }
    .layout-nav{
        width: 420px;
        margin: 0 auto;
        margin-right: 20%;
        float: right;
    }   
    .cardtest{
        /* float: left;
        width: 60%;
        height: auto;
        position: relative;
        left: 10px;
        top: 5px; */
        width: 60%;
        margin: 0 auto;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .cardtest2{
        float: right;
        width: 37%;
        height: auto;
        position: relative;
        right: 10px;
        top: 5px;
    }
</style>
<template>
    <div class="layout">
        <!-- <div class="layout-ceiling">
            <div class="layout-ceiling-main">
                <a href="/#/hello">注册登录</a> |
                <a href="#">帮助中心</a> |
                <a href="#">安全中心</a> |
                <a href="#">服务大厅</a>
            </div>
        </div> -->
        <div class="layout-header">
            <Menu mode="horizontal"  active-name="1" @on-select="jump">
                <div class="layout-logo">
                    <h2 style="text-decoration:;">Everglow</h2>
                </div>
                <div class="layout-nav">
                    <MenuItem name="1">
                        <Icon type="ios-musical-notes-outline" />
                        主页
                    </MenuItem>
                    <MenuItem name="2">
                        <Icon type="ios-musical-notes-outline" />
                        Item 2
                    </MenuItem>
                    <MenuItem name="3">
                        <Icon type="ios-musical-notes-outline" />
                        Item 3
                    </MenuItem>
                    <MenuItem name="4">
                        <Icon type="ios-musical-notes-outline" />
                        Item 4
                    </MenuItem>
                </div>
            </Menu>
        </div>
        <div style="height: auto">
            <div class="cardtest">
                <component :is="choosePage" :sendPage= this.pagemsg v-on:changePage="changePage" />
            </div>
            <!-- <div class="cardtest2">
                <cardtest2/>
            </div> -->
        </div>
        <div class="layout-copy">
            2019-2020 &copy; Everglow
        </div>
    </div>
</template>
<script>
    import cardtest from '@/components/card1'
    import cardtest2 from '@/components/card2'
    export default {
        components: {cardtest,cardtest2},
        data() {
            return{
                choosePage: "cardtest",
                pagemsg: {
                    page:'',
                    titile: '',
                    msg: '',
                    txt: ''
                }
            }
        },
        methods: {
            changePage(pagemsg){
                console.log(pagemsg);
                this.choosePage = pagemsg.page;
                this.pagemsg = pagemsg;
            },
            jump(name){
                console.log(name);
                if(name == "1"){
                    this.choosePage = "cardtest";
                }else{
                    console.log(name);
                }
            }
        }
    }
</script>
