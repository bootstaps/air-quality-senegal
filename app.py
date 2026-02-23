import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("Moniteur de Capteurs Régionaux")

# 1. Simuler ou récupérer les données (Normalement via API)
data = {
    'Region': ['Dakar', 'Saint-Louis', 'Ziguinchor'],
    'lat': [14.7167, 16.0333, 12.5833],
    'lon': [-17.4677, -16.5, -16.2719],
    'PM25': [25, 12, 5] # Données du capteur
}
df = pd.DataFrame(data)

# 2. Créer la carte
m = folium.Map(location=[14.4974, -14.4524], zoom_start=7)

# 3. Ajouter les capteurs sur la carte
for index, row in df.iterrows():
    folium.Marker(
        [row['lat'], row['lon']],
        popup=f"Région: {row['Region']} - PM2.5: {row['PM25']}",
        tooltip="Cliquez pour voir les données"
    ).add_to(m)

# Affichage
st_folium(m, width=700)