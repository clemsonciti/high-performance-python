
module load osg-proxy
conda create -n hpp-workshop python=3.5
source activate hpp-workshop
conda install -y numpy pandas h5py Pillow matplotlib scipy toolz pytables snakeviz dask distributed numba ipykernel
python -m ipykernel install --user --name hpp-workshop --display-name "High Performance Python workshop"