import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import Login from '../views/LogInPage.vue'
import Controll from '../views/ControllPage.vue'
import Camera from '../views/CameraPage.vue'
import Swarm from '../views/SwarmPage.vue'
import Wait from '../views/WaitingPage.vue'
import AdjustSwarm from '../views/SwarmPageAdjust.vue'
import Tabs from '../views/TabsPage.vue'


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: Login
  },
  {
    path: '/DroneControllPage',
    component: Controll
  },
  {
    path: '/DroneCameraPage',
    component: Camera
  },
  
  {
    path: '/DroneWaitingPage',
    component: Wait
  }, 
  {
    path: '/Swarm',
    component: Tabs,
    children: [
      {
        path: '/Swarm',
        redirect: '/Swarm/DroneSwarmPage',
      },
      {
        path: '/Swarm/DroneSwarmPage',
        component: Swarm
      },
      {
        path: '/Swarm/DroneSwarmAdjustPage',
        component: AdjustSwarm
      },
    ],
  },  
   
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
