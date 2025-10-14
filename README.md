# 🗺️ Mapa Turístico Interactivo de Bolivia

Este proyecto presenta un mapa interactivo de Bolivia que integra múltiples capas geoespaciales relacionadas con el turismo, cultura, medio ambiente y pueblos originarios. Utiliza Python, Folium y Streamlit para visualizar y explorar datos oficiales de manera dinámica.

## 🔍 Contenido del proyecto

- **Mapa interactivo con Folium**: incluye municipios, provincias, departamentos, atractivos turísticos, actividades, áreas protegidas y pueblos indígenas.
- **Visualizaciones comparativas**: gráficos por tipo de turismo, región y municipio.
- **Dashboard interactivo (Streamlit)**: permite filtrar, explorar y visualizar los datos de forma intuitiva.

## 📁 Estructura del repositorio
├── data/ # Archivos geoespaciales (.geojson, .shp, .csv) 
├── mapa_turismo_bolivia.html # Mapa exportado en HTML 
├── dashboard.py # Código del dashboard en Streamlit 
├── Mapas_Turismo_Bo.ipynb # Notebook de desarrollo en Colab 
└── README.md # Este archivo


## 🚀 Cómo ejecutar el dashboard

1. Instala Streamlit si no lo tienes:
   ```bash
   pip install streamlit streamlit-folium geopandas pandas matplotlib
2. Ejecuta el Dashboard
     streamlit run dashboard.py
3. Abre el enlace local que aparece en tu terminal para visualizar el dashboard.

🌐 ¿Quieres compartirlo?
Puedes desplegarlo gratis en Streamlit Community Cloud en solo tres pasos:

Inicia sesión con tu cuenta de GitHub.

Selecciona este repositorio y el archivo dashboard.py.

¡Haz clic en Deploy!

Tu app se actualizará automáticamente cada vez que hagas git push.

📌 Autor
Samir Saba – Explorador de datos geoespaciales, apasionado por el turismo, la visualización y el impacto territorial.
