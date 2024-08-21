"""Main entrypoint of our streamlit app."""
import streamlit as st
import os
import pandas as pd
import uuid
# create the forms to add vehicles details

def add_vehicle():
    st.title('Ajouter Votre Véhicule')
    vehicle_name = st.text_input('Nom du Véhicule')
    vehicle_owner_name = st.text_input('Nom du Propriétaire')
    vehicle_phone = st.text_input('Numéro de Téléphone')
    vehicle_type = st.selectbox('Type du Véhicule', ['Citadine', "Berline", "SUV", "Coupé", "Cabriolet", "Monospace", "Utilitaire"])
    vehicle_carburant = st.selectbox('Carburant', ['Essence', 'Diesel', 'Hybride', 'Electrique'])
    vehicle_km = st.number_input('Kilométrage', min_value=0)
    vehicle_year = st.number_input('Année de Mise en Circulation', min_value=2000, max_value=2024)
    vehicle_price = st.number_input('Prix en Millions de Centime', min_value=0)
    vehicle_description = st.text_area('Description du Véhicule')
    vehicle_image = st.file_uploader('Image du Véhicule', type=['jpg'])

    if st.button('Add Vehicle'):
        # upload the data saved in a csv file
        if not os.path.exists('vehicle_data.csv'):
            with open('vehicle_data.csv', 'w') as file:
                file.write('ID,Name,Owner,Phone,Type,Km,Year,Price,Description,Image\n')

        # check if images folder exists
        if not os.path.exists('images'):
            os.makedirs('images')

        # generate a unique ID for the vehicle
        vehicle_id = uuid.uuid4()
    
        # create folder with ID as name and save the image
        image_path = os.path.join('images', str(vehicle_id) + '.jpg')
        with open(image_path, 'wb') as file:
            file.write(vehicle_image.read())
        # read the csv file
        all_info = pd.read_csv('vehicle_data.csv')
        # save the vehicle details to a csv file
        vehicle_data = {
            'ID': vehicle_id,
            'Name': vehicle_name,
            'Owner': vehicle_owner_name,
            'Phone': vehicle_phone,
            'Type': vehicle_type,
            'Fuel': vehicle_carburant,
            'Km': vehicle_km,
            'Year': vehicle_year,
            'Price': vehicle_price,
            'Description': vehicle_description,
            'Image': image_path
        }

        all_info = all_info._append(vehicle_data, ignore_index=True)
        all_info.to_csv('vehicle_data.csv', index=False)
        st.success('Vehicle added successfully')

add_vehicle()