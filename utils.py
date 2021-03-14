import h5py
import numpy as np

# read HDF5 file：
def read_h5(h5_path):
    f = h5py.File(h5_path,'r')   #open h5 file
    print(f.keys())

    return f