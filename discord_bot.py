import discord
import pai

TOKEN = 'OTgzNjMyNjg2NjEyNjE1MTg4.GJcBDe.L0W4ftSPG_PVwHkuuT5KneFHpWhEi8N7yc-_QE' # TOKENを貼り付け
CHANNELID = 983734676365668432 # チャンネルIDを貼り付け
GUILD = 964402354805940225
client = discord.Client(intents=discord.Intents.all())

# 起動時処理
@client.event
async def on_ready():
    print('ログインしました')
    for channel in client.get_all_channels():
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
        print("----------")
    guild = client.get_guild(GUILD)
    
    print(guild.id)
    print(guild.name)
    print(guild.members)
    

    
# チャンネル入退室時の通知処理------------------------------------------------------------------------
@client.event
async def on_voice_state_update(member, before, after):
    
    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(983734676365668432)
    
        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [964402355263123481, 964402355263123481]
    
        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("**" + before.channel.name + "** チャンネルから、__" + member.name + "__  が抜けました！")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("**" + after.channel.name + "** チャンネルに、__" + member.name + "__  が参加しました！")
            
@client.event
async def on_reaction_add(reaction, user):

    # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
    botRoom = client.get_channel(983734676365668432)
    sabun = 0
    #　承認機能絵文字処理------------------------------------------------------------------------
    msid = reaction.message.author.id
    if user.id != msid :
        if reaction.emoji.id == 977208213986476093:
            if reaction.count - sabun == 3 and reaction.message.channel.id == 980453265563066398 :
                await botRoom.send("3人以上の承認が行われたので、"+reaction.message.author.nick+"早退届・遅刻届を受理致します。お疲れ様でした。")
        if reaction.emoji.id == 988403148072841236:
            if reaction.count - sabun == 1 and reaction.message.channel.id == 980453265563066398 :
                await botRoom.send("ドウェインジョンソン承認が行われたので、"+reaction.message.author.nick+"の早退届・遅刻届を強制受理致します。お疲れしたア。")
        if reaction.emoji.id == 978485509368188999:
            if reaction.count - sabun == 3 and reaction.message.channel.id == 980453265563066398 :
                await botRoom.send("3人以上の差し戻しが行われたので、"+reaction.message.author.nick+"早退届・遅刻届を再投稿お願いします。")
        if reaction.emoji.id == 988405507595305080:
            if reaction.count - sabun == 1 and reaction.message.channel.id == 980453265563066398 :
                await botRoom.send("橋本先生のガン萎えを確認しました。"+reaction.message.author.nick+"強制差し戻し致します。「おーとっやらかしたぁ・・・ チっ　もぉー！」")
    else :
        sabun = sabun +1
    
    botRoom = client.get_channel(994559802292314173)
    guild = client.get_guild(GUILD)
    print ("ここまで来たよやったね！")
    role = guild.get_role(992298617052348466)#容疑者ID
    sabun = 0
    mscotent = reaction.message.content
    if reaction.emoji.id == 977208213986476093:
        if reaction.count - sabun == 1 and reaction.message.channel.id == 994559802292314173 :
            if "社畜ではまい！" in mscotent :
                memberlist = guild.members
                for cnt in range(len(memberlist)):
                    user = memberlist[cnt]
                    print("ここ")
                    print(user)
                    if user.id == 766190879127502858:
                        user.add_rolse(role)
                men = client.get_user()
                print(men)
                await botRoom.send("3人以上の承認が行われたので、"+men.name+"を逮捕いたします。十分に反省してください。")
            if "社畜でびっくり！" in mscotent :
                for cnt in range(len(user)):
                    user = user[cnt]
                    if user.id == 607448697827229706:
                        user.add_rolse(role)
                        await botRoom.send("3人以上の承認が行われたので、"+reaction.message.author.nick+"を逮捕いたします。十分に反省してください。")
            if "突き刺さった社畜" in mscotent:
                await botRoom.send("3人以上の承認が行われたので、"+reaction.message.author.nick+"を逮捕いたします。十分に反省してください。")
            if "SUNバタコ" in mscotent:
                await botRoom.send("3人以上の承認が行われたので、"+reaction.message.author.nick+"を逮捕いたします。十分に反省してください。")
            if "56513" in mscotent:
                await botRoom.send("3人以上の承認が行われたので、"+reaction.message.author.nick+"を逮捕いたします。十分に反省してください。")
            if "ゆー者" in mscotent:
                await botRoom.send("3人以上の承認が行われたので、"+reaction.message.author.nick+"を逮捕いたします。十分に反省してください。")
        
def selectuser(user):
   if 766190879127502858 == user:
       return 1
   elif 607448697827229706 == user:
       return 2


@client.event
async def on_message(message):
    print(message.author.id)
    channel = message.channel
    content = message.content
    user = message.author.id
    Selection = 0
    character = ["神里","宵宮","胡桃"]
    usermap = [True,True,True],[True,True,True],[True,True,True],[True,True,True],[True,True,True],
    menber = 0
    count = 3
    ###　二次元配列の定義はこんな感じ(usermap)
    #             "神里","宵宮","胡桃"etc...... 
    #             _____________________________            
    #一宮　　　　｜_____|_____|_____|_____|____|
    #植松　　　　｜_____|_____|_____|_____|____|
    #金谷　　　　｜_____|_____|_____|_____|____|
    #宇野ちゃん　｜_____|_____|_____|_____|____|
    #吉田　　　　｜_____|_____|_____|_____|____|
    ###


    def check(m):
        return float(m.content) and m.channel == channel

    #　原神ダメージ計算処理-------------------------------------------------------------------------------------------------------------------
    if content.find("c//") and channel.id == 1075291090724323348:
        comand = content[idx+3:]  # スライスで半角空白文字のインデックス＋3以降を抽出
        if character[1] == comand:
            await channel.send("神里のダメージ計算を開始します")
            await channel.send("神里の攻撃力値を入力してください")
            Selection = 1
            menber = selectuser(user)
            usermap[menber][Selection] = True
        elif character[2] == comand:
            await channel.send("宵宮のダメージ計算を開始します")
            Selection = 2
            menber = selectuser(user)
            usermap[menber][Selection] = True
        elif character[3] == comand:
            await channel.send("胡桃のダメージ計算を開始します")
            Selection = 3
            menber = selectuser(user)
            usermap[menber][Selection] = True
    
    #　原神ダメージ計算引継ぎロジック---------------------------------------------------------------------------------
    if content.find(1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9)&channel.id == 1075291090724323348:
        try:
           content = float(content)
           menber = selectuser
           for continer in count:
               if True == usermap[menber][continer]:
                   if continer == 1:
                       attack = content
                       await channel.send("会心率値を入力してください")
                       ct = await client.wait_for('message', check=check)
                       await channel.send("会心ダメ値を入力してください")
                       ctd = await client.wait_for('message', check=check)
                       await channel.send("元素バフ値を入力してください")
                       elementDmg = await client.wait_for('message', check=check)
                       dmg = pai.dmg.ayaka(attack, ct, ctd, elementDmg)
        except TypeError as e:
            print(e)
            await channel.send(e)

        await channel.send("予想されるダメージは"+dmg+"です")
            


    #　お試し金谷君
    if content == "金谷":
       str = pai.Kintama.messager(message)
       await channel.send(str)
    
    if channel.id == 986992160719130654:
        if content == "s//":
            await channel.send("m!dc")
    
    if channel.id == 986992160719130654:
        idx = content.find('m//')
        comand = content[idx+3:]  # スライスで半角空白文字のインデックス＋3以降を抽出
        asta = "m//"
        if  asta in content:
            await channel.send("m!play "+comand)
    
    if channel.id == 986992160719130654:
        idx = content.find('g//')
        comand = content[idx+3:]  # スライスで半角空白文字のインデックス＋1以降を抽出
        asta = "g//"
        if  asta in content:
            result = "https://game8.jp/genshin/search?q="+comand
            await channel.send(result)

    messager = message.author.roles
    print (messager)
    for number  in range(len(messager)):
        role = messager[number]
        if role.name == "容疑者（逮捕済み）":
            await message.delete()
    
    if channel.id == 986992160719130654:
        we = client.get_channel(994559802292314173)
        idx = content.find('t//')
        comand = content[idx+3:]  # スライスで半角空白文字のインデックス＋3以降を抽出
        asta = "me1"
        if  asta in comand:
            await we.send("「社畜ではまい！」に逮捕状が卸されました。逮捕する場合三人以上の承認が必要です。投票お願いします。")
        asta = "me2"
        if  asta in comand:
            await we.send("「社畜でびっくり！」に逮捕状が卸されました。逮捕する場合三人以上の承認が必要です。投票お願いします。")
        asta = "me3"
        if  asta in comand:
            await we.send("「突き刺さった社畜」に逮捕状が卸されました。逮捕する場合三人以上の承認が必要です。投票お願いします。")
        asta = "me4"
        if  asta in comand:
            await we.send("「SUNバタコ」に逮捕状が卸されました。逮捕する場合三人以上の承認が必要です。投票お願いします。")
        asta = "me5"
        if  asta in comand:
            await we.send("「56513」に逮捕状が卸されました。逮捕する場合三人以上の承認が必要です。投票お願いします。")
        asta = "me6"
        if  asta in comand:
            await we.send("「ゆー者」に逮捕状が卸されました。逮捕する場合三人以上の承認が必要です。投票お願いします。")

            
client.run(TOKEN)