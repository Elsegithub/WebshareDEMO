<template>
    <Form ref="formInline" :model="formInline" :rules="ruleInline" inline>
        <FormItem prop="username">
            <Input type="text" v-model="formInline.username" placeholder="Username">
                <Icon type="ios-person-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        <FormItem prop="password">
            <Input type="password" v-model="formInline.password" placeholder="Password">
                <Icon type="ios-lock-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="handleSubmit('formInline')">Signin</Button>
        </FormItem>
        <FormItem prop="password">
            <Input type="result" v-model="result" placeholder="result">
                <Icon type="ios-lock-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
    </Form>
</template>
<script>
    import { testPost } from '@/api/api'
    export default {
        data () {
            return {
                result: '',
                formInline: {
                    username: '',
                    password: ''
                },
                ruleInline: {
                    username: [
                        { required: true, message: 'Please fill in the user name', trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: 'Please fill in the password.', trigger: 'blur' },
                        { type: 'string', min: 6, message: 'The password length cannot be less than 6 bits', trigger: 'blur' }
                    ]
                }
            }
        },
        methods: {
            handleSubmit(name) {
                // this.$refs[name].validate((valid) => {
                //     if (valid) {
                //         this.$Message.success('Success!');
                //     } else {
                //         this.$Message.error('Fail!');
                //     }
                // })
                testPost(this.formInline).then(res =>{
                    console.log(res)
                    console.log(res.data)
                    this.result = res.data
                })
            }
        }
    }
</script>
