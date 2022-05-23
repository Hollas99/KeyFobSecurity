"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import os
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Manage the peaking signal',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )

    def work(self, input_items, output_items):
        try:
            input_string = np.array2string(input_items[0]) #convert array to string
            if '1' in input_string:
                with open('tmp_start', 'r+') as s:
                    if s.read() == '0':
                        s.seek(0)  
                        s.write('1')
                #Start recording if not already
                with open('tmp_recording', 'w') as f:
                    f.write('1')
            else: #The signal isn't peaking
                #First check if the recording started
                with open('tmp_start', 'r+') as s2:
                    if '0' in s2.read():
                        return len(output_items[0])
                #Check if a counter has started already
                with open('tmp_counter', 'r+') as f2:
                    counter=f2.read() #Read the file
                    if int(counter) == 1000: #Check if the counter has reached 50
                        counter=0
                        f2.seek(0)
                        f2.write('0') #Reset the counter
                        with open('tmp_recording', 'w') as w1: #Stop the recording file
                            w1.write('0') #Stop recording
                            with open('tmp_signal', 'r+') as s1: #Open signal file
                                if s1.read() == '0': #This is the first signal
                                    s1.seek(0)  
                                    s1.write('1') #Start second recording
                                    print('First Recording Complete')
                                    #Reset start back to 0
                                    with open('tmp_start', 'w') as s3: #Resets the start back to 0, so the recording will start when the next peak is detected
                                        s3.seek(0)
                                        s3.write('0')
                                else: #Both signals have been captured
                                    print('Both Recordings Complete') #stop listening and jamming and replay first signal, make led green?
                                    s1.seek(0)
                                    s1.write('2') #Stop the writing to file
                                    #Stop jamming
                                    try:
                                        os.system('nmcli con down id "ESPap 1"')
                                    except:
                                        print("ESPap was not connected")
                                    #Run the splitting file
                                    #import subprocess
                                    #exec(open("/home/scott/Documents/GNURadio/CAR/split_files.py").read())
                                    #exec(open("/home/scott/Documents/GNURadio/CAR/transmit_signal.py").read())
                                    #subprocess.call('/home/scott/Documents/GNURadio/CAR/split_files.py',shell=True)
                                    #subprocess.call('/home/scott/Documents/GNURadio/CAR/transmit_signal.py', shell=True)

                                    '''
                                    #Turn off amber led
                                    LED_PIN = 17
                                    GPIO.setmode(GPIO.BCM)
                                    GPIO.output(LED_PIN, GPIO.LOW)
                                    #Light Up Green Led
                                    LED_PIN = 17
                                    GPIO.setup(LED_PIN, GPIO.OUT)
                                    GPIO.output(LED_PIN, GPIO.HIGH)
                                    time.sleep(1)
                                    GPIO.output(LED_PIN, GPIO.LOW)
                                    GPIO.cleanup()
                                    '''

                    if int(counter) != 0: #The counter has started already
                        counter= int(counter)+1 #add one ot the counter
                        f2.seek(0)
                        f2.write(str(counter)) #Write the incremented value ot the file
                    else: #If the counter hasn't started
                        with open('tmp_counter', 'w') as f3: #Open the file for write
                            f3.write('1') #Begin the count

        except Exception as e: 
            print(e)
        #output_items[0][:] = output
        
        return len(output_items[0])
