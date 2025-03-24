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
    print(action)

def process_menu_choice(choice):
    print(choice)