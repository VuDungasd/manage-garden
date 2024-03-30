import paho.mqtt.client as paho

MQTT_SERVER = "broker.mqttdashboard.com"
MQTT_PORT = 1883
TOPIC = '/htn/g6_smart_garden/' # land/temp/edit
TOPIC_TEMP = '/htn/g6_smart_garden/+/temp'
TOPIC_HUM = '/htn/g6_smart_garden/+/hum'
TOPIC_LIGHT = '/htn/g6_smart_garden/+/light'

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# nhận data rồi set vào db
def on_message(client, userdata, msg):
    global temp, hum
    data = str(msg.payload.decode("UTF-8"))
    print(msg.topic + " " + str(msg.qos) + " " + data)

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
client.subscribe(TOPIC_TEMP, qos=1)
client.subscribe(TOPIC_HUM, qos=1)
client.subscribe(TOPIC_LIGHT, qos=1)
