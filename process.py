#!/usr/bin/env python

import numpy as np
import datasets


for cls in [
    datasets.POWER,
    datasets.GAS,
    datasets.HEPMASS,
    datasets.MINIBOONE,
    datasets.BSDS300,
]:
    name = cls.__name__
    dataset = cls()
    data = np.concatenate((
        dataset.trn.x,
        dataset.val.x,
        dataset.tst.x,
    ))

    np.save(f'{name}.npy', data)
