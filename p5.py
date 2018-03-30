import ephem
import astropy
import astroplan
from astroplan import FixedTarget
from astroplan import Observer
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
import astropy.units as u
import matplotlib.pyplot as plt
from astropy.time import Time
from astroplan.plots import plot_sky
import numpy as np


mandi = ephem.Observer()
mandi.lon = '76.9861'
mandi.lat = '31.7754'
mandi.elevation = 1000
mandi.date = '2018/03/31 03:00:00'
# observer.epoch = ephem.J2000
# radec_of(az,alt)

star1_ra, star1_dec = mandi.radec_of(float (ephem.degrees('65.125')), float (ephem.degrees('45.645')))
star2_ra, star2_dec = mandi.radec_of(float (ephem.degrees('25.092')), float (ephem.degrees('50.491')))
star3_ra, star3_dec = mandi.radec_of(float (ephem.degrees('91.291')), float (ephem.degrees('19.254')))
star4_ra, star4_dec = mandi.radec_of(float (ephem.degrees('158.217')),float ( ephem.degrees('28.222')))
star5_ra, star5_dec = mandi.radec_of(float (ephem.degrees('224.402')),float ( ephem.degrees('73.078')))

print np.degrees(star1_ra), np.degrees(star1_dec)
print np.degrees(star2_ra), np.degrees(star2_dec)
print np.degrees(star3_ra), np.degrees(star3_dec)
print np.degrees(star4_ra), np.degrees(star4_dec)
print np.degrees(star5_ra), np.degrees(star5_dec)


star1_coord = SkyCoord(ra=np.degrees(star1_ra)*u.deg, dec=np.degrees(star1_dec)*u.deg)
star1_1 = FixedTarget(coord=star1_coord, name="star1")

star2_coord = SkyCoord(ra=np.degrees(star2_ra)*u.deg, dec=np.degrees(star2_dec)*u.deg)
star2_2 = FixedTarget(coord=star2_coord, name="star2")

star3_coord = SkyCoord(ra=np.degrees(star3_ra)*u.deg, dec=np.degrees(star3_dec)*u.deg)
star3_3 = FixedTarget(coord=star3_coord, name="star3")

star4_coord = SkyCoord(ra=np.degrees(star4_ra)*u.deg, dec=np.degrees(star4_dec)*u.deg)
star4_4 = FixedTarget(coord=star4_coord, name="star4")

star5_coord = SkyCoord(ra=np.degrees(star5_ra)*u.deg, dec=np.degrees(star5_dec)*u.deg)
star5_5 = FixedTarget(coord=star5_coord, name="star5")

star1 = ephem.FixedBody()
star1._ra = star1_ra
star1._dec = star1_dec

star2 = ephem.FixedBody()
star2._ra = star2_ra
star2._dec = star2_dec

star3 = ephem.FixedBody()
star3._ra = star3_ra
star3._dec = star3_dec

star4 = ephem.FixedBody()
star4._ra = star4_ra
star4._dec = star4_dec

star5 = ephem.FixedBody()
star5._ra = star5_ra
star5._dec = star5_dec


location1 = ephem.Observer()
location1.long =  ephem.degrees('76.9861')
location1.lat = ephem.degrees('31.7754')
location1.elevation = 1000
location1.date = '2018/03/30 12:00:00'

star1.compute(location1)
star2.compute(location1)
star3.compute(location1)
star4.compute(location1)
star5.compute(location1)


print np.degrees(star1.alt), np.degrees(star1.az)
print np.degrees(star2.alt), np.degrees(star2.az)
print np.degrees(star3.alt), np.degrees(star3.az)
print np.degrees(star4.alt), np.degrees(star4.az)
print np.degrees(star5.alt), np.degrees(star5.az)



file = open("testfile.txt","r")
value = map(float, file.readlines())
longitude = value[0] #float(76.9861)
latitude = value[1] #float(31.7754)

print latitude, longitude

location = EarthLocation.from_geodetic(longitude*u.deg, latitude*u.deg, 1000*u.m)
observer = Observer(location=location, name="observer", timezone="Asia/Kolkata")
# observer = Observer(longitude=longitude*u.deg, latitude=latitude*u.deg, elevation=1000*u.m, name="Observer1", timezone="Asia/Kolkata")
observer_time = Time(['2018-03-31 12:00:00'])

star1_style = {'color': 'k'}
star2_style = {'color': 'g'}
star3_style = {'color': 'r'}
star4_style = {'color': 'c'}
star5_style = {'color': 'b'}

plot_sky(star1_1, observer, observer_time, style_kwargs=star1_style)
plot_sky(star2_2, observer, observer_time, style_kwargs=star2_style)
plot_sky(star3_3, observer, observer_time, style_kwargs=star3_style)
plot_sky(star4_4, observer, observer_time, style_kwargs=star4_style)
plot_sky(star5_5, observer, observer_time, style_kwargs=star5_style)



plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
plt.savefig('fig1.png')
plt.show()


#star_ra = np.degrees(star1._ra)
#star_dec = np.degrees(star1._dec)
#step_ra = np.degrees((star2._ra - star1._ra)/10);
#step_dec = np.degrees((star2._dec - star2._dec)/10);

#for i in range(1,11) :
#	starz_coord = SkyCoord(ra=star_ra*u.deg, dec=star_dec*u.deg)
#	star = FixedTarget(coord=starz_coord, name="star" + str(i))
	#star_ra = star_ra + step_ra
#	# #star_dec = star_dec + step_dec
#	plot_sky(starz_coord, observer, observer_time, style_kwargs=star1_style)
#plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
#plt.show()