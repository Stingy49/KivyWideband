# Derek Eells
# I2C Wideband Readout
# March 2017

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.garden.graph import Graph, SmoothLinePlot
from threading import Thread
import smbus
from time import sleep

afr = 0

def i2cWorker():
  # I2C data gatherer
  # I figured I could use a seperate thread to gather my i2c data to prevent possible UI hangups
  # Obviously I haven't implemented this code yet
  print('Starting I2C Worker')

  global afr
  bus = smbus.SMBus(1)
  DEVICE_ADDRESS = 0x10
  MEMORY_ADDRESS = 0x23
  result = [0x00, 0x00, 0x00, 0x00]
  afr_avg = [0, 0, 0, 0, 0, 0]

  while True:
    #read that i2c data boiiiii
    #result = bus.read_block_data(DEVICE_ADDRESS, MEMORY_ADDRESS)
    try:
      result = bus.read_i2c_block_data(DEVICE_ADDRESS, MEMORY_ADDRESS, 3)
      #result[0] = bus.read_byte_data(DEVICE_ADDRESS, MEMORY_ADDRESS)
      #result[1] = bus.read_byte(DEVICE_ADDRESS)
    except:
      pass
    afr = float(result[0]<<8 | result[1])
    #afr = float(result[0]<<24 | result[1]<<16 | result[2]<<8 | result[3])
    #afr2 = float(result[3]<<24 | result[2]<<16 | result[1]<<8 | result[0])
    afr = afr*14.7*.005
    afr_avg.pop(0)
    afr_avg.append(afr)
    afr = 0
    for x in range(0,len(afr_avg)):
      afr += afr_avg[x]/len(afr_avg)
    # print(result)
    # print("Threaded AFR:")
    # print(afr)
    # print(afr2)
    sleep(.016)

class WidebandWidget(Widget):
  # Kivy property types
  h = NumericProperty(0)
  r = StringProperty("14.7")
  # Generateing the two arrays for the graph (NOTE: This should be moved to the i2c thread when it exists)
  # Also whenever the refresh rate or data persistence length is changed, these initializations change
  hist_t = [(t/60.0) for t in range(0,601)]
  hist_v = [(14.7) for v in range(0,601)]
  # Creating the array of tuples for kivy graph
  hist = zip(hist_t, hist_v)

  # bus = smbus.SMBus(1)
  # DEVICE_ADDRESS = 0x10
  # MEMORY_ADDRESS = 0x23
  # result = [0x00, 0x00]
  # afr = 0

  # For some reason the plot has to be initialized this way
  def __init__(self,):
    super(WidebandWidget, self).__init__()
    self.p = SmoothLinePlot(color=[1, 1, 1, 1])
    self.ids.graph.add_plot(self.p)


  def update(self, dT):
    # AFR Global variable
    global afr
    # try:
    #   self.result[0] = self.bus.read_byte_data(self.DEVICE_ADDRESS, self.MEMORY_ADDRESS)
    #   self.result[1] = self.bus.read_byte(self.DEVICE_ADDRESS)
    # except:
    #   self.result = [0x00, 0x00]
    # self.afr = (self.result[0]<<8 | self.result[1])*.005*14.7
    # print(self.afr)

    # print("App AFR:")
    # print(afr)

    # This could be conviently centered around the ideal green value
    # and then some abs value bullshit could be used to make it go red in both directions
    self.h = afr * .0497 - .3976
    self.r = '{:.4}'.format(str(afr))

    # Updating graph
    self.hist_v.pop(0)
    self.hist_v.append(afr)
    self.hist = zip(self.hist_t, self.hist_v)
    self.p.points = self.hist
    

class WidebandApp(App):
  def build(self):
    widget = WidebandWidget()
    Clock.schedule_interval(widget.update, 1.0/60.0)
    return widget

if __name__ == '__main__':
  i2c_thread = Thread(target = i2cWorker)
  i2c_thread.daemon = True
  i2c_thread.start()
  WidebandApp().run()
