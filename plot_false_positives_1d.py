'''generates a list of false positives, etc. Also plots along the relevant parameter space.'''
import numpy as np
import matplotlib.pyplot as plt

stars = np.genfromtxt("planetfits_matched2.csv", delimiter=",", names=True, dtype=None)
#nplanets = [(1,3), (1,4), (1,6), (4,4), (5,5), (6,6)]
nplanets = [(1,4), (1,7)]
nplanets = [(1,4)]
for minplanets, maxplanets in nplanets:
	f5p_yes_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_yes_per = [star["per_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_yes_per = [star["per_min_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_yes_per = [star["per_max_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_yes_k = [star["K"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_yes_k = [star["K_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_yes_k = [star["K_min_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_yes_k = [star["K_max_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_yes_e = [star["e"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_yes_e = [star["e_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_yes_e = [star["e_min_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_yes_e = [star["e_max_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_no_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_no_per = [star["per_mid_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_no_per = [star["per_min_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_no_per = [star["per_max_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_no_k= [star["K"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_no_k = [star["K_mid_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_no_k = [star["K_min_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_no_k = [star["K_max_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_no_e= [star["e"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_no_e = [star["e_mid_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_no_e = [star["e_min_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_no_e = [star["e_max_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_mar_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_mar_per = [star["per_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_mar_per = [star["per_min_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_mar_per = [star["per_max_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_mar_k = [star["K"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_mar_k = [star["K_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_mar_k = [star["K_min_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_mar_k = [star["K_max_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_mar_e = [star["e"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_mar_e = [star["e_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_mar_e = [star["e_min_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_mar_e = [star["e_max_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_false_per = [star["per"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5pfit_false_per = [star["per_mid_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5pmin_false_per = [star["per_min_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5pmax_false_per = [star["per_max_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5p_false_k = [star["K"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5pfit_false_k = [star["K_mid_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5pmin_false_k = [star["K_min_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5pmax_false_k = [star["K_max_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5p_false_e = [star["e"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5pfit_false_e = [star["e_mid_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5pmin_false_e = [star["e_min_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	f5pmax_false_e = [star["e_max_5p"] for star in stars if ((((abs(star["per"]-star["per_mid_5p"])/star["per"] > 0.05) and (((star["per_mid_5p"]-star["per"])/star["per_err_plus_5p"] > 3) or ((star["per"]-star["per_mid_5p"])/star["per_err_minus_5p"] > 3))) or ((abs(star["K"]-star["K_mid_5p"])/star["K"] > 0.05) and (((star["K_mid_5p"]-star["K"])/star["K_err_plus_5p"] > 3) or ((star["K"]-star["K_mid_5p"])/star["K_err_minus_5p"] > 3)))) and (star["num"] <= maxplanets) and (star["num"] >= minplanets) and (star["5p_Favored"] == b"Yes"))]
	
	f5pΔ_yes_per = np.zeros(len(f5pfit_yes_per))
	f5perrp_yes_per = np.zeros(len(f5pfit_yes_per))
	f5perrm_yes_per = np.zeros(len(f5pfit_yes_per))
	f5pΔ_yes_k = np.zeros(len(f5pfit_yes_k))
	f5perrp_yes_k = np.zeros(len(f5pfit_yes_k))
	f5perrm_yes_k = np.zeros(len(f5pfit_yes_k))
	f5pΔ_yes_e = np.zeros(len(f5pfit_yes_e))
	f5perrp_yes_e = np.zeros(len(f5pfit_yes_e))
	f5perrm_yes_e = np.zeros(len(f5pfit_yes_e))
	for j in np.arange(0, len(f5pfit_yes_per)):
		f5pΔ_yes_per[j] = (f5pfit_yes_per[j] - f5p_yes_per[j]) / (f5p_yes_per[j])
		f5perrp_yes_per[j] = (f5pmax_yes_per[j] - f5pfit_yes_per[j]) / (f5p_yes_per[j])
		f5perrm_yes_per[j] = (f5pfit_yes_per[j] - f5pmin_yes_per[j]) / (f5p_yes_per[j])
		f5pΔ_yes_k[j] = (f5pfit_yes_k[j] - f5p_yes_k[j]) / (f5p_yes_k[j])
		f5perrp_yes_k[j] = (f5pmax_yes_k[j] - f5pfit_yes_k[j]) / (f5p_yes_k[j])
		f5perrm_yes_k[j] = (f5pfit_yes_k[j] - f5pmin_yes_k[j]) / (f5p_yes_k[j])
		f5pΔ_yes_e[j] = (f5pfit_yes_e[j] - f5p_yes_e[j]) / (f5p_yes_e[j])
		f5perrp_yes_e[j] = (f5pmax_yes_e[j] - f5pfit_yes_e[j]) / (f5p_yes_e[j])
		f5perrm_yes_e[j] = (f5pfit_yes_e[j] - f5pmin_yes_e[j]) / (f5p_yes_e[j])
	f5pΔ_no_per = np.zeros(len(f5pfit_no_per))
	f5perrp_no_per = np.zeros(len(f5pfit_no_per))
	f5perrm_no_per = np.zeros(len(f5pfit_no_per))
	f5pΔ_no_k = np.zeros(len(f5pfit_no_k))
	f5perrp_no_k = np.zeros(len(f5pfit_no_k))
	f5perrm_no_k = np.zeros(len(f5pfit_no_k))
	f5pΔ_no_e = np.zeros(len(f5pfit_no_e))
	f5perrp_no_e = np.zeros(len(f5pfit_no_e))
	f5perrm_no_e = np.zeros(len(f5pfit_no_e))
	for j in np.arange(0, len(f5pfit_no_per)):
		f5pΔ_no_per[j] = (f5pfit_no_per[j] - f5p_no_per[j]) / (f5p_no_per[j])
		f5perrp_no_per[j] = (f5pmax_no_per[j] - f5pfit_no_per[j]) / (f5p_no_per[j])
		f5perrm_no_per[j] = (f5pfit_no_per[j] - f5pmin_no_per[j]) / (f5p_no_per[j])
		f5pΔ_no_k[j] = (f5pfit_no_k[j] - f5p_no_k[j]) / (f5p_no_k[j])
		f5perrp_no_k[j] = (f5pmax_no_k[j] - f5pfit_no_k[j]) / (f5p_no_k[j])
		f5perrm_no_k[j] = (f5pfit_no_k[j] - f5pmin_no_k[j]) / (f5p_no_k[j])
		f5pΔ_no_e[j] = (f5pfit_no_e[j] - f5p_no_e[j]) / (f5p_no_e[j])
		f5perrp_no_e[j] = (f5pmax_no_e[j] - f5pfit_no_e[j]) / (f5p_no_e[j])
		f5perrm_no_e[j] = (f5pfit_no_e[j] - f5pmin_no_e[j]) / (f5p_no_e[j])
	f5pΔ_mar_per = np.zeros(len(f5pfit_mar_per))
	f5perrp_mar_per = np.zeros(len(f5pfit_mar_per))
	f5perrm_mar_per = np.zeros(len(f5pfit_mar_per))
	f5pΔ_mar_k = np.zeros(len(f5pfit_mar_k))
	f5perrp_mar_k = np.zeros(len(f5pfit_mar_k))
	f5perrm_mar_k = np.zeros(len(f5pfit_mar_k))
	f5pΔ_mar_e = np.zeros(len(f5pfit_mar_e))
	f5perrp_mar_e = np.zeros(len(f5pfit_mar_e))
	f5perrm_mar_e = np.zeros(len(f5pfit_mar_e))
	for j in np.arange(0, len(f5pfit_mar_per)):
		f5pΔ_mar_per[j] = (f5pfit_mar_per[j] - f5p_mar_per[j]) / (f5p_mar_per[j])
		f5perrp_mar_per[j] = (f5pmax_mar_per[j] - f5pfit_mar_per[j]) / (f5p_mar_per[j])
		f5perrm_mar_per[j] = (f5pfit_mar_per[j] - f5pmin_mar_per[j]) / (f5p_mar_per[j])
		f5pΔ_mar_k[j] = (f5pfit_mar_k[j] - f5p_mar_k[j]) / (f5p_mar_k[j])
		f5perrp_mar_k[j] = (f5pmax_mar_k[j] - f5pfit_mar_k[j]) / (f5p_mar_k[j])
		f5perrm_mar_k[j] = (f5pfit_mar_k[j] - f5pmin_mar_k[j]) / (f5p_mar_k[j])
		f5pΔ_mar_e[j] = (f5pfit_mar_e[j] - f5p_mar_e[j]) / (f5p_mar_e[j])
		f5perrp_mar_e[j] = (f5pmax_mar_e[j] - f5pfit_mar_e[j]) / (f5p_mar_e[j])
		f5perrm_mar_e[j] = (f5pfit_mar_e[j] - f5pmin_mar_e[j]) / (f5p_mar_e[j])
	f5pΔ_false_per = np.zeros(len(f5pfit_false_per))
	f5perrp_false_per = np.zeros(len(f5pfit_false_per))
	f5perrm_false_per = np.zeros(len(f5pfit_false_per))
	f5pΔ_false_k = np.zeros(len(f5pfit_false_k))
	f5perrp_false_k = np.zeros(len(f5pfit_false_k))
	f5perrm_false_k = np.zeros(len(f5pfit_false_k))
	f5pΔ_false_e = np.zeros(len(f5pfit_false_e))
	f5perrp_false_e = np.zeros(len(f5pfit_false_e))
	f5perrm_false_e = np.zeros(len(f5pfit_false_e))
	for j in np.arange(0, len(f5pfit_false_per)):
		f5pΔ_false_per[j] = (f5pfit_false_per[j] - f5p_false_per[j]) / (f5p_false_per[j])
		f5perrp_false_per[j] = (f5pmax_false_per[j] - f5pfit_false_per[j]) / (f5p_false_per[j])
		f5perrm_false_per[j] = (f5pfit_false_per[j] - f5pmin_false_per[j]) / (f5p_false_per[j])
		f5pΔ_false_k[j] = (f5pfit_false_k[j] - f5p_false_k[j]) / (f5p_false_k[j])
		f5perrp_false_k[j] = (f5pmax_false_k[j] - f5pfit_false_k[j]) / (f5p_false_k[j])
		f5perrm_false_k[j] = (f5pfit_false_k[j] - f5pmin_false_k[j]) / (f5p_false_k[j])
		f5pΔ_false_e[j] = (f5pfit_false_e[j] - f5p_false_e[j]) / (f5p_false_e[j])
		f5perrp_false_e[j] = (f5pmax_false_e[j] - f5pfit_false_e[j]) / (f5p_false_e[j])
		f5perrm_false_e[j] = (f5pfit_false_e[j] - f5pmin_false_e[j]) / (f5p_false_e[j])
	
	fig, f5pp = plt.subplots()
	f5pp.errorbar(f5p_yes_per, f5pΔ_yes_per, yerr=[f5perrm_yes_per, f5perrp_yes_per], color="#0000FF", fmt='o')
	f5pp.scatter(f5p_yes_per, f5pΔ_yes_per, color="#0000FF", label="Recovered")
	f5pp.errorbar(f5p_mar_per, f5pΔ_mar_per, yerr=[f5perrm_mar_per, f5perrp_mar_per], color="#FF0000", fmt='o')
	f5pp.scatter(f5p_mar_per, f5pΔ_mar_per, color="#FF0000", label="Marginal")
	f5pp.errorbar(f5p_no_per, f5pΔ_no_per, yerr=[f5perrm_no_per, f5perrp_no_per], color="#000000", fmt='o')
	f5pp.scatter(f5p_no_per, f5pΔ_no_per, color="#000000", label="Excluded")
	f5pp.errorbar(f5p_false_per, f5pΔ_false_per, yerr=[f5perrm_false_per, f5perrp_false_per], color="#00AA00", fmt='o')
	f5pp.scatter(f5p_false_per, f5pΔ_false_per, color="#00AA00", label="False Positive")
	f5pp.set_xscale('log')
	f5pp.set_ylabel("Relative Error")
	f5pp.set_xlabel("Period (Days)")
	f5pp.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5pp.legend(loc=2)
	filename = "5pp_error_" + str(minplanets) + str(maxplanets) + ".png"
	#plt.savefig(filename)
	fig, f5pk = plt.subplots()
	f5pk.errorbar(f5p_yes_k, f5pΔ_yes_k, yerr=[f5perrm_yes_k, f5perrp_yes_k], color="#0000FF", fmt='o')
	f5pk.scatter(f5p_yes_k, f5pΔ_yes_k, color="#0000FF", label="Recovered")
	f5pk.errorbar(f5p_mar_k, f5pΔ_mar_k, yerr=[f5perrm_mar_k, f5perrp_mar_k], color="#FF0000", fmt='o')
	f5pk.scatter(f5p_mar_k, f5pΔ_mar_k, color="#FF0000", label="Marginal")
	f5pk.errorbar(f5p_no_k, f5pΔ_no_k, yerr=[f5perrm_no_k, f5perrp_no_k], color="#000000", fmt='o')
	f5pk.scatter(f5p_no_k, f5pΔ_no_k, color="#000000", label="Excluded")
	f5pk.errorbar(f5p_false_k, f5pΔ_false_k, yerr=[f5perrm_false_k, f5perrp_false_k], color="#00AA00", fmt='o')
	f5pk.scatter(f5p_false_k, f5pΔ_false_k, color="#00AA00", label="False Positive")
	f5pk.set_xscale('log')
	f5pk.set_ylabel("Relative Error")
	f5pk.set_xlabel("Semi-amplitude (m/s)")
	#f5pk.set_ylim(-0.2,1.5)
	#f5pk.set_xlim(6e-2,1e2)
	f5pk.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5pk.legend(loc=2)
	filename = "5pk_error_" + str(minplanets) + str(maxplanets) + ".png"
	#plt.savefig(filename)
	fig, f5pe = plt.subplots()
	f5pe.errorbar(f5p_yes_e, f5pΔ_yes_e, yerr=[f5perrm_yes_e, f5perrp_yes_e], color="#0000FF", fmt='o')
	f5pe.scatter(f5p_yes_e, f5pΔ_yes_e, color="#0000FF", label="Recovered")
	f5pe.errorbar(f5p_mar_e, f5pΔ_mar_e, yerr=[f5perrm_mar_e, f5perrp_mar_e], color="#FF0000", fmt='o')
	f5pe.scatter(f5p_mar_e, f5pΔ_mar_e, color="#FF0000", label="Marginal")
	f5pe.errorbar(f5p_no_e, f5pΔ_no_e, yerr=[f5perrm_no_e, f5perrp_no_e], color="#000000", fmt='o')
	f5pe.scatter(f5p_no_e, f5pΔ_no_e, color="#000000", label="Excluded")
	f5pe.errorbar(f5p_false_e, f5pΔ_false_e, yerr=[f5perrm_false_e, f5perrp_false_e], color="#00AA00", fmt='o')
	f5pe.scatter(f5p_false_e, f5pΔ_false_e, color="#00AA00", label="False Positive")
	f5pe.set_xscale('log')
	f5pe.set_ylabel("Relative Error")
	f5pe.set_xlabel("Eccentricity")
	f5pe.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5pe.legend(loc=2)
	filename = "5pe_error_" + str(minplanets) + str(maxplanets) + ".png"
	#plt.savefig(filename)
	plt.show()	
