from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
👻 **Merhaba !** {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
👻 **Ben Basit Bir Müzik Ve Yönetim Botuyum**
‣ **Sesli Sohbet'te Şarkılar Yada Videolar Oynatabilirim**
‣ **Müzik Botunda Gerektiren Tüm Özelliklere Sahibim**
‣ **Telethon tabanlı bir botum**
‣ **Yani diğer botlardan daha fazla stabilite sağlıyorum**
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
👻 **Daha Fazla Bilgi İçin Yardım Düğmesini Tıklayın**
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ Gruba Ekle", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 Kaynak Kodu", "https://github.com/suphiozturk8")],
        [Button.url("🗣️ Support", f"https://t.me/{Config.SUPPORT}"), Button.url("👻 Kanal", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("👻 Yardım Ve Komutlar", data="help")]])
       return

    if event.is_group:
       await event.reply("**Hey ! Ben Yaşıyorum ✓**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ Gruba Ekle", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 Kaynak Kodu", "https://github.com/Suphiozturk8")],
        [Button.url("🗣️ Support", f"https://t.me/{Config.SUPPORT}"), Button.url("👻 Kanal", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("👻 Yardım Ve Komutlar", data="help")]])
       return
