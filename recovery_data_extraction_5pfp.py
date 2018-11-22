'''Converting all those output CSV files into a single large CSV in an easier to deal with format'''
import numpy as np
import pandas as pd
import os.path

stars = np.genfromtxt("planets.csv", delimiter=',', names=True, dtype=("U23", "U9", int, float, float, float, float, float, float, float, float, float, float))
star_name = stars[0]["HIPnumber"]
file_postfix = "5p" # note: columns = 2+(planets*parameters). 5p and fp have 4 parameters, while ep and np have 3! ([5,e,f,n]n may have more like 5+(remaining_planets*parameters), and given the way planets are truncated can not be easily matched up)
maxplanets = 10

planetfits_results = open("planetfits_results"+file_postfix+".csv", 'w')
planetfits_results.write("Star,num,PlanetNumber,per_min_"+file_postfix+",per_mid_"+file_postfix+",per_max_"+file_postfix+",per_err_minus_"+file_postfix+",per_err_plus_"+file_postfix+",tc_min_"+file_postfix+",tc_mid_"+file_postfix+",tc_max_"+file_postfix+",tc_err_minus_"+file_postfix+",tc_err_plus_"+file_postfix+",e_min_"+file_postfix+",e_mid_"+file_postfix+",e_max_"+file_postfix+",e_err_minus_"+file_postfix+",e_err_plus_"+file_postfix+",K_min_"+file_postfix+",K_mid_"+file_postfix+",K_max_"+file_postfix+",K_err_minus_"+file_postfix+",K_err_plus\n")
for i in np.arange(1,len(stars)):
	if (star_name != stars[i]["HIPnumber"]):
		if (stars[i-1]["PlanetNumber"] <= maxplanets):
			if (os.path.isfile(star_name+file_postfix+"/"+star_name+file_postfix+"_post_summary.csv")):
				planets_pd = pd.read_csv(star_name+file_postfix+"/"+star_name+file_postfix+"_post_summary.csv")
				planets_columns = planets_pd.columns
				#planetfits_results.write(star_name)
				for x in np.arange(1, len(planets_columns)-2, 4):
					planetfits_results.write(star_name+","+str(stars[i-1]["PlanetNumber"])+","+str(int((x+3)/4)))
					planetfits_results.write(","+str(planets_pd[planets_columns[x]][0])+","+str(planets_pd[planets_columns[x]][1])+","+str(planets_pd[planets_columns[x]][2])) # per
					planetfits_results.write(","+str(planets_pd[planets_columns[x]][1]-planets_pd[planets_columns[x]][0])+","+str(planets_pd[planets_columns[x]][2]-planets_pd[planets_columns[x]][1]))
					planetfits_results.write(","+str(planets_pd[planets_columns[x+1]][0])+","+str(planets_pd[planets_columns[x+1]][1])+","+str(planets_pd[planets_columns[x+1]][2])) # tc
					planetfits_results.write(","+str(planets_pd[planets_columns[x+1]][1]-planets_pd[planets_columns[x+1]][0])+","+str(planets_pd[planets_columns[x+1]][2]-planets_pd[planets_columns[x+1]][1]))
					planetfits_results.write(","+str(planets_pd[planets_columns[x+2]][0])+","+str(planets_pd[planets_columns[x+2]][1])+","+str(planets_pd[planets_columns[x+2]][2])) # e
					planetfits_results.write(","+str(planets_pd[planets_columns[x+2]][1]-planets_pd[planets_columns[x+2]][0])+","+str(planets_pd[planets_columns[x+2]][2]-planets_pd[planets_columns[x+2]][1]))
					planetfits_results.write(","+str(planets_pd[planets_columns[x+3]][0])+","+str(planets_pd[planets_columns[x+3]][1])+","+str(planets_pd[planets_columns[x+3]][2])) # k
					planetfits_results.write(","+str(planets_pd[planets_columns[x+3]][1]-planets_pd[planets_columns[x+3]][0])+","+str(planets_pd[planets_columns[x+3]][2]-planets_pd[planets_columns[x+3]][1]))
					planetfits_results.write("\n")
		star_name = stars[i]["HIPnumber"]
planetfits_results.close()
