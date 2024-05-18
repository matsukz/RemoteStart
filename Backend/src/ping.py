from ping3 import ping

def checkping(ip) -> bool:

    result = ping(ip, timeout = 3)

    if result == False or result is None:
        #PINGの応答がないので電源オフ
        return False
    else:
        #PINGの応答があったので電源オン
        return True