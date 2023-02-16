import discord


class Kintama():
    def messager(message):
        channel = message.channel
        content = message.content

        if channel.id == 986992160719130654:
            return "消えろｄさっだｄさだｓｄ"


class ayaka():
    def messager(atk, ct, ctd, elementDmg):
        channel = atk.channel
        content = atk.content
        tenpu = 1.09
        if channel.id == 1075291090724323348:
            dmg = (atk * tenpu)*(1+elementDmg)*(1+(ct*ctd))
            return dmg
