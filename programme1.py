#This is a demonstration of how to use ggplot in python

#Import the necessary code library
from ggplot import *

#Preview the diamonds dataset
diamonds[:3]

#Generate a simple scatter diagram of price against carat weight
ggplot(diamonds,aes(x="carat",y="price")) + geom_point()

