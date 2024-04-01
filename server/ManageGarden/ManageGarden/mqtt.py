import paho.mqtt.client as paho
import json

MQTT_SERVER = "broker.mqttdashboard.com"
MQTT_PORT = 1883
TOPIC = '/htn/g6_smart_garden/' # land/temp/edit
TOPIC_CAMBIEN = '/htn/g6_smart_garden/+/cambien'
TOPIC_HANHDONG = '/htn/g6_smart_garden/+/hanhdong'

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# nhận data rồi set vào db
def on_message(client, userdata, msg):
    global temp, hum
    data = msg.payload.decode("UTF-8")
    try:
        sensor_data = json.loads(data)
        temp = sensor_data["temp"]
        hum = sensor_data["hum"]
        print("Received data from topic {}: Temperature: {}, Humidity: {}".format(msg.topic, temp, hum))
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

    # if msg.topic == topicTem:
    #     temp = data
    # if msg.topic == topicHum:
    #     hum = data

    # if temp != "" and hum != "":
    #     print(temp, hum)
    #     with open("data.txt", "a+", encoding="UTF-8") as file:
    #         file.write(temp + "; " + hum + "; " + str(datetime.now()) + "\n")
    #     temp, hum = "", ""
    # if msg.topic == topicAsk:
    #     ask = data
    #     client.publish(topicAnswer, Answer(ask), qos=0)


client = paho.Client(paho.CallbackAPIVersion.VERSION1)
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT)
# đăng ký các chủ đề (topics) để nhận dữ liệu từ broker MQTT
client.subscribe(TOPIC_CAMBIEN, qos=1)
client.subscribe(TOPIC_HANHDONG, qos=1)
