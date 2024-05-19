from fastapi import FastAPI
from pydantic import BaseModel
from wol import wake_computer
from ping import checkping
import logging

logger = logging.getLogger("uvicorn")
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

app = FastAPI()

#サーバー情報の定義
class Server_wol(BaseModel):
  mac: str
  ip: str

class Server_ping(BaseModel):
  ip: str

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.post("/wol/")
async def wol(server: Server_wol):

  logging.debug("wolが呼ばれました")

  resutl:int ; resutl = 10
  resutl = wake_computer(server.mac, server.ip)
  
  return {"msg": resutl}

@app.post("/ping/")
async def ping(server: Server_ping):
  return {"msg": checkping(server.ip)}