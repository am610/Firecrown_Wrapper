# Program to convert the SNANA format HD outputs to cosmoMC HD format
# Ayan Mitra @ 2022

import sys
import pandas as pd
import numpy as np

col = [
    "#name",
    "zcmb",
    "zhel",
    "dz",
    "mb",
    "dmb",
    "x1",
    "dx1",
    "color",
    "dcolor",
    "3rdvar",
    "d3rdvar",
    "cov_m_s",
    "cov_m_c",
    "cov_s_c",
    "set",
    "ra",
    "dec",
    "biascor",
]


input = sys.argv[1]
# /scratch/midway2/rkessler/PIPPIN_OUTPUT/PLASTICC_COMBINED/7_CREATE_COV/LSST_BINNED_COV_BBC_SIMDATA_PHOTOZ_11/output/hubble_diagram.txt


h = pd.read_csv(input, sep="\s+", comment="#")
h = h.iloc[:, 1:-1]

h.MU -= 19.36  # (h.MU[0]-d.mb[0])

h.insert(3, "dz", np.zeros(np.shape(h)[0]))
row = np.shape(h)[0]
# (np.zeros(np.shape(h)[0]))
colu = 13
# np.shape(d)[1] - np.shape(h)[1]
# join = pd.DataFrame(np.array([row,colu]))

join = np.zeros((row, colu))
hh = pd.DataFrame(np.concatenate([h, join], axis=1))

hh.columns = col
h = hh
h["#name"] = np.linspace(0, np.shape(h)[0] - 1, np.shape(h)[0]).astype(int)
h.to_csv("data.txt", sep=" ", index=None)


def conversion(h):
    h = h.iloc[:, 1:-1]
    h.MU -= 19.36
    h.insert(3, "dz", np.zeros(np.shape(h)[0]))
    row = np.shape(h)[0]
    colu = 13
    join = np.zeros((row, colu))
    hh = pd.DataFrame(np.concatenate([h, join], axis=1))
    hh.columns = col
    h = hh
    h["#name"] = np.linspace(0, np.shape(h)[0] - 1, np.shape(h)[0]).astype(int)
    return h
