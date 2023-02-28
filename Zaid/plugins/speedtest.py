from telethon import Button, events

from Zaid import *

import asyncio
import speedtest

# Commands

def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        test.download()
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        return
    return result

@Zaid.on(events.NewMessage(pattern="^/speedtest"))
async def speedtest_function(message):
    m = await message.reply("**Hız Testi Yapılıyor...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**Hız Testi Sonuçları**
    
**Müşteri:**
**ISP:** {result['client']['isp']}
**Ülke:** {result['client']['country']}
  
**Sunucu:**
**İsim:** {result['server']['name']}
**Ülke:** {result['server']['country']}, {result['server']['cc']}
**Sponsor:** {result['server']['sponsor']}
**Gecikme:** {result['server']['latency']}  
**Ping:** {result['ping']}"""
    await Zaid.send_file(message.chat.id, result["share"], caption=output)
    await m.delete()
