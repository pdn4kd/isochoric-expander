import numpy as np
import matplotlib.pyplot as plt

stars = np.genfromtxt("planetfits_matched.csv", delimiter=",", names=True, dtype=None)
#nplanets = [(1,3), (1,4), (1,6), (4,4), (5,5), (6,6)]
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
	
	f5p_mar_per = [star["per"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_mar_per = [star["per_mid_5p"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_mar_per = [star["per_min_5p"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_mar_per = [star["per_max_5p"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_mar_k = [star["K"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_mar_k = [star["K_mid_5p"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_mar_k = [star["K_min_5p"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_mar_k = [star["K_max_5p"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	f5p_mar_e = [star["e"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_mar_e = [star["e_mid_5p"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmin_mar_e = [star["e_min_5p"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pmax_mar_e = [star["e_max_5p"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
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
	
	fig, f5pp = plt.subplots()
	f5pp.errorbar(f5p_yes_per, f5pΔ_yes_per, yerr=[f5perrm_yes_per, f5perrp_yes_per], color="#0000FF", fmt='H')
	f5pp.errorbar(f5p_mar_per, f5pΔ_mar_per, yerr=[f5perrm_mar_per, f5perrp_mar_per], color="#FF0000", fmt='H')
	f5pp.errorbar(f5p_no_per, f5pΔ_no_per, yerr=[f5perrm_no_per, f5perrp_no_per], color="#000000", fmt='H')
	f5pp.set_xscale('log')
	f5pp.set_ylabel("Relative Error")
	#f5pp.set_x`lim(6,1e5) # k
	#f5ppk.set_xlim(8e-4,2e2) #sma
	f5pp.set_xlabel("Period (Days)")
	#f5pp.set_xlim(6,1e5) # per
	f5pp.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	#f5ppk.legend(loc=2)
	filename = "5pp_error_" + str(minplanets) + str(maxplanets) + ".png"
	#plt.savefig(filename)
	fig, f5pk = plt.subplots()
	f5pk.errorbar(f5p_yes_k, f5pΔ_yes_k, yerr=[f5perrm_yes_k, f5perrp_yes_k], color="#0000FF", fmt='H')
	f5pk.errorbar(f5p_mar_k, f5pΔ_mar_k, yerr=[f5perrm_mar_k, f5perrp_mar_k], color="#FF0000", fmt='H')
	f5pk.errorbar(f5p_no_k, f5pΔ_no_k, yerr=[f5perrm_no_k, f5perrp_no_k], color="#000000", fmt='H')
	f5pk.set_xscale('log')
	f5pk.set_ylabel("Relative Error")
	#f5pk.set_x`lim(6,1e5) # k
	#f5pkk.set_xlim(8e-4,2e2) #sma
	f5pk.set_xlabel("Semi-amplitude (m/s)")
	#f5pk.set_xlim(6,1e5) # per
	f5pk.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	#f5pkk.legend(loc=2)
	filename = "5pk_error_" + str(minplanets) + str(maxplanets) + ".png"
	#plt.savefig(filename)
	fig, f5pe = plt.subplots()
	f5pe.errorbar(f5p_yes_e, f5pΔ_yes_e, yerr=[f5perrm_yes_e, f5perrp_yes_e], color="#0000FF", fmt='H')
	f5pe.errorbar(f5p_mar_e, f5pΔ_mar_e, yerr=[f5perrm_mar_e, f5perrp_mar_e], color="#FF0000", fmt='H')
	f5pe.errorbar(f5p_no_e, f5pΔ_no_e, yerr=[f5perrm_no_e, f5perrp_no_e], color="#000000", fmt='H')
	f5pe.set_xscale('log')
	f5pe.set_ylabel("Relative Error")
	#f5pe.set_x`lim(6,1e5) # k
	#f5pek.set_xlim(8e-4,2e2) #sma
	f5pe.set_xlabel("Eccentricity")
	#f5pe.set_xlim(6,1e5) # per
	f5pe.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	#f5pek.legend(loc=2)
	filename = "5pe_error_" + str(minplanets) + str(maxplanets) + ".png"
	#plt.savefig(filename)
	plt.show()	
