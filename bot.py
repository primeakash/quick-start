import logging
from pyrogram import Client
from pyrogram.types import Message


from config import Credentials

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Client(name=str(Credentials.PHONE_NUMBER),api_id=Credentials.API_ID,api_hash=Credentials.API_HASH,phone_number=Credentials.PHONE_NUMBER)


@app.on_message()
async def message_handler(client:Client,message:Message):
    pass 


app.run()