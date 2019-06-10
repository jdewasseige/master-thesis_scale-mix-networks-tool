#!/usr/bin/env python

#############################################
###############
############### Tool for designing and scaling mix networks given some input characteristics.
###############
############### MASTER THESIS
###############     AUTHOR : JOHN DE WASSEIGE
###############     TITLE  : SYNCHRONOUS MIX NETWORKS FOR ANONYMOUS WEB COMMUNICATION
###############
#############################################

### MODULES ###
from __future__ import print_function

import sys
import os
import argparse
import math
import numpy as np

import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt

### CONSTANTS ###
Bsend = 1 # kB
Bresp = 50 # kB
Lmix = 5e-3 # seconds

### ARGUMENTS ###
parser = argparse.ArgumentParser(description="Simulate mix environment")
# number of users
parser.add_argument('-u', '--nbusers', default=400, type=int,  help="number of users per second")
# number of mixes
parser.add_argument('-n', '--nbmixes', default=4, type=int, help="total number of mixes available")
# number of layers
parser.add_argument('-l', '--nblayers', default=2, type=int, help="number of layers")
# latency added by every mix
parser.add_argument('-tl', '--mixlatency', default=1, type=float, help="latency added by mix")
# latency of server to compute the response
parser.add_argument('-ts', '--serverlatency', default=1, type=float, help="time for server to process request")
# split factor [not implemented yet]
parser.add_argument('-s', '--splitfactor', default=1, type=int, help="split factor of server response")
args = parser.parse_args()


# use replacement values
N = args.nbusers
n = args.nbmixes
l = args.nblayers
tl = args.mixlatency
ts = args.serverlatency

# set number of mixes per layers w
w = int(np.floor(n/l))
T = 2*l*tl + ts

### SUMMARY INPUTS ###
print("Summary of inputs\n-------")
print("nb users :\t\t\t", N)
print("nb mixes :\t\t\t", n)
print("nb layers :\t\t\t", l)
print("latency added by mix :\t\t", tl)
print("server time to respond :\t", ts)
print("")

### TYPES OF TOPOLOGIES
print("(F) = free route")
print("(C) = cascade")
print("(S) = free route")

### NUMBER OF PATH ###
nb_path_free = n
for i in range(1,l):
    nb_path_free *= n-i
nb_path_casc = w
nb_path_strat = w**l

print("(F) number paths = ", nb_path_free)
print("(C) number paths = ", nb_path_casc)
print("(S) number paths = ", nb_path_strat)
print("")

### ENTROPY ###
entropy_free = -n*(1/n)*np.log2(1/n)
entropy_casc = -w*(1/w)*np.log2(1/w)
entropy_strat = -n*(1/w)*np.log2(1/w)

print("(F) entropy = ", entropy_free)
print("(C) entropy = ", entropy_casc)
print("(S) entropy = ", entropy_strat)
print("")

### DUMMIES ###
Dmin = (max(T/tl, w)-1)*N*l
Dmax = (T/tl - 1)*w*N*l

Ntotmin = N + Dmin
Ntotmax = N + Dmax

### BANDWIDTH ###
b_send_min = round(Ntotmin*Bsend/100, 2)
b_resp_min = round(Ntotmin*Bresp/1000,2)

print("min bandwidth per relay [sending] = \t", b_send_min, "MB/s")
print("min bandwidth per relay [receiving] = \t", b_resp_min, "MB/s")

b_send_max = round(Ntotmax*Bsend/100, 2)
b_resp_max = round(Ntotmax*Bresp/1000,2)

print("adv. bandwidth per relay [sending] = \t", b_send_max, "MB/s")
print("adv. bandwidth per relay [receiving] = \t", b_resp_max, "MB/s")
print("")

### ROBUSTNESS ###
mess_path_free = int(N/nb_path_free)
mess_path_casc = int(N/nb_path_casc)
mess_path_strat = int(N/nb_path_strat)

print("anon. set when user-server obs. = ", N*T)
print("")

print("(F) anon. set when (l-1) compromised = ", mess_path_free)
print("(C) anon. set when (l-1) compromised = ", mess_path_casc)
print("(S) anon. set when (l-1) compromised = ", mess_path_strat)


## Types of relays and their bandwidth
# vfOR = 500e6 # bits
# fOR = 200e6 # bits
# nOR = 50e6 # bits
# sOR = 10e6 # bits
