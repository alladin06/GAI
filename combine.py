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
from sayantan import sos_main
from login import main_l

def main():
    st.sidebar.title("Geriatic AI")
    menu = ["Login","Track Progress","Data","Medicine Reminder", "Notes", "Locate Nearby Hospitals",  "Alert SOS"]
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
    elif app_selection=="Login":
        main_l()
        
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
    elif app_selection=="Data":
        # pass
        main_data()

if __name__ == "__main__":
    main()
