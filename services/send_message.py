from pyrogram import Client


async def send_message(app: Client, receiver_id: str, from_chat_id: int, message_id: int, from_user_id: int) -> None:
    """
    Resend message and send source chat.
    """
    await app.send_message(chat_id='-1001934317046',
                           text=f'Чат: https://web.telegram.org/a/#{from_chat_id};\
                                      \nавтор сообщения: https://web.telegram.org/a/#{from_user_id}')

    await app.forward_messages(chat_id=receiver_id, from_chat_id=from_chat_id, message_ids=message_id)
