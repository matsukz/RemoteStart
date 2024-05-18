from wakeonlan import send_magic_packet
from ping3 import ping
import time
import logging

logger = logging.getLogger("uvicorn")
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def wake_computer(mac,ip) -> int:
    # マジックパケットを送信する関数
    try:
        wake:bool ; wake = True
        for _ in range(10):

            ping_result = ping(ip,timeout=2)
            if ping_result == False or ping_result is None:
                wake = True

            else:
                return 0

            logging.debug(f"PINGの結果は{wake}でした")

            #起動シグナル送信
            logging.debug(f"{ip}にマジックパケットを送信します")
            send_magic_packet(mac,ip_address=ip)

            time.sleep(1)

        return 1
    
    except Exception as e:
        return 2

# 使用例
# mac = '047C16A35C06'
# ip = "192.168.11.21"
#wake_computer(mac,ip)

# def test(mac,ip):
#     return {"mac":mac,"ip":ip}

