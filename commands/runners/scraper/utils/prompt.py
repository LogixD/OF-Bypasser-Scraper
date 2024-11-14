import prompts.prompts as prompts
import utils.context.exit as exit
import utils.menu as menu


@exit.exit_wrapper
def process_prompts():
    while True:
        if menu.main_menu_action():
            break
        elif prompts.continue_prompt() == "No":
            break
