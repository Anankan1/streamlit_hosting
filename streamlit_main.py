import streamlit as st
from process_data import generate_email

def main():
    st.title("Contact Form")

    # Form fields
    name = st.text_input("Name")
    email = st.text_input("Email")
    linkedin = st.text_input("LinkedIn")
    website = st.text_input("Website")
    message = st.text_area("Message")

    # Submit button
    submit = st.button("Submit")

    if submit:
        # Write form data to a file
        with open("form_data.txt", "w") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"LinkedIn: {linkedin}\n")
            f.write(f"Website: {website}\n")
            f.write(f"Message: {message}\n")

        # Call the generate_email function and display the output
        output = generate_email()
        st.write(output)


if __name__ == "__main__":
    main()