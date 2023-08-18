# Hospital Management System Application using class. in our project. It supports data entry as well as report generation
# in plain text file with CRUD operation on doctor and patient's data records.

#Group No :9
#Group Members :Zahra Keshtkar, Adwaith Shini Ajith, Khushbu Shah
#Date: 17th August, 2023 

class Doctor:
    def __init__(self, doctorid, name, specialization, workingtime, qualification, roomnumber):
        self.doctorid = doctorid
        self.name = name
        self.specialization = specialization
        self.workingtime = workingtime
        self.qualification = qualification
        self.roomnumber = roomnumber

    def getdoctorid(self):
        return self.doctorid
    def getname(self):
        return self.name
    def getspecialization(self):
        return self.specialization
    def getworkingtime(self):
        return self.workingtime
    def getqualification(self):
        return self.qualification
    def getroomnumber(self):
        return self.roomnumber


class Patients():
    def __init__(self, patientid, pname, disease, gender, age):
        self.patientid = patientid
        self.pname = pname
        self.disease = disease
        self.gender = gender
        self.age = age
    def getpatientid(self):
        return self.patientid
    def getpname(self):
        return self.pname
    def getdisease(self):
        return self.disease
    def getgender(self):
        return self.gender
    def getage(self):
        return self.age


class DoctorManager:
    def __init__(self, filename):
        self.filename = filename


    def display_doctors_list(self):
        lines = open(self.filename, "r").read().strip().split('\n')
        headers = lines[0].split('_')
        max_lengths = [max(len(header), max(len(cell) for cell in line.split('_'))) for header, line in
                       zip(headers, lines[1:])]
        formatted_header = '   '.join(header.ljust(length) for header, length in zip(headers, max_lengths))
        print(formatted_header)
        for line in lines[1:]:
            cells = line.split('_')
            formatted_line = '   '.join(cell.ljust(length) for cell, length in zip(cells, max_lengths))
            print(formatted_line)

    def search_record_by_id(self, search_id):
        with open(self.filename, "r") as content:
            lines = content.read().strip().split('\n')
        for line in lines:
            cells = line.split('_')
            if cells[0] == search_id:
                return cells
        return None

    def search_record_by_name(self, search_name):
        with open(self.filename, "r") as content:
            lines = content.read().strip().split('\n')
        for line in lines:
            cells = line.split('_')
            if cells[1] == search_name:
                return cells
        return None

    def display_found_record(self, found_cells, headers):
        if found_cells:
            max_lengths = [max(len(header), len(cell)) for header, cell in zip(headers, found_cells)]
            formatted_header = '   '.join(header.ljust(length) for header, length in zip(headers, max_lengths))
            formatted_line = '   '.join(cell.ljust(length) for cell, length in zip(found_cells, max_lengths))


            print(formatted_header)
            print(formatted_line)
        else:
            print(f"Can't find the doctor with the same {found_cells} on the system")

    def search_and_display_record_by_id(self, search_id):
        lines = open(self.filename, "r").read().strip().split('\n')
        headers = lines[0].split('_')
        found_cells = self.search_record_by_id(search_id)
        self.display_found_record(found_cells, headers)

    def search_and_display_record_by_name(self, search_name):
        lines = open(self.filename, "r").read().strip().split('\n')
        headers = lines[0].split('_')
        found_cells = self.search_record_by_name(search_name)
        self.display_found_record(found_cells, headers)



    def add_dr_to_file(self, new_doctor):
        file = open(self.filename, "a")
        file.write("\n"+new_doctor.getdoctorid()+"_"+new_doctor.getname()+"_"+new_doctor.getspecialization()+"_"+
                   new_doctor.getworkingtime()+"_"+new_doctor.getqualification()+"_"+new_doctor.getroomnumber())
        print(f"Doctor whose ID is {new_doctor.getdoctorid()} has been added")
        file.close()

    def edit_dr_to_file(self, edit_doctor):
        file = open(self.filename, "r+")
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i]
            parts = line.strip().split("_")
            if parts and parts[0] == edit_doctor.getdoctorid():

                parts[1] = edit_doctor.getname()
                parts[2] = edit_doctor.getspecialization()
                parts[3] = edit_doctor.getworkingtime()
                parts[4] = edit_doctor.getqualification()
                parts[5] = edit_doctor.getroomnumber()
                lines[i] = "_".join(parts) + "\n"

        file.seek(0)
        file.writelines(lines)
        print(f"Doctor whose ID is {edit_doctor.getdoctorid()} has been edited")
        file.close()



class PatientManager():
    def __init__(self, filename):
        self.filename = filename

    def display_patient_list(self):
        lines = open(self.filename, "r").read().strip().split('\n')
        headers = lines[0].split('_')
        max_lengths = [max(len(header), max(len(cell) for cell in line.split('_'))) for header, line in
                       zip(headers, lines[1:])]
        formatted_header = '   '.join(header.ljust(length) for header, length in zip(headers, max_lengths))
        print(formatted_header)
        for line in lines[1:]:
            cells = line.split('_')
            formatted_line = '   '.join(cell.ljust(length) for cell, length in zip(cells, max_lengths))
            print(formatted_line)

    def search_and_display_record_by_id(self, search_id):
        lines = open(self.filename, "r").read().strip().split('\n')
        headers = lines[0].split('_')
        found_cells = self.search_patient_by_id(search_id)
        self.display_found_record(found_cells, headers)

    def search_patient_by_id(self, search_id):
        with open(self.filename, "r") as content:
            lines = content.read().strip().split('\n')
        for line in lines:
            cells = line.split('_')
            if cells[0] == search_id:
                return cells
        return None
    def display_found_record(self, found_cells, headers):
        if found_cells:
            max_lengths = [max(len(header), len(cell)) for header, cell in zip(headers, found_cells)]
            formatted_header = '   '.join(header.ljust(length) for header, length in zip(headers, max_lengths))
            formatted_line = '   '.join(cell.ljust(length) for cell, length in zip(found_cells, max_lengths))

            print("\nFound Record:")
            print(formatted_header)
            print(formatted_line)
        else:
            print("Can't find the Patient with the same id on the system")
    def add_patient_to_file(self, new_patient):

        file = open(self.filename, "a")
        file.write("\n"+new_patient.getpatientid() + "_" + new_patient.getpname() + "_" + new_patient.getdisease() + "_" +
                new_patient.getgender() + "_" + new_patient.getage())
        print(f"Patient whose ID is {new_patient.getpatientid()} has been added")
        file.close()

    def edit_patient_to_file(self, edit_patient):
        file = open(self.filename, "r+")
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i]
            parts = line.strip().split("_")
            if parts and parts[0] == edit_patient.getpatientid():

                parts[1] = edit_patient.getpname()
                parts[2] = edit_patient.getdisease()
                parts[3] = edit_patient.getgender()
                parts[4] = edit_patient.getage()

                lines[i] = "_".join(parts) + "\n"

        file.seek(0)
        file.writelines(lines)
        print(f"Patient whose ID is {edit_patient.getpatientid()} has been edited")
        file.close()





class Management:
    def __init__(self):
        self.record_system = DoctorManager("doctors.txt")
        self.record_patient = PatientManager("patients.txt")


    def display_doctors_list(self):
        self.record_system.display_doctors_list()

    def search_doctors_by_id(self):
        search_id = input("Enter the doctor ID: ")
        self.record_system.search_and_display_record_by_id(search_id)

    def search_doctors_by_name(self):
        search_name = input("Enter the doctor name: ")
        self.record_system.search_and_display_record_by_name(search_name)

    def add_doctor(self):
        doctorid = input("Enter the doctor’s ID: ")
        name = input("Enter the doctor’s name: ")
        specialization = input("Enter the doctor’s Enter the doctor’s specility: ")
        workingtime = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor’s qualification ")
        roomnumber = input("Enter the doctor’s room number: ")
        new_doctor = Doctor(doctorid, name, specialization, workingtime, qualification, roomnumber)
        self.record_system.add_dr_to_file(new_doctor)


    def edit_doctor_info(self):
        doctorid = input("Please enter the id of the doctor that you want to edit their information: ")
        name = input("Enter new Name: ")
        specialization = input("Enter new Specilist in: ")
        workingtime = input("Enter new Timing: ")
        qualification = input("Enter new Qualification: ")
        roomnumber = input("Enter new Room number: ")
        edit_doctor = Doctor(doctorid, name, specialization, workingtime, qualification, roomnumber)
        self.record_system.edit_dr_to_file(edit_doctor)


    def display_patient_list(self):
        self.record_patient.display_patient_list()

    def search_patient_by_Id(self):
        search_id = input("Enter the Patient Id: ")
        self.record_patient.search_and_display_record_by_id(search_id)

    def add_patient(self):
        patientid = input("Enter Patient id:: ")
        pname = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender:")
        age = input("Enter Patient age: ")

        new_patient = Patients(patientid, pname, disease, gender, age)
        self.record_patient.add_patient_to_file(new_patient)


    def edit_patient_info(self):
        patientid = input("Please enter the id of the Patient that you want to edit their information: ")
        pname = input("Enter new Name: ")
        disease = input("Enter new disease:: ")
        gender = input("Enter new gender: ")
        age= input("Enter new age:  ")

        edit_patient = Patients(patientid, pname, disease, gender, age)
        self.record_patient.edit_patient_to_file(edit_patient)







    def doctormanager(self):
        while True:

            doctorchoice = input(
                "Doctors Menu\n"
                "1 - Display Doctors list\n"
                "2 - Search for doctors by ID\n"
                "3 - Search for doctors by name\n"
                "4 - Add Doctor\n"
                "5 - Edit doctor info\n"
                "6 - Back to the Main Menu\n>>> "
            )

            if doctorchoice == "1":
                self.display_doctors_list()
            elif doctorchoice == "2":
                self.search_doctors_by_id()
            elif doctorchoice == "3":
                self.search_doctors_by_name()
            elif doctorchoice == "4":
                self.add_doctor()
            elif doctorchoice == "5":
                self.edit_doctor_info()
            elif doctorchoice == "6":
                Management().main()

            else:
                print("Invalid choice")


    def patientmanager(self):
        while True:

            patientchoice = input(
                "Doctors Menu\n"
                "1 - Display patients list\n"
                "2 - Search for patient by ID\n"
                "3 - Add patient\n"
                "4 - Edit patient info\n"
                "5 - Back to the Main Menu\n>>> "
            )
            if patientchoice == "1":
                self.display_patient_list()
            elif patientchoice == "2":
                self.search_patient_by_Id()
            elif patientchoice == "3":
                self.add_patient()
            elif patientchoice == "4":
                self.edit_patient_info()

            elif patientchoice <= "5":
                Management().main()
            else:
                print("Invalid Input")







    def main(self):
        mainmenu = eval(input(
            "Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 3 to stop:"
            "\n1 -     Doctors\n2 -     Patients\n3 -     Exit Program\n>>> "))
        if (mainmenu == 1):
            Management().doctormanager()
        if (mainmenu == 2):
            Management().patientmanager()
        if (mainmenu == 3):
            print("Thanks for using the program. Bye!")
            exit()


if __name__ == "__main__":

    Management().main()







