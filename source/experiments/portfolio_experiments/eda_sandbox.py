# Set up notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

home_directory = "C:/Users/rober/DataspellProjects/Machine-Learning-Sandbox"

wowah_data = pd.read_csv(
    filepath_or_buffer=home_directory + "/data/02_world_of_warcraft/avatar_history/wowah_data.csv"
)
zones = pd.read_csv(
    filepath_or_buffer=home_directory + "/data/02_world_of_warcraft/avatar_history/zones.csv"
)
location_coords = pd.read_csv(
    filepath_or_buffer=home_directory +
                       "/data/02_world_of_warcraft/avatar_history/location_coords.csv"
)
locations = pd.read_csv(
    filepath_or_buffer=home_directory + "/data/02_world_of_warcraft/avatar_history/locations.csv"
)

print(sorted(zones["Zone_Name"].unique()))

print(1)