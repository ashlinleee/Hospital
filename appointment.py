class Appointment:
    def __init__(self, patient_name, doctor_name, appointment_day, appointment_time, consultation_fee):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_day = appointment_day
        self.appointment_time = appointment_time
        self.consultation_fee = consultation_fee

    def display_info(self):
        print("\n---------------Appointment Details----------------\n")
        print(f"              Patient: {self.patient_name}")
        print(f"              Doctor: {self.doctor_name}")
        print(f"              Day: {self.appointment_day}")
        print(f"              Time: {self.appointment_time}")
        print(f"              Consultation Fee: Rs.{self.consultation_fee}\n")
        print("------------------------------------------------------")