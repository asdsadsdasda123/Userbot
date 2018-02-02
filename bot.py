
import time

from telethon import TelegramClient
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.channels import DeleteUserHistoryRequest
from telethon.tl.types import *
from telethon.errors import *

api_id = yourapiid
api_hash = 'yourapihash'

client = TelegramClient('session_name', api_id, api_hash, update_workers=0)
client.start()

print(client.get_me().stringify())

while True:
    try:
        update = client.updates.poll()
        if not update:
            continue
        if (isinstance(update, UpdateNewChannelMessage) and update.message.out == False):
            if(isinstance(update.message, Message)):
                messaggio = update.message.message
                if any(ord(char)>127 for char in messaggio):
                    client.delete_messages(update.message.to_id, [update.message.id])
                    if (isinstance(update.message, MessageService)):
                        client.delete_messages(update.message.to_id, [update.message.id])
                        if (isinstance(update.message.action, MessageActionChatAddUser)):
                            for boto in update.message.action.users:
                              if (client.get_entity(boto).bot == True):
                                  client(EditBannedRequest(update.message.to_id, boto, banned_rights=ChannelBannedRights(until_date=0, view_messages=True)))
                                  client(DeleteUserHistoryRequest(client.get_input_entity(update.message.to_id), client.get_input_entity(boto)))


        print('I received', update)
    except KeyboardInterrupt:
        break




while 1:
    time.sleep(10)
