import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st. set_page_config(layout="wide")
st.divider()
st.subheader('Todos os artistas')
st.divider()
col1, col2 = st.columns(2)

df = pd.read_csv('spotify-2023.csv', encoding='latin1')
df = df[["artist(s)_name", 'released_year', "track_name", "streams", "in_spotify_playlists",]]

# !@$ o edison lighthouse sem nenhum motivo especifico
df = df[df['artist(s)_name'] != 'Edison Lighthouse']
df = df.sort_values("streams", ascending=False)

fig_char = px.bar(df, x='artist(s)_name', y="streams", color="in_spotify_playlists", title="streams anuais", width=2000, height=500)
fig_char.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

fig_date = px.pie(df, values="track_name", names="released_year", title="Ano de lancamento das musicas")

col1.plotly_chart(fig_char, use_container_width=True)
col2.plotly_chart(fig_date, use_container_width=True)

st.dataframe(
    df, 
    width = 999999, 
    hide_index=True,
)

st.divider()
st.subheader('Busca por artista especifico')
st.divider()

options = st.selectbox(
    "Artista",
    df['artist(s)_name'].unique(),
)

if st.button('Pesquisar Artista'):
    df_filtered = df[df['artist(s)_name'] == options]

    st.dataframe(
        df_filtered,
        width = 999999, 
        hide_index=True,)
    
    fig_charf = px.bar(df_filtered, x='track_name', y="streams", color="in_spotify_playlists", title="streams anuais", width=2000, height=500)
    fig_charf.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    col3, col4 = st.columns(2)
    col3.plotly_chart(fig_charf, use_container_width=True)

st.divider()