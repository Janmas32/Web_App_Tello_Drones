# Web_App_Tello_Drones

En aquest repositori es pot trobar tot el codi desenvolupat durant el treball de final de grau que he realitzat. El projecte consta de la creació d'una aplicació web que permet el control d'un dron Tello EDU o més d'un a la vegada, el que en diem un "Swarm". Dins el repositori es pot trobar la memòria d'aquest projecte on s'explica amb més detall tot el procés de creació i com funciona l'entorn desenvolupat.

# 1. Distribució

Dins d'aquest repositori es troben dues carpetes:
- La carpeta myApp on trobarem l'aplicació Web implementada utilitzant Vue i Ionic.
- La carpeta TelloControll on estan inclosos els servidors que s'utilitzen per a la comunicació entre el dron i l'aplicació web. El fitxer main.py és pel control individual del dron, i el fitxer main_swarm.py és pel control de més d'un dron.

# 2. Instruccions per la instal·lació de l'entorn

Per la Web App, primer de tot, és necessari la instal·lació del framewok Vue.js. Tot i això, Vue requereix abans que ens descarreguem una versió de Node.js superior a la 16.0. (Es recomana fer servir la mateixa versió que s'ha fet servir durant la implementació d'aquest projecte: 16.13.0). Un cop instal·at Node en el nostre ordinador podem procedir amb la instal·lació de l'entorn Vue amb la següent comanda: npm install @vue/cli@4.5.15 (És important que la versió sigui la 4.5.15, ja que podrien haver-hi errors en funcions que s'han creat per a la Web App). Enllaç per descarregar Vue.js i tots els passos a seguir: https://vuejs.org/guide/quick-start.html#creating-a-vue-application

En el cas de Ionic s'ha fet servir la versió 6.20.6. Cal recalcar que quan es posa en marxa el servidor de la web app amb la comanda 'ionic serve' és important utilitzar la consola cmd, ja que amb powershell o d'altres no funcionarà correctament. Enllaç per descarregar Ionic i tots els passos a seguir: https://ionicframework.com/docs/intro/cli

Els servidors que connecten el dron amb la Web App estan implementats en Python i la versió usada és la 3.7.5.

# 3. Vídeos

Més endavant s'afegirà el vídeo explicatiu on es descriuen les idees generals del codi desenvolupat i també dos vídeos on es mostra el moviment dels drons controlats per la Web App en qüestió.

#

# Web_App_Tello_Drones

In this repository you can find all the code developed during the final thesis that I have done. The project consists of the creation of a web application that allows the control of a Tello EDU drone or more than one at a time or a Swarm. In the repository you can find the memo of this project where it is explained in more detail the whole process of creation and how the developed environment works.

# 1. Distribution

In this repository there are two folders:
- The myApp folder where we will find the Web application implemented using Vue and Ionic.
- The TelloControll folder where the servers used for the communication between the drone and the web application are included. The main.py folder is for individual control of the drone, and the main_swarm.py folder is for control of more than one drone.

# 2. Instructions for the installation of the environment

For the Web App, first of all, it is necessary to install the Vue.js framework. However, Vue requires that we first download a version of Node.js higher than 16.0. (It is recommended to use the same version that has been used during the implementation of this project: 16.13.0). Once Node is installed on our computer we can proceed with the installation of the Vue environment with the following command: npm install @vue/cli@4.5.15 (It is important that the version is 4.5.15, since there could be errors in functions that have been created for the Web App). Link to download Vue.js and all the steps to follow: https://vuejs.org/guide/quick-start.html#creating-a-vue-application

In the case of Ionic, version 6.20.6 has been used. It is important to emphasize that when the web app server is started with the command 'ionic serve' it is important to use the cmd console, since it will not work correctly with powershell or others. Link to download Ionic and all the steps to follow: https://ionicframework.com/docs/intro/cli

The servers that connect the drone to the Web App are implemented in Python and the version used is 3.7.5.

# 3. Videos

Later on we will add the explanatory video where the general ideas of the developed code are described and also two videos where the movement of the drones controlled by the Web App is shown.




