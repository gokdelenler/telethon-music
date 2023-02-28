from telethon import events, Button
from Zaid import Zaid, BOT_USERNAME
from Config import Config


btn =[
    [Button.inline("Admin", data="admin"), Button.inline("Play", data="play")],
    [Button.inline("Home", data="start")]]

HELP_TEXT = "**👻 Yardım Menüsünne Hoş geldiniz\n\nKomutları Görmek İçin Butonları Kullanın**"


@Zaid.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_group:
       await event.reply("**👻 Kullanılabilir yardım menüsünü almak için\nPM'de bana ulaşın !**", buttons=[
       [Button.url("👻 Yardım Ve Komutlar", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.NewMessage(pattern="^/start help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.edit(HELP_TEXT, buttons=btn)
