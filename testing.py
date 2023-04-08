# test with pyndl

from pyndl import preprocess
from pyndl import ndl
import xarray  

preprocess.create_event_file(corpus_file='./lcorpus.txt',
                             event_file='./levent.tab.gz',
                             allowed_symbols='a-zA-Z',
                             context_structure='document',
                             event_structure='consecutive_words',
                             event_options=(1, ),
                             cue_structure='bigrams_to_word')

weights = ndl.ndl(events='./levent.tab.gz', alpha=0.1, betas=(0.1, 0.1), method="threading")
weights.to_netcdf('./weights.nc')

with xarray.open_dataarray('./weights.nc') as weights_read:  
    weights_read