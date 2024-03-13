Simple userbot that allows to parce channels where is has been added and resend messages to any receiver (group chat, channel, or user).
To start bot need to:
  - install all dependencies using requirements.txt;
  - authorize userbot using pyrogram (see pyrogram docks)
  - setup list of keywords using const.py file;
  - create .env file and and set two enviroment variable: ADMIN_CHAT_ID and RECEIVER_ID
    ADMIN_CHAT_ID - chat id, where error messages will be sent if something goes wrong
    RECEIVER_ID - if of the channel where messages will be resent;
  - run bot using 'python main.py' comand.
