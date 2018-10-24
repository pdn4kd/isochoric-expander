import numpy as np
import matplotlib.pyplot as plt

stars = np.genfromtxt("planetfits_revised.csv", delimiter=",", names=True, dtype=None)
#nplanets = [(1,3), (1,4), (4,4)]
nplanets = [(1,6), (5,6), (5,5), (6,6)]
# iterate over: [5,e,f,n][n,p] fits, and 1-3, 4, 5, 6, 1-4, 5-6, 1-6 planet systems?
for minplanets, maxplanets in nplanets:
	nn_yes_per = [star["per"] for star in stars if ((star["nn_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_yes_a = [star["a"] for star in stars if ((star["nn_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_yes_k = [star["K"] for star in stars if ((star["nn_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_yes_mass = [star["PlanetMass"] for star in stars if ((star["nn_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_no_per = [star["per"] for star in stars if ((star["nn_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_no_a = [star["a"] for star in stars if ((star["nn_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_no_k= [star["K"] for star in stars if ((star["nn_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_no_mass = [star["PlanetMass"] for star in stars if ((star["nn_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_mar_per = [star["per"] for star in stars if (((star["nn_Favored"] == b"No*") or (star["nn_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_mar_a = [star["a"] for star in stars if (((star["nn_Favored"] == b"No*") or (star["nn_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_mar_k = [star["K"] for star in stars if (((star["nn_Favored"] == b"No*") or (star["nn_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	nn_mar_mass = [star["PlanetMass"] for star in stars if (((star["nn_Favored"] == b"No*") or (star["nn_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fig, nnam = plt.subplots()
	nnam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	nnam.scatter(nn_yes_a, nn_yes_mass, label="Recovered", color="blue")
	nnam.scatter(nn_mar_a, nn_mar_mass, label="Marginal", color="red")
	nnam.scatter(nn_no_a, nn_no_mass, label="Excluded", color="black")
	#nnam.plot(xs, y1, label="Earth density")
	nnam.set_xscale('log')
	nnam.set_yscale('log')
	nnam.set_xlabel("Semi-Major Axis (au)")
	nnam.set_xlim(6e-2,3e1)
	nnam.set_ylabel("Mass (Earth-Masses)")
	nnam.set_ylim(8e-2,1e4)
	nnam.set_title("Fitting: Period, K, Time of Conjunction; ecc = 0 ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	nnam.legend(loc=2)
	filename = "nnam" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, nnpk = plt.subplots()
	nnpk.scatter(stars["per"], stars["K"], color="gray", s=1)
	nnpk.scatter(nn_yes_per, nn_yes_k, label="Recovered", color="blue")
	nnpk.scatter(nn_mar_per, nn_mar_k, label="Marginal", color="red")
	nnpk.scatter(nn_no_per, nn_no_k, label="Excluded", color="black")
	#nnpk.plot(xs, y1, label="Earth density")
	nnpk.set_xscale('log')
	nnpk.set_yscale('log')
	nnpk.set_ylabel("Semi-Amplitude (m/s)")
	nnpk.set_ylim(8e-4,2e2)
	nnpk.set_xlabel("Period (Days)")
	nnpk.set_xlim(6,1e5)
	nnpk.set_title("Fitting: Period, K, Time of Conjunction; ecc = 0 ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	nnpk.legend(loc=2)
	filename = "nnpk" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	#plt.show()
	
	
	en_yes_per = [star["per"] for star in stars if ((star["en_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_yes_a = [star["a"] for star in stars if ((star["en_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_yes_k = [star["K"] for star in stars if ((star["en_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_yes_mass = [star["PlanetMass"] for star in stars if ((star["en_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_no_per = [star["per"] for star in stars if ((star["en_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_no_a = [star["a"] for star in stars if ((star["en_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_no_k= [star["K"] for star in stars if ((star["en_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_no_mass = [star["PlanetMass"] for star in stars if ((star["en_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_mar_per = [star["per"] for star in stars if (((star["en_Favored"] == b"No*") or (star["en_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_mar_a = [star["a"] for star in stars if (((star["en_Favored"] == b"No*") or (star["en_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_mar_k = [star["K"] for star in stars if (((star["en_Favored"] == b"No*") or (star["en_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	en_mar_mass = [star["PlanetMass"] for star in stars if (((star["en_Favored"] == b"No*") or (star["en_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fig, enam = plt.subplots()
	enam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	enam.scatter(en_yes_a, en_yes_mass, label="Recovered", color="blue")
	enam.scatter(en_mar_a, en_mar_mass, label="Marginal", color="red")
	enam.scatter(en_no_a, en_no_mass, label="Excluded", color="black")
	#enam.plot(xs, y1, label="Earth density")
	enam.set_xscale('log')
	enam.set_yscale('log')
	enam.set_xlabel("Semi-Major Axis (au)")
	enam.set_xlim(6e-2,3e1)
	enam.set_ylabel("Mass (Earth-Masses)")
	enam.set_ylim(8e-2,1e4)
	enam.set_title("Fitting: Period, K, Time of Conjunction ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	enam.legend(loc=2)
	filename = "enam" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, enpk = plt.subplots()
	enpk.scatter(stars["per"], stars["K"], color="gray", s=1)
	enpk.scatter(en_yes_per, en_yes_k, label="Recovered", color="blue")
	enpk.scatter(en_mar_per, en_mar_k, label="Marginal", color="red")
	enpk.scatter(en_no_per, en_no_k, label="Excluded", color="black")
	#enpk.plot(xs, y1, label="Earth density")
	enpk.set_xscale('log')
	enpk.set_yscale('log')
	enpk.set_ylabel("Semi-Amplitude (m/s)")
	enpk.set_ylim(8e-4,2e2)
	enpk.set_xlabel("Period (Days)")
	enpk.set_xlim(6,1e5)
	enpk.set_title("Fitting: Period, K, Time of Conjunction ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	enpk.legend(loc=2)
	filename = "enpk" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	#plt.show()
	
	
	f5n_yes_per = [star["per"] for star in stars if ((star["5n_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_yes_a = [star["a"] for star in stars if ((star["5n_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_yes_k = [star["K"] for star in stars if ((star["5n_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_yes_mass = [star["PlanetMass"] for star in stars if ((star["5n_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_no_per = [star["per"] for star in stars if ((star["5n_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_no_a = [star["a"] for star in stars if ((star["5n_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_no_k= [star["K"] for star in stars if ((star["5n_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_no_mass = [star["PlanetMass"] for star in stars if ((star["5n_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_mar_per = [star["per"] for star in stars if (((star["5n_Favored"] == b"No*") or (star["5n_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_mar_a = [star["a"] for star in stars if (((star["5n_Favored"] == b"No*") or (star["5n_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_mar_k = [star["K"] for star in stars if (((star["5n_Favored"] == b"No*") or (star["5n_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	f5n_mar_mass = [star["PlanetMass"] for star in stars if (((star["5n_Favored"] == b"No*") or (star["5n_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fig, f5nam = plt.subplots()
	f5nam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	f5nam.scatter(f5n_yes_a, f5n_yes_mass, label="Recovered", color="blue")
	f5nam.scatter(f5n_mar_a, f5n_mar_mass, label="Marginal", color="red")
	f5nam.scatter(f5n_no_a, f5n_no_mass, label="Excluded", color="black")
	#f5nam.plot(xs, y1, label="Earth density")
	f5nam.set_xscale('log')
	f5nam.set_yscale('log')
	f5nam.set_xlabel("Semi-Major Axis (au)")
	f5nam.set_xlim(6e-2,3e1)
	f5nam.set_ylabel("Mass (Earth-Masses)")
	f5nam.set_ylim(8e-2,1e4)
	f5nam.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5nam.legend(loc=2)
	filename = "5nam" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, f5npk = plt.subplots()
	f5npk.scatter(stars["per"], stars["K"], color="gray", s=1)
	f5npk.scatter(f5n_yes_per, f5n_yes_k, label="Recovered", color="blue")
	f5npk.scatter(f5n_mar_per, f5n_mar_k, label="Marginal", color="red")
	f5npk.scatter(f5n_no_per, f5n_no_k, label="Excluded", color="black")
	#f5npk.plot(xs, y1, label="Earth density")
	f5npk.set_xscale('log')
	f5npk.set_yscale('log')
	f5npk.set_ylabel("Semi-Amplitude (m/s)")
	f5npk.set_ylim(8e-4,2e2)
	f5npk.set_xlabel("Period (Days)")
	f5npk.set_xlim(6,1e5)
	f5npk.set_title("Fitting: Period, K, Time of Conjunction, Ecc (max 0.5) ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	f5npk.legend(loc=2)
	filename = "5npk" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	
	fn_yes_per = [star["per"] for star in stars if ((star["fn_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_yes_a = [star["a"] for star in stars if ((star["fn_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_yes_k = [star["K"] for star in stars if ((star["fn_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_yes_mass = [star["PlanetMass"] for star in stars if ((star["fn_Favored"] == b"Yes") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_no_per = [star["per"] for star in stars if ((star["fn_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_no_a = [star["a"] for star in stars if ((star["fn_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_no_k= [star["K"] for star in stars if ((star["fn_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_no_mass = [star["PlanetMass"] for star in stars if ((star["fn_Favored"] == b"No") and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_mar_per = [star["per"] for star in stars if (((star["fn_Favored"] == b"No*") or (star["fn_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_mar_a = [star["a"] for star in stars if (((star["fn_Favored"] == b"No*") or (star["fn_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_mar_k = [star["K"] for star in stars if (((star["fn_Favored"] == b"No*") or (star["fn_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fn_mar_mass = [star["PlanetMass"] for star in stars if (((star["fn_Favored"] == b"No*") or (star["fn_Favored"] == b"Yes*")) and (star["num"] >= minplanets) and (star["num"] <= maxplanets))]
	fig, fnam = plt.subplots()
	fnam.scatter(stars["a"], stars["PlanetMass"], color="gray", s=1)
	fnam.scatter(fn_yes_a, fn_yes_mass, label="Recovered", color="blue")
	fnam.scatter(fn_mar_a, fn_mar_mass, label="Marginal", color="red")
	fnam.scatter(fn_no_a, fn_no_mass, label="Excluded", color="black")
	#fnam.plot(xs, y1, label="Earth density")
	fnam.set_xscale('log')
	fnam.set_yscale('log')
	fnam.set_xlabel("Semi-Major Axis (au)")
	fnam.set_xlim(6e-2,3e1)
	fnam.set_ylabel("Mass (Earth-Masses)")
	fnam.set_ylim(8e-2,1e4)
	fnam.set_title("Fitting: Period, K, Time of Conjunction, Ecc ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	fnam.legend(loc=2)
	filename = "fnam" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
	
	fig, fnpk = plt.subplots()
	fnpk.scatter(stars["per"], stars["K"], color="gray", s=1)
	fnpk.scatter(fn_yes_per, fn_yes_k, label="Recovered", color="blue")
	fnpk.scatter(fn_mar_per, fn_mar_k, label="Marginal", color="red")
	fnpk.scatter(fn_no_per, fn_no_k, label="Excluded", color="black")
	#fnpk.plot(xs, y1, label="Earth density")
	fnpk.set_xscale('log')
	fnpk.set_yscale('log')
	fnpk.set_ylabel("Semi-Amplitude (m/s)")
	fnpk.set_ylim(8e-4,2e2)
	fnpk.set_xlabel("Period (Days)")
	fnpk.set_xlim(6,1e5)
	fnpk.set_title("Fitting: Period, K, Time of Conjunction, Ecc ("+str(minplanets)+"-"+str(maxplanets)+" planet systems)")
	fnpk.legend(loc=2)
	filename = "fnpk" + str(minplanets) + str(maxplanets) + ".png"
	plt.savefig(filename)
