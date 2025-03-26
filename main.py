from controllers.menu import init_home_menu
from const import  CREATE_PRESCRIPTION_OPT, SHOW_MEDICAL_PROFILE_OPT, MODIFY_MEDICAL_PROFILE_OPT, SET_MEDICAL_PROFILE
from controllers.actions import Actions

def main():
    actions = Actions()

    while True:
        selection = init_home_menu()
        if selection == -1:
            continue

        # transform selection to func name
        parsedSelection = str.lower(selection).replace(' ', '_')
        if selection == CREATE_PRESCRIPTION_OPT:
            getattr(actions, parsedSelection)() # Create medical document (.word)
        elif selection == SET_MEDICAL_PROFILE:
            getattr(actions, parsedSelection)() # Set medical profile
        elif selection == MODIFY_MEDICAL_PROFILE_OPT:
            getattr(actions, parsedSelection)() # Modify a profile attribute
        elif selection == SHOW_MEDICAL_PROFILE_OPT: 
            getattr(actions, parsedSelection)() # Show current profile status
        else:
            print(f'\nInvalid option. Try again\n')


if __name__ == '__main__':
    main()