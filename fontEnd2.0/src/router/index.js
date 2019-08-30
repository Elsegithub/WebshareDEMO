import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import test from '@/components/test'
import tableDemo from '@/components/tableDemo'
import main from '@/components/main'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },
    {
      path: '/',
      name: 'main',
      component: main
    }
  ]
})
