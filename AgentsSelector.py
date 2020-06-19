import datetime
import random
import re

# I have prefixed with __ in someplaces to hide variable and functions from user
# I have made Agent class assuming that each agent will have unique id which is automatically generated and cannot be changed by user of the code
#I have also assumed that as soon as Agent object( agent in real life) is created it will be available to work from then unless said otherwise via parameter
#I have used property decorators to manipulate the dot access to restrict user from changing or setting some values
#Also I have sometimes used direct dictionary access like obj.__dict__ to avoid dot lookup chain and infinite recursion in lookups

class Agent:

    __counter=0 #basically helps us in giving unique id to each Agent object

    def __init__(self,*,isAvailable=True,availableSince='',roles=''): #roles is space seperated string like 'a b   c' and format for availableSince parameter is 'yyyy-mm-dd'
        if isAvailable is True and availableSince:
            p=re.compile("^\d{4}-\d{2}-\d{2}$") #to check entered date pattern for availableSince
            m=p.match(availableSince)
            if m:
                dt=availableSince.split("-")
            else:
                raise ValueError("date for availableSince must be string of the form 'yyyy-mm-dd'")
            self.availableSince=datetime.date(int(dt[0]),int(dt[1]),int(dt[2]))
            self.__dict__['isAvailable']=True
        else:
            self.isAvailable=isAvailable
        self.roles=roles
        self.__dict__["id"]=Agent.__counter
        Agent.__counter+=1
            
    @property
    def isAvailable(self):
        return self.__dict__.get('isAvailable')

    @isAvailable.setter
    def isAvailable(self,boolean):
        # just setting isAvailable to true will automatically set the AvailableSince to current Date on which isAvailable is set to True
        if boolean is True:
            if not self.__dict__.get('isAvailable'): # this helps prevent user from updating availableSince by mistake, by checking if isAvailable is already set
                self.availableSince=datetime.date.today()
                self.__dict__['isAvailable']=True
        elif boolean is False:
            self.availableSince=None
            self.__dict__['isAvailable']=False
        else:
            raise ValueError("Allowed value is 'True' or 'False' ")
    
    @property
    def roles(self):
        return self.__dict__.get('roles')
    
    @roles.setter
    def roles(self,stringOfRoles):
        if isinstance(stringOfRoles,str):
            self.__dict__['roles']= stringOfRoles.split()
        else:
            raise ValueError("roles must be space seperated string")
    
    def __helper(self):
        if self.isAvailable:
            return "currently available"
        else:
            return "currently unavailable"

    def __str__(self):
        return f"Agent id: {self.id} roles: {self.roles} status: {self.__helper()}"

    @property
    def id(self):
        return self.__dict__['id']
    
    @id.setter
    def id(self,value):
        raise Exception("cannot set value to 'id' attribute of Agent object")

    def __repr__(self):
        return f"Agent id:{self.id}"


def returnSuitableAgents(listOfAgents,agentSelectionMode,issueRoles):# issueRoles to be matched with Agents having all required roles
    agentsToReturn=[]
    if agentSelectionMode=="Least Busy": #returns list of agents who are available with  required roles and also far more available than other agents. It may happen that two or more agents are available from same time that's why I have returned list
        currentdt=datetime.date.today()
        max_gap=None
        for agent in listOfAgents:
            if agent.isAvailable:
                for role in issueRoles: #if issueRoles is empty list then returns all available agents as there is no specific role requirement for that issue
                    if role not in agent.roles:
                        break #role requirement not satisfied by agent so move on to next agent
                else:
                    if max_gap is None:
                        max_gap=currentdt-agent.availableSince
                        agentsToReturn.append(agent)
                    elif currentdt-agent.availableSince>max_gap:
                        agentsToReturn=[]#resets the list to return new list of agents who are far more available
                        agentsToReturn.append(agent)
                        max_gap=currentdt-agent.availableSince
                    elif currentdt-agent.availableSince==max_gap:
                        agentsToReturn.append(agent)
        return agentsToReturn
    elif agentSelectionMode in ("All Available","Random") :
        #returns list of agents who are available and have required roles when agentSelectionMode=="All Available"
        #and will return Random agent who is available and have required roles when agentSelectionMode=="Random"
        for agent in listOfAgents:
            if agent.isAvailable:
                for role in issueRoles: #if issueRoles is empty list then returns all available agents as there is no specific role requirement for that issue
                    if role not in agent.roles:
                        break #role requirement not satisfied by agent so move on to next agent
                else:
                    agentsToReturn.append(agent)
        if agentSelectionMode=="All Available":
            return agentsToReturn 
        else:
            if agentsToReturn==[]:# done to prevent Exception on random.choices([])
                return []
            return random.choices(agentsToReturn)
    else:
        raise ValueError("agentSelection mode should be one of '(\"Least Busy\",\"Random\",\"All Available\")'")


