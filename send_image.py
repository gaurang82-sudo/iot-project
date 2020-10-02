import argparse
import base64
import binascii
import io
import os
import sys
import threading
import time

from google.cloud import pubsub
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'iot-cloud')
import run-led-gcp


def transmit_image(
        cloud_region, registry_id, device_id, rsa_private_path, ca_cert_path,
        image_path, project_id, service_account_json):
    """Send an inage to a device registry"""

    with io.open(image_path, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    sub_topic = 'events'
    mqtt_topic = '/devices/{}/{}'.format(device_id, sub_topic)

    client = run-led-gcp.get_client(
        project_id, cloud_region, registry_id, device_id,
        rsa_private_path, 'RS256', ca_cert_path,
        'mqtt.googleapis.com', 8883)

    client.loop_start()
    client.publish(mqtt_topic, image_data, qos=1)
    time.sleep(2)
    client.loop_stop()

transmit_image)('us-central1','rap-registry95','rap-device','/home/pi/rsa_private.pem','/home/pi/roots.pem','/home/pi/iot-cloud/download.jpeg','prime-chess-287006',os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))