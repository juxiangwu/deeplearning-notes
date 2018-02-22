from matplotlib import pyplot
import numpy as np
import time

# These are the droids you are looking for.
from caffe2.python import core, workspace
from caffe2.proto import caffe2_pb2

X = np.random.randn(3, 3)
W = np.random.randn(3, 3)
b = np.ones(3)
Y = X * W.T + b

net = core.Net("my_first_net")
print("Current network proto:\n\n{}".format(net.Proto()))

X = net.GaussianFill([], ["X"], mean=0.0, std=1.0, shape=[3, 3], run_once=0)
print("New network proto:\n\n{}".format(net.Proto()))
W = net.GaussianFill([], ["W"], mean=0.0, std=1.0, shape=[3 ,3], run_once=0)
b = net.ConstantFill([], ["b"], shape=[3,], value=1.0, run_once=0)
print("Current network proto:\n\n{}".format(net.Proto()))

from caffe2.python import net_drawer
from IPython import display
graph = net_drawer.GetPydotGraph(net, rankdir="LR")

#pyplot.imshow(graph.create_png())
#pyplot.show()

