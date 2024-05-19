from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from wol import wake_computer
from ping import checkping

app = FastAPI()

#CORSエラー対策
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

#サーバー情報の定義
class Server_wol(BaseModel):
  mac: str
  ip: str

class Server_ping(BaseModel):
  ip: str

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.post("/api/wol/")
async def wol(server: Server_wol):

  resutl:int ; resutl = 10
  resutl = wake_computer(server.mac, server.ip)
  
  return {"msg": resutl}

@app.post("/ping/")
async def ping(server: Server_ping):
  return {"msg": checkping(server.ip)}