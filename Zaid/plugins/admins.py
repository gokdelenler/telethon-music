from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
from Config import Config
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@Zaid.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« Geri", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« Geri", data="help")]])


ADMIN_TEXT = """
**👻 Sohbet yöneticilerinin kullanabileceği komutlar !**

‣ `?end` - Müzik akışını sonlandırmak için.
‣ `?skip` - Devam Eden Parçaları Atlamak İçin.
‣ `?pause` - Akışı duraklatmak için.
‣ `?resume` - Akışı Devam Ettirmek için.
‣ `?leavevc` - Asistanı Vc Chat'ten ayrılmaya zorlar (Bazen Katılır).
‣ `?playlist` - Çalma listelerini kontrol etmek için.
"""

PLAY_TEXT = """
**👻 Sohbet kullanıcılarının kullanabileceği komutlar !**

‣ `?play` - Ses Akışı için.
‣ `?vplay` - Video Akışı için (HEROKU_MODE > Desteklemiyor).
"""
