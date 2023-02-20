import discord


class Kintama():
    def messager(message):
        channel = message.channel
        content = message.content

        if channel.id == 986992160719130654:
            return "消えろ"


# ダメージ計算式
class dmg():
    # 神里綾華
    def ayaka(atk, ct, ctd, elementDmg):
        print("ここは金玉")
        atk =  change.changeFloat(atk)
        ct =  change.changeFloat(ct)
        ctd =  change.changeFloat(ctd)
        elementDmg =  change.changeFloat(elementDmg)
        print(atk)
        print(ct)
        print(ctd)
        print(elementDmg)
        ct = (ct/100)
        ctd = (ctd/100)
        kaisin = (1+(ct*ctd))
        zokusei = (1+(elementDmg/100))
        tenpu = 1.09
        kougeki = (atk * tenpu)
        dmg = kougeki * zokusei * kaisin
        return str(dmg)

# 型変換のクラス2.757496,,,1.616,,,2552.78


class change():
    # str → float
    def changeFloat(text):
        print("ここは変換")
        print(type(text))
        num = float(text)
        return num

    # str → int
    def changeInt(text):
        num = int(text)
        return num
