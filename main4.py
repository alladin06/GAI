import streamlit as st

def main():
    st.title("Language Selector App")

    # Language selection dropdown
    language = st.selectbox("Choose a language:", ["English", "Finnish", "German"])

    if language == "English":
        run_main("combine.py")
    elif language == "Finnish":
        run_main("main2.py")
    elif language == "German":
        run_main("main3.py")

def run_main(script):
    st.info(f"Running {script}")
    # You can add additional logic to run the chosen script here
    # For now, let's just print a message
    st.write(f"Script {script} executed successfully!")

if __name__ == "__main__":
    main()
