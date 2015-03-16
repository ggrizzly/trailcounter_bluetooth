#!/usr/bin/env python

import sys
import scipy.io

weightdat = scipy.io.loadmat(sys.argv[1])
template = scipy.io.loadmat(sys.argv[2])
unit_num = int(sys.argv[3])
wf = template['TIME_sampled_auto']

weightsIW = weightdat['weightsIW']
weightsLW = weightdat['weightsLW']

weights_ih = weightsIW[0,unit_num]
weights_ho = weightsLW[0,unit_num]

(hidden_neurons, hidden_neuron_inputs) = weights_ih.shape
(output_neurons, output_neuron_inputs) = weights_ho.shape

hidden_output = []
for neuron in range(hidden_neurons):
    sum = 0
    rc = hidden_neuron_inputs - 1
    for ninput in range(hidden_neuron_inputs):
        sum = sum + wf[rc,unit_num] * weights_ih[neuron,ninput]      
        rc = rc - 1 
    if (sum > 1):
        sum = 1
    if (sum < 0):
        sum = 0 
    hidden_output.append(sum)
    
network_output = 0
for ninput in range(output_neuron_inputs):
    network_output = network_output + hidden_output[ninput] * weights_ho[0,ninput]
print network_output
if (network_output > 1):
    network_output = 1
elif (network_output < 0):
    network_output = 0
print network_output








