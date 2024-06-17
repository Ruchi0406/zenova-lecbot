import asyncio
import importlib
from pyrogram import idle
from zenova import zenova
from zenova.modules import ALL_MODULES

loop = asyncio.get_event_loop()

async def zenova_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("zenova.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await idle()
    print("Caught an unknown error")

    
if __name__ == "__main__":
    loop.run_until_complete(zenova_boot())
    
