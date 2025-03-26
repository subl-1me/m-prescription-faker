from InquirerPy import prompt #type: ignore
from const import MAIN_MENU_SKELETON, HOME_MENU_ACTION
import pyfiglet

class Menu():
    def __init__(self):
        self.current_menu = "HOME" 

    def show_home_menu(self):
        self.current_menu = "HOME"
        title = pyfiglet.figlet_format('Medical Prescription Faker')
        print(title)

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


    def show_create_profile():
        profileQuestions = [
            {
                "type": "input",
                "message": "Type your name",
                "name": "name",
            },
                    {
                "type": "input",
                "message": "Type your NSS",
                "name": "nss",
            },
                    {
                "type": "input",
                "message": "Type your CURP",
                "name": "curp",
            },
                    {
                "type": "input",
                "message": "Type your birth date",
                "name": "bdate",
            },
                    {
                "type": "input",
                "message": "Type UMF no.",
                "name": "umf",
            },
                    {
                "type": "input",
                "message": "Type unity no.",
                "name": "unity",
            },
                    {
                "type": "list",
                "message": "Enter shift type",
                "name": "shift",
                "choices": ["MATUTINO", "VESPERTINO"]
            }
        ]

        result = prompt(profileQuestions)
        return result

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