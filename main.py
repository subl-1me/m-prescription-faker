from controllers.menu import Menu
from const import  CREATE_PRESCRIPTION_OPT, SHOW_MEDICAL_PROFILE_OPT, MODIFY_MEDICAL_PROFILE_OPT, SET_MEDICAL_PROFILE
from controllers.actions import Actions

def main():
    profile = None;

    while True:
        selection = Menu.show_home_menu()
        if selection == -1:
            continue

        # transform selection to func name
        parsedSelection = str.lower(selection).replace(' ', '_')
        if selection == CREATE_PRESCRIPTION_OPT:
            getattr(Actions, parsedSelection)() # Create medical document (.word)
        elif selection == SET_MEDICAL_PROFILE:
            profile = getattr(Actions, parsedSelection)() # Set medical profile
        elif selection == MODIFY_MEDICAL_PROFILE_OPT:
            profile = getattr(Actions, parsedSelection)(profile) # Modify a profile attribute
        elif selection == SHOW_MEDICAL_PROFILE_OPT: 
            getattr(Actions, parsedSelection)(profile) # Show current profile status
        else:
            print(f'\nInvalid option. Try again\n')


if __name__ == '__main__':
    main()