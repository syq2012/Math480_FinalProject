import numpy as np
import wave
import cmath
import matplotlib.pyplot as plt
import math
import os
import sys



def save(path, ext='png', close=True, verbose=True):
    """Save a figure from pyplot.
 
    Parameters
    ----------
    path : string
        The path (and filename, without the extension) to save the
        figure to.
 
    ext : string (default='png')
        The file extension. This must be supported by the active
        matplotlib backend (see matplotlib.backends module).  Most
        backends support 'png', 'pdf', 'ps', 'eps', and 'svg'.
 
    close : boolean (default=True)
        Whether to close the figure after saving.  If you want to save
        the figure multiple times (e.g., to multiple formats), you
        should NOT close it in between saves or you will have to
        re-plot it.
 
    verbose : boolean (default=True)
        Whether to print information about when and where the image
        has been saved.
 
    """
    
    # Extract the directory and filename from the given path
    directory = os.path.split(path)[0]
    filename = "%s.%s" % (os.path.split(path)[1], ext)
    if directory == '':
        directory = '.'
 
    # If the directory does not exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
 
    # The final path to save to
    savepath = os.path.join(directory, filename)
 
    if verbose:
        print("Saving figure to '%s'..." % savepath),
 
    # Actually save the figure
    plt.savefig(savepath)
    
    # Close it
    if close:
        plt.close()
 
    if verbose:
        print("Done")

# function to get wave to array data
def wavToArray(fileName):
    reader = wave.open(fileName, 'rb')
    nchannels, sampwidth, framerate, nframes, comptype, compname = reader.getparams()[:6]
    # assume chanel is 1
    time = framerate/nframes  #number of seconds in the file
    frame_list = []
    frame_list = np.fromstring(reader.readframes(nframes), dtype = np.int16)
    reader.close()
    frame_list = frame_list.astype(np.float)
    return frame_list

# Breaking up into roots of unity
def omega(p, q):
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

def padding(signal):
    for x in range(65536-len(signal)):
      signal.append(0)
    return signal

# The actual function
def fft(signal):
   n = len(signal)
    
   # if the input is only one then we can't really do a fft can we BITCHES
    
   if n == 1:
      return signal
    
   else:
      # breaking up into odd and even pieces
      F_even = fft([signal[i] for i in xrange(0, n, 2)])
      F_odd = fft([signal[i] for i in xrange(1, n, 2)])
        
      # defining new empty array with n entries
      combined = [0] * n
      
      # implementation of the alg lmao idk whats going on FUCK
      for m in xrange(n/2):
         combined[m] = F_even[m] + omega(n, -m) * F_odd[m]
         combined[m + n/2] = F_even[m] - omega(n, -m) * F_odd[m]
 
      return combined

b = wavToArray(sys.argv[1]).tolist()
b = padding(b)
test2 = fft(b)
test = [0]*10000
# need to only work with the magnitude - throw way phase. Also rounding in this example due to some random noise that all goes to 0
for i in range(65536):
	   test2[i] = round(abs(test2[i]))
ic = [2*math.pi*x for x in range(10000)]
for i in range(10000):
	test[i] = test2[i]
plt.plot(ic, test)
save("signal", ext="png", close=False, verbose=True)	
   
