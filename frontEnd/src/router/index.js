import Vue from 'vue'
import Router from 'vue-router'
import IntroPage from '@/components/IntroPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'IntroPage',
      component: IntroPage
    }
  ]
})
