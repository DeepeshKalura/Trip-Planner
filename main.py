import time
import folium
import streamlit as st
import numpy as np 
import pandas as pd 
from streamlit_folium import folium_static

from app.gmap import extract_locations
from app.gemini import ReGemnini


def draw_map(destination):
    locations = extract_locations(destination) 
    
    if locations == {}:
        st.error("No locations found in the destination. Please use correct spelling or provide a different destination...")
    else:
        st.success("Locations extracted successfully!")
        coordinates = [location for location in locations.values() if location is not None]
        map_center = [sum(coord) / len(coord) for coord in zip(*coordinates)] if coordinates else None

        if map_center:
                mymap = folium.Map(location=map_center, zoom_start=10)
                
                for place_name, loc in locations.items():
                    if loc is not None:
                        folium.Marker(loc, popup=place_name).add_to(mymap)

                folium_static(mymap)
        
def generate_trip_plan(destination, duration, budget):
    
    draw_map(destination=destination) 
    st.success("Trip plan generating.. 🧳")
    travel_planner = ReGemnini(destination=destination, budget=budget, days=duration)

    st.write_stream(travel_planner.on_time_stream_response())


    st.success("Engagement Graph is ready! 🚀")
    columns = []
    for i in range(1, duration + 1):
        columns.append(f"Day {i}")

    chart_data = pd.DataFrame( 
	np.random.randn(20, duration), 
	columns=columns
    )

    st.line_chart(chart_data, )
 
    

def main():
    st.title("🌍 AI-driven Trip Planner")
    st.write(
        """
        This AI-driven Trip Planner helps you plan your next adventure with ease! 
        Simply enter your desired destination, duration of stay, and budget in the sidebar, 
        and let our AI algorithm generate a personalized trip plan for you.
        """
    )

    # Sidebar
    st.sidebar.header("Let's Plan Your Trip! 🚀")
    destination = st.sidebar.text_input("Enter Destination", "")
    duration = st.sidebar.number_input("Duration of Stay (in days)", min_value=1, max_value=30, value=7)
    budget = st.sidebar.number_input("Budget (in USD)", min_value=1, value=1000)

    st.sidebar.markdown("---")
    st.sidebar.info("Adjust the parameters and click on 'Generate Trip Plan'.")

 
    if st.sidebar.button("Generate Trip Plan"):
        if destination:
            generate_trip_plan(destination, duration, budget)
        else:
            st.warning("Please enter a destination.")

if __name__ == "__main__":
    main()
