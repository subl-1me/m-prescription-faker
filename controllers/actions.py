from controllers.menu import Menu
from models.medical_profile import MedicalProfile
from models.prescription import Prescription
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Actions:

    @staticmethod
    def create_prescription(med_profile):
        if(type(med_profile) == None):
            return { "error": True, "message": "Please create a profile first." }
            
        # Select a med set
        # create prescription
        prescription = Prescription(med_profile, None)
        prescription = prescription.create()
        print(prescription)
        return prescription
        

    @staticmethod
    def set_medical_profile():
        response = Menu.show_create_profile()
        profile = MedicalProfile(response['name'], response['curp'], response['bdate'], response['umf_no'], response['unity_no'], response['shift'])
        return profile  
    
    @staticmethod
    def modify_medical_profile(profile):
        logger.info('Creating document...')

    @staticmethod
    def show_medical_profile(profile):
        profile.show()