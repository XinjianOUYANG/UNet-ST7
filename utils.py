import h5py
import numpy as np

# read HDF5 file：
def read_h5(h5_path):
    f = h5py.File(h5_path,'r')   #打开h5文件
    print(f.keys())

    return f