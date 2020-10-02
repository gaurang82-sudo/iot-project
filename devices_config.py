

import os


import json


from google.cloud import iot_v1

from google.oauth2 import service_account






project_id = 'prime-chess-287006'
cloud_region = 'us-central1'
registry_id = 'rap-registry95'
device_id = 'rap-device'
version = 34
config= 'off'
print("Set device configuration")
client = iot_v1.DeviceManagerClient()
device_path = client.device_path(project_id, cloud_region, registry_id, device_id)

data = config.encode("utf-8")

client.modify_cloud_to_device_config(
    name=device_path, binary_data = data,
)