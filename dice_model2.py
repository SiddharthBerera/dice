import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

T_START = 2020 
Ti_max = 100 
DELTA_T = 5


#---------------------------------------------------------------------------------
#Equation 1 - social welfare to be optimised
def social_welfare(c_s, L_s):
    total_social_welfare = 0
    for t in range(0,Ti_max):
        total_social_welfare += utility(c_s[t],L_s[t])*discount_factor(t)
    return total_social_welfare
#---------------------------------------------------------------------------------
#Equation 2
def utility(c,L):
    elasticity_marginal_utility = 1.5 #phi
    return L*(c**(1-elasticity_marginal_utility)/(1-elasticity_marginal_utility))
#Equation 3 (Psi)

def discount_factor(t): 
    pure_rate_social_time_pref = 0.01 #rho
    return 1/(1+pure_rate_social_time_pref)




#Equation 4 - labour
def labour():
    population_init = 7753
    population_growth_lim = 10825
    population_growth_rate = 0.145 #per 5 year period
    Labor = np.zeros(Ti_max)
    Labour[0] = population_init  
    for t in range(1,Ti_max):
        Labour[t] = Labour[t-1]*(population_growth_lim/Labour[t-1])**population_growth_rate
    
#Equation 4 - total factor productivity
def total_factor_productivity():
    tfp_init = 5.8416
    tfp_init_growth = 0.082
    tfp_decline = 0.0072 #per 5 year period 
    TFP = np.zeros(Ti_max)
    TFP[0] = tfp_init
    for t in range(1,Ti_max):
        TFP[t] = TFP[t-1]*(1-tfp_init_growth*np.exp(-tfp_decline*5*t))

#Equation 4 - global output
def production():
    capital_elasticity = 0.3
    Gross_Output = np.zeros(Ti_max)
    for t in range(0,Ti_max):
        Gross_Ouput[t] = (1-abatement[t])*(1-CD[t])*TFP[t]*(K(t)**capital_elasticity)*(Labour[t]**(1-capital_elasticity))

#Equation 5 - climate damages
def climate_damage(t):
    phsi1 = 0
    phsi2 = 0.003467
    CD = np.zeros(T_max)
    for t in range(0,Ti_max)
        CD[t] = phsi1*T_AT(t)+phsi2*(T_AT(t)**2)

#Equation 6 - abatement cost
def abatement_cost():
    theta2 = 2.6
    abatement = np.zero(Ti_max)
    for t in range(0,Ti_max):
        abatement[t] = theta1[t]*mu(t)**theta2

#Equation 6 - theta1
def output_proportion_to_abate():
    opta_init = 0.109062
    zero_emission_abatement_ratio1 = 1.7 #until 2100
    zero_emission_abatement_ratio2 = 2.7
    theta1 = np.zeros(Ti_max)
    for t in range(0,Ti_max):
        if t<=14:
            theta1[t] = opta_init*(1-zero_emission_abatement_ratio1)**(5*t)
        if t>14:
            theta1[t] = opta_init*((1-zero_emission_abatement_ratio1)**70)*((1-zero_emission_abatement_ratio2)**(5*(t-14)))

#Equation 6 - backstop cost
def backstop_cost():
    backstop_cost_2050 = 515
    learningrate1 = 0.01
    learningrate2 = 0.001
    backstop_cost_2020 = backstop_cost_2050/(1-learningrate1)**30
    p_B = np.zeros(Ti_max)
    for t in range(0,Ti_max):
        if t<=5:
            p_B[t] = backstop_cost_2020*(1-learningrate1)**t
        if t>5:
            p_B[t] = backstop_cost_2020*((1-learningrate1)**5)*((1-learningrate2)**(t-5))

#sigma
