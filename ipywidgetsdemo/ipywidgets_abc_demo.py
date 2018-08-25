
# coding: utf-8

# # ipywidgets ABC demo
# - Update an output widget with the sum of two input widgets when the 'change' event fires

# In[1]:


# https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html
# https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html
from ipywidgets import interact
import ipywidgets as widgets
def add(x, y):
    return sum((x,y))
widget_x = widgets.IntText(value=0, description='#1')
widget_y = widgets.IntText(value=0, description='#2')
interact(add, x=widget_x, y=widget_y)


# In[2]:


# https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Events.html#Registering-callbacks-to-trait-changes-in-the-kernel
from IPython.display import display
from ipywidgets import interact
import ipywidgets as widgets

widget_x = widgets.IntText(value=0, description='#1')
widget_y = widgets.IntText(value=0, description='#2')
widget_sigma = widgets.IntText(value=0, description='sum')

def add_event(event):
    widget_sigma.value = sum((widget_x.value, widget_y.value))
    
widget_x.observe(add_event, names='value')
widget_y.observe(add_event, names='value')

display(widgets.HBox([widget_x, widget_y, widget_sigma]))

