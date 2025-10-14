# -*- coding: utf-8 -*-
import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
import folium
import streamlit.components.v1 as components

# --- Configuración de la app ---
st.set_page_config(page_title="Dashboard Turístico Bolivia", layout="wide")
st.title("📊 Dashboard Turístico Interactivo de Bolivia")

st.markdown("""
Explora los atractivos y actividades turísticas por tipo, región y categoría. 
Filtra, visualiza y analiza los datos geoespaciales de Bolivia. 
Además, accede a mapas temáticos cargados desde Google Drive.
""")

# --- Cargar datos ---
# --- Cargar datos ---
bo = gpd.read_file("data/municipios339.shp")
bo_ap = gpd.read_file("data/mmaya_aps.shp")
bo_gr = gpd.read_file("data/grandes_regiones.shp")
bo_pio = gpd.read_file("data/indigena.shp")
bo_act = gpd.read_file("data/Mapa de actividades turisticas de Bolivia_2012.json")
bo_atr = gpd.read_file("data/atractivos_turisticos_bolivia_2024.geojson.json")
bo_atr2 = pd.read_csv("data/atractivos_turisticos2012 - atractivos_turisticos.csv")


# --- Filtros ---
st.sidebar.header("🎛️ Filtros")

tipos_vocacion = bo_atr['vocaciÓn'].dropna().unique()
vocacion_seleccionada = st.sidebar.multiselect("Tipo de vocación turística", tipos_vocacion, default=tipos_vocacion)

tipos_actividad = bo_act['tipo_activ'].dropna().unique()
actividad_seleccionada = st.sidebar.multiselect("Tipo de actividad turística", tipos_actividad, default=tipos_actividad)

# --- Filtrar datos ---
atr_filtrados = bo_atr[bo_atr['vocaciÓn'].isin(vocacion_seleccionada)]
act_filtradas = bo_act[bo_act['tipo_activ'].isin(actividad_seleccionada)]

# --- Gráfico comparativo por región ---
st.subheader("📍 Atractivos turísticos por región")
bo_atr_reg = gpd.sjoin(atr_filtrados, bo_gr, how='left', predicate='intersects')
conteo_por_region = bo_atr_reg['region'].value_counts()

fig, ax = plt.subplots()
conteo_por_region.plot(kind='barh', ax=ax, color='skyblue', edgecolor='black')
ax.set_xlabel("Cantidad de atractivos")
ax.set_ylabel("Región")
st.pyplot(fig)

# --- Mapas HTML desde Google Drive ---
st.subheader("🗺️ Mapas Temáticos Interactivos")
st.markdown("Los siguientes mapas están alojados en Google Drive para facilitar su visualización en línea.")

# Mapa 1: Municipios coloreados
st.markdown("### 📍 Mapa de Municipios Coloreados")
components.iframe("https://drive.google.com/file/d/1lyhBDiIAMchtzDUSpMlUyGzGTjiC70Cj/preview", height=600)

# Mapa 2: Pueblos Indígenas
st.markdown("### 🧑🏽‍🌾 Mapa de Pueblos Indígenas u Originarios")
components.iframe("https://drive.google.com/file/d/1w-JytBcsp_T-0RLI6MIJ2OQukT4zNYU1/preview", height=600)

# Mapa 3: Mapa Turístico General
st.markdown("### 🌄 Mapa Turístico Interactivo 2024")
components.iframe("https://drive.google.com/file/d/1HWzfH5J_fGFoxWrmH4Y4xDlmSSzyz3Rj/preview", height=600)
