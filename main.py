import streamlit as st
from scholarly import scholarly
import time

def fetch_google_scholar_data(researcher_name):
    try:
        # Search for the researcher's profile by name
        search_query = scholarly.search_author(researcher_name)
        author = next(search_query)  # Get the first result

        # Load the author's complete profile
        author = scholarly.fill(author)

        # Collect the desired information
        citations = author.get("citedby", "Information not available")
        h_index = author.get("hindex", "Information not available")
        i10_index = author.get("i10index", "Information not available")
        
        return citations, h_index, i10_index
    except StopIteration:
        return "Profile not found on Google Scholar.", "-", "-"
    except Exception as e:
        return f"Error fetching data: {e}", "-", "-"

# Streamlit Interface
st.title("Google Scholar Data Search")

# Input for multiple researcher names separated by commas
researcher_names = st.text_input("Enter the names of researchers on Google Scholar, separated by commas:")

if st.button("Search"):
    if researcher_names:
        with st.spinner("Searching..."):
            # Split the list of names and remove extra spaces
            names_list = [name.strip() for name in researcher_names.split(",")]
            for name in names_list:
                st.subheader(f"Data for: {name}")
                citations, h_index, i10_index = fetch_google_scholar_data(name)
                st.write(f"Citations: {citations}")
                st.write(f"h-index: {h_index}")
                st.write(f"i10-index: {i10_index}")
                # Add a 2-second interval between searches
                time.sleep(2)
    else:
        st.warning("Please enter at least one researcher's name.")

# Add source and developer credit at the end of the application
st.write("Source: Google Scholar.")
st.markdown("<p><strong>Tool developed by Darliane Cunha.</strong></p>", unsafe_allow_html=True)

