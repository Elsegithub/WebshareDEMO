<template>
    <div>
        <Card>
            <i-form :model="cx" :label-width="100">
                <i-col span="6">
                    <Form-item label="username">
                        <i-input :value.sync="cx.username" placeholder="请输入" style="width:200px"></i-input>
                    </Form-item>
                </i-col>
                <br>
                <i-col span="6">
                    <Form-item label="email">
                        <i-input :value.sync="cx.email" placeholder="请输入" style="width:200px"></i-input>
                    </Form-item>                    
                </i-col>
                <br>
                <Form-item style="text-align:left">
                    <!-- <i-button type="primary">提交</i-button> -->
                    <i-button type="primary"  icon="md-search" @click="search()">search</i-button>
                </Form-item>
            </i-form>
            <br>
            <i-table border :content="self" :columns="columns7" :data="data6"></i-table>
        </Card>
    </div>
</template>
<script>
    import { search_list } from '@/api/api'
    export default {
        data () {
            return {
                cx: {
                    username: '',
                    email: ''
                },
                self: this,
                columns7: [
                    {
                        title: 'id',
                        key: 'id',
                        // render (row, column, index) {
                        //     return `<Icon type="person"></Icon> <strong>${row.id}</strong>`;
                        // }
                        render: (h, params) => {
                            return h('div',[
                                h('Icon', {
                                    props: {
                                        type: 'person'
                                    }
                                }),
                                h('strong', {}, params.row.id)
                            ]);
                        }
                    },
                    {
                        title: 'username',
                        key: 'username'
                    },
                    {
                        title: 'password',
                        key: 'password'
                    },
                    {
                        title: 'email',
                        key: 'email'
                    },
                    {
                        title: 'sex',
                        key: 'sex'
                    },
                    {
                        title: 'lrrq',
                        key: 'lrrq'
                    },
                    {
                        title: '操作',
                        key: 'action',
                        width: 150,
                        align: 'center',
                        render: (h, params) => {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'primary',
                                    size: 'small'
                                },
                                style: {
                                    marginRight: '5px'
                                },
                                on: {
                                    click: () => {
                                        this.show(params.index)
                                    }
                                }
                            }, 'View'),
                            h('Button', {
                                props: {
                                    type: 'error',
                                    size: 'small'
                                },
                                on: {
                                    click: () => {
                                        this.remove(params.index)
                                    }
                                }
                            }, 'Delete')
                            ]);
                        }
                    }
                ],
                data6: [
                    {
                        id: '1',
                        username: 'ewew',
                        email: '123123',
                        password: '12321312',
                        sex: '12321312'
                    }
                ]
            }
        },
        methods: {
            show (index) {
                this.$Modal.info({
                    title: '用户信息',
                    content: `姓名：${this.data6[index].username}<br>密码：${this.data6[index].password}<br>地址：${this.data6[index].email}`
                })
            },
            remove (index) {
                let a = this.data6[index].password;
                this.data6.splice(index, 1);
                console.log(a)
            },
            search(){
                search_list().then(res =>{
                    console.log(res.data[0].id)
                    this.data6 = res.data
            
                    // for(let i = 0; i < res.date.size(); i++){
                    //     params.id = res.data[i].id;
                    //     params.username = res.data[i].username;
                    //     params.password = res.data[i].password;
                    //     params.email = res.data[i].email;
                    //     params.sex = res.data[i].sex;
                    //     params.lrrq = res.data[i].lrrq;
                    //     data6[i] = params
                    // }
                })
            }
        },
        beforeRouteEnter(to, from, next){
            window.document.body.style.backgroundColor = '#C0C0C0';
            next();
        },
        beforeRouteLeave(to, from, next){
            window.document.body.style.backgroundColor = '';
            next();
        },
        mounted(){
            
        }
    }
</script>

<style scoped>
    .bg {
        background-color: burlywood
    }
</style>