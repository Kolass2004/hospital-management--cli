class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_details(self):
        return f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def get_appointments(self):
        return self.appointments


class Appointment:
    def __init__(self, appointment_id, date, time, doctor_name, reason):
        self.appointment_id = appointment_id
        self.date = date
        self.time = time
        self.doctor_name = doctor_name
        self.reason = reason

    def get_details(self):
        return f"Appointment ID: {self.appointment_id}, Date: {self.date}, Time: {self.time}, Doctor: {self.doctor_name}, Reason: {self.reason}"


class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient_id, name, age, gender):
        if patient_id not in self.patients:
            patient = Patient(patient_id, name, age, gender)
            self.patients[patient_id] = patient
            print("Patient added successfully.")
        else:
            print("Patient with this ID already exists.")

    def add_appointment(self, patient_id, appointment_id, date, time, doctor_name, reason):
        if patient_id in self.patients:
            appointment = Appointment(appointment_id, date, time, doctor_name, reason)
            self.patients[patient_id].add_appointment(appointment)
            print("Appointment added successfully.")
        else:
            print("Patient not found.")

    def view_patient_details(self, patient_id):
        if patient_id in self.patients:
            print(self.patients[patient_id].get_details())
        else:
            print("Patient not found.")

    def view_appointments(self, patient_id):
        if patient_id in self.patients:
            appointments = self.patients[patient_id].get_appointments()
            if appointments:
                for appointment in appointments:
                    print(appointment.get_details())
            else:
                print("No appointments found.")
        else:
            print("Patient not found.")


def main():
    system = HospitalManagementSystem()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Add Appointment")
        print("3. View Patient Details")
        print("4. View Appointments")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))
            gender = input("Enter Patient Gender: ")
            system.add_patient(patient_id, name, age, gender)
        elif choice == '2':
            patient_id = input("Enter Patient ID: ")
            appointment_id = input("Enter Appointment ID: ")
            date = input("Enter Appointment Date (YYYY-MM-DD): ")
            time = input("Enter Appointment Time (HH:MM): ")
            doctor_name = input("Enter Doctor's Name: ")
            reason = input("Enter Reason for Appointment: ")
            system.add_appointment(patient_id, appointment_id, date, time, doctor_name, reason)
        elif choice == '3':
            patient_id = input("Enter Patient ID: ")
            system.view_patient_details(patient_id)
        elif choice == '4':
            patient_id = input("Enter Patient ID: ")
            system.view_appointments(patient_id)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
