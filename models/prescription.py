import win32com.client as win32
import time
from const import PATIENT_NAME_PLACEHOLDER, NSS_NUMBER_PLACEHOLDER, CURP_PLACEHOLDER, BIRTH_DATE_PLACEHOLDER, STATE_PLACEHOLDER, OFFICE_NO_PLACEHOLDER, UNITY_PLACEHOLDER, SHIFT_PLACEHOLDER

class Prescription:
    def __init__(self, profile, medSet):
        self.profile = profile 
        self.medSet = medSet
        
    def create(self):
        response = {
            "error": False,
            "mesasage": "",
            "docPath": "",
            "profile": self.profile,
            "medSet": self.medSet          
        }
        
        try:
            TEMPLATE_FILE = "C:/Users/subl-1me/Documents/dev-projects/m-prescription-faker/prescription.docx"
            word = win32.Dispatch('Word.Application')
            word.Visible = False
            doc = word.Documents.Open(TEMPLATE_FILE)
            
            for i, shape in enumerate(doc.Shapes, 1):
                if shape.TextFrame.hasText:
                    shape.TextFrame.TextRange.Text = shape.TextFrame.TextRange.Text.replace(PATIENT_NAME_PLACEHOLDER, self.profile.name)
                    # shape.TextFrame.TextRange.Text = shape.TextFrame.TextRange.Text.replace(NSS_NUMBER_PLACEHOLDER, self.profile.nss)
                    shape.TextFrame.TextRange.Text = shape.TextFrame.TextRange.Text.replace(CURP_PLACEHOLDER, self.profile.curp)
                    shape.TextFrame.TextRange.Text = shape.TextFrame.TextRange.Text.replace(BIRTH_DATE_PLACEHOLDER, self.profile.bdate)
                    # shape.TextFrame.TextRange.Text = shape.TextFrame.TextRange.Text.replace(STATE_PLACEHOLDER, self.profile.nss)
                    shape.TextFrame.TextRange.Text = shape.TextFrame.TextRange.Text.replace(OFFICE_NO_PLACEHOLDER, self.profile.unity_no)
                    shape.TextFrame.TextRange.Text = shape.TextFrame.TextRange.Text.replace(UNITY_PLACEHOLDER, self.profile.umf_no)
                    shape.TextFrame.TextRange.Text = shape.TextFrame.TextRange.Text.replace(SHIFT_PLACEHOLDER, self.profile.shift)


            timestamp = time.time()
            MODF_TEMPLATE = "C:/Users/subl-1me/Documents/dev-projects/m-prescription-faker/prescription_modf_" + str(timestamp) + ".docx"
            doc.SaveAs(MODF_TEMPLATE)
            response["docPath"] = MODF_TEMPLATE
            return response
        except:
            response["error"] = True
            response["mesasage"] = "Error trying to create prescription (.docx)"
            return response
            
        
        
        