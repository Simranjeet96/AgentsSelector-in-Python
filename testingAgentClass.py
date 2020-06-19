import unittest
import datetime
from AgentsSelector import Agent
from AgentsSelector import returnSuitableAgents

class TestAgent(unittest.TestCase):
    
    def test_AgentObjectCreation(self):
        agent_0=Agent(roles='a b   c',isAvailable=False,availableSince="1997-09-19")
        self.assertEqual(agent_0.roles,['a','b','c'])
        self.assertEqual(agent_0.availableSince,None)
        self.assertEqual(agent_0.isAvailable,False)

        agent_1=Agent(roles='a      b   c',isAvailable=True,availableSince="1997-09-19")
        self.assertEqual(agent_1.roles,['a','b','c'])
        self.assertEqual(str(agent_1.availableSince),"1997-09-19")
        self.assertEqual(agent_1.isAvailable,True)
        
        with self.assertRaises(ValueError):
            #raises ValueError because required date format which is 'yyyy-mm-dd' for availableSince is not satisifed
            agent_2=Agent(roles='a b d',isAvailable=True,availableSince="97-09-19")

        agent_3=Agent(roles='a b e  c',isAvailable=True)
        self.assertEqual(agent_3.roles,['a','b','e','c'])
        self.assertNotEqual(agent_3.availableSince,None) #agent_3.availableSince will have date on which agent_3 was created since no value is passed to availableSince argument during agent object creation
        self.assertEqual(agent_3.isAvailable,True)

        agent_4=Agent(roles='a b e  c',isAvailable=False,availableSince="1997-09-19")
        #setting value of availableSince when isAvailable=False will set availableSince to None so it doesn't matter what value you give to availableSince when isAvailable=False
        self.assertEqual(agent_4.roles,['a','b','e','c'])
        self.assertEqual(agent_4.availableSince,None)
        self.assertEqual(agent_4.isAvailable,False)

        agent_5=Agent(roles='',isAvailable=True,availableSince="1997-09-19")
        self.assertEqual(agent_5.roles,[])
        self.assertEqual(str(agent_5.availableSince),"1997-09-19")
        self.assertEqual(agent_5.isAvailable,True)

        with self.assertRaises(ValueError):
            #raises ValueError because required date format which is 'yyyy-mm-dd' for availableSince is not satisifed
            agent_6=Agent(roles='a b d',isAvailable=True,availableSince="23 JAN 19")
        
        with self.assertRaises(ValueError):
            #raises ValueError because required roles value is string
            agent_7=Agent(roles=['a', 'b', 'd'],isAvailable=True,availableSince="1997-09-19")

        agent_8=Agent(roles='a b')
        self.assertEqual(agent_8.roles,['a','b'])
        self.assertNotEqual(agent_8.availableSince,None)
        self.assertEqual(agent_8.isAvailable,True)#default value of isAvailable is True and it also sets the value of availableSince attribute of agent object to its initialization date that's why above testCase also passes

        agent_9=Agent()
        self.assertEqual(agent_9.roles,[])
        self.assertNotEqual(agent_9.availableSince,None)
        self.assertEqual(agent_9.isAvailable,True)#default value of isAvailable is True and it also sets the value of availableSince attribute of agent object to its initialization date that's why above testCase also passes

        agent_10=Agent(availableSince="1997-09-19")
        self.assertEqual(agent_10.roles,[])
        self.assertEqual(str(agent_10.availableSince),"1997-09-19")
        self.assertEqual(agent_10.isAvailable,True)#default value of isAvailable is True

    def test_AvailableSince(self):
        agent_11=Agent(roles='a b',isAvailable=True,availableSince="1998-03-18")
        self.assertEqual(str(agent_11.availableSince),"1998-03-18")
        agent_11.isAvailable=False
        self.assertEqual(agent_11.availableSince,None)
        agent_11.isAvailable=True# should change the availableSince date to when isAvailable attribute is set to true
        dt=datetime.date.today()
        self.assertEqual(agent_11.availableSince,dt)
        agent_11.isAvailable=True# again setting it to True shouldn't change the date of attribute availableSince
        self.assertEqual(agent_11.availableSince,dt)

    def test_id(self):
        agent_12=Agent()
        with self.assertRaises(Exception):
            agent_12.id=1 # cannot set id as its unique and automatically assigned during initialization so it must raise Exception

if __name__=="__main__":
    unittest.main()