'''generates a list of false positives, etc. Also plots along the relevant parameter space.'''
import numpy as np
import matplotlib.pyplot as plt

stars = np.genfromtxt("planetfits_matched2.csv", delimiter=",", names=True, dtype=None)
#nplanets = [(1,4), (1,7)]
nplanets = [(1,4)]
# iterate over: [5,e,f,n][p] fits, and 1-3, 4, 5, 6, 1-4, 5-6, 1-6 planet systems?
for minplanets, maxplanets in nplanets:
	f5p_false_per = [star["per"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5p_false_K = [star["K"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5p_false_per_mid = [star["per_mid_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5p_false_K_mid = [star["K_mid_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5p_false_per_err_minus = [star["per_err_minus_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5p_false_K_err_minus = [star["K_err_minus_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5p_false_per_err_plus = [star["per_err_plus_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5p_false_K_err_plus = [star["K_err_plus_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	
	f5p_K = [star["K"] for star in stars if (star["num"] <= maxplanets)]
	#f5p_fav = [star["5p_Favored"] for star in stars if (star["num"] <= maxplanets)]
	f5p_per = [star["per"] for star in stars if (star["num"] <= maxplanets)]
	
	f5p_yes_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_K = [star["K"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_K = [star["K"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_K = [star["K"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_yes_per_mid = [star["per_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_K_mid = [star["K_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_per_mid = [star["per_mid_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_K_mid = [star["K_mid_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_per_mid = [star["per_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_K_mid = [star["K_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_per_err_minus = [star["per_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_K_err_minus = [star["K_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_per_err_minus = [star["per_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_K_err_minus = [star["K_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_per_err_minus = [star["per_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_K_err_minus = [star["K_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_per_err_plus = [star["per_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_K_err_plus = [star["K_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_per_err_plus = [star["per_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_K_err_plus = [star["K_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_per_err_plus = [star["per_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_K_err_plus = [star["K_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	fig, f5ppk_fit = plt.subplots()
	#f5ppk_fit.scatter(stars["per"], stars["K"], color="gray", s=1, s=2.5)
	f5ppk_fit.scatter(f5p_yes_per_mid, f5p_yes_K_mid, label="Recovered", color="blue", s=2.5)
	f5ppk_fit.errorbar(f5p_yes_per_mid, f5p_yes_K_mid, xerr=[f5p_yes_per_err_minus, f5p_yes_per_err_plus], yerr=[f5p_yes_K_err_minus, f5p_yes_K_err_plus], color="blue", fmt='.')
	f5ppk_fit.scatter(f5p_mar_per_mid, f5p_mar_K_mid, label="Marginal", color="black", s=2.5)
	f5ppk_fit.errorbar(f5p_mar_per_mid, f5p_mar_K_mid, xerr=[f5p_mar_per_err_minus, f5p_mar_per_err_plus], yerr=[f5p_mar_K_err_minus, f5p_mar_K_err_plus], color="black", fmt='.')
	f5ppk_fit.scatter(f5p_no_per_mid, f5p_no_K_mid, label="Excluded", color="gray", s=2.5)
	f5ppk_fit.errorbar(f5p_no_per_mid, f5p_no_K_mid, xerr=[f5p_no_per_err_minus, f5p_no_per_err_plus], yerr=[f5p_no_K_err_minus, f5p_no_K_err_plus], color="gray", fmt='.')
	f5ppk_fit.scatter(f5p_false_per_mid, f5p_false_K_mid, label="False Positive", color="red", s=2.5)
	f5ppk_fit.errorbar(f5p_false_per_mid, f5p_false_K_mid, xerr=[f5p_false_per_err_minus, f5p_false_per_err_plus], yerr=[f5p_false_K_err_minus, f5p_false_K_err_plus], color="red", fmt='.')
	f5ppk_fit.set_xscale('log')
	f5ppk_fit.set_yscale('log')
	f5ppk_fit.set_ylabel("Recovered Semi-Amplitude (m/s)")
	f5ppk_fit.set_ylim(8e-4,2e2)
	f5ppk_fit.set_xlabel("Recovered Period (Days)")
	f5ppk_fit.set_xlim(6,1e5)
	f5ppk_fit.set_title("Fitting: Period, K, Time of Conjunction; eccentricity set to 0 ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5ppk_fit.legend(loc=0)
	filename = "f5ppk_fit" + str(minplanets) + str(maxplanets) + ".png"
	#plt.savefig(filename)
	fig, f5ppk_false = plt.subplots()
	#f5ppk_false.scatter(stars["per"], stars["K"], color="gray", s=1, s=2.5)
	f5ppk_false.scatter(f5p_yes_per, f5p_yes_K, label="Recovered", color="blue", s=2.5)
	f5ppk_false.scatter(f5p_mar_per, f5p_mar_K, label="Marginal", color="black", s=2.5)
	f5ppk_false.scatter(f5p_no_per, f5p_no_K, label="Excluded", color="gray", s=2.5)
	f5ppk_false.scatter(f5p_false_per, f5p_false_K, label="False Positive", color="red", s=2.5)
	f5ppk_false.set_xscale('log')
	f5ppk_false.set_yscale('log')
	f5ppk_false.set_ylabel("Input Semi-Amplitude (m/s)")
	f5ppk_false.set_ylim(8e-4,2e2)
	f5ppk_false.set_xlabel("Input Period (Days)")
	f5ppk_false.set_xlim(6,1e5)
	f5ppk_false.set_title("Fitting: Period, K, Time of Conjunction; eccentricity set to 0 ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5ppk_false.legend(loc=0)
	filename = "f5ppk_false" + str(minplanets) + str(maxplanets) + ".png"
	#plt.savefig(filename)
	plt.show()
