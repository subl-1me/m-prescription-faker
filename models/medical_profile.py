class MedicalProfile:
    def __init__(self, name, curp, bdate, umf_no, unity_no, shift):
        self.name = name
        self.curp = curp
        self.bdate = bdate
        self.umf_no = umf_no
        self.unity_no = unity_no
        self.shift = shift
    
    def get(self):
        print('Printing profile...')
    
    def set(self, prop):
        print('Updating profile...')
        print(prop)

    def show(self):
        print("\n----------")
        print(' CURRENT PROFILE ')
        print("Name: " + self.name);
        print("CURP: " + self.curp);
        print("Birthdate: " + self.bdate);
        print("UMF: " + self.umf_no);
        print("Unity: " + self.unity_no);
        print("Shift: " + self.shift);
        print("----------\n")

    
    