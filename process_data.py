import json
from linkedin_api import Linkedin
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from send_email import send_email
import streamlit as st

def generate_profile(profile_name):
    # Authenticate using any LinkedIn account credentials
    api = Linkedin('starman112003@gmail.com', 'starwars135')
    # Fetch the LinkedIn profile data
    profile_data = api.get_profile(profile_name)
    # For demonstration purposes, let's use a sample profile data
    profile_json = json.dumps(profile_data, indent=4)
    return profile_json

def generate_email():
# Read the form data from the file
    with open('form_data.txt', 'r') as f:
        lines = f.readlines()

    # Extract the form data from the file
    # name = lines[0].split(': ')[1].strip()
    email = lines[1].split(': ')[1].strip()
    # linkedin = lines[2].split(': ')[1].strip()
    website = lines[3].split(': ')[1].strip()
    # list1=[]
    # for i in range(len(linkedin)-2,0,-1):
    #     if linkedin[-1]=="/":
    #         if linkedin[i]=="/":
    #             name=linkedin[i+1:-1]
    #             list1.append(name)
    #             break
    #     else:
    #         if linkedin[i]=="/":
    #             name=linkedin[i+1:len(linkedin)]
    #             list1.append(name)
    #             break
    # profile_name=list1[0]
    # profile_details=generate_profile(profile_name)

    # Set your OpenAI API key
    api_key=st.secrets["openai_apikey"]
    client=OpenAI(api_key=api_key)
    # Define the website URL for analysis
    website_url = website # Replace with the actual website URL
    response = requests.get(website_url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")
    website_text = soup.get_text()

    prompt = f" Generate an email from Anankan R to Analyze the following website content and perform a SWOT analysis:\n\n{website_text}\n\nThen, and presenting the SWOT analysis for the client's website. give the swot analysis within the mail."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.7,
    )

    generated_email = response.choices[0].message.content
    # Extract the subject (assuming it's the first line)
    subject = generated_email.split('\n', 1)[0]
    cleaned_subject = subject.replace("Subject:", "").strip()
    # Extract the body (excluding the subject)
    body = generated_email.split('\n', 1)[1]
    send_email(cleaned_subject, body, email)
    return generated_email

def generate_email_linkedin():
# Read the form data from the file
    with open('form_data.txt', 'r') as f:
        lines = f.readlines()

    # Extract the form data from the file
    email = lines[1].split(': ')[1].strip()
    linkedin = lines[2].split(': ')[1].strip()
    list2=[]
    for i in range(len(linkedin)-2,0,-1):
        if linkedin[-1]=="/":
            if linkedin[i]=="/":
                name=linkedin[i+1:-1]
                list2.append(name)
                break
        else:
            if linkedin[i]=="/":
                name=linkedin[i+1:len(linkedin)]
                list2.append(name)
                break
    profile_name=list2[0]
    profile_details=generate_profile(profile_name)
    
    # Set your OpenAI API key
    client=OpenAI(api_key=api_key)

    prompt = f"Analyze the LinkedIn profile {profile_details}."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    generated_email = response.choices[0].message.content
    
    return generated_email
