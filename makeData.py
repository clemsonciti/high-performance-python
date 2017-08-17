import os
import numpy as np
import pandas as pd
from glob import glob

def create_weather_big(growth=12800):
    filenames = sorted(glob(os.path.join('data', 'weather-small', '*.hdf5')))

    if not os.path.exists(os.path.join('data', 'weather-big')):
        os.mkdir(os.path.join('data', 'weather-big'))

    if all(os.path.exists(fn.replace('small', 'big')) for fn in filenames):
        return

    from scipy.misc import imresize
    import h5py

    for fn in filenames:
        print("Creating big weather data from file {}".format(fn))
        with h5py.File(fn, mode='r') as f:
            x = f['/t2m'][:]

        y = np.float64(imresize(x, growth))
 
        out_fn = os.path.join('data', 'weather-big', os.path.split(fn)[-1])

        try:
            with h5py.File(out_fn) as f:
                f.create_dataset('/t2m', data=y, chunks=(500, 500))
        except:
            pass

        
def create_weather_medium(growth=3200):
    filenames = sorted(glob(os.path.join('data', 'weather-small', '*.hdf5')))

    if not os.path.exists(os.path.join('data', 'weather-medium')):
        os.mkdir(os.path.join('data', 'weather-medium'))

    if all(os.path.exists(fn.replace('small', 'medium')) for fn in filenames):
        return

    from scipy.misc import imresize
    import h5py

    for fn in filenames:
        print("Creating medium weather data from file {}".format(fn))
        with h5py.File(fn, mode='r') as f:
            x = f['/t2m'][:]

        y = np.float64(imresize(x, growth))
 
        out_fn = os.path.join('data', 'weather-medium', os.path.split(fn)[-1])

        try:
            with h5py.File(out_fn) as f:
                f.create_dataset('/t2m', data=y, chunks=(500, 500))
        except:
            pass

if __name__ == '__main__':
    create_weather_big()
    create_weather_medium()
