# import streamlit as st
# import subprocess

# # Function to execute the selected Python script
# def execute_script(script_name):
#     subprocess.run(["streamlit", "run", script_name])

# # Streamlit App
# st.title("Geriatic AI")

# selected_option = st.sidebar.radio("Select an option", [
#     "Medicine Reminder",
#     "Notes",
#     "Locate Nearby Hospitals",
#     "Alert SOS",
#     "Track Progress"

# ])

# options_to_scripts = {
#     "Medicine Reminder": "main.py",
#     "Notes": "notes.py",
#     "Locate Nearby Hospitals": "app.py",
#     "Alert SOS": "main_s.py",
#     "Track Progress": "visualize_data.py"
# }

# # Execute the selected script
# if selected_option in options_to_scripts:
#     script_name = options_to_scripts[selected_option]
#     execute_script(script_name)
# else:
#     st.error("Invalid option selected.")

import streamlit as st
from streamlit_option_menu import option_menu
# from main import main
from notes import notes_main
from enter_data import main_data
from app import nearby_hospi
from visualize_data import  track_progress_main
from acne import main_acne
from sayantan import sos_main
from hair_app import hair_health_main
# from login import main_l

def main():

    PAGE_CONFIG = {"page_title": "Geriatric AI",
               "page_icon": "icon.png", "layout": "centered"}
    st.set_page_config(**PAGE_CONFIG)
    
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://img.freepik.com/premium-photo/green-background-with-bokeh-rays_582451-37.jpg");
    background-size: cover;
    background-position: top left;
    background-repeat: no-repeat;
    }}
    [data-testid="stHeader"] {{
    color: black;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.sidebar.title("Geriatric AI")
    menu = [ "Health Data Recorder", "Track Progress", "Locate Nearby Hospitals", "Acne Detection", "Hair Health Prediction", "Alert SOS", "Notes","Events Near Me"]
    with st.sidebar:
        app_selection = option_menu(
        menu_title = None,
        options = menu,
        # icons = ['house', 'bullseye', 'card-checklist', 'emoji-smile', 'journal']
    )
    # app_selection = st.sidebar.radio("Select an option", ["Data","Medicine Reminder", "Notes", "Locate Nearby Hospitals", "Track Progress", "Alert SOS"])

    if app_selection == "Medicine Reminder":
        # main()
        pass
    # elif app_selection=="Login":
    #     main_l()
        
    elif app_selection == "Notes":
        notes_main()
    elif app_selection == "Locate Nearby Hospitals":
        nearby_hospi()
        # pass
    elif app_selection == "Track Progress":
        track_progress_main()
        # pass
    elif app_selection == "Alert SOS":
        sos_main()
        # pass
    elif app_selection=="Health Data Recorder":
        # pass
        main_data()
    elif app_selection=="Acne Detection":
        main_acne()
    elif app_selection=="Hair Health Prediction":
        hair_health_main()
    elif app_selection == "Events Near Me":
        st.markdown("""
        **Remote event**: Digivartti: the topic is Google Calendar  
        **When:** Fri, 20.9.2024 from 10 to 10.30  
        **Where:** remotely on Zoom  
        [More information](https://www.entersenior.fi/tapahtumat/digivartti-0924/)
        
        **Local event**: Solutions for a good everyday life  
        **When**:Wed-Thurs, 2-3 October 2024 
        *Where:** Helsinki Exhibition Centre, Messuaukio 1, 00520 Helsinki  
        [More information](https://hyvaika.expomark.fi/)
        
        **Travel**: Northern Portugal, Porto and port wine farms  
        **When**: Mon-Sat, 21-26 October 2024  
        **Where**: Porto, Portugal 
        [More information](https://kilta.senioriliitto.fi/Tapahtumat/tapahtumatiedot.aspx?id=28261)
        
        **A hybrid event**: Identify an online scam  
        **When**: Wed, 23.10.2024 at 1:30 p.m. to 3:00 p.m 
        **Where**:remotely in Zoom, stand in Kampi 
        [More information](https://www.entersenior.fi/tapahtumat/tunnista-nettihuijaus/)
        
        **Local event**: Guided gym  
        **When**: Mon, 30.12.2024 at 10.00-11.00
        **Where**: Myllypuro senior center/service center, Myllymatkantie 4, Helsinki  
        [More information](https://tapahtumat.hel.fi/fi/events/helsinki:agh3rorroe)
        """)

if __name__ == "__main__":
    main()
