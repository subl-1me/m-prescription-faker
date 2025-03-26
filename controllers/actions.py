from controllers.menu import Menu
from models.medical_profile import MedicalProfile
menu = Menu()

class Actions:
    def create_prescription():
        print('Creating document...')
    def set_medical_profile():
        response = menu.show_create_profile();
        profile = MedicalProfile(response.fullName, response.curpCode, response.address, response.date)
        return profile
    def modify_medical_profile(profile):
        print('modifying')
    def show_medical_profile(profile):
        print('Showing')