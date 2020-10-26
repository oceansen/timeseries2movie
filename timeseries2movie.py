import pandas as pd
import csv
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

import pandas as pd
import os


FREQUENCY_POINT_PER_SECOND = 10
PATH = f"{os.getcwd()}/"
IMG_FOLDER = f"{PATH}/img"
SECONDS_TO_DISPLAY = 50 * FREQUENCY_POINT_PER_SECOND


def readCSVFile(file):
    try:
        df = pd.read_csv(file)
        print(df)
    finally:
        return df




def move_x(frame):
    ax1.set_xlim(frame,frame+SECONDS_TO_DISPLAY)
    ax2.set_xlim(frame,frame+SECONDS_TO_DISPLAY)
    ax3.set_xlim(frame,frame+SECONDS_TO_DISPLAY)
    ax4.set_xlim(frame,frame+SECONDS_TO_DISPLAY)
    ax5.set_xlim(frame,frame+SECONDS_TO_DISPLAY)
    ax6.set_xlim(frame,frame+SECONDS_TO_DISPLAY)
    ax7.set_xlim(frame,frame+SECONDS_TO_DISPLAY)
    ax8.set_xlim(frame,frame+SECONDS_TO_DISPLAY)
    ax9.set_xlim(frame,frame+SECONDS_TO_DISPLAY)
    ax1.annotate('Actual and Command Posistion of part (x,y,z) in mm', xy=(frame,0))
    ax2.annotate('Actual and Command Velocity of part (x,y,z) in mm/s', xy=(frame,-55))
    ax3.annotate('Actual Acceleration of part (x,y,z) in mm/s/s', xy=(frame,-1205))
    ax4.annotate('Command Acceleration of part (x,y,z) in mm/s/s', xy=(frame,-1205))
    ax5.annotate('Current feedback (x,y,z) in A', xy=(frame,-30))
    ax6.annotate('DCBusVoltage (x,y,z) in V', xy=(frame,-0.4))
    ax7.annotate('Output Current (x,y,z) in A', xy=(frame,300))
    ax8.annotate('Output Voltage (x,y,z) in V', xy=(frame,0))
    ax9.annotate('Spindle Actual and Command Position in mm', xy=(frame,-2150))
    ax10.annotate('Spindle Actual and Command Velocity in mm/s', xy=(frame,0))
    ax11.annotate('Spindle Actual and Command Accelaration in mm/s/s', xy=(frame,-125))
    ax12.annotate('Spindle Current Feedback (A)', xy=(frame,-10))
    ax13.annotate('Spindle DC Bus Voltage (V)', xy=(frame,0))
    ax14.annotate('Spindle Output Current (A)', xy=(frame,300))
    ax15.annotate('Spindle Output Voltage (V)', xy=(frame,0))
    ax16.annotate('Spindle Output Power (A)', xy=(frame,0))
    ax17.annotate('Spindle System Interia (kg*m^2)', xy=(frame,0))
    ax18.annotate('Spindle Feed Rate (100 rpm)', xy=(frame,0))




def add_patch_to_plot(plot,start,end):
    rect = patches.Rectangle((start,-1),width=end-start,height=2,linewidth=1,edgecolor='r',facecolor='none')
    plot.add_patch(rect)

fig, (ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12,ax13,ax14,ax15,ax16,ax17,ax18) = plt.subplots(18, 1, sharex='all')



def generateVideoFromTimeSeries(path):
    timeseries = readCSVFile(path)

    #Variables plotted in first axes
    #X1_ActualPosition: actual x position of part (mm)
    #Y1_ActualPosition: actual y position of part (mm)
    #Z1_ActualPosition: actual z position of part (mm)
    #X1_CommandPosition: reference x position of part (mm)
    #Y1_CommandPosition: reference y position of part (mm)
    #Z1_CommandPosition: reference z position of part (mm)
    min_ActualPosition = 0
    max_ActualPosition = 200

    ax1.set_ylim(min_ActualPosition,max_ActualPosition)
    ax1.set_title('Actual Position of Part')
    ax1.set_xlim(0,SECONDS_TO_DISPLAY)

    #Actual position
    timeseries["X1_ActualPosition"].plot(figsize=(10,10),color="red",ax=ax1)
    timeseries["Y1_ActualPosition"].plot(figsize=(10,10),color="green",ax=ax1)
    timeseries["Z1_ActualPosition"].plot(figsize=(10,10),color="blue",ax=ax1)

    #Reference position
    timeseries["X1_CommandPosition"].plot(figsize=(10,10),color="darkred",ax=ax1,linestyle='--')
    timeseries["Y1_CommandPosition"].plot(figsize=(10,10),color="darkgreen",ax=ax1,linestyle='--')
    timeseries["Z1_CommandPosition"].plot(figsize=(10,10),color="darkblue",ax=ax1,linestyle='--')


    

    #Variables plotted in second axes
    #X1_ActualVelocity: actual x velocity of part (mm/s)
    #Y1_ActualVelocity: actual y velocity of part (mm/s)
    #Z1_ActualVelocity: actual z velocity of part (mm/s)
    #X1_CommandVelocity: actual x velocity of part (mm/s)
    #Y1_CommandVelocity: actual y velocity of part (mm/s)
    #Z1_CommandVelocity: actual z velocity of part (mm/s)
    
    min_ActualVelocity = -55
    max_ActualVelocity = 55
    ax2.set_ylim(min_ActualVelocity,max_ActualVelocity)
    ax2.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["X1_ActualVelocity"].plot(figsize=(10,10),color="red",ax=ax2)
    timeseries["Y1_ActualVelocity"].plot(figsize=(10,10),color="green",ax=ax2)
    timeseries["Z1_ActualVelocity"].plot(figsize=(10,10),color="blue",ax=ax2)
    #Reference velocity
    timeseries["X1_CommandVelocity"].plot(figsize=(10,10),color="darkred",ax=ax2,linestyle='--')
    timeseries["Y1_CommandVelocity"].plot(figsize=(10,10),color="darkgreen",ax=ax2,linestyle='--')
    timeseries["Z1_CommandVelocity"].plot(figsize=(10,10),color="darkblue",ax=ax2,linestyle='--')

    #Variables plotted in third axes
    #X1_ActualAcceleration: actual x acceleration of part (mm/s/s)
    #Y1_ActualAcceleration: actual x acceleration of part (mm/s/s)
    #Z1_ActualAcceleration: actual x acceleration of part (mm/s/s)
    


    min_ActualAcceleration = -1200
    max_ActualAcceleration = 1200
    ax3.set_ylim(min_ActualAcceleration,max_ActualAcceleration)
    ax3.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["X1_ActualAcceleration"].plot(figsize=(10,10),color="red",ax=ax3)
    timeseries["Y1_ActualAcceleration"].plot(figsize=(10,10),color="green",ax=ax3)
    timeseries["Z1_ActualAcceleration"].plot(figsize=(10,10),color="blue",ax=ax3)
   
    #Variables plotted in 4th axes
    #X1_CommandAcceleration: actual x acceleration of part (mm/s/s)
    #Y1_CommandAcceleration: actual x acceleration of part (mm/s/s)
    #Z1_CommandAcceleration: actual x acceleration of part (mm/s/s)
    min_CommandAcceleration = -1200
    max_CommandAcceleration = 1200
    ax4.set_ylim(min_CommandAcceleration,max_CommandAcceleration)
    ax4.set_xlim(0,SECONDS_TO_DISPLAY)
    #Reference acceleration   
    timeseries["X1_CommandAcceleration"].plot(figsize=(10,10),color="darkred",ax=ax4)
    timeseries["Y1_CommandAcceleration"].plot(figsize=(10,10),color="darkgreen",ax=ax4)
    timeseries["Z1_CommandAcceleration"].plot(figsize=(10,10),color="darkblue",ax=ax4)


    #Variables plotted in 5th axes
    #X1_CurrentFeedback: current (A)
    #Y1_CurrentFeedback: current (A)
    #Z1_CurrentFeedback: current (A)

    min_CurrentFeedback = -30
    max_CurrentFeedback = +30
    ax5.set_ylim(min_CurrentFeedback,max_CurrentFeedback)
    ax5.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["X1_CurrentFeedback"].plot(figsize=(10,10),color="red",ax=ax5)
    timeseries["Y1_CurrentFeedback"].plot(figsize=(10,10),color="green",ax=ax5)
    timeseries["Z1_CurrentFeedback"].plot(figsize=(10,10),color="blue",ax=ax5)

    #Variables plotted in 6th axes
    #X1_DCBusVoltage: voltage (V)
    #Y1_DCBusVoltage: voltage (V)
    #Z1_DCBusVoltage: voltage (V)

    min_DCBusVoltage = -0.4
    max_DCBusVoltage = +0.4
    ax6.set_ylim(min_DCBusVoltage,max_DCBusVoltage)
    ax6.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["X1_DCBusVoltage"].plot(figsize=(10,10),color="red",ax=ax6)
    timeseries["Y1_DCBusVoltage"].plot(figsize=(10,10),color="green",ax=ax6)
    timeseries["Z1_DCBusVoltage"].plot(figsize=(10,10),color="blue",ax=ax6)

    #Variables plotted in 7th axes
    #X1_OutputCurrent: current (A)
    #Y1_OutputCurrent: current (A)
    #Z1_OutputCurrent: current (A)

    min_OutputCurrent = 300
    max_OutputCurrent = 350
    ax7.set_ylim(min_OutputCurrent,max_OutputCurrent)
    ax7.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["X1_OutputCurrent"].plot(figsize=(10,10),color="red",ax=ax7)
    timeseries["Y1_OutputCurrent"].plot(figsize=(10,10),color="green",ax=ax7)
    timeseries["Z1_OutputCurrent"].plot(figsize=(10,10),color="blue",ax=ax7)

    #Variables plotted in 8th axes
    #X1_OutputVoltage: voltage (V)
    #Y1_OutputVoltage: voltage (V)
    #Z1_OutputVoltage: voltage (V)
    min_OutputVoltage = 0
    max_OutputVoltage = 100
    ax8.set_ylim(min_OutputVoltage,max_OutputVoltage)
    ax8.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["X1_OutputVoltage"].plot(figsize=(10,10),color="red",ax=ax8)
    timeseries["Y1_OutputVoltage"].plot(figsize=(10,10),color="green",ax=ax8)
    timeseries["Z1_OutputVoltage"].plot(figsize=(10,10),color="blue",ax=ax8)

    #Variables plotted in 9th axes
    #S1_ActualPosition: actual position of spindle (mm)
    #S1_CommandPosition: reference position of spindle (mm)
    min_S_ActualPosition = -2150
    max_S_ActualPosition = 2150
    ax9.set_ylim(min_S_ActualPosition,max_S_ActualPosition)
    ax9.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["S1_ActualPosition"].plot(figsize=(10,10),color="darkgrey",ax=ax9,linestyle='--')
    timeseries["S1_CommandPosition"].plot(figsize=(10,10),color="gold",ax=ax9)
    
    #Variables plotted in 10th axes
    #S1_ActualVelocity: actual velocity of spindle (mm/s)
    #S1_CommandVelocity: reference velocity of spindle (mm/s)
    min_S_ActualVelocity = 0
    max_S_ActualVelocity = 54
    ax10.set_ylim(min_S_ActualVelocity,max_S_ActualVelocity)
    ax10.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["S1_ActualVelocity"].plot(figsize=(10,10),color="darkgrey",ax=ax10,linestyle='--')
    timeseries["S1_CommandVelocity"].plot(figsize=(10,10),color="gold",ax=ax10)

    #Variables plotted in 11th axis
    #S1_ActualAcceleration: actual acceleration of spindle (mm/s/s)
    #S1_CommandAcceleration: reference acceleration of spindle (mm/s/s)
    min_S_ActualAcceleration = -125
    max_S_ActualAcceleration = 125
    ax11.set_ylim(min_S_ActualAcceleration,max_S_ActualAcceleration)
    ax11.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["S1_ActualAcceleration"].plot(figsize=(10,10),color="darkgrey",ax=ax11,linestyle='--')
    timeseries["S1_CommandAcceleration"].plot(figsize=(10,10),color="gold",ax=ax11)


    #Variables plotted in 12th axis
    #S1_CurrentFeedback: current (A)
    min_S_CurrentFeedback = -10
    max_S_CurrentFeedback = 80
    ax12.set_ylim(min_S_CurrentFeedback,max_S_CurrentFeedback)
    ax12.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["S1_CurrentFeedback"].plot(figsize=(10,10),color="gold",ax=ax12)

    #Variables plotted in 13th axis
    #S1_DCBusVoltage: voltage (V)
    min_S1_DCBusVoltage = 0
    max_S1_DCBusVoltage = 3.5
    ax13.set_ylim(min_S1_DCBusVoltage,max_S1_DCBusVoltage)
    ax13.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["S1_DCBusVoltage"].plot(figsize=(10,10),color="gold",ax=ax13)


    #Variables plotted in 14th axis
    #S1_OutputCurrent: current (A)
    min_S1_OutputCurrent = 300
    max_S1_OutputCurrent = 330
    ax14.set_ylim(min_S1_OutputCurrent,max_S1_OutputCurrent)
    ax14.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["S1_OutputCurrent"].plot(figsize=(10,10),color="gold",ax=ax14)


    #Variables plotted in 15th axis
    #S1_OutputVoltage: voltage (V)
    min_S1_OutputVoltage = 0
    max_S1_OutputVoltage = 128
    ax15.set_ylim(min_S1_OutputVoltage,max_S1_OutputVoltage)
    ax15.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["S1_OutputVoltage"].plot(figsize=(10,10),color="gold",ax=ax15)

    #Variables plotted in 16th axis
    #S1_OutputPower: current (A)
    min_S1_OutputPower = 0
    max_S1_OutputPower = 1
    ax16.set_ylim(min_S1_OutputPower,max_S1_OutputPower)
    ax16.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["S1_OutputPower"].plot(figsize=(10,10),color="gold",ax=ax16)

    #Variables plotted in 17th axis
    #S1_SystemInertia: torque inertia (kg*m^2)
    min_S1_SystemInertia = 0
    max_S1_SystemInertia = 20
    ax17.set_ylim(min_S1_SystemInertia,max_S1_SystemInertia)
    ax17.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["S1_SystemInertia"].plot(figsize=(10,10),color="gold",ax=ax17)


    #Variables plotted in 18th axis
    #M1_CURRENT_FEEDRATE: instantaneous feed rate of spindle
    min_M1_CURRENT_FEEDRATE = 0
    max_M1_CURRENT_FEEDRATE = 150
    ax18.set_ylim(min_M1_CURRENT_FEEDRATE,max_M1_CURRENT_FEEDRATE)
    ax18.set_xlim(0,SECONDS_TO_DISPLAY)
    timeseries["M1_CURRENT_FEEDRATE"].plot(figsize=(10,10),color="gold",ax=ax18)


    ax1.axis('off')
    ax2.axis('off')
    ax3.axis('off')
    ax4.axis('off')
    ax5.axis('off')
    ax6.axis('off')
    ax7.axis('off')
    ax8.axis('off')
    ax9.axis('off')
    ax10.axis('off')
    ax11.axis('off')
    ax12.axis('off')
    ax13.axis('off')
    ax14.axis('off')
    ax15.axis('off')
    ax16.axis('off')
    ax17.axis('off')
    ax18.axis('off')
   

    #add_patch_to_plot(ax1 , 40, 80)

    fig.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)

    anim = animation.FuncAnimation(fig,move_x,interval=100,frames=1000)
    plt.axis('off')
    plt.show()
    #anim.save('experiment_01.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

generateVideoFromTimeSeries("./input/CNC_Milling_Wear/experiment_06.csv")