from controllers.menu import init_home_menu, ask_for_prop, askForProfile
from const import CREATE_PRESCRIPTION_OPT, MODIFY_MEDICAL_PROFILE_OPT, SHOW_MEDICAL_PROFILE_OPT, SET_MEDICAL_PROFILE
from models.medical_profile import MedicalProfile

def main():
    profile = None

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
            #ask for profile information
            profile_data = askForProfile()
            profile = MedicalProfile()
        elif selection == 3:
            profile.show()
            # Ask for prop to modify
            prop = ask_for_prop()
            print(prop)
        elif selection == 4: 
            profile.show()
        else:
            print(f'Invalid option.')




if __name__ == '__main__':
    main()