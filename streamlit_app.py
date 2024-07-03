import streamlit as st
import httpimport
import mag4 as mg
import pandas as pd
import matplotlib.pyplot as plt

st.title('my Dashboard')

list_df = mg.available_datasets()
#st.write(list_df)

sel_db = st.selectbox('Welche georoc Datei soll geladen werden', list_df)
#st.write(sel_db)
geo_db = pd.DataFrame(mg.get_data(sel_db))

#st.write(geo_db.columns)
elements = geo_db.columns.tolist()[27:]

#st.write(elements)

x_axis = st.selectbox('Wähle das Element für die x Achse', elements)
y_axis = st.selectbox('Wähle das Element für die y Achse', elements)

plt.scatter(geo_db[x_axis], geo_db[y_axis])
st.scatter_chart(data=geo_db, x=x_axis, y=y_axis, x_label=str(x_axis), y_label=str(y_axis), color=None, size=None, width=None, height=None, use_container_width=True)



