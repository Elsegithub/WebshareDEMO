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
    .wz_login{
        text-align: center;
        margin-top: 20px;
    }
</style>
<template>
    <div class="layout">
        <Drawer title="MAGIC" width="500" :closable="false" v-model="value5">
            <!-- <Button @click="value6 = true" type="primary">Two-level Drawer</Button> -->
            <login class="wz_login" :login-do = logindo @childFn = "loginMsg"></login>
        </Drawer>
        <Drawer title="Login" width="380" :closable="false" v-model="value6">
            <loginmain @childFn = "logindoMsg"></loginmain>
        </Drawer>
        <Drawer title="Register" width="380" :closable="false" v-model="value7">
            <register   @childFn = "cancleRe"></register>
        </Drawer>
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
                        灰烬
                    </MenuItem>
                    <MenuItem name="3">
                        <Icon type="ios-musical-notes-outline" />
                        Item 3
                    </MenuItem>
                    <MenuItem name="4">
                        <Icon type="ios-musical-notes-outline" />
                        信息
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
    import login from '@/components/loginorregister'
    import loginmain from '@/components/login'
    import register from '@/components/register'
    export default {
        components: {cardtest,cardtest2,login,loginmain,register},
        data() {
            return{
                choosePage: "cardtest",
                pagemsg: {
                    page:'',
                    titile: '',
                    msg: '',
                    txt: ''
                },
                logindo: {
                    login: false,
                    register: false,
                    logout: true,
                    user: ''
                },
                 value5: false,
                value6: false,
                value7: false
            }
        },
        methods: {
            logindoMsg(logindoMsg){
                console.log(logindoMsg);
                this.logindo = logindoMsg;
                this.value6 = false;
            },
            cancleRe(msg){
                console.log(msg);
                this.value7 = msg.value7;
                this.value6 = msg.value6;
            },
            loginMsg(loginMsg){
                console.log(loginMsg);
                if(loginMsg == "Login"){
                    this.value6 = true;
                }else{
                    this.value7 = true;
                }
            },
            changePage(pagemsg){
                console.log(pagemsg);
                this.choosePage = pagemsg.page;
                this.pagemsg = pagemsg;
            },
            jump(name){
                console.log(name);
                if(name == "1"){
                    this.choosePage = "cardtest";
                }else if(name == "4"){
                    this.value5 = true;
                }else if(name == "2"){
                    let txt = sessionStorage.getItem("name");
                    if(txt == null){
                        this.$Message.error("no login");      
                    }else{
                        console.log(txt);
                    }
                }else{
                    console.log(name);
                }
                
            }
        }
    }
</script>
