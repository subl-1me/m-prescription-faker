from controllers.menu import Menu
from models.medical_profile import MedicalProfile
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Actions:

    @staticmethod
    def create_prescription():
        logger.info('Creating document...')

    @staticmethod
    def set_medical_profile():
        response = Menu.show_create_profile()
        profile = MedicalProfile(response.fullName, response.curpCode, response.address, response.date)
        logger.debug(profile)
        return profile
    
    @staticmethod
    def modify_medical_profile(profile):
        logger.info('Creating document...')

    @staticmethod
    def show_medical_profile(profile):
        logger.info('Creating document...')
