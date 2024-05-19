from wakeonlan import send_magic_packet
from ping3 import ping
import time
import logging

def wake_computer(mac,ip) -> int:
    # マジックパケットを送信する関数
    try:
        wake:bool ; wake = True
        for _ in range(30):

            #pingを実行して対象がオンラインなのかを確認する
            ping_result = ping(ip,timeout=2)
            if ping_result == False or ping_result is None:
                #応答があるなら続行する
                wake = True

            else:
                #応答があればFastAPIに0を返す
                return 0

            #起動シグナル送信
            send_magic_packet(mac,ip_address=ip)

            time.sleep(1)

        return 1 #20回のうちにオンラインにならなければ1を返す
    
    except Exception as e:
        #エラーが発生したら2を返す
        return 2