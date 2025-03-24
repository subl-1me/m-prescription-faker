from InquirerPy import prompt #type: ignore
from const import MAIN_MENU_SKELETON, HOME_MENU_ACTION

def init_home_menu():
    menu = [
        {
        "type": "list",
        "message": "Select an option:",
        "name": HOME_MENU_ACTION,
        "choices": MAIN_MENU_SKELETON
        }
    ]

    result = prompt(menu)
    action = result[HOME_MENU_ACTION]
    return action

def ask_for_prop():
    propPrompt = [
        {
            "type": "list",
            "message": "Select an option to modify",
            "name": "PROP_SELECTION",
            "choices": ["Name", "CURP", "NSS No.", "Birth date", "UMF No.", "Shift", "State", "Office No."]
        }
    ]

    result = prompt(propPrompt)
    selection = result["PROP_SELECTION"]
    return selection

def process_menu_choice(choice):
    print(choice)