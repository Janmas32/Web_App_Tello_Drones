<template>
    <ion-page>
      <ion-header>
        <ion-toolbar>
          <ion-title class="ion-text-center">Drone Engineering Ecosystem</ion-title>
          <ion-progress-bar v-if = "connecting" type="indeterminate"></ion-progress-bar>
        </ion-toolbar>
      </ion-header>
      <ion-content>
        <div style="margin-top: 20px;">
          <ion-list>
            <ion-item>
              <ion-label>Register to login</ion-label>
            </ion-item>
            <ion-item>
              <ion-input v-model="nameInput" placeholder="Your name" ></ion-input>           
            </ion-item>
            <ion-item>
              <ion-input v-model="ageInput" type="number" placeholder="Your age"></ion-input>
            </ion-item>
          </ion-list>
        </div>
        <div style="display: flex; justify-content: center">
          <ion-button :disabled="connecting" @click = 'connect' class="connectButton" >Connect to the tello drone</ion-button>
        </div>
        <div style="display: flex; justify-content: center">
          <ion-button :disabled="connecting" @click = "connectSwarm" class="connectButton" >Connect to the swarm</ion-button>
        </div>
        <div v-if = "connecting" style="display: flex; justify-content: center; margin-top: 50px;">Waiting for a second player</div>
      </ion-content>
    </ion-page>
</template>
  
<script>
  import { defineComponent, ref, onMounted } from 'vue';
  import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonButton, IonItem, IonInput, IonLabel, alertController, IonList, IonProgressBar } from '@ionic/vue';
  import { useRouter } from 'vue-router';
  import { useMQTT } from 'mqtt-vue-hook'
  
  export default  defineComponent({
    name: 'ComponentTab',
    components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage, IonButton, IonItem, IonInput, IonLabel, IonList, IonProgressBar }, 

    setup() {
      const nameInput = ref(undefined);
      const ageInput = ref(undefined);
      const router = useRouter();
      const mqttHook = useMQTT()
      const User = ref();
      const connecting = ref(false)
      
      const interval = setInterval(() => {
        if (connecting.value){
          console.log('waiting...')
          mqttHook.publish('waiting2ndPly','',1)
        }
      }, 1000);

      function connect () {
        // if (nameInput.value == undefined || ageInput.value == undefined){
        //   Alert_blank()
        // }
        // else{
          // console.log('Name:', nameInput.value, 'Age: ', ageInput.value)
          mqttHook.publish('Connect','myAppTello',1)
          // publish('command')
        // }
        
      }
      function connectSwarm () {
        mqttHook.publish('ConnectSwarm','myAppTello',1)
      }

      const Alert_blank = async () => {
        const alert = await alertController.create({
          header: 'Alert',
          subHeader: 'Missing information!',
          message: 'You must write your name and age in order to login.',
          buttons: ['OK'],
        });
      await alert.present();
      };

      const Alert_full = async () => {
        const alert = await alertController.create({
          header: 'Alert',
          subHeader: 'Too many players!',
          message: 'You must wait for the players to finish their game before you can log in.',
          buttons: ['OK'],
        });
      await alert.present();
      };

      onMounted (()=>{
        mqttHook.subscribe('connected', 1)
        mqttHook.registerEvent('connected', (topic, message) => {
          console.log(topic)
          User.value = JSON.parse(message)
          if (User.value == 1){
            console.log('PLAYER 1')
            connecting.value = true
          }
          else if (User.value == 2){
            console.log('PLAYER 2')
            router.push('/DroneWaitingPage')
          }
          else{
            Alert_full()
          }
        });
        mqttHook.subscribe('StartGame', 1)
        mqttHook.registerEvent('StartGame', () => {
          clearInterval(interval)
          router.push('/DroneControllPage')
        })
        mqttHook.subscribe('connectedSwarm', 1)
        mqttHook.registerEvent('connectedSwarm', () => {
          router.push('/Swarm')
        })
      })
      
      return {
        connect,
        connectSwarm,
        nameInput,
        ageInput,
        router,
        Alert_blank,
        Alert_full,
        onMounted,
        User,
        connecting,
        interval
      }
    }
  })
</script>

<style>

.connectButton {
  display: flex;
  margin-top: 30px;
  width: 300px;
}

</style>
  