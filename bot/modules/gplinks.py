import random
import string
from telegram.ext import CommandHandler
from bot.helper.mirror_utils.upload_utils import gdriveTools
from bot.helper.telegram_helper.message_utils import sendMessage, sendMarkup, deleteMessage, delete_all_messages, update_all_messages, sendStatusMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.mirror_utils.status_utils.clone_status import CloneStatus
from bot import dispatcher, LOGGER, CLONE_LIMIT, STOP_DUPLICATE, download_dict, download_dict_lock, Interval
from bot.helper.ext_utils.bot_utils import get_readable_file_size, is_gdrive_link, is_gdtot_link ,is_gp_link
from bot.helper.mirror_utils.download_utils.direct_link_generator import gdtot
from bot.helper.ext_utils.exceptions import DirectDownloadLinkException

import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def gplinks(update ,context):
    args = update.message.text.split(" ", maxsplit=1)
    reply_to = update.message.reply_to_message
    if len(args) > 1:
         link = args[1]
    elif reply_to is not None:
         link = reply_to.text
    else:
        link = ''
    gp_link = is_gp_link(link)
    if gp_link:
       client = requests.Session()
       res = client.get(link)
       
       bs4 = BeautifulSoup(res.content, 'lxml')
       inputs = bs4.find_all('input')
       data = { input.get('name'): input.get('value') for input in inputs }

       h = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
    }
       time.sleep(10)
       p = urlparse(link)
       final_url = f'{p.scheme}://{p.netloc}/links/go'
       res = client.post(final_url, data=data, headers=h).json()

       return res
      

    
gplink_handler = CommandHandler(BotCommands.GplinkCommand, gplinks, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(gplink_handler)
