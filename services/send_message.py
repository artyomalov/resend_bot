from pyrogram import Client


async def send_message(app: Client, receiver_id: str, from_chat_id: int, message_id: int, from_user_id: int) -> None:
    """
    Resend message and send source chat.
    """
    await app.forward_messages(chat_id=receiver_id, from_chat_id=from_chat_id, message_ids=message_id)

    await app.send_message(chat_id=receiver_id,
                           text=f'Chat: https://web.telegram.org/a/#{from_chat_id};\
                                      \nMessage\'s author: https://web.telegram.org/a/#{from_user_id}')
