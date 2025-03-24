from controllers.menu import init_home_menu, ask_for_prop
from const import CREATE_PRESCRIPTION_OPT, MODIFY_MEDICAL_PROFILE_OPT, SHOW_MEDICAL_PROFILE_OPT, SET_MEDICAL_PROFILE
from models.medical_profile import MedicalProfile

def main():
    selection = init_home_menu()
    profile = MedicalProfile('', '', '', '')

    if selection == CREATE_PRESCRIPTION_OPT:
        print(selection)
    elif selection == SET_MEDICAL_PROFILE:
        print(selection)
    elif selection == MODIFY_MEDICAL_PROFILE_OPT:
        profile.show()
        # Ask for prop to modify
        prop = ask_for_prop()
        print(prop)
    elif selection == SHOW_MEDICAL_PROFILE_OPT: 
        print(selection)



if __name__ == '__main__':
    main()