'''generates a list of false positives, etc. Also plots along the relevant parameter space.'''
import numpy as np
import matplotlib.pyplot as plt

stars = np.genfromtxt("matched_65p.csv", delimiter=",", names=True, dtype=None)
nplanets = [(1,7)]
for minplanets, maxplanets in nplanets:
	f65p_false_per = [star["per"] for star in stars if ((((abs(star["per"]-star["per_mid_65p"])/star["per"] > 0.05) and (((star["per_mid_65p"]-star["per"])/star["per_err_plus_65p"] > 3) or ((star["per"]-star["per_mid_65p"])/star["per_err_minus_65p"] > 3))) or ((abs(star["K"]-star["K_mid_65p"])/star["K"] > 0.05) and (((star["K_mid_65p"]-star["K"])/star["K_err_plus_65p"] > 3) or ((star["K"]-star["K_mid_65p"])/star["K_err_minus_65p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["65p_Favored"] == b"Yes"))]
	f65p_false_K = [star["K"] for star in stars if ((((abs(star["per"]-star["per_mid_65p"])/star["per"] > 0.05) and (((star["per_mid_65p"]-star["per"])/star["per_err_plus_65p"] > 3) or ((star["per"]-star["per_mid_65p"])/star["per_err_minus_65p"] > 3))) or ((abs(star["K"]-star["K_mid_65p"])/star["K"] > 0.05) and (((star["K_mid_65p"]-star["K"])/star["K_err_plus_65p"] > 3) or ((star["K"]-star["K_mid_65p"])/star["K_err_minus_65p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["65p_Favored"] == b"Yes"))]
	f65p_false_per_mid = [star["per_mid_65p"] for star in stars if ((((abs(star["per"]-star["per_mid_65p"])/star["per"] > 0.05) and (((star["per_mid_65p"]-star["per"])/star["per_err_plus_65p"] > 3) or ((star["per"]-star["per_mid_65p"])/star["per_err_minus_65p"] > 3))) or ((abs(star["K"]-star["K_mid_65p"])/star["K"] > 0.05) and (((star["K_mid_65p"]-star["K"])/star["K_err_plus_65p"] > 3) or ((star["K"]-star["K_mid_65p"])/star["K_err_minus_65p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["65p_Favored"] == b"Yes"))]
	f65p_false_K_mid = [star["K_mid_65p"] for star in stars if ((((abs(star["per"]-star["per_mid_65p"])/star["per"] > 0.05) and (((star["per_mid_65p"]-star["per"])/star["per_err_plus_65p"] > 3) or ((star["per"]-star["per_mid_65p"])/star["per_err_minus_65p"] > 3))) or ((abs(star["K"]-star["K_mid_65p"])/star["K"] > 0.05) and (((star["K_mid_65p"]-star["K"])/star["K_err_plus_65p"] > 3) or ((star["K"]-star["K_mid_65p"])/star["K_err_minus_65p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["65p_Favored"] == b"Yes"))]
	f65p_false_per_err_minus = [star["per_err_minus_65p"] for star in stars if ((((abs(star["per"]-star["per_mid_65p"])/star["per"] > 0.05) and (((star["per_mid_65p"]-star["per"])/star["per_err_plus_65p"] > 3) or ((star["per"]-star["per_mid_65p"])/star["per_err_minus_65p"] > 3))) or ((abs(star["K"]-star["K_mid_65p"])/star["K"] > 0.05) and (((star["K_mid_65p"]-star["K"])/star["K_err_plus_65p"] > 3) or ((star["K"]-star["K_mid_65p"])/star["K_err_minus_65p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["65p_Favored"] == b"Yes"))]
	f65p_false_K_err_minus = [star["K_err_minus_65p"] for star in stars if ((((abs(star["per"]-star["per_mid_65p"])/star["per"] > 0.05) and (((star["per_mid_65p"]-star["per"])/star["per_err_plus_65p"] > 3) or ((star["per"]-star["per_mid_65p"])/star["per_err_minus_65p"] > 3))) or ((abs(star["K"]-star["K_mid_65p"])/star["K"] > 0.05) and (((star["K_mid_65p"]-star["K"])/star["K_err_plus_65p"] > 3) or ((star["K"]-star["K_mid_65p"])/star["K_err_minus_65p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["65p_Favored"] == b"Yes"))]
	f65p_false_per_err_plus = [star["per_err_plus_65p"] for star in stars if ((((abs(star["per"]-star["per_mid_65p"])/star["per"] > 0.05) and (((star["per_mid_65p"]-star["per"])/star["per_err_plus_65p"] > 3) or ((star["per"]-star["per_mid_65p"])/star["per_err_minus_65p"] > 3))) or ((abs(star["K"]-star["K_mid_65p"])/star["K"] > 0.05) and (((star["K_mid_65p"]-star["K"])/star["K_err_plus_65p"] > 3) or ((star["K"]-star["K_mid_65p"])/star["K_err_minus_65p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["65p_Favored"] == b"Yes"))]
	f65p_false_K_err_plus = [star["K_err_plus_65p"] for star in stars if ((((abs(star["per"]-star["per_mid_65p"])/star["per"] > 0.05) and (((star["per_mid_65p"]-star["per"])/star["per_err_plus_65p"] > 3) or ((star["per"]-star["per_mid_65p"])/star["per_err_minus_65p"] > 3))) or ((abs(star["K"]-star["K_mid_65p"])/star["K"] > 0.05) and (((star["K_mid_65p"]-star["K"])/star["K_err_plus_65p"] > 3) or ((star["K"]-star["K_mid_65p"])/star["K_err_minus_65p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["65p_Favored"] == b"Yes"))]
	
	f65p_K = [star["K"] for star in stars if (star["num"] <= maxplanets)]
	#f65p_fav = [star["65p_Favored"] for star in stars if (star["num"] <= maxplanets)]
	f65p_per = [star["per"] for star in stars if (star["num"] <= maxplanets)]
	
	f65p_yes_per = [star["per"] for star in stars if ((star["65p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_yes_K = [star["K"] for star in stars if ((star["65p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_no_per = [star["per"] for star in stars if ((star["65p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_no_K = [star["K"] for star in stars if ((star["65p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_mar_per = [star["per"] for star in stars if ((star["65p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_mar_K = [star["K"] for star in stars if ((star["65p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f65p_yes_per_mid = [star["per_mid_65p"] for star in stars if ((star["65p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_yes_K_mid = [star["K_mid_65p"] for star in stars if ((star["65p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_no_per_mid = [star["per_mid_65p"] for star in stars if ((star["65p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_no_K_mid = [star["K_mid_65p"] for star in stars if ((star["65p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_mar_per_mid = [star["per_mid_65p"] for star in stars if ((star["65p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_mar_K_mid = [star["K_mid_65p"] for star in stars if ((star["65p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_yes_per_err_minus = [star["per_err_minus_65p"] for star in stars if ((star["65p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_yes_K_err_minus = [star["K_err_minus_65p"] for star in stars if ((star["65p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_no_per_err_minus = [star["per_err_minus_65p"] for star in stars if ((star["65p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_no_K_err_minus = [star["K_err_minus_65p"] for star in stars if ((star["65p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_mar_per_err_minus = [star["per_err_minus_65p"] for star in stars if ((star["65p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_mar_K_err_minus = [star["K_err_minus_65p"] for star in stars if ((star["65p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_yes_per_err_plus = [star["per_err_plus_65p"] for star in stars if ((star["65p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_yes_K_err_plus = [star["K_err_plus_65p"] for star in stars if ((star["65p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_no_per_err_plus = [star["per_err_plus_65p"] for star in stars if ((star["65p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_no_K_err_plus = [star["K_err_plus_65p"] for star in stars if ((star["65p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_mar_per_err_plus = [star["per_err_plus_65p"] for star in stars if ((star["65p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f65p_mar_K_err_plus = [star["K_err_plus_65p"] for star in stars if ((star["65p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	fig, f65ppk_fit = plt.subplots()
	x1s = [1826.25]*10
	y1s = np.linspace(8e-4,1e-1,10)
	x2s = np.linspace(1826,1e5,100)
	y2s = [5.476e-5*x for x in x2s]
	f65ppk_fit.plot(x1s, y1s, color="#A0BBFF")
	f65ppk_fit.plot(x2s, y2s, color="#A0BBFF")
	#f65ppk_fit.scatter(stars["per"], stars["K"], color="gray", s=1, s=2.5)
	f65ppk_fit.scatter(f65p_yes_per_mid, f65p_yes_K_mid, label="Recovered", color="blue", s=2.5)
	f65ppk_fit.errorbar(f65p_yes_per_mid, f65p_yes_K_mid, xerr=[f65p_yes_per_err_minus, f65p_yes_per_err_plus], yerr=[f65p_yes_K_err_minus, f65p_yes_K_err_plus], color="blue", fmt='.')
	f65ppk_fit.scatter(f65p_mar_per_mid, f65p_mar_K_mid, label="Marginal", color="black", s=2.5)
	f65ppk_fit.errorbar(f65p_mar_per_mid, f65p_mar_K_mid, xerr=[f65p_mar_per_err_minus, f65p_mar_per_err_plus], yerr=[f65p_mar_K_err_minus, f65p_mar_K_err_plus], color="black", fmt='.')
	f65ppk_fit.scatter(f65p_no_per_mid, f65p_no_K_mid, label="Excluded", color="gray", s=2.5)
	f65ppk_fit.errorbar(f65p_no_per_mid, f65p_no_K_mid, xerr=[f65p_no_per_err_minus, f65p_no_per_err_plus], yerr=[f65p_no_K_err_minus, f65p_no_K_err_plus], color="gray", fmt='.')
	f65ppk_fit.scatter(f65p_false_per_mid, f65p_false_K_mid, label="False Positive", color="red", s=2.5)
	f65ppk_fit.errorbar(f65p_false_per_mid, f65p_false_K_mid, xerr=[f65p_false_per_err_minus, f65p_false_per_err_plus], yerr=[f65p_false_K_err_minus, f65p_false_K_err_plus], color="red", fmt='.')
	f65ppk_fit.set_xscale('log')
	f65ppk_fit.set_yscale('log')
	f65ppk_fit.set_ylabel("Recovered Semi-Amplitude (m/s)")
	f65ppk_fit.set_ylim(8e-4,2e2)
	f65ppk_fit.set_xlabel("Recovered Period (Days)")
	f65ppk_fit.set_xlim(6,1e5)
	#f65ppk_fit.set_title("Fitting: Period, K, Time of Conjunction; eccentricity set to 0 ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f65ppk_fit.set_title("Earthfinder Untruncated Examples (Fits)")
	f65ppk_fit.legend(loc=0)
	#filename = "f65ppk_fit" + str(minplanets) + str(maxplanets) + ".png"
	filename = "Earthfinder_extras_output.png"
	#plt.savefig(filename)
	fig, f65ppk_false = plt.subplots()
	f65ppk_false.plot(x1s, y1s, color="#A0BBFF")
	f65ppk_false.plot(x2s, y2s, color="#A0BBFF")
	#f65ppk_false.scatter(stars["per"], stars["K"], color="gray", s=1, s=2.5)
	f65ppk_false.scatter(f65p_yes_per, f65p_yes_K, label="Recovered", color="blue", s=2.5)
	f65ppk_false.scatter(f65p_mar_per, f65p_mar_K, label="Marginal", color="black", s=2.5)
	f65ppk_false.scatter(f65p_no_per, f65p_no_K, label="Excluded", color="gray", s=2.5)
	f65ppk_false.scatter(f65p_false_per, f65p_false_K, label="False Positive", color="red", s=2.5)
	f65ppk_false.set_xscale('log')
	f65ppk_false.set_yscale('log')
	f65ppk_false.set_ylabel("Input Semi-Amplitude (m/s)")
	f65ppk_false.set_ylim(8e-4,2e2)
	f65ppk_false.set_xlabel("Input Period (Days)")
	f65ppk_false.set_xlim(6,1e5)
	#f65ppk_false.set_title("Fitting: Period, K, Time of Conjunction; eccentricity set to 0 ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f65ppk_false.set_title("Earthfinder Untruncated Examples (Input)")
	f65ppk_false.legend(loc=0)
	#filename = "f65ppk_false" + str(minplanets) + str(maxplanets) + ".png"
	filename = "Earthfinder_extras_input.png"
	#plt.savefig(filename)
	plt.show()
