# Web_App_Tello_Drones

En aquest repositori es pot trobar tot el codi desenvolupat durant el treball de final de grau que he realitzat. El projecte consta de la creació d'una aplicació web que permet el control d'un dron Tello EDU o més d'un a la vegada, el que en diem un "Swarm". Dins el repositori es pot trobar la memòria d'aquest projecte on s'explica amb més detall tot el procés de creació i com funciona l'entorn desenvolupat.

# 1. Distribució

Dins d'aquest repositori es troben dues carpetes:

La carpeta myApp on trobarem l'aplicació Web implementada utilitzant Vue i Ionic.

La carpeta TelloControll on estan inclosos els servidors que s'utilitzen per a la comunicació entre el dron i l'aplicació web.

# 2. Instruccions per la instal·lació de l'entorn

Per la Web App, primer de tot, és necessari la instal·lació del framewok Vue.js. Tot i això, Vue requereix abans que ens descarreguem una versió de Node.js superior a la 16.0. (Es recomana fer servir la mateixa versió que s'ha fet servir durant la implementació d'aquest projecte: 16.13.0). Un cop instal·at Node en el nostre ordinador podem procedir amb la instal·lació de l'entorn Vue amb la següent comanda: npm install @vue/cli@4.5.15 (És important que la versió sigui la 4.5.15, ja que podrien haver-hi errors en funcions que s'han creat per a la Web App). Enllaç per descarregar Vue.js i tots els passos a seguir: https://vuejs.org/guide/quick-start.html#creating-a-vue-application

En el cas de Ionic s'ha fet servir la versió 6.20.6. Cal recalcar que quan es posa en marxa el servidor de la web app amb la comanda 'ionic serve' és important utilitzar la consola cmd, ja que amb powershell o d'altres no funcionarà correctament. Enllaç per descarregar Ionic i tots els passos a seguir: https://ionicframework.com/docs/intro/cli

Els servidors que connecten el dron amb la Web App estan implementats en Python i la versió usada és la 3.7.5.

# 3. Vídeos

Més endavant s'afegirà el vídeo explicatiu on es descriuen les idees generals del codi desenvolupat i també dos vídeos on es mostra el moviment dels drons controlats per la Web App en qüestió.
