# # sos_app.py
# import streamlit as st
# import geopy
# from geopy.geocoders import Nominatim
# from geopy.point import Point
# from googlesearch import search
# import requests
# import requests
# import json
# import time
# import pandas as pd
# st.title("Hospitals Near me")
# df = pd.read_csv("hospital_directory.csv")
# r = requests.get("https://get.geojs.io/v1/ip.json")
# ip_address = r.json()["ip"]
# url = 'https://get.geojs.io/v1/ip/geo/'+ip_address+'.json'
# loc = requests.get(url)
# loc = loc.json()
# st.write(loc)
# geoLoc = Nominatim(user_agent=loc["city"])

# longitude =  float(loc['longitude'])
# latitude =float(loc['latitude'])
# # finding distance between tutor and student locations
# import math
# distances = []
# Time = []
# # student_x, student_y = map(float, coordinates.split(','))
# student_x = 23.2487
# student_y = 77.4066
# i = 0
# for value in df['Location_Coordinates']:

#     R = 6371.0
#     try:
#         tutor_x, tutor_y = map(str, value.split(','))
    
#         tutor_x, tutor_y = float(tutor_x), float(tutor_y)    
        
#         lat1_rad = math.radians(student_x)
#         lon1_rad = math.radians(student_y)
#         lat2_rad = math.radians(tutor_x)
#         lon2_rad = math.radians(tutor_y)
    
#         dlat = abs(lat2_rad - lat1_rad)
#         dlon = abs(lon2_rad - lon1_rad)
        
#         a = math.sin(dlat / 2)*2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)*2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#         distance = R * c
    
#         # distance = math.sqrt((tutor_x - student_x)*2 + (tutor_y - student_y)*2)
    
#         distances.append(distance)
    
#         speed = 50
#         time = round(distance/speed, 2)
#         Time.append(time)
#         i = i+1
        
#     except:
#         distances.append(a)
#         Time.append(i)
#         i = i+1
# cord = df["Location_Coordinates"].values
# loca = df["Location"].values
# hos = df['Hospital_Name'].values
# sta = df["State"].values
# dis = df["District"].values

# result_df = pd.DataFrame({
#     'Hospital_Name': df['Hospital_Name'],  # Change 'Hospital_Name' to the actual column name
#     'State': df['State'],  # Change 'State' to the actual column name
#     'Distance': distances,
#     'Time(hrs)': Time,
#     'District':dis,
#     'Address': loca

# })

# top_5_hospitals = result_df.nsmallest(5, 'Distance')

# # Print or use the top 5 hospitals as needed
# # query = "list of hospitals near "+loc["city"]

# # url = "https://google.serper.dev/search"

# # payload = json.dumps({
# #   "q": query
# # })
# # headers = {
# #   'X-API-KEY': 'd1f58d901e02cf4e4c83c4749e8b5a28f7f4e8f9',
# #   'Content-Type': 'application/json'
# # }

# # response = requests.request("POST", url, headers=headers, data=payload)
# # r = response.json()

# if st.button("Get Nearby Hospitals"):
#     # st.write(r["organic"][0]['link'])
#     st.write(top_5_hospitals)



import streamlit as st
import geopy
from geopy.geocoders import Nominatim
from geopy.point import Point
# from googlesearch import search
import requests
import json
import time
import pandas as pd

def locate_nearby_hospitals_main():
    st.title("Hospitals Near me")
    df = pd.read_csv("hospital_directory.csv")
    r = requests.get("https://get.geojs.io/v1/ip.json")
    ip_address = r.json()["ip"]
    url = 'https://get.geojs.io/v1/ip/geo/'+ip_address+'.json'
    loc = requests.get(url)
    loc = loc.json()
    st.write(loc)
    geoLoc = Nominatim(user_agent=loc["city"])

    longitude =  float(loc['longitude'])
    latitude =float(loc['latitude'])
    
    # finding distance between tutor and student locations
    import math
    distances = []
    Time = []
    
    # student_x, student_y = map(float, coordinates.split(','))
    student_x =latitude
    student_y = longitude
    i = 0
    
    for value in df['Location_Coordinates']:
    
        R = 6371.0
        try:
            tutor_x, tutor_y = map(str, value.split(','))
        
            tutor_x, tutor_y = float(tutor_x), float(tutor_y)    
            
            lat1_rad = math.radians(student_x)
            lon1_rad = math.radians(student_y)
            lat2_rad = math.radians(tutor_x)
            lon2_rad = math.radians(tutor_y)
        
            dlat = abs(lat2_rad - lat1_rad)
            dlon = abs(lon2_rad - lon1_rad)
            
            a = math.sin(dlat / 2)*2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)*2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
            distance = R * c
        
            # distance = math.sqrt((tutor_x - student_x)*2 + (tutor_y - student_y)*2)
        
            distances.append(distance)
        
            speed = 50
            time = round(distance/speed, 2)
            Time.append(time)
            i = i+1
            
        except:
            distances.append(a)
            Time.append(i)
            i = i+1
    
    cord = df["Location_Coordinates"].values
    loca = df["Location"].values
    hos = df['Hospital_Name'].values
    sta = df["State"].values
    dis = df["District"].values
    
    result_df = pd.DataFrame({
        'Hospital_Name': df['Hospital_Name'],
        'State': df['State'],
        'Distance': distances,
        'Time(hrs)': Time,
        'District':dis,
        'Address': loca
    })
    
    top_5_hospitals = result_df.nsmallest(5, 'Distance')

    if st.button("Get Nearby Hospitals"):
        st.write(top_5_hospitals)

if __name__ == "__main__":
    locate_nearby_hospitals_main()
