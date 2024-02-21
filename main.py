import asyncio
from notificationapi_python_server_sdk import notificationapi
from dotenv import load_dotenv
import os
import ssl 

import requests as r
print(r.certs.where())

load_dotenv()

async def send_notification():
  notificationapi.init(
    os.getenv("CLIENT_ID"),
    os.getenv("CLIENT_SECRET")
  )
  
  await notificationapi.send({
    "notificationId": "order_tracking",
    "user": {
      "id": "kbarros@incomm.com",
      "email": "kbarros@incomm.com",
      "number": os.getenv('PERSONAL_NUMBER')
    },
    "mergeTags": {
      "item": "Krabby Patty Burger",
      "address": "124 Conch Street",
      "orderId": "1234567890"
    }
  })
  
asyncio.run(send_notification())