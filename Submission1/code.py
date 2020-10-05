from openpyxl import load_workbook, Workbook
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u
from astropy.time import Time

import pylab as plt

import ephem
import numpy as np

putter_string = "BCDEF"

stars_alt = [45.645, 50.491, 19.254, 28.222, 73.078]
stars_az = [65.125, 25.092, 91.291, 158.217, 224.402]

def get_results(lat, lon, elev, observation_time):
	if observation_time == "": observation_time = "2018/03/31 00:00:00.00"
	alts, azs = [], []
	observer = ephem.Observer()
	observer.lon = np.radians(lon)
	observer.lat = np.radians(lat)
	observer.elevation = elev
	observer.date = ephem.Date(observation_time) 

	temp = ((observation_time.split())[0]).split('/')
	observation_time = "-".join(temp) + " " + (observation_time.split())[1]

	for l in xrange(5):
		names = ['Star1','Star2','Star3','Star4','Star5']
		ra, dec = observer.radec_of(np.radians(stars_az[l]), np.radians(stars_alt[l]))
		new_location = EarthLocation(lat=lat, lon=lon, height=elev*u.m)
		new_time = Time(observation_time)
		aa = AltAz(location=new_location, obstime=new_time)

		coord = SkyCoord(str(ra), str(dec), unit='deg')
		g = coord.transform_to(aa)
		az, alt = boring_function(str(g.az)), boring_function(str(g.alt))

		azs.append(az)
		alts.append(alt)

	fig, ax = plt.subplots()
	xmin, xmax = min(azs), max(azs)
	ymin, ymax = min(alts), max(alts)
	ax.set_xlim([xmin,xmax])
	ax.set_ylim([ymin,ymax])
	ax.scatter(azs, alts)

	for i, txt in enumerate(names):
	    ax.annotate(txt, (azs[i], alts[i]))

	plt.savefig("new_place.png",bbox_inches='tight')

	return alts, azs

def boring_function(kill):
	first_index = kill.find('d')
	d = kill[:first_index] 
	kill = kill[first_index:]
	m = kill[1:kill.find('m')]
	kill = kill[kill.find('m')+1:-1]
	return float(d) + float(m)/60. + float(kill)/3600.

mandi_lat, mandi_lon, mandi_alt = 31.7754, 76.9861, 1000

observation_time = ephem.Date('2018/3/30 03:00:00.00') 

for i in xrange(len(data)):
	observer = ephem.Observer()
	observer.lon = np.radians(mandi_lon)
	observer.lat = np.radians(mandi_lat)
	observer.elevation = 1000
	observer.date = observation_time

	output_alt, output_az = [], []

	for l in xrange(5):
		names = ['Star1','Star2','Star3','Star4','Star5']
		ra, dec = observer.radec_of(np.radians(stars_az[l]), np.radians(stars_alt[l]))
		ab = data[i]
		lato, lono = ab['latitude'], ab['longitude']
		new_location = EarthLocation(lat=lato, lon=lono, height=100*u.m)
		new_time = Time('2018-3-30 12:00:00')
		aa = AltAz(location=new_location, obstime=new_time)
		coord = SkyCoord(str(ra), str(dec), unit='deg')
		g = coord.transform_to(aa)
		az, alt = boring_function(str(g.az)), boring_function(str(g.alt))
		output_az.append(az)
		output_alt.append(alt)
		wb = load_workbook('output.xlsx')
		sheet = wb.get_sheet_by_name('N-W')
		sheet[putter_string[l]+str(i+2)] = "alt=" + str(alt) + ", az=" + str(az)
		wb.save(filename='output.xlsx')