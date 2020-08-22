#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# set the module
import nibabel as nib
from glob import glob
import numpy as np
import os
import shutil
import argparse

# HELP Section
parser = argparse.ArgumentParser(description='## Automatic DICOM converting script ##', formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog='''\
version history:
    [ver0.10]       release of this script (2020.08.22)

++ Copyright at uschoi@nict.go.jp / qtwing@naver.com ++
''')

parser.add_argument('--version', action='version', version='Version 0.1')
parser.parse_args()

## assign input arguments
print("")
print(" <<<<  Welcome to dcmConvert >>>> ")
print("")
dir_path = str(input('++ Enter the path of dicom file directory:  '))
print("")

## unlimit
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (8192, 9223372036854775807))

## change directory
os.chdir(dir_path)

## convert dicom files to nifti format
path_current = os.getcwd()
os.system('mkdir -p ./dcmConvertFiles')
# set paths
path_nii = path_current + '/dcmConvertFiles'
path_dcm = path_current
# run dcm2niix
dcm2niix_command = 'dcm2niix -o ' + path_nii + ' -f %p_%s ' + path_dcm
os.system(dcm2niix_command)

## extract unique file prefix
path_n = 'dcmConvertFiles/*.nii'
fnames = glob(path_n)

uni_fname_tmp = []
for fn in fnames:
    fname_tmp1 = fn.rsplit("_", 1)[0]
    fname_tmp2 = fname_tmp1.rsplit("/",1)[1]
    uni_fname_tmp.append(fname_tmp2)
# unique file name list
uni_fname = list(set(uni_fname_tmp))

## merge multiple nii files to single nii file
for uni_fn in uni_fname:
    path_x = 'dcmConvertFiles/' + uni_fn + '_*.nii'
    spe_fnames = glob(path_x)
    # print(spe_fnames)
    imgs = [nib.load(spe_fn) for spe_fn in spe_fnames]
    img_data = np.stack([img.dataobj for img in imgs], axis=-1)
    converted = nib.Nifti1Image(img_data, imgs[0].affine, imgs[0].header)
    merg_fname = uni_fn + '.nii.gz'
    converted.to_filename(merg_fname)

## greeting
print("")
print(" <<<<  Thank you for using dcmConvert >>>> ")
print("")
##
