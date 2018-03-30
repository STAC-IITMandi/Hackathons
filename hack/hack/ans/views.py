from django.shortcuts import render

from .forms import Myform, NayaForm

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

def get_results(lat, lon, elev, observation_time=''):
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

def app(request):
    if request.method == 'POST':
        form = Myform(request.POST)
        form1 = NayaForm(request.POST)
        if form.is_valid():
            lat = request.POST['lat']
            lon = request.POST['lon']
            ele = request.POST['ele']
            # time = request.POST['time']
            alt, az = get_results(lat, lon, ele)
            array = []
            for i in range(5):
                array.append({'a':i+1,'b':alt[i],'c':az[i]})
            context = {'lat': lat, 'lon': lon, 'ele': ele, 'form': form, 'form1':form1, 'array': array}
            return render(request, 'input.html', context)
        elif form1.is_valid():
            city = request.POST['city']
            context = {'lat': lat, 'lon': lon, 'ele':ele, 'form':form, 'form1':form1}
            return render(request, 'input.html', context)
    else:
        form = Myform()
        form1 = NayaForm()
    return render(request, 'input.html', {'form': form, 'form1':form1})
