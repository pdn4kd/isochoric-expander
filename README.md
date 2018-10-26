# isochoric-expander
Collection of data processing scripts for analizing radial velocity timeseries and finding/confirming/excluding exoplanets.

Probably not very coherent initially, but should ultimately cohere with dispatch_scheduler and reimagined-palm-tree. (as well as other codes in the Earthfinder project) This is likely to retain far too many 'hand' steps to be able to be plugged in easily, but should hopefully make replication easy (if desired). Also allow for similar analysis in future projects.

planets.py generates input files for radvel, given an existing set of planetary systems (and RVs).
recovery_plots.py generates plots, given a table of planets (same as above) plus if the fits recovered/were marginal/excluded a planet. This determination currently must be done manually based on the results of radvel model comparison (favored model == recovered, nearly indistinguishable or somewhat disfavored == marginal, rest == excluded).
recovery_data_extraction.py takes the results of some of radvel's output files (specifically CSVs with the fit planetary parameters), and combines them into a single large CSV for all stars fit a given way. Currently grabs the most likely and ±1 σ values, then converts those into ±1 σ errors.

9 fits are being considered at the moment: null, and [5,e,f,n][n,p]. null has all parameters fixed as a baseline. The rest fit semi-amplitude, period, and time of conjunction for all planets. e- fixes eccentricity at the 'known' value, while 5- and f- allow eccentricity to vary (capped at 0.5 and 0.99, respectively). n- fixes eccentricity at 0 (circular orbits). -p has all planets in the system, while -n drops the long period (currently >3654.0 days) ones, and fits an additional quadratic function for radial velocity.
