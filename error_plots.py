import numpy as np
import matplotlib.pyplot as plt

stars = np.genfromtxt("planetfits_matched.csv", delimiter=",", names=True, dtype=None)
#nplanets = [(1,3), (1,4), (4,4)]
#nplanets = [(1,6), (5,6), (5,5), (6,6)]
nplanets = [(1,4), (1,6), (5,5), (6,6)]
# iterate over: [5,e,f,n][p] fits, and 1-3, 4, 5, 6, 1-4, 5-6, 1-6 planet systems?
for minplanets, maxplanets in nplanets:
	f5p_yes_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_yes_per = [star["per_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrm_yes_per = [star["per_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrp_yes_per = [star["per_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_a = [star["a"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_k = [star["K"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_yes_k = [star["K_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrm_yes_k = [star["K_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrp_yes_k = [star["K_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_mass = [star["PlanetMass"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_no_per = [star["per_mid_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrm_no_per = [star["per_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrp_no_per = [star["per_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_a = [star["a"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_k= [star["K"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_no_k = [star["K_mid_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrm_no_k = [star["K_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrp_no_k = [star["K_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_mass = [star["PlanetMass"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_mar_per = [star["per_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrm_mar_per = [star["per_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrp_mar_per = [star["per_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_a = [star["a"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_k = [star["K"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5pfit_mar_k = [star["K_mid_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrm_mar_k = [star["K_err_minus_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5perrp_mar_k = [star["K_err_plus_5p"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_mass = [star["PlanetMass"] for star in stars if ((star["5p_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	fig, f5pam = plt.subplots()
	f5pam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	f5pam.scatter(f5p_yes_a, f5p_yes_mass, label="Recovered", color="#AAAAFF")
	f5pam.scatter(f5p_mar_a, f5p_mar_mass, label="Marginal", color="#FFAAAA")
	f5pam.scatter(f5p_no_a, f5p_no_mass, label="Excluded", color="#AAAAAA")
	#5pam.plot(xs, y1, label="Earth density")
	f5pam.set_xscale('log')
	f5pam.set_yscale('log')
	f5pam.set_xlabel("Semi-Major Axis (au)")
	f5pam.set_xlim(6e-2,3e1)
	f5pam.set_ylabel("Mass (Earth-Masses)")
	f5pam.set_ylim(8e-2,1e4)
	f5pam.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5pam.legend(loc=2)
	filename = "5pam_error_" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, f5ppk = plt.subplots()
	f5ppk.scatter(stars["per"], stars["K"], color="gray", s=1)
	f5ppk.scatter(f5p_yes_per, f5p_yes_k, label="Recovered", color="#AAAAFF")
	f5ppk.errorbar(f5pfit_yes_per, f5pfit_yes_k, xerr=[f5perrm_yes_per, f5perrp_yes_per], yerr=[f5perrm_yes_k, f5perrp_yes_k], color="#0000FF", fmt='o')
	f5ppk.scatter(f5p_mar_per, f5p_mar_k, label="Marginal", color="#FFAAAA")
	f5ppk.errorbar(f5pfit_mar_per, f5pfit_mar_k, xerr=[f5perrm_mar_per, f5perrp_mar_per], yerr=[f5perrm_mar_k, f5perrp_mar_k], color="#FF0000", fmt='o')
	f5ppk.scatter(f5p_no_per, f5p_no_k, label="Excluded", color="#AAAAAA")
	f5ppk.errorbar(f5pfit_no_per, f5pfit_no_k, xerr=[f5perrm_no_per, f5perrp_no_per], yerr=[f5perrm_no_k, f5perrp_no_k], color="#000000", fmt='o')
	f5ppk.set_xscale('log')
	f5ppk.set_yscale('log')
	f5ppk.set_ylabel("Semi-Amplitude (m/s)")
	f5ppk.set_ylim(8e-4,2e2)
	f5ppk.set_xlabel("Period (Days)")
	f5ppk.set_xlim(6,1e5)
	f5ppk.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5ppk.legend(loc=2)
	filename = "5ppk_error_" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	ep_yes_per = [star["per"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	epfit_yes_per = [star["per_mid_ep"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrm_yes_per = [star["per_err_minus_ep"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrp_yes_per = [star["per_err_plus_ep"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_yes_a = [star["a"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_yes_k = [star["K"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	epfit_yes_k = [star["K_mid_ep"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrm_yes_k = [star["K_err_minus_ep"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrp_yes_k = [star["K_err_plus_ep"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_yes_mass = [star["PlanetMass"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_no_per = [star["per"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	epfit_no_per = [star["per_mid_ep"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrm_no_per = [star["per_err_minus_ep"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrp_no_per = [star["per_err_plus_ep"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_no_a = [star["a"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_no_k= [star["K"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	epfit_no_k = [star["K_mid_ep"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrm_no_k = [star["K_err_minus_ep"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrp_no_k = [star["K_err_plus_ep"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_no_mass = [star["PlanetMass"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_mar_per = [star["per"] for star in stars if ((star["ep_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	epfit_mar_per = [star["per_mid_ep"] for star in stars if ((star["ep_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrm_mar_per = [star["per_err_minus_ep"] for star in stars if ((star["ep_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrp_mar_per = [star["per_err_plus_ep"] for star in stars if ((star["ep_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_mar_a = [star["a"] for star in stars if ((star["ep_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_mar_k = [star["K"] for star in stars if ((star["ep_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	epfit_mar_k = [star["K_mid_ep"] for star in stars if ((star["ep_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrm_mar_k = [star["K_err_minus_ep"] for star in stars if ((star["ep_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	eperrp_mar_k = [star["K_err_plus_ep"] for star in stars if ((star["ep_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_mar_mass = [star["PlanetMass"] for star in stars if ((star["ep_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	fig, epam = plt.subplots()
	epam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	epam.scatter(ep_yes_a, ep_yes_mass, label="Recovered", color="#AAAAFF")
	epam.scatter(ep_mar_a, ep_mar_mass, label="Marginal", color="#FFAAAA")
	epam.scatter(ep_no_a, ep_no_mass, label="Excluded", color="#AAAAAA")
	#epam.plot(xs, y1, label="Earth density")
	epam.set_xscale('log')
	epam.set_yscale('log')
	epam.set_xlabel("Semi-Major Axis (au)")
	epam.set_xlim(6e-2,3e1)
	epam.set_ylabel("Mass (Earth-Masses)")
	epam.set_ylim(8e-2,1e4)
	epam.set_title("Fitting: Period, K, Time of Conjunction ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	epam.legend(loc=2)
	filename = "epam_error_" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, eppk = plt.subplots()
	eppk.scatter(stars["per"], stars["K"], color="gray", s=1)
	eppk.scatter(ep_yes_per, ep_yes_k, label="Recovered", color="#AAAAFF")
	eppk.errorbar(epfit_yes_per, epfit_yes_k, xerr=[eperrm_yes_per, eperrp_yes_per], yerr=[eperrm_yes_k, eperrp_yes_k], color="#0000FF", fmt='o')
	eppk.scatter(ep_mar_per, ep_mar_k, label="Marginal", color="#FFAAAA")
	eppk.errorbar(epfit_mar_per, epfit_mar_k, xerr=[eperrm_mar_per, eperrp_mar_per], yerr=[eperrm_mar_k, eperrp_mar_k], color="#FF0000", fmt='o')
	eppk.scatter(ep_no_per, ep_no_k, label="Excluded", color="#AAAAAA")
	eppk.errorbar(epfit_no_per, epfit_no_k, xerr=[eperrm_no_per, eperrp_no_per], yerr=[eperrm_no_k, eperrp_no_k], color="#000000", fmt='o')
	eppk.set_xscale('log')
	eppk.set_yscale('log')
	eppk.set_ylabel("Semi-Amplitude (m/s)")
	eppk.set_ylim(8e-4,2e2)
	eppk.set_xlabel("Period (Days)")
	eppk.set_xlim(6,1e5)
	eppk.set_title("Fitting: Period, K, Time of Conjunction ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	eppk.legend(loc=2)
	filename = "eppk_error_" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fp_yes_per = [star["per"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fpfit_yes_per = [star["per_mid_fp"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrm_yes_per = [star["per_err_minus_fp"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrp_yes_per = [star["per_err_plus_fp"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_yes_a = [star["a"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_yes_k = [star["K"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fpfit_yes_k = [star["K_mid_fp"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrm_yes_k = [star["K_err_minus_fp"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrp_yes_k = [star["K_err_plus_fp"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_yes_mass = [star["PlanetMass"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_no_per = [star["per"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fpfit_no_per = [star["per_mid_fp"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrm_no_per = [star["per_err_minus_fp"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrp_no_per = [star["per_err_plus_fp"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_no_a = [star["a"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_no_k= [star["K"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fpfit_no_k = [star["K_mid_fp"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrm_no_k = [star["K_err_minus_fp"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrp_no_k = [star["K_err_plus_fp"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_no_mass = [star["PlanetMass"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_mar_per = [star["per"] for star in stars if ((star["fp_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fpfit_mar_per = [star["per_mid_fp"] for star in stars if ((star["fp_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrm_mar_per = [star["per_err_minus_fp"] for star in stars if ((star["fp_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrp_mar_per = [star["per_err_plus_fp"] for star in stars if ((star["fp_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_mar_a = [star["a"] for star in stars if ((star["fp_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_mar_k = [star["K"] for star in stars if ((star["fp_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fpfit_mar_k = [star["K_mid_fp"] for star in stars if ((star["fp_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrm_mar_k = [star["K_err_minus_fp"] for star in stars if ((star["fp_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fperrp_mar_k = [star["K_err_plus_fp"] for star in stars if ((star["fp_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_mar_mass = [star["PlanetMass"] for star in stars if ((star["fp_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	fig, fpam = plt.subplots()
	fpam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	fpam.scatter(fp_yes_a, fp_yes_mass, label="Recovered", color="#AAAAFF")
	fpam.scatter(fp_mar_a, fp_mar_mass, label="Marginal", color="#FFAAAA")
	fpam.scatter(fp_no_a, fp_no_mass, label="Excluded", color="#AAAAAA")
	#fpam.plot(xs, y1, label="Earth density")
	fpam.set_xscale('log')
	fpam.set_yscale('log')
	fpam.set_xlabel("Semi-Major Axis (au)")
	fpam.set_xlim(6e-2,3e1)
	fpam.set_ylabel("Mass (Earth-Masses)")
	fpam.set_ylim(8e-2,1e4)
	fpam.set_title("Fitting: Period, K, Time of Conjunction, Ecc ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	fpam.legend(loc=2)
	filename = "fpam_error_" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, fppk = plt.subplots()
	fppk.scatter(stars["per"], stars["K"], color="gray", s=1)
	fppk.scatter(fp_yes_per, fp_yes_k, label="Recovered", color="#AAAAFF")
	fppk.errorbar(fpfit_yes_per, fpfit_yes_k, xerr=[fperrm_yes_per, fperrp_yes_per], yerr=[fperrm_yes_k, fperrp_yes_k], color="#0000FF", fmt='o')
	fppk.scatter(fp_mar_per, fp_mar_k, label="Marginal", color="#FFAAAA")
	fppk.errorbar(fpfit_mar_per, fpfit_mar_k, xerr=[fperrm_mar_per, fperrp_mar_per], yerr=[fperrm_mar_k, fperrp_mar_k], color="#FF0000", fmt='o')
	fppk.scatter(fp_no_per, fp_no_k, label="Excluded", color="#AAAAAA")
	fppk.errorbar(fpfit_no_per, fpfit_no_k, xerr=[fperrm_no_per, fperrp_no_per], yerr=[fperrm_no_k, fperrp_no_k], color="#000000", fmt='o')
	fppk.set_xscale('log')
	fppk.set_yscale('log')
	fppk.set_ylabel("Semi-Amplitude (m/s)")
	fppk.set_ylim(8e-4,2e2)
	fppk.set_xlabel("Period (Days)")
	fppk.set_xlim(6,1e5)
	fppk.set_title("Fitting: Period, K, Time of Conjunction, Ecc ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	fppk.legend(loc=2)
	filename = "fppk_error_" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	np_yes_per = [star["per"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	npfit_yes_per = [star["per_mid_np"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrm_yes_per = [star["per_err_minus_np"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrp_yes_per = [star["per_err_plus_np"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_yes_a = [star["a"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_yes_k = [star["K"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	npfit_yes_k = [star["K_mid_np"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrm_yes_k = [star["K_err_minus_np"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrp_yes_k = [star["K_err_plus_np"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_yes_mass = [star["PlanetMass"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_no_per = [star["per"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	npfit_no_per = [star["per_mid_np"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrm_no_per = [star["per_err_minus_np"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrp_no_per = [star["per_err_plus_np"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_no_a = [star["a"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_no_k= [star["K"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	npfit_no_k = [star["K_mid_np"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrm_no_k = [star["K_err_minus_np"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrp_no_k = [star["K_err_plus_np"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_no_mass = [star["PlanetMass"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_mar_per = [star["per"] for star in stars if ((star["np_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	npfit_mar_per = [star["per_mid_np"] for star in stars if ((star["np_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrm_mar_per = [star["per_err_minus_np"] for star in stars if ((star["np_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrp_mar_per = [star["per_err_plus_np"] for star in stars if ((star["np_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_mar_a = [star["a"] for star in stars if ((star["np_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_mar_k = [star["K"] for star in stars if ((star["np_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	npfit_mar_k = [star["K_mid_np"] for star in stars if ((star["np_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrm_mar_k = [star["K_err_minus_np"] for star in stars if ((star["np_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nperrp_mar_k = [star["K_err_plus_np"] for star in stars if ((star["np_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_mar_mass = [star["PlanetMass"] for star in stars if ((star["np_Favored"] == b"Marginal") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	
	fig, npam = plt.subplots()
	npam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	npam.scatter(np_yes_a, np_yes_mass, label="Recovered", color="#AAAAFF")
	npam.scatter(np_mar_a, np_mar_mass, label="Marginal", color="#FFAAAA")
	npam.scatter(np_no_a, np_no_mass, label="Excluded", color="#AAAAAA")
	#npam.plot(xs, y1, label="Earth density")
	npam.set_xscale('log')
	npam.set_yscale('log')
	npam.set_xlabel("Semi-Major Axis (au)")
	npam.set_xlim(6e-2,3e1)
	npam.set_ylabel("Mass (Earth-Masses)")
	npam.set_ylim(8e-2,1e4)
	npam.set_title("Fitting: Period, K, Time of Conjunction; eccentricity set to 0 ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	npam.legend(loc=2)
	filename = "npam_error_" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, nppk = plt.subplots()
	nppk.scatter(stars["per"], stars["K"], color="gray", s=1)
	nppk.scatter(np_yes_per, np_yes_k, label="Recovered", color="#AAAAFF")
	nppk.errorbar(npfit_yes_per, npfit_yes_k, xerr=[nperrm_yes_per, nperrp_yes_per], yerr=[nperrm_yes_k, nperrp_yes_k], color="#0000FF", fmt='o')
	nppk.scatter(np_mar_per, np_mar_k, label="Marginal", color="#FFAAAA")
	nppk.errorbar(npfit_mar_per, npfit_mar_k, xerr=[nperrm_mar_per, nperrp_mar_per], yerr=[nperrm_mar_k, nperrp_mar_k], color="#FF0000", fmt='o')
	nppk.scatter(np_no_per, np_no_k, label="Excluded", color="#AAAAAA")
	nppk.errorbar(npfit_no_per, npfit_no_k, xerr=[nperrm_no_per, nperrp_no_per], yerr=[nperrm_no_k, nperrp_no_k], color="#000000", fmt='o')
	nppk.set_xscale('log')
	nppk.set_yscale('log')
	nppk.set_ylabel("Semi-Amplitude (m/s)")
	nppk.set_ylim(8e-4,2e2)
	nppk.set_xlabel("Period (Days)")
	nppk.set_xlim(6,1e5)
	nppk.set_title("Fitting: Period, K, Time of Conjunction; eccentricity set to 0 ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	nppk.legend(loc=2)
	filename = "nppk_error_" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
