import paho.mqtt.client as mqtt
from djitellopy import Tello, TelloSwarm

import base64
import time

def on_message(cli, userdata, message):
    global sending_video
    global client

    print(message.topic)
    message.payload = message.payload.decode("utf-8")
    # print(message.payload)

    if message.topic == 'ConnectSwarm':
        client.subscribe('takeoff')
        client.subscribe('land')
        client.subscribe('forward')
        client.subscribe('left')
        client.subscribe('right')
        client.subscribe('back')
        client.subscribe('stop')
        client.subscribe('up')
        client.subscribe('down')
        client.subscribe('TRight')
        client.subscribe('TLeft')
        client.subscribe('state')

        swarm.connect()
        client.publish('connectedSwarm', 'ok')
        for tello in swarm:
            print(tello.get_battery())

    if message.topic == 'takeoff':
        swarm.takeoff()
    elif message.topic == 'land':
        swarm.land()

    elif message.topic == 'forward':
        if message.payload == '0':
            move_drones(message.topic)
        else:
            move_one_drone(message.topic, message.payload)
    elif message.topic == 'left':
        if message.payload == '0':
            move_drones(message.topic)
        else:
            move_one_drone(message.topic, message.payload)
    elif message.topic == 'right':
        if message.payload == '0':
            move_drones(message.topic)
        else:
            move_one_drone(message.topic, message.payload)

    elif message.topic == 'back':
        # swarm.send_rc_control(0, -30, 0, 0)
        print('BACK')
    elif message.topic == 'stop':
        swarm.send_rc_control(0, 0, 0, 0)
    elif message.topic == 'up':
        swarm.send_rc_control(0, 0, 30, 0)
    elif message.topic == 'down':
        swarm.send_rc_control(0, 0, -30, 0)
    elif message.topic == 'TRight':
        swarm.send_rc_control(0, 0, 0, -50)
    elif message.topic == 'TLeft':
        swarm.send_rc_control(0, 0, 0, 50)

def move_drones(direction):
    directions.pop()
    directions.insert(0, direction)
    print(directions)
    for i, tello in zip(directions, swarm):
        if i == 'left':
            tello.rotate_counter_clockwise(90)
        elif i == 'right':
            tello.rotate_clockwise(90)
        # tello.move_forward(50)

    swarm.move_forward(50)


def move_one_drone(dir, drone_id):
    for i, tello in enumerate(swarm):
        if str(i+1) == drone_id:
            tello.move(dir, 20)


def dummy_service():
    global client
    global cap
    # ws://broker.hivemq.com:8000/mqtt (ionic vue)
    broker_address = 'broker.hivemq.com'
    broker_port = 8000
    client = mqtt.Client("Dash", transport="websockets")
    client.on_message = on_message
    client.connect(broker_address, broker_port)
    client.subscribe('ConnectSwarm')
    print('Waiting connection')
    client.loop_forever()


# def get_possible_ips(self):
#     """
#     Gets all the possible IP addresses for subnets that the computer is a part of.
#     :return: List of IP addresses.
#     """
#     infos = self.get_subnets()
#     ips = SubnetInfo.flatten([info.get_ips() for info in infos])
#     ips = list(filter(lambda ip: ip.startswith('192.168.3.'), ips))cmd
#     return ips


if __name__ == '__main__':

    # Before to create the swarm, configurate the drone tello for AP mode ('DESKTOPJanMas', 'janmasmartinez')
    # tello = Tello()
    # tello.connect()
    # bat = tello.get_battery()
    # print('Battery: ', bat)
    # tello.connect_to_wifi('TP-Link_E10A', '73136620')

    # create the swarm with all the drones connected to the AP
    # macs = ['60:60:1F:5D:BD:4D', '60:60:1F:D3:E4:5E', '60:60:1F:DC:32:88']
    # IPs = []
    # out = subprocess.run(["arp", "-a"], check=True, capture_output=True, text=True).stdout
    # res = out.split('\n')
    # for w in res:
    #     if '60-60-1f-dc-32-88' in w or \
    #             '60-60-1f-fd-1b-ca' in w or \
    #             '60-60-1f-5d-bd-4d' in w:
    #         IPs.append(w.split()[0])
    # print(IPs)

    directions = ['forward', 'forward', 'forward']
    IPs = ['192.168.0.101', '192.168.0.102', '192.168.0.103']
    swarm = TelloSwarm.fromIps(IPs)
    # initiate the server
    dummy_service()
