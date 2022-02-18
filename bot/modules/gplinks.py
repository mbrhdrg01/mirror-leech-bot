import random
import string
from telegram.ext import CommandHandler
from bot.helper.mirror_utils.upload_utils import gdriveTools
from bot.helper.telegram_helper.message_utils import sendMessage, sendMarkup, deleteMessage, delete_all_messages, update_all_messages, sendStatusMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.mirror_utils.status_utils.clone_status import CloneStatus
from bot import dispatcher, LOGGER, CLONE_LIMIT, STOP_DUPLICATE, download_dict, download_dict_lock, Interval
from bot.helper.ext_utils.bot_utils import get_readable_file_size, is_gdrive_link, is_gdtot_link
from bot.helper.mirror_utils.download_utils.direct_link_generator import gdtot
from bot.helper.ext_utils.exceptions import DirectDownloadLinkException

import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
