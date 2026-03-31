'''
Author: Zih-Sing Fu
Date: 2026-03-31

Example script for downloading using the TartanAir dataset toolbox for datasets used in GMMap.
'''

# General imports.
import sys

# Local imports.
sys.path.insert(0, '..')
import tartanair as ta

# Create a TartanAir object.
tartanair_data_root = 'datasets/Tartanair-V2'

ta.init(tartanair_data_root)

# Download via a yaml config file.
ta.download(config = 'configs/download_gmmap.yaml')
