from controllers.menu import init_home_menu, ask_for_prop, askForProfile
from const import CREATE_PRESCRIPTION_OPT, MODIFY_MEDICAL_PROFILE_OPT, SHOW_MEDICAL_PROFILE_OPT, SET_MEDICAL_PROFILE
from controllers.actions import Actions

def main():
    profile = None
    actions = Actions()

    menu_actions = {
        1: CREATE_PRESCRIPTION_OPT,
        2: SET_MEDICAL_PROFILE,
        3: MODIFY_MEDICAL_PROFILE_OPT,
        4: SHOW_MEDICAL_PROFILE_OPT
    }

    while True:
        selection = init_home_menu()
        if selection == -1:
            continue
        
        if selection == 1:
            menu_actions[selection]() # Create medical document (.word)
        elif selection == 2:
            profile = menu_actions[selection]() # Set medical profile
        elif selection == 3:
            menu_actions[selection](profile)
        elif selection == 4: 
            menu_actions[selection](profile)
        else:
            print(f'Invalid option.')




if __name__ == '__main__':
    main()