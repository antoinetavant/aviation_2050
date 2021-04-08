import numpy as np
import matplotlib.pyplot as plt


def traj_ref(config, years):
    """ creat the Reference trajectory 'business as usual' taking intoo account the Covid impact
    The coefficient are use to reproduce the impactes on the World market, starting in 2018"""
    traj = np.zeros_like(years)
    
    traj[0] = float(config["ImpactCovid"]["year_2018"])
    traj[1] = float(config["ImpactCovid"]["year_2019"])
    traj[2] = float(config["ImpactCovid"]["year_2020"])
    traj[3] = float(config["ImpactCovid"]["year_2021"])
    traj[4] = float(config["ImpactCovid"]["year_2022"])
    traj[5] = float(config["ImpactCovid"]["year_2023"])
    traj[6] = float(config["ImpactCovid"]["year_2024"])

    growthCoef = 1 + float(config["referenceWord"]["increaseTraficPerCent"])/100
    
    for index in np.arange(7, len(years)):
        traj[index] = traj[index-1]*growthCoef
    
    return traj


def traj_objective(config, years):
    
    traj = np.zeros_like(years)
    growthCoef = 1 + float(config["ObjectifWord"]["increaseTraficPerCent"])/100

    traj[0] = float(config["InitialState"]["emission_2018_wd"])
    for index in np.arange(1, len(years)):
        traj[index] = traj[index-1]*growthCoef
        
    return traj

def optimisation_traj(trajectory, factor=None, factor_yearly=None):
    """reduce the reference trajectory """
    
    if factor_yearly is None:
        factor_yearly = 1-(1-factor) ** (1/ (len(trajectory)) ) 
    #print(factor_yearly)
    
    trajectory_opt = trajectory.copy()
    
    firstIndex = 1
    for i in np.arange(firstIndex,len(trajectory)):
        trajectory_opt[i] = trajectory[i]* (1 - factor_yearly)**(i-firstIndex)
        
    return trajectory_opt


