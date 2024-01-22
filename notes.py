# import streamlit as st

# def write_note():
#     note = st.text_area("Write your note here:")
#     return note

# def save_note_to_file(note):
#     with open("notes.txt", "a") as file:
#         file.write(note + "\n")
# def download_file():
#     with open("notes.txt", "r") as file:
#         notes_content = file.read()
#     return notes_content
# def main():
#     st.title("Notes")

#     # Get the note from the user
#     note = write_note()

#     # Save the note to a text file when the user clicks the button
#     if st.button("Save Note"):
#         save_note_to_file(note)
#         st.success("Note saved successfully!")
#     if st.button("Download Notes"):
#         notes_content = download_file()
#         st.download_button(
#             label="Download Notes",
#             data=notes_content,
#             file_name="notes.txt",
#             key="download_notes"
#         )

# if __name__ == "__main__":
#     main()

import streamlit as st

def write_note():
    note = st.text_area("Write your note here:")
    return note

def save_note_to_file(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

def download_file():
    with open("notes.txt", "r") as file:
        notes_content = file.read()
    return notes_content

def notes_main():
    st.title("Notes")

    # Get the note from the user
    note = write_note()

    # Save the note to a text file when the user clicks the button
    if st.button("Save Note"):
        save_note_to_file(note)
        st.success("Note saved successfully!")

    # Download the notes content when the user clicks the button
    if st.button("Download Notes"):
        notes_content = download_file()
        st.download_button(
            label="Download Notes",
            data=notes_content,
            file_name="notes.txt",
            key="download_notes"
        )

if __name__ == "__main__":
    notes_main()
