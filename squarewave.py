# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 17:00:02 2016
Script written to plot ideal square waves.
@author: Giacomo Marchioro
"""
import matplotlib.pyplot as plt
import numpy as np
from __future__ import print_function
from __future__ import division 


def sqwav(freq,duration='half period',x_offset=0,name='',amplitude=1,xlim='auto',y_offset=0,plot=False):

    """Plot a square wave.

    Keyword arguments:
    freq -- The frequency of the wave in Hz
    duration -- The duration of the signal in milliseconds (default is half period)
    x_offset -- the starting time of the first wave in milliseconds (default is 0)
    amplitued -- The amplitude of the wave (default is 1)
    name -- A name to be written in the label
    xlim -- set the x axis limit in ms (default is auto).
    
    Return x,y values of the wave.
    """
    

    if duration=='half period':
        duration=1000/(freq*2.)#The duration is set to default to half the period
    if duration>=1000/freq:
        print("Pulse duration exeeds frequency!") 
    if xlim=='auto':
        xlim=1000/(freq*2.)*4
    starting_points=np.linspace(-1000,2000,freq*3+1)+x_offset #define the starting point
    ending_points=[]
    for i in starting_points:
        ending_points.append(i+duration)
    x=np.vstack([starting_points,starting_points,ending_points,ending_points]).ravel('F')
    #repeat the same point twice e.g. [0,0,1,1,2,2]
    zero=np.zeros(len(x)//4)
    one=np.ones(len(x)//4)
    y=np.vstack([zero,one,one,zero,]).ravel('F')*amplitude+y_offset
    if plot:
        plt.plot(x,y,label='%s %s Hz, duration: %s ms' %(name,freq,duration))
        plt.xlim(0,xlim)
        plt.ylim(-0.2,1.2)
        plt.xlabel('(ms)')
        plt.legend(fontsize='small')
    return x,y

if __name__ == "__main__":
    #This is  a simple example that shows how to use the function to plot multiple
    #frequencies in the same plot. e.g. we have a tringger witha frequency of
    #90 Hz, duration of 2 ms that trigger form time 0. We use scale to facilitate
    #the visualization of the signals. 
    names=['Trigger','Sensor','Laser']
    freq=[90,34,10] #put always the lowest frequency at the end
    durations=[2,8,70]
    offsets=[0,23,0]
    a= zip(freq,durations,offsets,names)
    scale=1
    y_offset=0
    for i in a:
         sqwav(i[0],i[1],i[2],i[3],y_offset = y_offset,plot=True)
         y_offset+=1.5
    plt.yticks(np.arange(0.5, y_offset, 1.5),names)
    plt.ylim(-0.2,y_offset)

