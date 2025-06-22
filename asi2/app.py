import pandas as pd
import streamlit as st
from datetime import datetime
from kedro.framework.session import KedroSession
from kedro.framework.project import configure_project
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent / "src"))

df = pd.read_csv("data/01_raw/vehicles_short.csv", nrows=15000)
#df.to_csv("data/01_raw/vehicles_short.csv", sep=",", index=False)

project_path = Path.cwd()
package_name = "asi2"
configure_project(package_name)
with KedroSession.create(project_path=project_path) as session:
    context = session.load_context()
    predictor = context.catalog.load("predictors")


def start_prediction():
    entered_data = {
        'year': st.session_state.year,
        'manufacturer': st.session_state.manufacturer,
        'model': st.session_state.model,
        'condition': st.session_state.condition,
        'cylinders': st.session_state.cylinders,
        'fuel': st.session_state.fuel,
        'odometer': st.session_state.odometer,
        'title_status': st.session_state.title_status,
        'transmission': st.session_state.transmission,
        'drive': st.session_state.drive,
        'size': st.session_state.size,
        'type': st.session_state.type,
        'paint_color': st.session_state.paint_color,
        'state': st.session_state.state
    }
    entered_df = pd.DataFrame([entered_data])
    with st.spinner("Calculating car price..."):
        result = predictor.predict(entered_df)
    st.info("Predicted car price is " + str(round(result.values[0], 2)) + " USD")

st.title("Car Price Predictor")
with st.form("car"):
    st.subheader("Enter car data:")
    st.number_input("Year of manufacture:", min_value=1950, max_value=datetime.now().year, key="year")
    st.text_input("Manufacturer:", key="manufacturer")
    st.text_input("Model:", key="model")
    st.selectbox("Condition:", options=df['condition'].unique()[1:], key="condition")
    st.selectbox("Cylinders:", options=df['cylinders'].unique()[1:], key="cylinders")
    st.selectbox("Fuel:", options=df['fuel'].unique()[1:], key="fuel")
    st.number_input("Odometer value:", min_value=0, max_value=1000000, key="odometer")
    st.selectbox("Title status:", options=df['title_status'].unique()[1:], key="title_status")
    st.selectbox("Transmission:", options=df['transmission'].unique()[1:], key="transmission")
    st.selectbox("Drive:", options=df['drive'].unique()[1:], key="drive")
    st.selectbox("Size:", options=df['size'].unique()[1:], key="size")
    st.selectbox("Type:", options=df['type'].unique()[1:], key="type")
    st.selectbox("Paint color:", options=df['paint_color'].unique()[1:], key="paint_color")
    st.selectbox("US State:", options=df['state'].unique()[1:], key="state")
    st.form_submit_button("Predict my price", on_click=start_prediction)
# ℹ️ Sidebar info
st.sidebar.header("ℹ️ O aplikacji")
st.sidebar.write("""
Aplikacja wykorzystuje model AI (AutoGluon), który analizuje dane techniczne pojazdu 
i przewiduje jego wartość rynkową.
""")