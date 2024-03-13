import logging
import services
from os import environ
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import Message
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

# Get environment's variables
CHAT_ID = environ.get('CHAT_ID')
ADMIN_CHAT_ID = environ.get('ADMIN_CHAT_ID')
RECEIVER_ID = environ.get('RECEIVER_ID')

# Create app
app = Client("my_account")


@app.on_message(filters.photo | filters.document | filters.video)
async def resend_file_capture(app: Client, message: Message):
    logging.info(f"Received file: {message.caption}")
    """
    Resends messages with videos or files to selected chat if message's caption contains keywords.
    """
    try:
        if not message.from_user.id:
            return

        is_suitable = False
        caption = message.caption

        if caption:
            is_suitable = services.check_is_suitable(message.caption)

        if is_suitable:
            await services.send_message(app=app,
                                        receiver_id=RECEIVER_ID,
                                        from_chat_id=message.chat.id,
                                        message_id=message.id,
                                        from_user_id=message.from_user.id,
                                        )

    except RPCError as error:
        await app.send_message(chat_id=ADMIN_CHAT_ID, text=f'TG error: {str(error)}')

    except Exception as error:
        await app.send_message(chat_id=ADMIN_CHAT_ID, text=f'Another error: {str(error)}')


@app.on_message(filters.text)
async def resend_text_message(app: Client, message: Message):
    logging.info(f"Received message: {message.text}")
    """
    Resends text messages to selected chat.
    """
    try:
        if not message.from_user.id:
            return
        is_suitable = services.check_is_suitable(message.text)

        if is_suitable:
            await services.send_message(app=app,
                                        receiver_id=RECEIVER_ID,
                                        from_chat_id=message.chat.id,
                                        message_id=message.id,
                                        from_user_id=message.from_user.id,
                                        )

    except RPCError as error:
        logging.error(f'Error: {message.text}')
        await app.send_message(chat_id=ADMIN_CHAT_ID, text=f'TG error: {str(error)}')

    except Exception as error:
        logging.error(f'Error: {message.text}')
        await app.send_message(chat_id=ADMIN_CHAT_ID, text=f'Another error: {str(error)}')


app.run()

