
class Patient:
    """ base class """
    def __init__(self, name, admit, cost):
        self.name = name
        self.admit = admit
        self.cost = cost

    def discharge(self):
        """ abstract method to be overridden in derived classes
        :returns name and type of patient """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class EmergencyPatient(Patient):
    def __init__(self, name, admit, cost):
       Patient.__init__(self, name, admit, cost)

    def discharge(self):
        return str(self.admit)

    def patient_cost(self):
        return self.cost

class HospitalizedPatient(Patient):
    def __init__(self, name, admit, cost):
        Patient.__init__(self, name, admit, cost)

    def discharge(self):
        return str(self.admit)

    def cost(self):
        return self.cost

class Hospital:
    def __init__(self, discharge_all,get_total_cost):
        self.discharge_all = discharge_all
        self.get_total_cost = get_total_cost

    def dischargeAll(self):
        outcomes = dict()
        for patient in self.discharge_all:
            outcomes[patient.name]= patient.discharge()
        return outcomes

    def getTotalCost(self):
        TotalCost = sum()
        for patient in self.get_total_cost:
            TotalCost[patient.cost] = sum(patient.cost())
        return TotalCost

ep_cost = 1000
hp_cost = 2000

P1 = EmergencyPatient("Larry","Emergency Patient",ep_cost)
P2 = HospitalizedPatient("Moe","Hospital Patient",hp_cost)
H = Hospital([P1, P2],[P1,P2])

print (H.dischargeAll())
print (H.getTotalCost())
