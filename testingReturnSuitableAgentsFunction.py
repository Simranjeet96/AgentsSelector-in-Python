import unittest
import AgentsSelector
import importlib
class TestReturnSuitableAgents(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.issueXRoles=['a','b']#roles required by agent to solve issue X
        cls.issueYRoles=['a']
        cls.issueZRoles=['b','c']
        cls.issueARoles=['a','c']
        cls.issueBRoles=['e']
        cls.issueCRoles=[]
        cls.issueDRoles=['a','b','c','e']
        cls.issueERoles=['a','d']
        cls.issuesList=[('issueA',cls.issueARoles),('issueB',cls.issueBRoles),('issueC',cls.issueCRoles),('issueD',cls.issueDRoles),('issueE',cls.issueERoles),('issueX',cls.issueXRoles),('issueY',cls.issueYRoles),('issueZ',cls.issueZRoles)]


    def setUp(self):
        importlib.reload(AgentsSelector)
        self.agent_0=AgentsSelector.Agent(roles='a b e',isAvailable=True,availableSince="2019-03-15")
        self.agent_1=AgentsSelector.Agent(roles='a c',isAvailable=True,availableSince="2019-04-15")
        self.agent_2=AgentsSelector.Agent(roles='a',isAvailable=True,availableSince="2020-05-25")
        self.agent_3=AgentsSelector.Agent(roles='a b c',isAvailable=False)
        self.agent_4=AgentsSelector.Agent(roles='a c e b',isAvailable=True)#will set availableSince value to object initialization date
        self.agent_5=AgentsSelector.Agent()
        self.agentsList=[self.agent_0,self.agent_1,self.agent_2,self.agent_3,self.agent_4,self.agent_5]
        print("AGENTS INFO")
        for agent in self.agentsList:
            print(agent)
        for issueName,issueRoles in self.issuesList:
            print(issueName,":",issueRoles)
    def testOutputsWithLeastBusyMode(self):
        print("--Running Least Busy Mode--"*3)
        for issueName,issueRoles in self.issuesList:
            print(f'Agents for {issueName} are',AgentsSelector.returnSuitableAgents(self.agentsList,"Least Busy",issueRoles))
        print("\n\n")

    def testOutputsWithRandomMode(self):
        print("--Running Random Mode--"*3)
        for issueName,issueRoles in self.issuesList:
            print(f'Agents for {issueName} are',AgentsSelector.returnSuitableAgents(self.agentsList,"Random",issueRoles))
        print("\n\n")

    def testOutputsWithAllAvailableMode(self):
        print("--Running All Available Mode--"*3)
        for issueName,issueRoles in self.issuesList:
            print(f'Agents for {issueName} are',AgentsSelector.returnSuitableAgents(self.agentsList,"All Available",issueRoles))
        print("\n\n")

if __name__=="__main__":
    unittest.main()
