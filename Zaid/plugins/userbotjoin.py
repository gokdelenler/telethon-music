
import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Zaid import *
from Zaid.status import *



@Zaid.on(events.NewMessage(pattern="^[!?/]join ?(.*)"))
@Zaid.on(events.NewMessage(pattern="^[!?/]userbotjoin ?(.*)"))
@is_admin
async def _(e, perm):
    chat_id = e.chat_id
    usage = "**Modül ismi = join**\n**Komut:**\n`/join <Grup Bağlantısı/Kullanıcı Adı>`\n**Grubunuz özelse** `!pjoin <Sohbet bağlantısı>`"
    if e.is_group:
        umm = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = umm[0]
            text = "**Katılıyor...**"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("**Başarıyla Katıldı ✓\nKatılmadıysa !pjoin'i ve grup bağlantınızı kullanın**")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@Zaid.on(events.NewMessage(pattern="^[!?/]pjoin ?(.*)"))
@is_admin        
async def _(e, perm):
    chat_id = e.chat_id
    usage = "**Modül İsmi = pjoin\nKomut:**\n`!pjoin <özel kanal veya grubun davet bağlantısı>`\n**Örnek:\nLink =** `https://t.me/joinchat/Ihsvig1907226#`\n`!pjoin Ihsvig1907226`"
    if e.is_group:
        umm = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            invitelink = umm[0]
            text = "**Katılıyor...**"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await client(ImportChatInviteRequest(invitelink))
                await event.edit("**Başarıyla Katıldı ✓**")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
    
