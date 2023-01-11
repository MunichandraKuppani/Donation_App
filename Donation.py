import streamlit as st
from streamlit_lottie import st_lottie
import razorpay
from PIL import Image
import requests

st.set_page_config(page_title="Ganapati_Youth_Page",page_icon=":tada:",layout="wide")
img_contact_form = Image.open("images\Ganapati.png")

def load_lottieurl(url):
    r =requests.get(url)
    if r.status_code !=200:
      return None
    return r.json()

lottie_coding =load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_Z0QWsPCUJj.json")

with st.container():
     st.write("---")
     left_column, right_column = st.columns(2)
     with left_column:
          st.title("Ganapati_Chanda:wave:")
          st.subheader("I request everyone to give Donation")
with right_column:        
     # st.image(img_contact_form,width=200)
      st_lottie(lottie_coding, height=300, key="coding")

with st.container():
      name = st.text_input("Name")
      amount = st.number_input("Please enter Amount")

      

# Set up the UPI payment functionality
razorpay_Upi = razorpay.Client(auth=("",""))

# Add a button to the Streamlit app to initiate the UPI payment process
if st.button("Pay with UPI"):
   razorpay_Upi.start_payment(

      )