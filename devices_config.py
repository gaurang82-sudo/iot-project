import argparse
import io
import os
import sys
import time
import json

from google.api_core.exceptions import AlreadyExists
from google.cloud import iot_v1

from google.oauth2 import service_account
from google.protobuf import field_mask_pb2 as gp_field_mask
from googleapiclient import discovery
from googleapiclient.errors import HttpError

sjson={
  "type": "service_account",
  "project_id": "prime-chess-287006",
  "private_key_id": "f09e6c038d7b40fe863aa47850b8f5a12ab280b2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCaTV9OW3s9h6Lr\nM3SfigWUsxhYcykojc1Mt8gfjl/UM+lj4Rq+ErcU4UtsHER543F20XiBzuF5lnjj\n9CRq483dbBKI/rz+RmHlrUQjGdyTuIYu1kGIM0oCOpIB+aonhT2wEELYJqer0Y9N\n5wzQg4XnICaULlpEt70WHMr/A5NbxfLkqAs+9QqD9ydx5oVIFBDXY4MLsd/4jc/O\nYfUH8//AqDxkWhjsL7bJP6B9YIBiGcniM8WrDnnpkXAXYsikuMC1/OY2flofGvOl\nR4/B9rappOvUDg0wBFeS8fq00NZL4MrCA/uQeEV7rEBdIs13D7WFpggV5B2RXEt5\nYFh0ZhAZAgMBAAECggEAB5AOgWiMMSs4VdsRJp8lECFZin9Fd4iAtReGYl6P7ZaI\nREYUkZeY+9fhgphdllRKm8JfS8x0ImmYvgJ5tPf6n3VEMMz8fiF8u507C1XhiOd4\nwyuq7VYnNNYCUUC3gWWfTQV1A0NcwTf9lDnEd+VUXyxFG8rsT3Uqej6Zx/c4xh0J\nbouU0Qqz08kcqaMZPTFXVQgZY5312jRhHYG8tTyl1sMKMyqp2DaXnoLm8SEH5zwk\nfymzB8q5w9lCUkkcz/mqT1v2fjhoptf6VN/WSEz/RkfOpF4xyzghx/YlM8Y7n4BR\n/vnJ7DNt31FJ+E4MUfAyA2Jv81gmqKa2SRTRxqYfsQKBgQDZ6ewadRDdLQ03YZOl\nVbUNED/9eSTqmTz3ynQmsAjxm/S/UDhP9vDwmbQG6lMxi8L/nhQpqRMi9QO4x6P7\nD+HGkg0DjBv5oNQrBSqPgDL2IsNaAyZGifnWXuNh8xVa6Kgjw5sQvbZEAE6R0VQt\nnr8kSkJCXkFC/aNFsiuejtCU8QKBgQC1RUpkUi7xvH5oyVJlgeQUHbxy2yhVC+7m\nOwgtzcXuCs8WSqV3E/5mx2h/JF+fnCVWxPCP7Joxdh7m/0uhsNDHHJzr7QJ7Azju\nohy6v84B1lLWLErMPooFgSu0DL5KICFKgrIgxQqqJKG2B77+Xi+tAqYQeLdn24fv\nAs0/6VuNqQKBgBcjlrWMfrjtoryhuNrSigIUGqdgqMHcebPaJJFDGgAFzmxOKVyc\nXSM/PvWJBkJ5k8Au2fc+g9CvcbC6SjhLjG7YbVdWFlZgdIcI6mcIduDZ+iJhuTu+\nRPA1bTGmbTsU/12k1J9ndaYs3irvrl+VvrgsxnJjrcxeQGsTKzyP76gRAoGBAIJz\nx0HDUz1s5ZwLplyeycEgVUpjJfduixLtUMmF2Peil733InU70k2tHCrDxn1bJhP3\nzxgEskL+OucKuyc11Eo28UdoXeyhOQujZwGOn3b7AspXPc0XBMVJXGZK9XbrAIpa\n3E5w/2fKzQXvNShiJ/VefpxEA9meR4lefs+L5PNhAoGBAIVC+jigRXJgAYHkS2uz\nIH0ld+sJwSZtbuu3m3A0fS3tO26e716iX4WEAuFHkLCKDj1ua2nBhxJpBxw5bfA/\n+Qp6cc+rxZhuC/DgdMWRB2b4BauEwmC2q8c0/syFK/y0KRhmTqLG1/rixqCleoXi\ns8u7q+NVIc67cHcNmHUY0FFu\n-----END PRIVATE KEY-----\n",
  "client_email": "rpi95-276@prime-chess-287006.iam.gserviceaccount.com",
  "client_id": "108361372774527791018",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/rpi95-276%40prime-chess-287006.iam.gserviceaccount.com"
}

  
service_account_json="/home/lucifer/Downloads/prime-chess-287006-2948842cddda.json"


project_id = 'prime-chess-287006'
cloud_region = 'us-central1'
registry_id = 'rap-registry95'
device_id = 'rap-device'
version = 34
config= 'hello'
print("Set device configuration")
client = iot_v1.DeviceManagerClient()
device_path = client.device_path(project_id, cloud_region, registry_id, device_id)

data = config.encode("utf-8")

client.modify_cloud_to_device_config(
    name=device_path, binary_data = data, version_to_update= version
)