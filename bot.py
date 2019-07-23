from pyrogram import Client, Filters, MessageHandler
from pyrogram.api import functions, types
import redis, random, time, os, requests, configparser, re
import jdatetime

#BY JESUS
#Version 1.1
#in the name of "mame"



config = configparser.ConfigParser()
config.read("config.ini")
c = config["jesus_self"]
r = redis.StrictRedis(decode_responses=True)


#Do Not Fucking touch this shits
#isshhconnect = False # Just for Jss
#sshc = None # //
app = Client(c["SEASION_NAME"],int(c["API_ID"]),c["API_HASH"])
helptext = """
> l 
>> forward, link
قفل لینک یا فوروارد
l link

> m 
>> photo ,sticker, text, voice, gif
قفل فرد حتی در پیوی با ریپلای 
m text

> addf
>> fosh
افزودن فحش
addf ممه

> list
>> help
راهنمای لیست ها
list help

> pin
پین کردن با ریپلای

> ck
سیک کردن افراد با ریپلای 

> clearf
پاک کردن فحش ها
> clearb
پاک کردن بلک لیست

> reload
کصنمک بازی در اوردن جلوی بقیه

> d
حذف

> fuck it
نمودن طرف با ریپلی 
> del fuck
حذف طرف از بلک لیست با ریپلای

> py
ران کردن اسکریپت پایتون با ریپلای 
بلد نیستی دس نزن

> p
>> bitcoin, bitcoin-cash , ...
قیمت تمام ارزای مجاری
p bitcoin

> id
بدست اوردن ایدی عددی هرچیزی با ریپلای

> server
مقدار استفاده شده از سرور

> action
فعال و غیرفعال کردن اکشن در چت ها
همون تایپینگ پلینگ و غیره

> action 
>> all, users, off, clear, list
قعال کردن در همه یا گروه یا پیوی ها
پاکسازی ایدی هایی ک در انجا فعال است

> settings
تنظیمات

> setaction
>> PLAYING,...
اگه نمیدونی چیه اینو بزن
Actionlist

> spamf
>> 1 ela 100
فوش دادن به طرف با ریپلی کردن روش
توجه کن اگه فوش ساز روشن باشه فوشایی ک اضافه کردید رو نمیفرسته

> spam
>> 1 ela 100
اسپم کردن چیزی با فورواردش 

> Nobody
ست کردن وضعیت انلاینی شما روی Nobody can see

> Everybody
ست کردن وضعیت انلاینی شما روی everybody can see

> filterf
روشن کردن فیلتر کردن فحشا
مخصوص گروهایی ک فحش قفله توش

> fmaker
روشن و خاموش کردن فحش ساز 
روشن باشه خودش رندوم فوش میده
فحش یا فوش بکیرم ک اشتبا نوشتم

> seen
سین خودکار گپایی ک توشون این رو فرستادید 

> seen 
>> group, pv, channel
سین خودکار گپ یا پیوی و چنل ها

> unmark 
>> id ya hichi
سین نزدن این چت ها مخصوص وقتی ک گذاشتید همرو سین بزنه

Good Luck!
@D_P_R
"""

def me(app):
    my = app.get_me()
    uid = my.id
    return uid


def admins(app,message):
    chatid = message.chat.id
    nn = app.get_chat_members(chatid,filter="administrators").chat_members
    admin = [i.user.id for i in nn]
    return admin


if not r.get("autodeltime"): r.set("autodeltime", "10")


#######BOSS MODE#######
#Deleted
######################


###MAKE FOUSH###
four = [
    "تو",
    "وسط",
    "لا",
    "داخل",
    "رو",
]

three = [
    "ننت",
    "خالت",
    "مادرت",
    "نانات",
    "مامانت",
    "خواهرت",
    "خارت",
    "ننه جندت",
    "خار جندت",
    "خاله جندت",
    "مادر جندت",

]
two = [
    "کص",
    "مهبل",
    "سولاخ",
    "کث",
    "ممه",
    "کون",
    "صورت",
    "گوش",
    "ناف",
    "گردن",
    "کتف",
    "رون",
    "لاپا",
    "کبص",
    "کوبص",
    "چشم",
    
]
one = [
    "کیرم",
    "کیر خلیل",
    "دسته مبل",
    "ایفون صوتی با سیم",
    "گوشیم",
    "بزرکترین برج هاای جهان به ترتیب",
    "کیر امام اخر",
    "کیر امام خلیل",
    "کیر خمینی",
    "کیر عظیم حضرت جیزز",
    "کیر امام جیزز",
    "هایپ ایرانی",
    "هایپ خارجی",
    "قاب سیلی کونی",
    "چاقو میوه خوری",
    "جیتوز",
    "تصمیم کبری",
    "تصمیم خلیل",
    "کیر حلزون",
    "کیر فیل",
    "کیر خر",
    "کیر زرافه",
    "خرتوم فیل",
    "جفت پاهای جلوی فیل",
    "کص ننت",
    "کفشم",
    "سشوار",
    "کیر پلاستیکی",
    "ظروف یکبار مصرف",
    "سیب",
    "خیار",
    "دوتا موز",
    "سه تا موز",
    "چهارتا موز",
    "کیر اسب ابی",
    "کیر میمون",
    "کیر خلیل پلاستیکی",

]

imoji = [
    "😂😂😂",
    " ",
    " ",
    "😂😂",
    " ",
    "😂",
    "🤡",

]


def makef():
    o1 = random.choice(one)
    o2 = random.choice(two)
    o3 = random.choice(three)
    o4 = random.choice(imoji)
    o5 = random.choice(four)
    text1 = f"{o1} {o5} {o2} {o3} {o4}"
    return text1


locks = [
    "link",
    "forward",
]

mutes = [
    "text",
    "photo",
    "sticker",
    "gif",
    "voice",
]




def mark(app, message):
    dialog_peer = app.resolve_peer(message.chat.id)
    try:
        app.send(functions.channels.ReadHistory(dialog_peer, 0))
    except:
        app.send(functions.messages.ReadHistory(dialog_peer, 0))



@app.on_message(Filters.regex("^[Ll] (.*)$") & Filters.group , group=-20)
def jss_lock(client, message):
    lock = message.text.split(" ")[1]
    chatid = message.chat.id
    userid = message.from_user.id
    if userid != me(app):return
    if lock not in locks:return
    if str(chatid) in r.smembers("lock"+lock):
        r.srem("lock"+lock,str(chatid))
        text = f"`{lock}` __UNlocked__ JSS!"
    else:
        r.sadd("lock"+lock,str(chatid))
        text = f"`{lock}` __Locked__ JSS!"

    send = app.edit_message_text(chatid, message.message_id, text)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(message.chat.id,[send.message_id])


# Input Link
@app.on_message(Filters.regex(r"[Hh][Tt][Tt][Pp]|[tT].[Mm][Ee]|[Ww][Ww][Ww]|\.[Mm][Ee]") & Filters.group , group=-21)
def jss_link(client, message):
    chatid = message.chat.id
    userid = message.from_user.id
    if int(userid) in admins(app,message): return
    if str(chatid) not in r.smembers(f"locklink"):return
    app.delete_messages(chatid,[message.message_id])


# Input Forward
@app.on_message(Filters.forwarded & Filters.group, group=-22)
def jss_forawrd(client, message):
    chatid = message.chat.id
    userid = message.from_user.id
    if int(userid) in admins(app,message): return
    if str(chatid) not in r.smembers(f"lockforward"):return
    app.delete_messages(chatid,[message.message_id])



@app.on_message(Filters.reply & Filters.regex("^[Mm] (.*)$"))
def jss_reply(client, message):
    m = message.text.split(" ")[1]
    fname = message.reply_to_message.from_user.first_name
    userid = message.reply_to_message.from_user.id
    myid = message.from_user.id
    if myid != me(app):return
    if m not in mutes:return
    if str(userid) == str(547038341):return
    if str(userid) in r.smembers("mute"+m):
            r.srem("mute"+m,str(userid))
            text = f"`{m}` __UNmuted__ for **{fname}**\nBy JSS!"
    else:
        r.sadd("mute"+m,str(userid))
        text = f"`{m}` __Muted__ for **{fname}**\nBy JSS!"

    send =app.edit_message_text(message.chat.id,message.message_id,text)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(message.chat.id,[send.message_id])


def filterfosh(f):
    if "کص" in f:
        f = f.replace("کص", "ک.ص")
    if "خار" in f:
        f = f.replace("خار", "خ.ار")
    if "کس" in f:
        f = f.replace("کس", "ک.س")
    if "کیر" in f:
        f = f.replace("کیر", "ک.یر")
    if "ننت" in f:
        f = f.replace("ننت", "ن.نت")
    if "جنده" in f:
        f = f.replace("جنده", "ج.نده")
    if "سیک" in f:
        f = f.replace("سیک", "س.یک")
    if "تخم" in f:
        f = f.replace("تخم", "ت.خم")
    if "ممه" in f:
        f = f.replace("ممه", "ممع")
    if "مادر" in f:
        f = f.replace("مادر", "م.ادر")
    return f
    
@app.on_message(Filters.text & Filters.group)
def jss_text(client, message):
    chatid = message.chat.id
    userid = message.from_user.id
    if str(userid) in r.smembers("mutetext"):
        app.delete_messages(chatid,[message.message_id])
    if str(userid) in r.smembers("blacklist"):
        fosh = random.choice(list(r.smembers("fosh")))
        if r.get("fmaker") == "on":
            fosh = makef()
        if r.get("filterfosh") == "on": fosh = filterfosh(fosh)
        app.send_message(chatid,fosh, reply_to_message_id=message.message_id)


@app.on_message(Filters.text & Filters.private, group=-23)
def jss_text_priv(client, message):
    chatid = message.chat.id
    userid = message.from_user.id
    if str(userid) in r.smembers("mutetext"):
        app.delete_messages(chatid,[message.message_id])
    if str(userid) in r.smembers("blacklist"):
        fosh = random.choice(list(r.smembers("fosh")))
        if r.get("fmaker") == "on":
            fosh = makef()
        if r.get("filterfosh") == "on": fosh = filterfosh(fosh)
        app.send_message(chatid,fosh, reply_to_message_id=message.message_id)


@app.on_message(Filters.text & Filters.me, group=-2)
def jss_text_me(client, message):
    rmsg = None
    text = message.text

    if text in r.hgetall("cards"):
        txt = r.hgetall("cards")[text]
        send = app.edit_message_text(message.chat.id, message.message_id, txt)
        if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(message.chat.id,[send.message_id])
    elif text in r.hgetall("qanswer"):
        txt = r.hgetall("qanswer")[text]
        t = txt.split(":")
        if message.reply_to_message:
            rmsg = message.reply_to_message.message_id

        if t[0] == "GIF":
            #sendgif
            app.send_animation(message.chat.id,t[1], reply_to_message_id=rmsg)
        elif t[0] == "STICKER":
            app.send_sticker(message.chat.id, t[1], reply_to_message_id=rmsg)

        elif t[0] == "VN":
            app.send_video_note(message.chat.id, t[1], reply_to_message_id=rmsg)

        elif t[0] == "VOICE":
            app.send_voice(message.chat.id, t[1], reply_to_message_id=rmsg)

        elif t[0] == "VIDEO":
            app.send_video(message.chat.id, t[1], reply_to_message_id=rmsg)

        elif t[0] == "DOC":
            app.send_document(message.chat.id, t[1], reply_to_message_id=rmsg)

        elif t[0] == "PHOTO":
            app.send_photo(message.chat.id, t[1], reply_to_message_id=rmsg)

        app.delete_messages(message.chat.id, [message.message_id])
    
    else:return



@app.on_message(Filters.regex("^[Aa]ddf (.*)"), group=6)
def jss_addfo(client,message):
    _ = message.text.split(" ")[0]
    fo = message.text.replace(_,"")
    r.sadd("fosh",fo)
    myid = message.from_user.id
    if myid != me(app):return
    text = f"`ADD shd`"
    app.delete_messages(message.chat.id,[message.message_id])



@app.on_message(Filters.regex("[Dd]elf (.*)"), group=4)
def jss_delfo(client, message):
    _ = message.text.split(" ")[0]
    fo = message.text.replace(_,"")
    r.srem("fosh",fo)
    myid = message.from_user.id
    if myid != me(app):return
    text = f"`Del shd`"
    app.delete_messages(message.chat.id,[message.message_id])



#@app.on_message(Filters.regex("[Ll]istf"), group=5)
def l_listf(message):
    fl = r.smembers("fosh")
    text = ""
    count = 1
    for i in fl:
        text = text + f"{count} - `{i}`\n"
        count+=1
    send =app.edit_message_text(message.chat.id,message.message_id,text)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(message.chat.id,[send.message_id])



@app.on_message(Filters.regex("(\d*) ta (\d*) (.*)"), group=3)
def jss_count(client, message):
    from_ = message.text.split(" ")[0]
    n = message.text.split(" ")[2]
    text = message.text
    count = f"{from_} ta {n} "
    text = text.replace(count, "")
    myid = message.from_user.id
    if myid != me(app):return
    for i in range(int(from_),int(n)):
        app.send_message(message.chat.id,str(i))
    app.send_message(message.chat.id,str(text))



@app.on_message(Filters.animation & (Filters.group | Filters.private), group=-5)
def jss_gif(client, message):
    chatid = message.chat.id
    userid = message.from_user.id
    if str(userid) not in r.smembers("mutegif"):return
    app.delete_messages(chatid,[message.message_id])


@app.on_message(Filters.voice & (Filters.group | Filters.private), group=-6)
def jss_voice(client, message):
    chatid = message.chat.id
    userid = message.from_user.id
    if str(userid) not in r.smembers("mutevoice"):return
    app.delete_messages(chatid,[message.message_id])


@app.on_message(Filters.photo & (Filters.group | Filters.private), group=-7)
def jss_photo(client, message):
    chatid = message.chat.id
    userid = message.from_user.id
    if str(userid) not in r.smembers("mutephoto"):return
    app.delete_messages(chatid,[message.message_id])



@app.on_message(Filters.sticker & (Filters.group | Filters.private), group=-8)
def jss_sticker(client, message):
    chatid = message.chat.id
    userid = message.from_user.id
    if str(userid) not in r.smembers(f"mutesticker"):return
    app.delete_messages(chatid,[message.message_id])





@app.on_message(Filters.group & Filters.reply & Filters.regex("^([Cc]k)$"), group=2)
def jss_ck(client,message):
    myid = message.from_user.id
    if myid != me(app):return
    userid = message.reply_to_message.from_user.id
    fname = message.reply_to_message.from_user.first_name
    app.kick_chat_member(message.chat.id,userid)
    text = f"**{fname}** __Cked__ ;)"
    send =app.edit_message_text(message.chat.id,message.message_id,text)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.group & Filters.reply & Filters.regex("^[Pp]in$") , group=1)
def jss_pin(client,message):
    myid = message.from_user.id
    if myid != me(app):return
    msgid = message.reply_to_message.message_id
    app.pin_chat_message(message.chat.id,msgid )
    text = f"**Pin** __Shd__ ;)"
    send =app.edit_message_text(message.chat.id,message.message_id,text)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(message.chat.id,[send.message_id])
    
reloadl = [
    "`start reloading`",
    "░░░░░░░░░░░░░░",
    "▓░░░░░░░░░░░░░",
    "▓▓░░░░░░░░░░░░",
    "▓▓▓░░░░░░░░░░░",
    "▓▓▓▓░░░░░░░░░░",
    "▓▓▓▓▓░░░░░░░░░",
    "▓▓▓▓▓▓░░░░░░░░",
    "▓▓▓▓▓▓▓░░░░░░░",
    "▓▓▓▓▓▓▓▓░░░░░░",
    "▓▓▓▓▓▓▓▓▓░░░░░",
    "▓▓▓▓▓▓▓▓▓▓░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
    "reloading.",
    "reloading..",
    "reloading...",
    "reloading.",
    "reloading..",
    "reloading...",
    "reloading.",
    "reloading..",
    "reloading...",
    "`reloaded! :)`",
]

#Just For Fun :)
@app.on_message((Filters.group|Filters.private) & Filters.regex("^[Rr]eload$") , group=1)
def jss_reload(client,message):
    myid = message.from_user.id
    if myid != me(app):return
    for i in reloadl:
        time.sleep(0.2)
        send =app.edit_message_text(message.chat.id,message.message_id,i)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])



@app.on_message(Filters.regex("^[Ff]uck it$") & Filters.reply , group=1)
def jss_addblacklist(client,message):
    myid = message.from_user.id
    userid = message.reply_to_message.from_user.id
    if myid != me(app):return
    r.sadd("blacklist",str(userid))
    app.delete_messages(message.chat.id,[message.message_id])




@app.on_message(Filters.regex("^[Dd]el fuck$") & Filters.reply , group=7)
def jss_delblacklist(client,message):
    myid = message.from_user.id
    userid = message.reply_to_message.from_user.id
    if myid != me(app):return
    r.srem("blacklist",str(userid))
    app.delete_messages(message.chat.id,[message.message_id])



@app.on_message(Filters.regex("^[Pp]y$") & Filters.reply , group=8)
def jss_runpy(client,message):
    myid = message.from_user.id
    text = message.reply_to_message.text
    if myid != me(app):return
    with open("script.py", "a+") as f_w:
        f_w.write(text)
    os.system("python3 script.py > out.txt")
    with open("out.txt", "r") as f_r:
        out = f_r.read()
        out = "Output:\n" + out
    os.remove("script.py")
    os.remove("out.txt")
    send =app.edit_message_text(message.chat.id,message.message_id,out)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.regex("^[Dd]$"),group=9)
def jss_delete(client,message):
    myid = message.from_user.id
    if myid != me(app):return
    msgid = message.reply_to_message.message_id
    mymsg = message.message_id
    app.delete_messages(message.chat.id, [msgid,mymsg])



@app.on_message(Filters.regex("^[Cc]learb$") , group=10)
def jss_clearf(client,message):
    myid = message.from_user.id
    if myid != me(app):return
    r.delete("blacklist")
    send =app.edit_message_text(message.chat.id,message.message_id,"`Blacklist` is Clear Now")
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])

@app.on_message(Filters.regex("^([Ii]d)$") , group=11)
def jss_myid(client,message):
    myid = message.from_user.id
    if myid != me(app):return
    if "reply_to_message" in str(message):
        if message.reply_to_message.forward_from_chat:
            uid = message.reply_to_message.forward_from_chat.id
        else:
            uid = message.reply_to_message.from_user.id
    else:
        uid = message.chat.id
    send =app.edit_message_text(message.chat.id,message.message_id,f"`{uid}`")
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.regex("^([Pp]) (.*)$") , group=12)
def jss_myid(client,message):
    myid = message.from_user.id
    if myid != me(app):return
    name = message.text.split(" ")[1]
    url = requests.get(f"https://api.coinmarketcap.com/v1/ticker/{name}/")
    change1h = url.json()[0]["percent_change_1h"]
    change24h = url.json()[0]["percent_change_24h"]
    change7d = url.json()[0]["percent_change_7d"]
    price = url.json()[0]["price_usd"]
    send =app.edit_message_text(text="**-{}-** \n__Price__ : `${}`\n__Change 1h__ : `{}%`\n__Change 24h__ : `{}%`\n__Change 7d__ : `{}%`".format(name,price,change1h,change24h,change7d),
        chat_id=message.chat.id,
        message_id=message.message_id,)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])



@app.on_message(Filters.regex("^([Nn]obody|[Ee]verybody)$") & Filters.me , group=15)
def jss_setprivacy(client,message):
    if  "obody" in str(message.text):
        app.send(
            functions.account.SetPrivacy(
                key=types.InputPrivacyKeyStatusTimestamp(),
                rules=[types.InputPrivacyValueDisallowAll()]
            )
        )
        send =app.edit_message_text(text="Now Nobody Can See your Last seen!",
            chat_id=message.chat.id,
            message_id=message.message_id,)
        r.set("lastseen", "NoBody")
        if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(message.chat.id,[send.message_id])


    else:
        app.send(
            functions.account.SetPrivacy(
                key=types.InputPrivacyKeyStatusTimestamp(),
                rules=[types.InputPrivacyValueAllowAll()]
            )
        )

        send =app.edit_message_text(text="Now Everybody Can See your Last seen!",
            chat_id=message.chat.id,
            message_id=message.message_id,)
        r.set("lastseen", "EveryBody")
        if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(message.chat.id,[send.message_id])




@app.on_message(Filters.regex("^[Ss]pam (\d*)$") & Filters.reply , group=16)
def jss_spam(client,message):
    myid = message.from_user.id
    msgid = message.reply_to_message.message_id
    chatid = message.chat.id
    spam = int(message.text.split(" ")[1])
    if myid != me(app):return
    for i in range(spam):
        app.forward_messages(
            chat_id=chatid,
            from_chat_id=chatid,
            message_ids=[msgid]
        )
    app.delete_messages(message.chat.id,[message.message_id])


@app.on_message(Filters.regex("^[Ss]pamf (\d*)$") & Filters.reply & Filters.me , group=17)
def jss_spamf(client,message):
    msgid = message.reply_to_message.message_id
    chatid = message.chat.id
    spam = int(message.text.split(" ")[1])
    foshes = list(r.smembers("fosh"))
    for i in range(spam):
        fosh = random.choice(foshes)
        if r.get("fmaker") == "on":
            fosh = makef()
        app.send_message(chatid,fosh, reply_to_message_id=msgid)
    app.delete_messages(message.chat.id,[message.message_id])


@app.on_message(Filters.regex("^[Aa]ction$") & Filters.me, group=18)
def jss_action(client,message):
    chatid = message.chat.id
    if str(chatid) in r.smembers("chataction"):
        r.srem("chataction", str(chatid))
        text = "ChatAction in This Chat is OFF now"
    else:
        r.sadd("chataction", str(chatid))
        text = "ChatAction in This Chat is ON now"

    send = app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])



def jss_incoming(message):
    action = r.get("action") or "PLAYING"
    chatid = message.chat.id
    mode = r.get("actionmode") or "users"
    if str(chatid) in r.smembers("chataction"):
        for i in range(3):
            app.send_chat_action(
                chatid, 
                action
            )
        return
    if mode == "all" :
        for i in range(3):
            app.send_chat_action(
            chatid, 
            action
            )
        return
    if mode == "off":return
    if mode == "users":
        if str(chatid) in r.smembers("chataction"):
            for i in range(3):
                app.send_chat_action(
                    chatid, 
                    action
                )
        return
    else:
        if str(chatid) in r.smembers("chataction"):
            for i in range(3):
                app.send_chat_action(
                    chatid, 
                    action
                )
        return

    

@app.on_message(Filters.regex("^[Ss]etaction (.*)$") & Filters.me , group=19)
def jss_setaction(client,message):
    action = str(message.text.split(" ")[1])
    r.set("action", action)
    send =app.edit_message_text(text=f"Action Seted to {action}",
            chat_id=message.chat.id,
            message_id=message.message_id,)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.regex("^[Aa]ctionlist$") & Filters.me , group=20)
def jss_actionlist(client,message):
    text = """
actions:

`CANCEL`
`TYPING`
`PLAYING`
`CHOOSE_CONTACT`
`UPLOAD_PHOTO`
`RECORD_VIDEO`
`RECORD_AUDIO`
`UPLOAD_VIDEO`
`UPLOAD_AUDIO`
`UPLOAD_DOCUMENT`
`FIND_LOCATION`
`RECORD_VIDEO_NOTE`
`UPLOAD_VIDEO_NOTE`

cmd:

Setaction [action]
"""
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.regex("^[sS]ettings$") & Filters.me , group=21)
def jss_settings(client,message):
    global password
    password = password[0] + "*" * (len(password) - 2) + password[-1]
    chatid = message.chat.id
    text = f"""
JSettings:

**ChatAction:** `{r.get("action") or "PLAYING"}`
┣ Mode: `{r.get("actionmode")}`
**AntiSpamMode**: `ON`
┣ ifSpam: `BLOCK`
**Password:** Just Jss
**Boss:** Just Jss
**LastSeen:** `{r.get("lastseen")}`
**FilterFosh:** `{r.get("filterfosh")}`
**FoshMaker:** `{r.get("fmaker")}`
**AutoDel:** `{r.get("autodel")}`
┣ Time: {r.get("autodeltime")}
**AutoSeen:** `{r.get("autoseen")}`
┣ Mode: `{",".join([i for i in r.smembers("seen:mode")])}`
┣ ThisChatinUnmarks? `{"YES" if str(chatid) in r.smembers("unmark") else "NO"}`
**ServerSet:** Just Jss
┣ IP: 
┣ PASS: 
"""
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])



#Added To list
#@app.on_message(Filters.regex("^[Bb]lacklist$") & Filters.me , group=22)
def l_blacklist(message):
    blist = r.smembers("blacklist")
    text = "BlackList:\n"
    count = 1
    for i in blist:
        text = text + f"{count} - [{i}](tg://user?id={i})\n"
        count+=1
    send =app.edit_message_text(message.chat.id,message.message_id,text)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(message.chat.id,[send.message_id])


def l_action(message):
    actionchats = r.smembers("chataction")
    text = "ActionChats:\n\n"
    count = 1
    for i in actionchats:
        text = text + f"{count} - [{i}](tg://user?id={i})\n"
        count+=1
    send =app.edit_message_text(text=text,
                chat_id=message.chat.id,
                message_id=message.message_id,)
    
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])
    return

@app.on_message(Filters.regex("^[Aa]ction (.*)$") & Filters.me, group=23)
def jss_actionmode(client,message):
    chatid = message.chat.id
    mode = str(message.text.split(" ")[1])
    if mode == "off":r.set("actionmode", mode)
    elif mode == "all":r.set("actionmode", mode)
    elif mode == "users":r.set("actionmode", mode)

    elif mode == "clear":
        r.delete("chataction")
        send =app.edit_message_text(text="ActionChats Is Clear Now!",
                    chat_id=message.chat.id,
                    message_id=message.message_id,)
        
        if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(message.chat.id,[send.message_id])
        return
    send =app.edit_message_text(text=f"ActionMode Seted to {mode}",
                    chat_id=message.chat.id,
                    message_id=message.message_id,)
    
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])
    return



@app.on_message(Filters.regex("^[Cc]learf$") & Filters.me, group=24)
def jss_clearf(client,message):
    r.delete("fosh")
    send =app.edit_message_text(message.chat.id,message.message_id,"foshList Deleted!")
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])

@app.on_message(Filters.regex("^[Ff]ilterf$") & Filters.me, group=25)
def jss_foshfiltere(client,message):
    f = r.get("filterfosh")
    if f == "on":
        r.set("filterfosh", "off")
        text = "off"
    else:
        r.set("filterfosh", "on")
        text = "on"
    send =app.edit_message_text(message.chat.id,message.message_id,f"filterf {text} shod")
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])

@app.on_message(Filters.regex("^[hH]elp$") & Filters.me, group=26)
def jss_clearf(client,message):
    send =app.edit_message_text(message.chat.id,message.message_id,helptext)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.regex("^[Ss]et (.*)$") & Filters.me , group=30)
def jss_setcmd(client, message):
    cmd = message.text.split(" ")[1]
    rmsg = message.reply_to_message
    if rmsg.sticker:
        fid = "STICKER:"+str(rmsg.sticker.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.animation:
        fid = "GIF:"+str(rmsg.animation.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.photo:
        fid = "PHOTO:"+str(rmsg.photo.sizes[-1].file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.video:
        fid = "VIDEO:"+str(rmsg.video.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.document:
        fid = "DOC:"+str(rmsg.document.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif  rmsg.video_note:
        fid = "VN:"+str(rmsg.video_note.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.voice:
        fid = "VOICE:"+str(rmsg.voice.file_id)
        r.hmset("qanswer", {cmd: fid})
    else:return
    send =app.edit_message_text(message.chat.id,message.message_id,f"Done, {cmd} Seted!")
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id, [send.message_id])
        


@app.on_message(Filters.regex("^[Dd]cmd (.*)$") & Filters.me , group=32)
def jss_delcmd(client,message):
    cmd = message.text.split(" ")[1]
    r.hdel("qanswer", cmd)
    send =app.edit_message_text(message.chat.id,message.message_id,f"Done, {cmd} Deleted!")
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.regex("^[Aa]utodel? ?(\d*)$") & Filters.me , group=33)
def jss_autodel(client,message):
    if " " in message.text:
        timer = message.text.split(" ")[1]
        r.set("autodeltime", timer)
        text = f"AutoDelTime Seted to `{time}` Secend"
    else:
        if r.get("autodel") == "on":
            r.set("autodel", "off")
            text = "Auto Delete Is `OFF` Now"
        else:
            r.set("autodel", "on")
            text = "Auto Delete Is `ON` Now"
    
    send =app.edit_message_text(message.chat.id,message.message_id,text)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])

@app.on_message(Filters.regex("^[Ff]maker$") & Filters.me , group=34)
def jss_foshmaker(client,message):


    if r.get("fmaker") == "on":
        r.set("fmaker", "off")
        text = "FoshMaker Is `OFF` Now"
    else:
        r.set("fmaker", "on")
        text = "FoshMaker Is `ON` Now"

    send =app.edit_message_text(message.chat.id,message.message_id,text)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


#@app.on_message(Filters.regex("^[Aa]ddserver$") & Filters.me & Filters.reply, group=35)
#Deleted


#@app.on_message(Filters.regex("^[Cc]onnect$") & Filters.me , group=36)
#Deleted

@app.on_message(Filters.regex("^[Ss]een? ?(.*)$") & Filters.me , group=37)
def jss_seen(client, message):
    if " " in message.text:
        mode = message.text.split(" ")[1]
        if mode == "pv":
            if "pv" in r.smembers("seen:mode"):
                r.srem("seen:mode", "pv")
                text = "pv Deleted from MarkList"
            else:
                r.sadd("seen:mode", "pv")
                text = "pv Added to MarkList"
        elif mode == "channel":
            if "channel" in r.smembers("seen:mode"):
                r.srem("seen:mode", "channel")
                text = "channel Deleted from MarkList"
            else:
                r.sadd("seen:mode", "channel")
                text = "channel Added to MarkList"
        elif mode == "sgroup":
            if "sgroup" in r.smembers("seen:mode"):
                r.srem("seen:mode", "sgroup")
                text = "sgroup(SuperGroups) Deleted from MarkList"
            else:
                r.sadd("seen:mode", "sgroup")
                text = "sgroup(SuperGroups) Added to MarkList"

    else:
        if r.get("autoseen") == "on":
            r.set("autoseen", "off")
            text = "AutoSeen(Markread) Is `OFF` Now"
        else:
            r.set("autoseen", "on")
            text = "AutoSeen(Markread) Is `ON` Now"

    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.incoming & Filters.private, group=38)
def jss_in_priv(client, message):
    chatid = message.chat.id
    jss_incoming(message)
    if str(chatid) in r.smembers("mark"):
        mark(app, message)
        return
    elif r.get("autoseen") == "on":
        chatid = message.chat.id
        if str(chatid) in r.smembers("unmark"): return
        if "pv" not in r.smembers("seen:mode"): return
        mark(app, message)
        return
    else:return

@app.on_message(Filters.incoming & Filters.channel, group=39)
def jss_in_channel(client, message):
    chatid = message.chat.id
    if str(chatid) in r.smembers("mark"):
        mark(app, message)
        return
    elif r.get("autoseen") == "on":
        chatid = message.chat.id
        if str(chatid) in r.smembers("unmark"): return
        if "channel" not in r.smembers("seen:mode"): return
        mark(app, message)
        return
    else:return

@app.on_message(Filters.incoming & Filters.group, group=40)
def jss_in_sgroup(client, message):
    chatid = message.chat.id
    jss_incoming(message)
    if str(chatid) in r.smembers("mark"):
        mark(app, message)
        return
    elif r.get("autoseen") == "on":
        chatid = message.chat.id
        if str(chatid) in r.smembers("unmark"): return
        if "sgroup" not in r.smembers("seen:mode"): return
        mark(app, message)
        return
    else:return


def l_unmark(message):

    text = "UnmarkList:\n"
    count = 1
    for i in r.smembers("unmark"):
        text = text + f"{count} - `{i}`\n"
        count += 1
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)     
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.regex("^[Uu]nmark? ?(.*)$") & Filters.me, group=41)
def jss_addordelunmark(client, message):
    if " " in message.text:
        chatid = str(message.text.split(" ")[1])
        if chatid in r.smembers("unmark"):
            r.srem("unmark", chatid)
            text = "The Chat Deleted from UnmarkList"
        else:
            r.sadd("unmark", chatid)
            text = "The Chat Added to UnmarkList"
    else:
        chatid = str(message.chat.id)
        if chatid in r.smembers("unmark"):
            r.srem("unmark", chatid)
            text = "This Chat Deleted from UnmarkList"
        else:
            r.sadd("unmark", chatid)
            text = "This Chat Added to UnmarkList\nDont Mark Anyway"
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)     
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


#@app.on_message(Filters.regex("GET") & Filters.me, group=42)




def l_mark(message):
    text = "MarkList:\n"
    count = 1
    for i in r.smembers("mark"):
        text = text + f"{count} - `{i}`\n"
        count += 1
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)     
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])



@app.on_message(Filters.regex("^[Mm]ark") & Filters.me, group=43)
def jss_addmark(client, message):
    chatid = str(message.chat.id)
    if chatid in r.smembers("mark"):
        r.srem("mark", chatid)
        text = "This Chat Deleted from MarkList"
    else:
        r.sadd("mark", chatid)
        text = "This Chat Added to MarkList\nMark Anyway"
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)     
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.regex("^[Pp]rice (.*)$") & Filters.me, group=44)
def jss_getprice(client, message):
    userid = message.from_user.id
    if str(userid) not in r.smembers("vip"):return
    text = list_of_coin()
    args = str(message.text.split(" ")[1])
    if args == "channel" or args == "Channel":
        chatid = r.get("cchannel")
    else: chatid = message.chat.id
    app.send_message(chat_id=chatid,text=text)
    
@app.on_message(Filters.regex("^[Rr]set (.*)$") & Filters.me, group=45)
def jss_rset(client, message):
    if message.text.count(" ") == 2:
        args = message.text.split(" ")
        r.set(args[1], args[2])
        text = f"{args[1]} Seted to {args[2]} in Redis"
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)     
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])

@app.on_message(Filters.regex("^[Rr]sadd (.*)$") & Filters.me, group=46)
def jss_rset(client, message):
    if message.text.count(" ") == 2:
        args = message.text.split(" ")
        r.sadd(args[1], args[2])
        text = f"{args[2]} Added to {args[1]} in Redis"
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)     
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])

@app.on_message(Filters.regex("^[Rr]srem (.*)$") & Filters.me, group=47)
def jss_rset(client, message):
    if message.text.count(" ") == 2:
        args = message.text.split(" ")
        r.srem(args[1], args[2])
        text = f"{args[2]} Removed from {args[1]} in Redis"
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)     
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


def l_help(message):
    text = """
List Help
cmds:

f `OR` fosh = show fosh list
black `OR` blacklist `OR` b = show blacklist
action  `OR` a = show actionlist
help `OR` h = show this message
cmd  `OR` c = show cmdlist
um `OR unmark = show unmarklist
mark = show Marklist

List <cmd> OR list <cmd>
[Dd]el <cmd> <num>
"""
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)     
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])



def l_mute(message, name):
    text = f"{name} Mute list:\n"
    count = 1
    for i in r.smembers(f"mute:{name}"):
        text = text + f"{count} - `{i}`\n"
        count += 1
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)     
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


@app.on_message(Filters.regex("^[Ll]ist (.*)$") & Filters.me, group=48)
def jss_listt(client, message):
    name = message.text.split(" ")[1]
    if name in ("f", "fosh"):
        l_listf(message) 
    elif name in ("black", "blacklist", "b"):
        l_blacklist(message)
    elif name in ("action", "a"):
        l_action(message)
    elif name in ("help", "h"):
        l_help(message)
    elif name in ("cmd", "c"):
        l_cmdlist(message)
    elif name in ("unmark", "um"):
        l_unmark(message)
    elif name in ("mark"):
        l_mark(message)
    elif name == "m":
        a = message.text.split(" ")[2]
        l_mute(message, a)
    else:return



@app.on_message(Filters.regex("^[Dd]el (.*) (.*)$") & Filters.me, group=49)
def jss_ddel(client, message):
    name = message.text.split(" ")[1]
    num = message.text.split(" ")[2]
    if name in ("f", "fosh"):
        rname = "fosh" 
    elif name in ("black", "blacklist", "b"):
        rname = "blacklist"
    elif name in ("action", "a"):
        rname = "chataction"
    elif name in ("unmark", "um"):
        rname = "unmark"
    elif name in ("mark"):
        rname = "mark"
    elif name == "m":
        a = message.text.split(" ")[2]
        num = message.text.split(" ")[3]
        rname = "mute" + a
    else: return
        
    try:
        num = int(num) - 1
        p = list(r.smembers(rname))[num]
        r.srem(rname, p)
        text = f"{p} Removed from {rname} :)"

    except:
        text = f"Somthing rong! ,try again"


    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,)     
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])





#Fuck this shit 
#@app.on_message(Filters.regex("^[Bb]io? ?(.*)$" & filters.me) , group=50)
def bio(client,message):

    if " " in message.text:

        args = message.text.split(" ")
        mode =  args[1]

        #r.set("UpdateBio","False")
        if mode == "timer":
            r.set("bioaction", "timer")
            bio = "timer"
            text = f"BioAction `{bio}` Set Shode!"
        else:
            bio = " ".join(args[1:])
            r.set("biotext", bio)
            text = f"Biotext Seted to `{bio}` !"
    else:
        if r.get("UpdateBio") == "True":
            r.set("UpdateBio","False")
            text = f"BioAction Off Shod!"

        else:
            r.set("UpdateBio","True")
            text = f"BioAction On Shod!"
            send =app.edit_message_text(text=text,
                chat_id=message.chat.id,
                message_id=message.message_id)
            return bioaction()

        
    send =app.edit_message_text(text=text,
                chat_id=message.chat.id,
                message_id=message.message_id)
        
    if r.get("autodel") == "on":
        time.sleep(float(r.get("autodeltime")))
        app.delete_messages(message.chat.id,[send.message_id])


def biotext():
    if r.get("bioaction") == "timer":
        h, m, s = jdatetime.datetime.now().strftime("%H:%M:%S").split(":")
        Y, M, D = jdatetime.datetime.now().strftime("%y/%m/%d").split("/")
        bio = r.get("biotext")
        bio = bio.format(h=h, m=m, s=s, Y=Y, M=M, D=D)
    else:
        return False

    return bio

def bioaction():
 
    if r.get=="False":
        return


    print(biotext())
    app.send(
        functions.account.UpdateProfile(
            about=biotext()
        )
    )   
    
    time.sleep(int(r.get("biotime")) if r.get("biotime") else 65)
    return bioaction()


@app.on_message(Filters.regex("^[Tt]oday$") & Filters.me ,group=50)
def today(client,message):
    t = jdatetime.datetime.now().strftime("%H:%M:%S")
    d = jdatetime.datetime.now().strftime("%y/%B/%d")
    text = f"TODAY\nClock : `{t}`\nDate : `{d}`"
    send =app.edit_message_text(text=text,
            chat_id=message.chat.id,
            message_id=message.message_id,) 
    



@app.on_message(Filters.regex("[\+\-\*\%]+") & Filters.me, group=52)
def calc(client, message):
    text = message.text
    out = eval(str(text))
    send =app.edit_message_text(text=f"{text} =\n{out}",
        chat_id=message.chat.id,
        message_id=message.message_id,) 




#@app.on_message(Filters.me & Filters.regex("^![Tt] (.*) (.*)$") , group=54)
#Just JSS


#@app.on_message(Filters.group & Filters.photo , group=55)
#Just JSS
    

#@app.on_message(Filters.me & Filters.regex("^[Rr]iz (.*)$") , group=56)
#Just JSS
    

app.run()


#By JESUS
#Version 1.1
