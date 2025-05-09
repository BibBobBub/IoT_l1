from paho.mqtt import client as mqtt_client
import json
import time
from schema.aggregated_data_schema import AggregatedDataSchema
from file_datasource import FileDatasource
import config


def connect_mqtt(broker, port):
    """Create MQTT client"""
    print(f"CONNECT TO {broker}:{port}")

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to MQTT Broker ({broker}:{port})!")
        else:
            print("Failed to connect {broker}:{port}, return code %d\n", rc)
            exit(rc)  # Stop execution

    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    client.loop_start()
    return client


def publish(client, topic, datasource, delay):
    datasource.startReading()
    while True:
        time.sleep(delay)
        data = datasource.read()
        #msg = AggregatedDataSchema().dumps(data)
        '''
        msg, errors = AggregatedDataSchema().dump(data), AggregatedDataSchema().validate(data)
        print(errors)  # See if 'cars' is causing issues

        #print(msg)
        print(data)
        '''
        from dataclasses import asdict
        data_dict = asdict(data)  # Convert object to dictionary
        msg = AggregatedDataSchema().dumps(data_dict)
        print(data_dict)
        #print(msg)
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            pass
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")


def run():
    # Prepare mqtt client
    #config.MQTT_BROKER_HOST = "test.mosquitto.org"
    #config.MQTT_BROKER_HOST = "127.0.0.1"
    client = connect_mqtt(config.MQTT_BROKER_HOST, config.MQTT_BROKER_PORT)
    print(config.MQTT_BROKER_HOST)
    # Prepare datasource
    datasource = FileDatasource("data/data.csv", "data/gps_data.csv", "data/traffic_data.csv")
    try: # Infinity publish data
        publish(client, config.MQTT_TOPIC, datasource, config.DELAY)
    except:
        print("err")


if __name__ == "__main__":
    run()
