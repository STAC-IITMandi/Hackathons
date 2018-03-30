import ephem
from django.shortcuts import render
from astroplan import Observer
import astropy.units as u
from datetime import datetime
from astropy.time import Time, TimezoneInfo
from astroplan import FixedTarget
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
from astroplan.plots import plot_sky


def index(request):
    return render(request, 'astro/index.html')


def result(request):
    long = request.POST.get('obsLon')
    lat = request.POST.get('obsLat')
    obsdate = request.POST.get('obsDate')
    obsTime = request.POST.get('obsTime')
    ob = ephem.Observer()
    ob.long = long
    ob.lat = lat
    ob.date = ephem.localtime(ephem.Date(str(obsdate) + " " + str(obsTime)))
    ob.elevation = 100
    stars = [["65:7:30", "45:38:42"], ["25:5:31.2", "50:29:27.6"], ["91.17.27.6", "19:15:14.4"], ["158:13:1.2", "25:13:19.2"], ["224:24:7.2", "73:4:40.8"]]
    mandiobserver = ephem.Observer()
    mandiobserver.long = "31:46:31.44"
    mandiobserver.lat = "76.59.9.96"
    mandiobserver.elevation = 1000
    mandiobserver.date = ephem.localtime(ephem.Date("2018/03/30 03:00:00"))
    new_values = []
    for star in stars:
        ra, dec = mandiobserver.radec_of(star[0], star[1])
        star1 = ephem.FixedBody()
        star1._ra = ra
        star1._dec = dec
        star1.compute(ob)
        new_values.append(star1)
    new_values1 = []
    for value in new_values:
        s = [str(value.alt), str(value.az)]
        new_values1.append(s)
    context = {
        'values': new_values1,
        'long': long,
        'lat': lat
    }
    newt = TimezoneInfo(utc_offset=5.5 * u.hour)
    ob1 = Observer(latitude=ob.lat * u.deg, longitude=ob.long * u.deg, elevation=ob.elevation * u.m, timezone=newt)
    for value in new_values:
        starCoord = SkyCoord(ra=value.ra*u.deg, dec=value.dec*u.deg)
        starObj = FixedTarget(coord=starCoord)
        plot_sky(starObj, ob1, Time(["2018-03-30 12:00:00"]))
    plt.show()
    # plt.savefig('static/astro/images/plot.jpg')
    return render(request, 'astro/result.html', context)