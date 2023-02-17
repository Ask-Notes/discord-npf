import discord


class Kintama():
    def messager(message):
        channel = message.channel
        content = message.content

        if channel.id == 986992160719130654:
            return "消えろ"
        


class dmg():
    def ayaka(atk, ct, ctd, elementDmg):
        channel = atk.channel
        content = atk.content
        tenpu = 1.09
        if channel.id == 1075291090724323348:
            dmg = (atk * tenpu)*(1+elementDmg)*(1+(ct*ctd))
            return dmg

#型変換のクラス  
class change():
    # str → float
    def changeFloat(text):
        print("おっぱい.py")
        print(text)
        print(type(text))
        num = float(text)
        print(type(num))
        return num
    
    # str → int
    def changeInt(text):
        num = int(text)
        return num
