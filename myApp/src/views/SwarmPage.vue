<template>
    <ion-page>
      <ion-header>
        <ion-toolbar>
          <ion-buttons slot="primary">
            <ion-button href="/">
              <ion-icon slot="icon-only" :icon="exit"></ion-icon>
            </ion-button>
          </ion-buttons>
          <ion-buttons slot="start">
            <ion-menu-button :auto-hide="false"></ion-menu-button>
          </ion-buttons>
          <ion-title class="ion-text-center">Swarm</ion-title>
        </ion-toolbar>
      </ion-header>
      <ion-content :fullscreen="true">

        <div style="margin: 50px" class="autopilot">
          <ion-button class="autopilotButton" @click="takeOff">Take Off</ion-button>
          <ion-button class="autopilotButton" @click="land">Land</ion-button>
        </div>

        <div style="margin: 20px"></div>

        <div style="margin-top: 40px;">
        <div class="direction">

            <div class="buttonTurnL"></div>

            <div class="buttonForward">
                <ion-icon :icon="arrowUp" size="large" id="forward" v-on:click="go($event)"/>
            </div>

            <div class="buttonTurnR"></div>

        </div>
        <div class="direction">  
          
            <div class="buttonLeft">
                <ion-icon :icon="arrowBack" size="large" id="left" v-on:click="go($event)"/>
            </div>

            <div class="buttonStop"></div>

            <div class="buttonRight">
                <ion-icon :icon="arrowForward" size="large" id="right" v-on:click="go($event)"/>
            </div>

        </div>
        <!-- <div class="direction">

            <div class="buttonUp"></div>

            <div class="buttonBack">
                <ion-icon :icon="arrowDown" size="large" id="back" v-on:click="go($event)"/>
            </div>

            <div class="buttonDown"></div>

        </div> -->
      </div>
  
      </ion-content>
    </ion-page>
  </template>
  
  <script>
  import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonButton, IonButtons, IonIcon } from '@ionic/vue';
  import { exit, arrowUp, arrowBack, arrowForward, arrowDown} from 'ionicons/icons';
  import { defineComponent, ref, onMounted } from 'vue'
  import { useMQTT } from 'mqtt-vue-hook'
  
  export default  defineComponent({
    name: 'CameraPage',
    components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage, IonButton, IonButtons, IonIcon },
  
    setup () {
      const mqttHook = useMQTT()

      function takeOff(){
      mqttHook.publish('takeoff','',1)
      mqttHook.publish('stop','',1)
      }

      function land(){
        mqttHook.publish('land','',1)
      }

      function go (event) {
        const dir = event.currentTarget.id;
        mqttHook.publish(dir,'0',1)  
        console.log(dir)   
      }
      
      return {
        arrowUp, 
        arrowBack, 
        arrowForward, 
        arrowDown,
        exit,
        takeOff,
        land,
        go
      }
    }
  });
  </script>
  
  <style>
    .buttonTurnL {
    width: 100px;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgb(16, 26, 205);
    font-size: 18px;
  }
  .buttonForward {
    width: 100px;
    height: 100px;
    border-top: 2px solid  rgb(16, 26, 205);
    border-left: 2px solid  rgb(16, 26, 205);
    border-right: 2px solid  rgb(16, 26, 205);
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgb(16, 26, 205);
    font-size: 18px;
  }
  .buttonTurnR {
    width: 100px;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    color:  rgb(16, 26, 205);
    font-size: 18px;
  }
  .buttonLeft {
    width: 100px;
    height: 100px;
    border-top: 2px solid  rgb(16, 26, 205);
    border-left: 2px solid  rgb(16, 26, 205);
    border-bottom: 2px solid  rgb(16, 26, 205);
    display: flex;
    align-items: center;
    justify-content: center;
    color:  rgb(16, 26, 205);
    font-size: 18px;
  }
  .buttonStop {
    width: 100px;
    height: 100px;
    border-bottom: 2px solid  rgb(16, 26, 205);
    display: flex;
    align-items: center;
    justify-content: center;
    color:  rgb(16, 26, 205);
    font-size: 18px;
  }
  .buttonRight {
    width: 100px;
    height: 100px;
    border-top: 2px solid  rgb(16, 26, 205);
    border-bottom: 2px solid  rgb(16, 26, 205);
    border-right: 2px solid  rgb(16, 26, 205);
    display: flex;
    align-items: center;
    justify-content: center;
    color:  rgb(16, 26, 205);
    font-size: 18px;
  }
  
  </style>