class Patient:  # parent class #
    def __init__(self, name):
        self.name = name

    def discharge(self):
        # abstract method to be overridden in derived classes#
        # :returns name and type of patient #
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class EmergencyPatient(Patient):  # child class #
    def __init__(self, name):
        Patient.__init__(self, name)
        self.departmentCost = ep_cost  # general cost = # department specific cost #

    def discharge(self):
        print(self.name, ": Emergency Patient")  # discharge name and type #


class HospitalizedPatient(Patient):  # child class #
    def __init__(self, name):
        Patient.__init__(self, name)
        self.departmentCost = hp_cost  # general cost = department specific cost #

    def discharge(self):
        print(self.name, ": Hospitalized Patient")  # discharge name and type #


class Hospital:
    def __init__(self):
        self.cost = 0  # self.cost is the base cost #
        self.patients = []  # to create list pf patients #

    def admit(self,Patient):  # calls patient from Patient class #
        self.patients.append(Patient)  # admits by adding patient to the patients variable #

    def discharge_all(self):
        for Patient in self.patients:  # for each member of the patients list#
            Patient.discharge()  # calls the discharge function with each patient child class #
            self.cost += Patient.departmentCost  # the discharge call also initializes the cost function #

    def get_total_cost(self):
        return self.cost  # returns self.cost for each discharge #


ep_cost = 1000  # emergency room cost #
hp_cost = 2000  # hospitalization cost #

H1 = Hospital()  # create an instance of the hospital #

P1 = EmergencyPatient("Larry")
P2 = EmergencyPatient("Moe")
P3 = EmergencyPatient("Curly")
P4 = HospitalizedPatient("Punch")
P5 = HospitalizedPatient("Judy")

H1.admit(P1)
H1.admit(P2)
H1.admit(P3)
H1.admit(P4)
H1.admit(P5)
H1.discharge_all()
H1.get_total_cost()

print("Total cost for the day: "'${:,.2f}'.format(H1.get_total_cost()))

