import csv
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.time import Time
from astroplan.plots import plot_sky
from astroplan import FixedTarget
from astroplan import Observer
plt.style.use(astropy_mpl_style)

plt.xlim(0, 90)
plt.ylim(0, 360)
plt.xlabel('Altitude')
plt.ylabel('Azimuthal') 

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

def inp(places, lat, lon):
	place = int(input())
	if (place<21 and place>=0) :
		new_obj = obj(place, lon[place], lat[place], places[place])
	else :
		lonlat = list(map(float,input().split()))
		place_name = input()
		new_obj = obj(place, lonlat[0], lonlat[1], place_name)
	return new_obj

class obj:
	def __init__(self, index, lon, lat, name):
		global arr
		self.index=index
		self.lon=lon
		self.lat=lat
		self.name=name
		self.elocation=EarthLocation(lat=lat*u.deg, lon=lon*u.deg,height=100*u.m)
		self.transformed = []
		self.observer = Observer(location=self.elocation,name=name) #### timezone fix
		for i in range(len(arr)):
			self.transformed.append(arr[i].transform_to(AltAz(obstime=reftime,location=self.elocation)))

	
	def print(self):
		print (self.name)
		print (self.lat)
		print (self.lon)

	def show_graph(self):
		global plt
		for i in range(len(arr)):
			star1 = FixedTarget(coord=self.transformed[i].transform_to('fk5'), name="Star"+str(i))
			plot_sky(star1, self.observer, reftime)
			plt.plot(self.transformed[i].alt, self.transformed[i].az, 'bo')
		plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
		plt.show()

	def add_to_csv(self, csv_path):
		with open(csv_path, "w") as output:
			writer = csv.writer(output, lineterminator='\n')
			writer.writerow([self.name,  "Altitude", "Azimuthal"])
			for i,val in enumerate(self.transformed):
				writer.writerow(["Star " + str(i+1), val.alt, val.az]) 
	
mandi =  EarthLocation(lat=31.7754*u.deg, lon=76.9861*u.deg,height=1000*u.m)
utcoffset = +5*u.hour + 30*u.min  # IST
obstime = Time('2018-3-30 03:00:00') - utcoffset

arr = []

star1AltAz = AltAz(representation=None,az=65.125*u.deg,alt=45.645*u.deg,obstime=obstime,location=mandi)
star2AltAz = AltAz(representation=None,az=25.092*u.deg,alt=50.251*u.deg,obstime=obstime,location=mandi)
star3AltAz = AltAz(representation=None,az=91.291*u.deg,alt=19.254*u.deg,obstime=obstime,location=mandi)
star4AltAz = AltAz(representation=None,az=158.217*u.deg,alt=28.222*u.deg,obstime=obstime,location=mandi)
star5AltAz = AltAz(representation=None,az=224.402*u.deg,alt=73.078*u.deg,obstime=obstime,location=mandi)

arr.append( SkyCoord(alt = star1AltAz.alt, az = star1AltAz.az, obstime = obstime, frame = 'altaz', location = mandi))
arr.append( SkyCoord(alt = star2AltAz.alt, az = star2AltAz.az, obstime = obstime, frame = 'altaz', location = mandi))
arr.append( SkyCoord(alt = star3AltAz.alt, az = star3AltAz.az, obstime = obstime, frame = 'altaz', location = mandi))
arr.append( SkyCoord(alt = star4AltAz.alt, az = star4AltAz.az, obstime = obstime, frame = 'altaz', location = mandi))
arr.append( SkyCoord(alt = star5AltAz.alt, az = star5AltAz.az, obstime = obstime, frame = 'altaz', location = mandi))

reftime = Time('2018-3-30 12:00:00') - utcoffset

places = ["london", "NewYork", "LosAngeles", "Chicago", "Boston", "Seattle", "LasVegas", "Greenwich", "Delhi", "Mumbai", "Pune", "Dispur", "Islamabad", "Dhaka", "Berlin", "Rome", "Paris", "Moscow", "Amsterdam", "Budapest", "Tokyo"]
lat = [51.5074, 40.7128, 34.0522, 41.8781, 42.3601, 47.6062, 36.1699, 51.4826, 28.7041, 19.076, 23.022, 26.006, 33.6844, 23.685, 52.52, 41.9028, 48.8566, 55.7558, 52.3702, 47.4979, 35.6895]
lon = [0.1278, 74.006, 118.2437, 87.6298, 71.0589, 122.3321, 115.1398, 0.0077, 77.1025, 72.8777, 72.5714, 92.9376, 73.0479, 90.3563, 13.405, 12.4964, 2.3522, 37.6173, 4.8952, 19.0402, 139.6917]

print("Enter the index for the location")
for i in range(len(places)):
	print(i,". ", places[i])
print("21 . Enter long and lat of place with name")

london = inp(places, lat, lon)
london.print()
london.show_graph()

#res = [x, y, z, ....]
csvfile = london.name
london.add_to_csv(csvfile+".csv")
