'''Attempts to generate configuration files for a given list of stars and their associated planets.'''
import numpy as np
import datetime

#initializing
stars = np.genfromtxt("planets.csv", delimiter=',', names=True, dtype=("U23", "U9", int, float, float, float, float, float, float, float, float, float, float))
star_name = stars[0]["HIPnumber"]
max_period = 3654.0
file_postfix = "en.py"

for i in np.arange(1,len(stars)):
	if (star_name != stars[i]["HIPnumber"]):
		planets = stars[i-1]["PlanetNumber"]
		#start a new file
		now = str((datetime.datetime.now()).isoformat())
		star_config = open(star_name+file_postfix, 'w')
		star_config.write("# Test Keplerian fit configuration file for "+star_name+"\n")
		star_config.write("# Features: Short period (t<"+str(max_period)+" days) planets fit via period, tc, k; e fixed; trends fit\n")
		star_config.write("# Generated on "+now+"\n\n")
		star_config.write("import os\n")
		star_config.write("import pandas as pd\n")
		star_config.write("import numpy as np\n")
		star_config.write("import radvel\n")
		star_config.write("starname = '"+star_name+"'\n")
		star_config.write("instnames = [\'NEID\']\n")
		star_config.write("ntels = len(instnames)\n")
		star_config.write("fitting_basis = \'per tc e w k\'\n")
		star_config.write("bjd0 = 2458850.\n")
		star_config.write("planet_letters = {")
		short_planets = 0
		planet_names = "bcdefghijk"
		for	j in np.arange(0, planets):
			if (stars["per"][i-planets+j] < max_period):
				short_planets += 1
				if (short_planets > 1):
					star_config.write(", ")
				star_config.write(str(short_planets)+": '"+planet_names[j]+"'")
		star_config.write("}\n\n")
		star_config.write("nplanets = "+str(short_planets)+" # out of "+str(planets)+"\n")
		star_config.write("anybasis_params = radvel.Parameters(nplanets,basis='per tp e w k')\n\n")
		star_config.write("anybasis_params['dvdt'] = radvel.Parameter(value=0.0)\n")
		star_config.write("anybasis_params['curv'] = radvel.Parameter(value=0.0)\n")
		star_config.write("anybasis_params['gamma_NEID'] = radvel.Parameter(value=0.0)\n")
		star_config.write("anybasis_params['jit_NEID'] = radvel.Parameter(value=0.0)\n")
		#loop to add planets (before)
		short_planets = 0
		for x in np.arange(0, planets):
			if (stars["per"][i-planets+x] < max_period):
				short_planets += 1
				star_config.write("anybasis_params['per"+str(short_planets)+"'] = radvel.Parameter(value="+str(stars[i-planets+x]["per"])+")\n")
				star_config.write("anybasis_params['tp"+str(short_planets)+"'] = radvel.Parameter(value="+str(stars[i-planets+x]["t_p"])+")\n")
				star_config.write("anybasis_params['e"+str(short_planets)+"'] = radvel.Parameter(value="+str(stars[i-planets+x]["e"])+")\n")
				star_config.write("anybasis_params['w"+str(short_planets)+"'] = radvel.Parameter(value="+str(stars[i-planets+x]["omega"])+")\n")
				star_config.write("anybasis_params['k"+str(short_planets)+"'] = radvel.Parameter(value="+str(stars[i-planets+x]["K"])+")\n")
		star_config.write("\nparams = anybasis_params.basis.to_any_basis(anybasis_params,fitting_basis)\n\n")
		#loop to add planets (after)
		short_planets = 0
		for x in np.arange(0, planets):
			if (stars["per"][i-planets+x] < max_period):
				short_planets += 1
				star_config.write("params['per"+str(short_planets)+"'].vary = True\n")
				star_config.write("params['tc"+str(short_planets)+"'].vary = True\n")
				star_config.write("params['e"+str(short_planets)+"'].vary = False\n")
				star_config.write("params['w"+str(short_planets)+"'].vary = False\n")
				star_config.write("params['k"+str(short_planets)+"'].vary = True\n")
		#write end of file
		star_config.write("params['dvdt'].vary = True\n")
		star_config.write("params['curv'].vary = True\n")
		star_config.write("params['gamma_NEID'].vary = True\n")
		star_config.write("params['jit_NEID'].vary = False\n\n")
		star_config.write("path = '"+str(stars['RVfilename'][i-1])+"'\n")
		star_config.write("data = pd.read_csv(path)\n")
		star_config.write("data['time'] = (data.obs_start+data.obs_end)/2\n")
		star_config.write("data['mnvel'] = data.mnvel\n")
		star_config.write("data['errvel'] = data.rvprec\n")
		star_config.write("data['tel'] = 'NEID'\n\n")
		star_config.write("priors = [\n")
		star_config.write("    radvel.prior.EccentricityPrior( nplanets, ),\n")
		star_config.write("    radvel.prior.PositiveKPrior( nplanets ),\n")
		star_config.write("    radvel.prior.HardBounds('jit_NEID', 0.0, 15.0)\n")
		star_config.write("]\n\n")
		star_config.write("time_base = np.mean([np.min(data.time), np.max(data.time)])\n")
		star_config.close()
		star_name = stars[i]["HIPnumber"]
# We missed the last star
star_name = stars[i]["HIPnumber"]
planets = stars[i]["PlanetNumber"]
#start a new file
now = str((datetime.datetime.now()).isoformat())
star_name = stars[i]["HIPnumber"]
star_config = open(star_name+file_postfix, 'w')
star_config.write("# Test Keplerian fit configuration file for "+star_name+"\n")
star_config.write("# Features: Short period (t<"+str(max_period)+" days) planets fit via period, tc, k; e fixed; trends fit\n")
star_config.write("# Generated on "+now+"\n\n")
star_config.write("import os\n")
star_config.write("import pandas as pd\n")
star_config.write("import numpy as np\n")
star_config.write("import radvel\n")
star_config.write("starname = '"+star_name+"'\n")
star_config.write("instnames = [\'NEID\']\n")
star_config.write("ntels = len(instnames)\n")
star_config.write("fitting_basis = \'per tc e w k\'\n")
star_config.write("bjd0 = 2458850.\n")
star_config.write("planet_letters = {")
short_planets = 0
planet_names = "bcdefghijk"
for	j in np.arange(1, planets+1):
	if (stars["per"][i-planets+j] < max_period):
		short_planets += 1
		if (short_planets > 1):
			star_config.write(", ")
		star_config.write(str(short_planets)+": '"+planet_names[j]+"'")
star_config.write("}\n\n")
star_config.write("nplanets = "+str(short_planets)+" # out of "+str(planets)+"\n")
star_config.write("anybasis_params = radvel.Parameters(nplanets,basis='per tp e w k')\n\n")
star_config.write("anybasis_params['dvdt'] = radvel.Parameter(value=0.0)\n")
star_config.write("anybasis_params['curv'] = radvel.Parameter(value=0.0)\n")
star_config.write("anybasis_params['gamma_NEID'] = radvel.Parameter(value=0.0)\n")
star_config.write("anybasis_params['jit_NEID'] = radvel.Parameter(value=0.0)\n")
#loop to add planets (before)
short_planets = 0
for x in np.arange(1, planets+1):
	if (stars["per"][i-planets+x] < max_period):
		short_planets += 1
		star_config.write("anybasis_params['per"+str(short_planets)+"'] = radvel.Parameter(value="+str(stars[i-planets+x]["per"])+")\n")
		star_config.write("anybasis_params['tp"+str(short_planets)+"'] = radvel.Parameter(value="+str(stars[i-planets+x]["t_p"])+")\n")
		star_config.write("anybasis_params['e"+str(short_planets)+"'] = radvel.Parameter(value="+str(stars[i-planets+x]["e"])+")\n")
		star_config.write("anybasis_params['w"+str(short_planets)+"'] = radvel.Parameter(value="+str(stars[i-planets+x]["omega"])+")\n")
		star_config.write("anybasis_params['k"+str(short_planets)+"'] = radvel.Parameter(value="+str(stars[i-planets+x]["K"])+")\n")
star_config.write("params = anybasis_params.basis.to_any_basis(anybasis_params,fitting_basis)\n\n")
#loop to add planets (after)
short_planets = 0
for x in np.arange(1, planets+1):
	if (stars["per"][i-planets+x] < max_period):
		short_planets += 1
		star_config.write("params['per"+str(short_planets)+"'].vary = True\n")
		star_config.write("params['tc"+str(short_planets)+"'].vary = True\n")
		star_config.write("params['e"+str(short_planets)+"'].vary = False\n")
		star_config.write("params['w"+str(short_planets)+"'].vary = False\n")
		star_config.write("params['k"+str(short_planets)+"'].vary = True\n")
#write end of file
star_config.write("params['dvdt'].vary = True\n")
star_config.write("params['curv'].vary = True\n")
star_config.write("params['gamma_NEID'].vary = True\n")
star_config.write("params['jit_NEID'].vary = False\n\n")
star_config.write("path = '"+str(stars['RVfilename'][i])+"'\n")
star_config.write("data = pd.read_csv(path)\n")
star_config.write("data['time'] = data.obs_start\n")
star_config.write("data['mnvel'] = data.mnvel\n")
star_config.write("data['errvel'] = data.rvprec\n")
star_config.write("data['tel'] = 'NEID'\n\n")
star_config.write("priors = [\n")
star_config.write("    radvel.prior.EccentricityPrior( nplanets, ),\n")
star_config.write("    radvel.prior.PositiveKPrior( nplanets ),\n")
star_config.write("    radvel.prior.HardBounds('jit_NEID', 0.0, 15.0)\n")
star_config.write("]\n\n")
star_config.write("time_base = np.mean([np.min(data.time), np.max(data.time)])\n")
star_config.close()
