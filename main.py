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

def i2cWorker():
  # I2C data gatherer
  # I figured I could use a seperate thread to gather my i2c data to prevent possible UI hangups
  # Obviously I haven't implemented this code yet
  print('Starting I2C Worker')
  while True:
    #read that i2c data boiiiii
    print('poop')

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

  # For some reason the plot has to be initialized this way
  def __init__(self,):
    super(WidebandWidget, self).__init__()
    self.p = SmoothLinePlot(color=[1, 1, 1, 1])
    self.ids.graph.add_plot(self.p)


  def update(self, dT):
    # This could be conviently centered around the ideal green value
    # and then some abs value bullshit could be used to make it go red in both directions
    self.h = self.ids.s1.value * .0497 - .3976
    self.r = str(self.ids.s1.value)

    # Updating graph
    self.hist_v.pop(0)
    self.hist_v.append(self.ids.s1.value)
    self.hist = zip(self.hist_t, self.hist_v)
    self.p.points = self.hist
    

class WidebandApp(App):
  def build(self):
    widget = WidebandWidget()
    Clock.schedule_interval(widget.update, 1.0/60.0)
    return widget

if __name__ == '__main__':
  WidebandApp().run()
