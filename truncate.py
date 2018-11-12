'''reorganizes full 20 year 100% timeseries into 25/50/100% 5/10/20 year ones. So less extensive sureys can be done.
2020-01-01T19:00:00.000 = 2458850.29166667 # start date
2025-01-01T19:00:00.000 = 2460677.29166667 # 5 years
2030-01-01T19:00:00.000 = 2462503.29166667 # 10 years
2040-01-01T19:00:00.000 = 2466155.29166667 # 20 years
'''
import numpy as np

#Filenames list is subject to change. You should probably hand edit it for a given series.
filenames=["HIP104214_rvPlanets.txt","HIP19849_rvPlanets.txt","HIP49908_rvPlanets.txt","HIP7513_rvPlanets.txt","HIP104217_rvPlanets.txt","HIP22449_rvPlanets.txt","HIP51459_rvPlanets.txt","HIP77257_rvPlanets.txt","HIP10644_rvPlanets.txt","HIP23311_rvPlanets.txt","HIP54035_rvPlanets.txt","HIP78072_rvPlanets.txt","HIP114622_rvPlanets.txt","HIP24813_rvPlanets.txt","HIP56997_rvPlanets.txt","HIP7981_rvPlanets.txt","HIP12114_rvPlanets.txt","HIP25878_rvPlanets.txt","HIP57757_rvPlanets.txt","HIP8102_rvPlanets.txt","HIP12777_rvPlanets.txt","HIP27072_rvPlanets.txt","HIP57939_rvPlanets.txt","HIP81300_rvPlanets.txt","HIP13402_rvPlanets.txt","HIP29295_rvPlanets.txt","HIP61317_rvPlanets.txt","HIP8362_rvPlanets.txt","HIP14632_rvPlanets.txt","HIP3093_rvPlanets.txt","HIP64394_rvPlanets.txt","HIP84478_rvPlanets.txt","HIP1475B_rvPlanets.txt","HIP32984_rvPlanets.txt","HIP64924_rvPlanets.txt","HIP88972_rvPlanets.txt","HIP1475_rvPlanets.txt","HIP37279_rvPlanets.txt","HIP67927_rvPlanets.txt","HIP96100_rvPlanets.txt","HIP15457_rvPlanets.txt","HIP3765_rvPlanets.txt","HIP68184_rvPlanets.txt","HIP98036_rvPlanets.txt","HIP16537_rvPlanets.txt","HIP3821_rvPlanets.txt","HIP72848_rvPlanets.txt","HIP99825_rvPlanets.txt","HIP17378_rvPlanets.txt","HIP47080_rvPlanets.txt","HIP73184_rvPlanets.txt"]
for filename in filenames:
	print(filename)
	star = np.genfromtxt(filename, delimiter=',', names=True, dtype=None)
	# open 5, 10 year 100%
	star5year100 = open(filename+"05100", 'w')
	star5year100.write("obs_start,obs_end,duration,altitude,azimuth,exposures,photonprec,instprec,rvprec,rvmeas,mnvel\n")
	star10year100 = open(filename+"10100", 'w')
	star10year100.write("obs_start,obs_end,duration,altitude,azimuth,exposures,photonprec,instprec,rvprec,rvmeas,mnvel\n")
	for line in star:
		if (line["obs_start"] < 2460677.29166667):
			star5year100.write(str(line)[2:-1]+"\n")
		if (line["obs_start"] < 2462503.29166667):
			star10year100.write(str(line)[2:-1]+"\n")
	star5year100.close()
	star10year100.close()
	
	star5year050 = open(filename+"05050", 'w')
	star5year050.write("obs_start,obs_end,duration,altitude,azimuth,exposures,photonprec,instprec,rvprec,rvmeas,mnvel\n")
	star10year050 = open(filename+"10050", 'w')
	star10year050.write("obs_start,obs_end,duration,altitude,azimuth,exposures,photonprec,instprec,rvprec,rvmeas,mnvel\n")
	star20year050 = open(filename+"20050", 'w')
	star20year050.write("obs_start,obs_end,duration,altitude,azimuth,exposures,photonprec,instprec,rvprec,rvmeas,mnvel\n")
	np.random.shuffle(star)
	starpos = np.arange(int(0.5*len(star)))
	for line in starpos: # iterate over the first half of a random shuffle of our observations
		star20year050.write(str(star[line])[2:-1]+"\n")
		if (star[line]["obs_start"] < 2460677.29166667):
			star5year050.write(str(star[line])[2:-1]+"\n")
		if (star[line]["obs_start"] < 2462503.29166667):
			star10year050.write(str(star[line])[2:-1]+"\n")
	star5year050.close()
	star10year050.close()
	star20year050.close()
	
	star5year025 = open(filename+"05025", 'w')
	star5year025.write("obs_start,obs_end,duration,altitude,azimuth,exposures,photonprec,instprec,rvprec,rvmeas,mnvel\n")
	star10year025 = open(filename+"10025", 'w')
	star10year025.write("obs_start,obs_end,duration,altitude,azimuth,exposures,photonprec,instprec,rvprec,rvmeas,mnvel\n")
	star20year025 = open(filename+"20025", 'w')
	star20year025.write("obs_start,obs_end,duration,altitude,azimuth,exposures,photonprec,instprec,rvprec,rvmeas,mnvel\n")
	np.random.shuffle(star) # new shuffle so 25% is different from 50%
	starpos = np.arange(int(0.25*len(star)))
	for line in starpos:
		star20year025.write(str(star[line])[2:-1]+"\n")
		if (star[line]["obs_start"] < 2460677.29166667):
			star5year025.write(str(star[line])[2:-1]+"\n")
		if (star[line]["obs_start"] < 2462503.29166667):
			star10year025.write(str(star[line])[2:-1]+"\n")
	star5year025.close()
	star10year025.close()
	star20year025.close()
