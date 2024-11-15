import logging
import traceback

import classes.media as media_class
import actions.utils.log as logs
import utils.text as text
from utils.context.run_async import run
import utils.args.accessors.read as read_args
import utils.settings as settings
from utils.args.accessors.command import get_command




@run
async def textDownloader(objectdicts, username=None):
    log = logging.getLogger("shared")
    if get_command() == "metadata":
        return
    elif not bool(objectdicts):
        return
    elif not settings.get_download_text():
        return
    try:
        objectdicts = (
            [objectdicts] if not isinstance(objectdicts, list) else objectdicts
        )
        log.info("Downloading Text Files")
        data = (
            {
                e.postid if isinstance(e, media_class.Media) else e.id: e
                for e in objectdicts
            }
        ).values()
        count, fails, exists = await text.get_text(data)
        username = username or "Unknown"
        return logs.text_log(username, count, fails, exists, log=log)
    except Exception as E:
        log.debug(f"Issue with text {E}")
        log.debug(f"Issue with text {traceback.format_exc()}")
