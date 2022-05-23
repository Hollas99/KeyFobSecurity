"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
from gnuradio import blocks

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Record Signal when peak detected',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )

    def work(self, input_items, output_items):
        try:
            with open('tmp_recording', 'r') as f:
                f=f.read()
                with open('tmp_signal', 'r+') as f2:
                    f_read=f2.read()
                    if '0' in f_read:
                     #   file = 'signal_1'
                        f = np.fromfile(open("signal_1"), dtype=np.complex64)
                        f=np.append(f,input_items[0]) #Append to array 
                        f.astype(np.complex64).tofile("signal_1") #Save the new array
                    if '1' in f_read: #Start recording the second signal
                        f = np.fromfile(open("signal_2"), dtype=np.complex64)
                        f=np.append(f,input_items[0]) #Append to array 
                        f.astype(np.complex64).tofile("signal_2") #Save the new array

                        #output_items[0][:] = 12345.123
                        f2.seek(0)
                        f2.write('3')
                        #Record to signal 1
                #if '1' in f:
                 #   output_items[0][:] = input_items[0]

        except Exception as e:
            print(e)
        return len(output_items[0])

