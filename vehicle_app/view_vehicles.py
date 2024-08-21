"""Contains code to view all vehicles in the database."""
import streamlit as st
import pandas as pd
import os
import base64


def open_image(path: str):
    with open(path, "rb") as p:
        image = p.read()
        return f"""data:image/jpg;base64,{base64.b64encode(image).decode("utf-8")}"""


def view_vehicles():
    st.title("Vehicules Disponibles")
    if not os.path.exists("vehicle_data.csv"):
        st.error("No vehicles found")
    else:
        all_info = pd.read_csv("vehicle_data.csv")
        if all_info.empty:
            st.error("No vehicles found")

    data = all_info.copy()
    # preprocess the data
    data["Year"] = data["Year"].astype(int)
    data.drop("ID", axis=1, inplace=True)
    # processing the image
    data["Image_encoded"] = data.apply(lambda x: open_image(x["Image"]), axis=1)
    data.drop("Image", axis=1, inplace=True)
    data.rename(
        columns={
            "Name": "Nom",
            "Type": "Type",
            "Fuel": "Carburant",
            "Km": "Kilométrage",
            "Year": "Année",
            "Price": "Prix",
            "Image_encoded": "Image",
        },
        inplace=True,
    )
    # re-order the columns
    data = data[
        [
            "Nom",
            "Type",
            "Carburant",
            "Kilométrage",
            "Année",
            "Prix",
            "Image",
        ]
    ]

    # display dataframe
    selected_vehicle = st.dataframe(
        data,
        on_select="rerun",
        use_container_width=True,
        hide_index=True,
        column_config={"Image": st.column_config.ImageColumn()},
        selection_mode="single-row",
    )
    if len(selected_vehicle.selection.rows) > 0:
        left, right = st.columns([2, 2], vertical_alignment="center")
        left.image(all_info.iloc[selected_vehicle.selection.rows[0]]["Image"], width=300)
        right.markdown(f"""**Propriétaire** :{all_info.iloc[selected_vehicle.selection.rows[0]]["Owner"]}""")
        right.markdown(f"""**Numéro de Téléphone du Propriétaire** :{all_info.iloc[selected_vehicle.selection.rows[0]]["Phone"]}""")
        right.markdown(f"""**Kilométrage** :{all_info.iloc[selected_vehicle.selection.rows[0]]["Name"]}""")
        right.markdown(f"""**Année** :{all_info.iloc[selected_vehicle.selection.rows[0]]["Year"]}""")
        right.markdown(f"""**Prix** :{all_info.iloc[selected_vehicle.selection.rows[0]]["Price"]}""")
        right.markdown(f"""**Carburant** :{all_info.iloc[selected_vehicle.selection.rows[0]]["Fuel"]}""")
        right.markdown(f"""**Type** :{all_info.iloc[selected_vehicle.selection.rows[0]]["Type"]}""")
        right.markdown(f"""**Description** :{all_info.iloc[selected_vehicle.selection.rows[0]]["Description"]}""")

view_vehicles()