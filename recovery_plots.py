import numpy as np
import matplotlib.pyplot as plt

stars = np.genfromtxt("planetfits_revised.csv", delimiter=",", names=True, dtype=None)
#nplanets = [(1,3), (1,4), (4,4)]
nplanets = [(1,6), (5,6), (5,5), (6,6)]
# iterate over: [5,e,f,n][n,p] fits, and 1-3, 4, 5, 6, 1-4, 5-6, 1-6 planet systems?
for minplanets, maxplanets in nplanets:
	np_yes_per = [star["per"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_yes_a = [star["a"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_yes_k = [star["K"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_yes_mass = [star["PlanetMass"] for star in stars if ((star["np_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_no_per = [star["per"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_no_a = [star["a"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_no_k= [star["K"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_no_mass = [star["PlanetMass"] for star in stars if ((star["np_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_mar_per = [star["per"] for star in stars if (((star["np_Favored"] == b"No*") or (star["np_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_mar_a = [star["a"] for star in stars if (((star["np_Favored"] == b"No*") or (star["np_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_mar_k = [star["K"] for star in stars if (((star["np_Favored"] == b"No*") or (star["np_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	np_mar_mass = [star["PlanetMass"] for star in stars if (((star["np_Favored"] == b"No*") or (star["np_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fig, npam = plt.subplots()
	npam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	npam.scatter(np_yes_a, np_yes_mass, label="Recovered", color="blue")
	npam.scatter(np_mar_a, np_mar_mass, label="Marginal", color="red")
	npam.scatter(np_no_a, np_no_mass, label="Excluded", color="black")
	#npam.plot(xs, y1, label="Earth density")
	npam.set_xscale('log')
	npam.set_yscale('log')
	npam.set_xlabel("Semi-Major Axis (au)")
	npam.set_xlim(6e-2,3e1)
	npam.set_ylabel("Mass (Earth-Masses)")
	npam.set_ylim(8e-2,1e4)
	npam.set_title("Fitting: Period, K, Time of Conjunction; eccentricity set to 0 ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	npam.legend(loc=2)
	filename = "npam" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, nppk = plt.subplots()
	nppk.scatter(stars["per"], stars["K"], color="gray", s=1)
	nppk.scatter(np_yes_per, np_yes_k, label="Recovered", color="blue")
	nppk.scatter(np_mar_per, np_mar_k, label="Marginal", color="red")
	nppk.scatter(np_no_per, np_no_k, label="Excluded", color="black")
	#nppk.plot(xs, y1, label="Earth density")
	nppk.set_xscale('log')
	nppk.set_yscale('log')
	nppk.set_ylabel("Semi-Amplitude (m/s)")
	nppk.set_ylim(8e-4,2e2)
	nppk.set_xlabel("Period (Days)")
	nppk.set_xlim(6,1e5)
	nppk.set_title("Fitting: Period, K, Time of Conjunction; eccentricity set to 0 ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	nppk.legend(loc=2)
	filename = "nppk" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	#plt.show()
	
	
	ep_yes_per = [star["per"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_yes_a = [star["a"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_yes_k = [star["K"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_yes_mass = [star["PlanetMass"] for star in stars if ((star["ep_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_no_per = [star["per"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_no_a = [star["a"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_no_k= [star["K"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_no_mass = [star["PlanetMass"] for star in stars if ((star["ep_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_mar_per = [star["per"] for star in stars if (((star["ep_Favored"] == b"No*") or (star["ep_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_mar_a = [star["a"] for star in stars if (((star["ep_Favored"] == b"No*") or (star["ep_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_mar_k = [star["K"] for star in stars if (((star["ep_Favored"] == b"No*") or (star["ep_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	ep_mar_mass = [star["PlanetMass"] for star in stars if (((star["ep_Favored"] == b"No*") or (star["ep_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fig, epam = plt.subplots()
	epam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	epam.scatter(ep_yes_a, ep_yes_mass, label="Recovered", color="blue")
	epam.scatter(ep_mar_a, ep_mar_mass, label="Marginal", color="red")
	epam.scatter(ep_no_a, ep_no_mass, label="Excluded", color="black")
	#epam.plot(xs, y1, label="Earth density")
	epam.set_xscale('log')
	epam.set_yscale('log')
	epam.set_xlabel("Semi-Major Axis (au)")
	epam.set_xlim(6e-2,3e1)
	epam.set_ylabel("Mass (Earth-Masses)")
	epam.set_ylim(8e-2,1e4)
	epam.set_title("Fitting: Period, K, Time of Conjunction ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	epam.legend(loc=2)
	filename = "epam" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, eppk = plt.subplots()
	eppk.scatter(stars["per"], stars["K"], color="gray", s=1)
	eppk.scatter(ep_yes_per, ep_yes_k, label="Recovered", color="blue")
	eppk.scatter(ep_mar_per, ep_mar_k, label="Marginal", color="red")
	eppk.scatter(ep_no_per, ep_no_k, label="Excluded", color="black")
	#eppk.plot(xs, y1, label="Earth density")
	eppk.set_xscale('log')
	eppk.set_yscale('log')
	eppk.set_ylabel("Semi-Amplitude (m/s)")
	eppk.set_ylim(8e-4,2e2)
	eppk.set_xlabel("Period (Days)")
	eppk.set_xlim(6,1e5)
	eppk.set_title("Fitting: Period, K, Time of Conjunction ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	eppk.legend(loc=2)
	filename = "eppk" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	#plt.show()
	
	
	f5p_yes_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_a = [star["a"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_k = [star["K"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_yes_mass = [star["PlanetMass"] for star in stars if ((star["5p_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_per = [star["per"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_a = [star["a"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_k= [star["K"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_no_mass = [star["PlanetMass"] for star in stars if ((star["5p_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_per = [star["per"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_a = [star["a"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_k = [star["K"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5p_mar_mass = [star["PlanetMass"] for star in stars if (((star["5p_Favored"] == b"No*") or (star["5p_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fig, f5pam = plt.subplots()
	f5pam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	f5pam.scatter(f5p_yes_a, f5p_yes_mass, label="Recovered", color="blue")
	f5pam.scatter(f5p_mar_a, f5p_mar_mass, label="Marginal", color="red")
	f5pam.scatter(f5p_no_a, f5p_no_mass, label="Excluded", color="black")
	#f5pam.plot(xs, y1, label="Earth density")
	f5pam.set_xscale('log')
	f5pam.set_yscale('log')
	f5pam.set_xlabel("Semi-Major Axis (au)")
	f5pam.set_xlim(6e-2,3e1)
	f5pam.set_ylabel("Mass (Earth-Masses)")
	f5pam.set_ylim(8e-2,1e4)
	f5pam.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5pam.legend(loc=2)
	filename = "5pam" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, f5ppk = plt.subplots()
	f5ppk.scatter(stars["per"], stars["K"], color="gray", s=1)
	f5ppk.scatter(f5p_yes_per, f5p_yes_k, label="Recovered", color="blue")
	f5ppk.scatter(f5p_mar_per, f5p_mar_k, label="Marginal", color="red")
	f5ppk.scatter(f5p_no_per, f5p_no_k, label="Excluded", color="black")
	#f5ppk.plot(xs, y1, label="Earth density")
	f5ppk.set_xscale('log')
	f5ppk.set_yscale('log')
	f5ppk.set_ylabel("Semi-Amplitude (m/s)")
	f5ppk.set_ylim(8e-4,2e2)
	f5ppk.set_xlabel("Period (Days)")
	f5ppk.set_xlim(6,1e5)
	f5ppk.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5ppk.legend(loc=2)
	filename = "5ppk" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	
	fp_yes_per = [star["per"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_yes_a = [star["a"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_yes_k = [star["K"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_yes_mass = [star["PlanetMass"] for star in stars if ((star["fp_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_no_per = [star["per"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_no_a = [star["a"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_no_k= [star["K"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_no_mass = [star["PlanetMass"] for star in stars if ((star["fp_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_mar_per = [star["per"] for star in stars if (((star["fp_Favored"] == b"No*") or (star["fp_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_mar_a = [star["a"] for star in stars if (((star["fp_Favored"] == b"No*") or (star["fp_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_mar_k = [star["K"] for star in stars if (((star["fp_Favored"] == b"No*") or (star["fp_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fp_mar_mass = [star["PlanetMass"] for star in stars if (((star["fp_Favored"] == b"No*") or (star["fp_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fig, fpam = plt.subplots()
	fpam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	fpam.scatter(fp_yes_a, fp_yes_mass, label="Recovered", color="blue")
	fpam.scatter(fp_mar_a, fp_mar_mass, label="Marginal", color="red")
	fpam.scatter(fp_no_a, fp_no_mass, label="Excluded", color="black")
	#fpam.plot(xs, y1, label="Earth density")
	fpam.set_xscale('log')
	fpam.set_yscale('log')
	fpam.set_xlabel("Semi-Major Axis (au)")
	fpam.set_xlim(6e-2,3e1)
	fpam.set_ylabel("Mass (Earth-Masses)")
	fpam.set_ylim(8e-2,1e4)
	fpam.set_title("Fitting: Period, K, Time of Conjunction, Ecc ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	fpam.legend(loc=2)
	filename = "fpam" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, fppk = plt.subplots()
	fppk.scatter(stars["per"], stars["K"], color="gray", s=1)
	fppk.scatter(fp_yes_per, fp_yes_k, label="Recovered", color="blue")
	fppk.scatter(fp_mar_per, fp_mar_k, label="Marginal", color="red")
	fppk.scatter(fp_no_per, fp_no_k, label="Excluded", color="black")
	#fppk.plot(xs, y1, label="Earth density")
	fppk.set_xscale('log')
	fppk.set_yscale('log')
	fppk.set_ylabel("Semi-Amplitude (m/s)")
	fppk.set_ylim(8e-4,2e2)
	fppk.set_xlabel("Period (Days)")
	fppk.set_xlim(6,1e5)
	fppk.set_title("Fitting: Period, K, Time of Conjunction, Ecc ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	fppk.legend(loc=2)
	filename = "fppk" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
