# Derek Eells
# I2C Wideband Readout

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.garden.graph import Graph, SmoothLinePlot
from threading import Thread
#from collections import deque

def i2cWorker():
  # I2C data gatherer
  print('Starting I2C Worker')
  while True:
    #read that i2c data boiiiii
    print('poop')

class WidebandWidget(Widget):
  h = NumericProperty(0)
  r = StringProperty("14.7")
  hist_t = [(t/60.0) for t in range(0,601)]
  #print(hist_t)
  hist_v = [(14.7) for v in range(0,601)]
  #print(hist_v)
  hist = zip(hist_t, hist_v)
  # print(hist)
  test = 1

  def __init__(self,):
    super(WidebandWidget, self).__init__()
    self.p = SmoothLinePlot(color=[1, 1, 1, 1])
    self.ids.graph.add_plot(self.p)


  def update(self, dT):
    # This could be conviently centered around the green value
    # and then some abs bullshit could be used to make it go red in both directions
    self.h = self.ids.s1.value * .0497 - .3976
    self.r = str(self.ids.s1.value)

    # Updating graph
    self.hist_v.pop(0)
    self.hist_v.append(self.ids.s1.value)
    self.hist = zip(self.hist_t, self.hist_v)
    # if (self.test >= 1):
    #   self.test = 1
    # self.test += 1.0/10.0
    # if(len(self.hist) >= 10):
    #self.hist.pop(0)
    #self.hist.append((self.test, self.ids.s1.value))
    self.p.points = self.hist
    

class WidebandApp(App):
  def build(self):
    widget = WidebandWidget()
    Clock.schedule_interval(widget.update, 1.0/60.0)
    return widget

if __name__ == '__main__':
  WidebandApp().run()
