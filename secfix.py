import math

def sectotime(sec): #秒をsecとして受け取り週日時分秒の形式で返す
    fixedtime = ""
    week = sec // 604800
    sec %= 604800
    day = sec // 86400
    sec %= 86400
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60

    if week == 0:
        pass
    else:
        fixedtime += f"{week}w, "
    if day == 0:
        pass
    else:
        fixedtime += f"{day}d, "
    if hour == 0:
        pass
    else:
        fixedtime += f"{hour}h, "
    if min == 0:
        pass
    else:
        fixedtime += f"{min}m, "
    fixedtime += f"{sec}s"
    
    return fixedtime


def mintotimejp(min): #分をminとして受け取り日本語で時間分秒の形式で返す
    f, i = math.modf(min)
    i = int(i)
    fixedtime = ""
    hour = 0
    if i > 0:
        hour = i // 60
        i -= hour * 60
    sec = int(f * 60)

    if hour == 0:
        pass
    else:
        fixedtime += f"{hour}時間"
    if i == 0:
        pass
    else:
        fixedtime += f"{i}分"
    if sec == 0:
        pass
    else:
        fixedtime += f"{sec}秒"

    return fixedtime