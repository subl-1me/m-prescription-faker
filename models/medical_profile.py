class MedicalProfile:
    def __init__(self, fullName, curpCode, address, date):
        self.fullname = fullName
        self.curpCode = curpCode
        self.address = address
        self.date = date
    
    def get(self):
        print('Printing profile...')
    
    def set(self, prop):
        print('Updating profile...')
        print(prop)

    def show(self):
        print("\n----------")
        print(' CURRENT PROFILE ')
        print("Name: " + self.fullname);
        print("CURP: " + self.curpCode);
        print("Address: " + self.address);
        print("Date: " + self.date);
        print("----------\n")
    
    