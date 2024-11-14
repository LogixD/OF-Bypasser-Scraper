import  runner.manager as manager
import utils.actions as actions
from commands.managers.db import DBManager




def db():
    actions.select_areas()
    for model in manager.Manager.model_manager.getselected_usernames(rescan=False):
        db_manager = DBManager(model.name, model.id)
        db_manager.print_media()

