import logging
import os

from aiotdlib import Client
from aiotdlib.api import UpdateNewMessage

API_ID = int(os.environ.get("API_ID", 1234))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client(api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@bot.bot_command_handler(command='help')
async def on_help_command(client: Client, update: UpdateNewMessage):
    await client.send_text(update.message.chat_id, "No help for you 😒")


async def on_start_command(client: Client, update: UpdateNewMessage):
    print(update.EXTRA)
    await client.send_text(update.message.chat_id, "Hai 🙋🏻")


async def on_custom_command(client: Client, update: UpdateNewMessage):
    print(update.EXTRA)
    await client.send_text(update.message.chat_id, "OkDa")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    bot.bot_command_handler(on_start_command, command='start')
    bot.bot_command_handler(on_custom_command, command='custom')
    bot.run()
