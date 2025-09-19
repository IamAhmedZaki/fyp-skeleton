import asyncio
import base64
import json 
import os
import dotenv import load_dotenv

load_dotenv()

def sts_connect():
    api_key=os.getenv("DEEPGRAM_API_KEY")
    if not api_key:
        raise Exception("DEEPGRAM_API_KEY not found ")
    sts_ws= websockets.connect(
        uri:"wss://agent.deepgram.com/v1/agent/converse",
        subprotocols=["token",api_key]
    )
    
    return sts_ws

def load_config():
    with with open('config.json', 'r') as f:
       return json.load(f   )