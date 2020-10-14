import numpy as np
import os

fpath = ''
file_list = os.listdir(fpath)
ras_files = [f[:-3] for f in file_list if f[-3:] == 'ras']
xye_files = [f[:-3] for f in file_list if f[-3:] == 'xye']
ras_notxye = [rf for rf in ras_files if rf not in xye_files]
sizes = [(os.stat(r + 'ras')).st_size for r in ras_notxye]
ras_todo = [rn for i, rn in enumerate(ras_notxye) if sizes[i] > 0]

for rf in ras_todo:
    fname = rf + 'ras'
    new_fname = fname[:-3] + 'xye'
    data = np.genfromtxt(fname, comments='*', usecols=[0, 1])
    new_data = np.column_stack((data, data[:, 1]**0.5))
    np.savetxt(new_fname, new_data)
    print(f'Written {new_fname}')

