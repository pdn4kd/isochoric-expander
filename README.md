# isochoric-expander
Collection of data processing scripts for analizing radial velocity timeseries and finding/confirming/excluding exoplanets. Required libraries: numpy, matplotlib, datetime, pandas, os.

Probably not very coherent initially, but should ultimately cohere with dispatch_scheduler and reimagined-palm-tree. (as well as other codes in the Earthfinder project) This is likely to retain far too many 'hand' steps to be able to be plugged in easily, but should hopefully make replication easy (if desired). Also allow for similar analysis in future projects.

Provisional workflow:
* Generate radial velocities (typically via dispatch_scheduler, then reimagined-palm-tree, then by injecting planet signals with code outside of this context)
* Generate a (provisional) list of planets per star. Currently this is beyond the context of my code, though 'real' planets can be gotten from the above planet injection code. Plans are to have a first-pass fit via repeatedly running generalized Lomb-Scargle analysis.
* Place these scripts in the same folder as the guessed planet and measured RV data.
* run planets.py to generate input files for radvel. This step should probably also generate a shell script to make the next simpler/more consistent.
* Run radvel to find the best fits. Batch runs of radvel are not yet properly automated.
* Determine what planets were successfully recovered or not. This is currently a manual process (as far as looking at best fit, somewhat disfavored etc). Recovered parameters can be put into a single CSV via recovery_parameter_extraction.py. Finding false positives (for the 'real' planets anyway) should be automatable.
* Generate plots of the recovery results with recovery_plots.py, relative_error_plots.py, and error_plots.py.

planets.py generates input files for radvel, given an existing set of planetary systems (and RVs).
recovery_plots.py generates plots, given a table of planets (same as above) plus if the fits recovered/were marginal/excluded a planet. This determination currently must be done manually based on the results of radvel model comparison (favored model == recovered, nearly indistinguishable or somewhat disfavored == marginal, rest == excluded).
recovery_data_extraction.py takes the results of some of radvel's output files (specifically CSVs with the fit planetary parameters), and combines them into a single large CSV for all stars fit a given way. Currently grabs the most likely and ±1 σ values, then converts those into ±1 σ errors.

error_plots.py generate error vs actual value plots for K, period, and (if available) e. This is in contrast to the recovery_plots.py which does period-K and a-m.

Currently 9 fits are being considered for testing properties: null, and [5,e,f,n][n,p]. null has all parameters fixed as a baseline. The rest fit semi-amplitude, period, and time of conjunction for all planets. e- fixes eccentricity at the 'known' value, while 5- and f- allow eccentricity to vary (capped at 0.5 and 0.99, respectively). n- fixes eccentricity at 0 (circular orbits). -p has all planets in the system, while -n drops the long period (currently >3654.0 days) ones, and fits an additional quadratic function for radial velocity. We are drifting towards 5p as the best fit given survey assumptions, and tests on recovery results.

Addendum: We are shifting towards planets65.py, as that generates eccentricities better (max of 0.65, moves large inputs below the limit to prevent unpredictable radvel behavior).

truncate.py Creates a bunch of chopped up surveys (5/10/20 year at 25/50/100% telescope time) given 20 year 100% time surveys.
