import logging

import actions.actions.metadata.batch.metadatabatch as batch
import actions.actions.metadata.normal.metadata as normal
import utils.constants as constants
import utils.settings as settings
import utils.system.system as system
from actions.utils.log import final_log_text
from utils.context.run_async import run as run_async
from runner.close.final.final_user import post_user_script


@run_async
async def metadata_process(username, model_id, medialist, posts=None):
    data = await metadata_picker(username, model_id, medialist)
    post_user_script(username, medialist, posts)
    return data


async def metadata_picker(username, model_id, medialist):
    if len(medialist) == 0:
        out = final_log_text(username, 0, 0, 0, 0, 0, 0)
        logging.getLogger("shared").error(out)
        return out
    elif (
        system.getcpu_count() > 1
        and (
            len(medialist)
            >= settings.get_threads() * constants.getattr("DOWNLOAD_THREAD_MIN")
        )
        and settings.not_solo_thread()
        and system.platform.system()=="Linux"

    ):
        return batch.process_dicts(username, model_id, medialist)
    else:
        return await normal.process_dicts(username, model_id, medialist)
