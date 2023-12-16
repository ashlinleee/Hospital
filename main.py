from Hospital.appointment import *
from Hospital.patients import *
from Hospital.doctor import *


def main():
    doctor1 = ExtDoc("Dr. Akriti", "Cardiology🫀", "Cardiology Department", 1500, [
        DoctorAvailability("monday", ["09:00", "11:00", "14:00"]),
        DoctorAvailability("thursday", ["10:00", "12:00"]),
        DoctorAvailability("friday", ["15:00", "16:00", "17:00"])
    ])
    doctor2 = ExtDoc("Dr. Bhagyashree", "Orthopedics🦴", "Orthopedics Department", 1800, [
        DoctorAvailability("tuesday", ["08:00", "10:00", "13:00"]),
        DoctorAvailability("wednesday", ["11:00", "12:00"]),
        DoctorAvailability("thursday", ["14:00", "15:00", "16:00"])
    ])
    doctor3 = ExtDoc("Dr. Riya", "Neurology🧠", "Neurology Department", 2000, [
        DoctorAvailability("monday", ["09:00", "11:00", "14:00"]),
        DoctorAvailability("thursday", ["10:00", "12:00"]),
        DoctorAvailability("friday", ["15:00", "16:00", "17:00"])
    ])
    doctor4 = ExtDoc("Dr. Ashlin", "Paediatric👶🏻", "Paediatric Department", 1600, [
        DoctorAvailability("monday", ["09:00", "11:00", "14:00"]),
        DoctorAvailability("thursday", ["10:00", "12:00"]),
        DoctorAvailability("friday", ["15:00", "16:00", "17:00"])
    ])

    patient_name = input("\nEnter patient name: ")
    patient_age = int(input("Enter patient age: "))
    patient_gender = input("Enter patient gender: ")

    patient = Patient(patient_name, patient_age, patient_gender)
    patient.display_info()
    print("--------------------------------------------")
    

    print("ID: 1")
    doctor1.display_info()
    print("--------------------------------------------")
    

    print("ID: 2")
    doctor2.display_info()
    print("--------------------------------------------")

    
    print("ID: 3")
    doctor3.display_info()
    print("--------------------------------------------")

    
    print("ID: 4")
    doctor4.display_info()
    print("--------------------------------------------")



    choice = input("\nSelect a doctor by entering their ID: ")
    selected_doctor = None
    if choice == "1":
        selected_doctor = doctor1
    elif choice == "2":
        selected_doctor = doctor2
    elif choice == "3":
        selected_doctor = doctor3
    elif choice == "4":
        selected_doctor = doctor4
    else:
        print("Invalid choice")
    

    if selected_doctor:
        selected_day = input("Enter preferred day for appointment (e.g., Monday, Tuesday, etc.): ").lower()
        available_times = None

        for availability in selected_doctor.availability:
            if availability.day_of_week == selected_day:
                available_times = availability.times_available
                break

        if available_times:
            print(f"Available times on {selected_day.capitalize()}: {', '.join(available_times)}")
            selected_time = input("Select appointment time: ")

            if selected_time in available_times:
                appointment = Appointment(patient_name, selected_doctor.name, selected_day.capitalize(), selected_time, selected_doctor.consultation_fee)
                appointment.display_info()
                print("Appointment booked successfully!")
            else:
                print("Invalid time selected. Appointment not booked.")
        else:
            print("Doctor not available on the selected day.")
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
