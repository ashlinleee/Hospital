class Doctor:
    def __init__(self, name, specialization, department, consultation_fee):
        self.name = name
        self.specialization = specialization
        self.department = department
        self.consultation_fee = consultation_fee

    def display_info(self):
        print(f"Doctor: {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"Department: {self.department}")
        print(f"Consultation Fee: Rs.{self.consultation_fee}")
        print("--------------------------------------------")



class DoctorAvailability:
    def __init__(self, day_of_week, times_available):
        self.day_of_week = day_of_week
        self.times_available = times_available


class ExtDoc(Doctor):
    def __init__(self, name, specialization, department, consultation_fee, availability):
        super().__init__(name, specialization, department, consultation_fee)
        self.availability = availability

    def display_info(self):
        super().display_info()
        print("Available Days and Times:")
        for avail in self.availability:
            print(f"Day: {avail.day_of_week.capitalize()} - Times: {', '.join(avail.times_available)}")
        print("--------------------------------------------")
        
