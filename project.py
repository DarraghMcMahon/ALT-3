#Import the librarys needed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

#Create the seirModel function
def seirModel(populationSize, initialInfected, initialRecovered, transmissionRate, contactRate, infectiousPeriod, incubationPeriod, simulationDays):
    
    #Change the rates
    recoveryRate = 1/infectiousPeriod
    incubationRate = 1/incubationPeriod
    
    #Create arrays to store results inside
    listS = np.zeros(simulationDays + 1)
    listE = np.zeros(simulationDays + 1)
    listI = np.zeros(simulationDays + 1)
    listR = np.zeros(simulationDays + 1)
    
    #Create intial conditions
    listS[0] = populationSize - (initialInfected + initialRecovered)
    listE[0] = 0
    listI[0] = initialInfected
    listR[0] = initialRecovered
    
    #Change the current Values
    S = listS[0]
    E = listE[0]
    I = listI[0]
    R = listR[0]
    
    #This loop simulates each day
    for day in range(1, simulationDays + 1):
        
        #Newly changed equations
        newlyExposed = (transmissionRate * contactRate * S * I) / populationSize #I initially forgot to divide by populationSize and that threw off the acuracy at this part
        newlyInfected = (incubationRate * E)
        newlyRecovered = (recoveryRate * I)
        
        #Update values
        S = S - newlyExposed
        E = E + (newlyExposed - newlyInfected)
        I = I + (newlyInfected - newlyRecovered)
        R = R + newlyRecovered
        
        #Store the results
        listS[day] = S
        listE[day] = E
        listI[day] = I
        listR[day] = R
        
    return listS, listE, listI, listR
    
#Inputs from the user
print("Virus SEIR Model")
print("Press enter to input 'e.g' values")
pop = int(input("Enter population size (e.g. 1,000,000): ")or 1000000)
inf = int(input("Enter People infected(e.g. 10): ")or 10)
rec = int(input("Enter number of people already recovered (e.g. 0): ")or 0)
tra = float(input("Enter transmission rate (e.g. 0.3): ")or 0.3)
con = float(input("Enter contact rate per person (e.g. 10): ")or 10)
infp = float(input("Enter infectious period in days (e.g. 14): ")or 14)
inc = float(input("Enter incubation period in days (e.g. 5): ")or 5)
days = int(input("Enter number of days to simulate (e.g. 160): ")or 160)

#Run the seirModel function
S, E, I, R = seirModel(pop, inf, rec, tra, con, infp, inc, days)

#Plot the results
days = np.arange(len(S))
plt.figure(figsize=(10,6))
plt.plot(days, S, label="Susceptible")
plt.plot(days, E, label="Exposed")
plt.plot(days, I, label="Infected")
plt.plot(days, R, label="Recovered")

#Labels/Formating
plt.xlabel("Days")
plt.ylabel("Number of People")
plt.title("Virus SEIR Model")
plt.legend()
plt.grid()

#This part ensures the y axis labels are whole numbers and include commas
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.show()

#67
