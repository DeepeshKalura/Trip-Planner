import os
import requests
import spacy


nlp = spacy.load("en_core_web_sm")

def geocode_location(location):
    api_key = os.environ.get("GOOGLEMAPS_API_KEY") 
    map_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address': location, 'key': api_key}
    response = requests.get(map_url, params=params).json()
    if response['status'] == 'OK':
        latlng = response['results'][0]['geometry']['location']
        return latlng['lat'], latlng['lng']
    else:
        return None

def extract_locations(text):
    if type(text) is dict:
        a = ""
        for t in text.values():    
            a += f"{t}"
        text = a
        
    locations = {}
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "GPE":  
            locations[ent.text] = geocode_location(ent.text)
    return {k: v for k, v in locations.items() if v is not None}


