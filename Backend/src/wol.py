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
        for _ in range(20):

            #pingを実行して対象がオンラインなのかを確認する
            ping_result = ping(ip,timeout=2)
            if ping_result == False or ping_result is None:
                #応答があるなら続行する
                wake = True

            else:
                #応答があればFastAPIに0を返す
                return 0

            logging.debug(f"PINGの結果は{wake}でした")

            #起動シグナル送信
            logging.debug(f"{ip}にマジックパケットを送信します")
            send_magic_packet(mac,ip_address=ip)

            time.sleep(1)

        return 1 #20回のうちにオンラインにならなければ1を返す
    
    except Exception as e:
        #エラーが発生したら2を返す
        return 2