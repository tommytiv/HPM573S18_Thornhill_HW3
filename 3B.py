class Node:
    """ base class """

    def __init__(self, name, cost, utility):
        """
        :param name:
        :param cost:
        :param utility:
        """
        self.name = name
        self.cost = cost
        self.utility = utility

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to implemented in derived classes.")

    def get_expected_utility(self):
        """ abstract method to be overridden in derived classes
        :returns expected utility of this node """
        raise NotImplementedError("This is an abstract method and needs to implemented in derived classes.")

class ChanceNode(Node):
    def __init__(self, name, cost, utility, future_nodes, probs):
        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        exp_cost = self.cost  # the expected cost of this node including cost of visit
        i = 0  # index to iterate over probabilities
        for node in self.futureNodes:
            exp_cost += self.probs[i] * node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_utility(self):
        exp_utility = self.utility  # the expected utility of this node including utility of visit
        i = 0  # index to iterate over probabilities
        for node in self.futureNodes:
            exp_utility += self.probs[i] * node.get_expected_utility()
            i += 1
        return exp_utility


class TerminalNode(Node):
    def __init__(self, name, cost, utility):
        Node.__init__(self, name, cost, utility)

    def get_expected_cost(self):
        return self.cost

    def get_expected_utility(self):
        return self.utility

class DecisionNode(Node):
    def __init__(self, name, cost, utility, future_nodes):
        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes

    def get_expected_cost(self):
        """return the expected cost of associated future nodes"""
        outcomes = dict()  # dictionary to store expected cost of future nodes
        for thisNode in self.futureNodes:
            outcomes[thisNode.name] = thisNode.get_expected_cost()
        return outcomes

    def get_expected_utility(self):
        """return the expected utility of associated future nodes"""
        outcomes = dict()  # dictionary to store expected utility of future nodes
        for thisNode in self.futureNodes:
            outcomes[thisNode.name] = thisNode.get_expected_utility()
        return outcomes


# creating terminal nodes
T1 = TerminalNode("T1", cost=10, utility = 0.9)
T2 = TerminalNode("T2", cost=20, utility = 0.8)
T3 = TerminalNode("T3", cost=30, utility = 0.7)
T4 = TerminalNode("T4", cost=40, utility = 0.6)
T5 = TerminalNode("T5", cost=50, utility = 0.5)

# creating future nodes & chance nodes, note this order works #

C2FutureNodes = [T1, T2]
C2 = ChanceNode("C2", 35, 0, C2FutureNodes, [0.7, 0.3])

C1FutureNodes = [C2, T3]
C1 = ChanceNode("C1", 25, 0, C1FutureNodes, [0.2, 0.8])

C3 = ChanceNode("C3", 45, 0, [T4, T5], [0.1, 0.9])

D1 = DecisionNode("D1", 0, 0, [C1, C3])

print("Expected costs of nodes C1 and C3: ", D1.get_expected_cost())
print("Expected health utility of nodes C1 and C3:", D1.get_expected_utility())
