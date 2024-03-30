from .mqtt import client
try:
    client.loop_start()
except Exception as e:
    print(e)
    client.disconnect()