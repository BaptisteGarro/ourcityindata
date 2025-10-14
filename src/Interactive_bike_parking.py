# Analysis bike parkings
## Preprocessing
import pandas as pd
import geopandas as gpd
import json
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_folium import st_folium
#import folium

gdf_results = gpd.read_file("bike_locks_analysis.json")

analysis = st.sidebar.selectbox(
    "What analysis do you want to see?",
    ("Bike locks per living space", "Bike locks per block", "Living space per block")
)

# Interactive plots
if analysis == "Bike locks per living space":
    st_folium(gdf_results.explore(
        column="log_bike_locks_per_living", 
        tooltip=["bike_locks", "living_space", "bike_locks_per_living"],
    ), width=1000, height= 600)
elif analysis == "Bike locks per block":
    st_folium(gdf_results.explore(
        column="log_bike_locks", 
        tooltip=["bike_locks", "living_space", "bike_locks_per_living"],
    ), width=1000, height= 600)
else:
    st_folium(gdf_results.explore(
        column="log_living_space", 
        tooltip=["bike_locks", "living_space", "bike_locks_per_living"],
    ), width=1000, height= 600)