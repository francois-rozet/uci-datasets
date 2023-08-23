# UCI datasets

This repository is a lightweight fork of [gpapamak/maf](https://github.com/gpapamak/maf) meant to download and process the UCI datasets of the MAF paper.

> G. Papamakarios, T. Pavlakou and I. Murray, _Masked Autoregressive Flow for Density Estimation_, NeurIPS 2017 </br>
> https://arxiv.org/abs/1705.07057

## Getting started

1. Clone the `uci-datasets` repository.
2. Download the datasets from https://zenodo.org/record/1161203.
3. Unpack the archive.
4. Process and save the datasets as `.npy` files. This step requires `h5py` and `pandas<2.0` to be installed.
5. Enjoy!

```console
user@device:~ $ git clone https://github.com/francois-rozet/uci-datasets
user@device:~ $ cd uci-datasets
user@device:~/uci-datasets $ wget https://zenodo.org/record/1161203/files/data.tar.gz
user@device:~/uci-datasets $ tar -xzf data.tar.gz
user@device:~/uci-datasets $ python process.py
```

## Datasets

All datasets are processed versions of public datasets.

| Dataset   | URL |
|:---------:|:----|
| POWER     | https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption |
| GAS       | https://archive.ics.uci.edu/ml/datasets/Gas+sensor+array+under+dynamic+gas+mixtures |
| HEPMASS   | https://archive.ics.uci.edu/ml/datasets/HEPMASS |
| MINIBOONE | https://archive.ics.uci.edu/ml/datasets/MiniBooNE+particle+identification |
| BSDS300   | https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/ |
