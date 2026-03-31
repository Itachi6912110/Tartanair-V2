'''
Author: Yorai Shaoul
Date: 2023-02-03

Example script for downloading using the TartanAir dataset toolbox.
'''

# General imports.
import sys

# Local imports.
sys.path.append(0, '..')
import tartanair as ta

# Create a TartanAir object.
tartanair_data_root = 'datasets/Tartanair-V2'

ta.init(tartanair_data_root)

# List available trajectories.
ta.visualize('SoulCity', 
              difficulty='easy', 
              trajectory_id = 'P003', 
              modality = ['image', 'depth'], 
              camera_name = ['lcam_front'])