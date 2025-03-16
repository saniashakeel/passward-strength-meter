import re
import streamlit as st

#PAGE STYLING
st.set_page_config(page_titles="Passward Strength Meter by Sania Shakeel",page_icon=🔐,layout="centered")

#CUSTOM CSS
st.markdown("""
<style>
.main{text-align: center }
.stTextInput{width: 60% !important; margin: auto;}
.stButton button {width :50%; background-color # 4CAF50; color: white; font-size: 18px;}
.stButton button:hover {background-color: #45a049;}
</style>
""",unsafe_allow-html=True)

#PAGE TITLE AND DESCRIPTION
st.tittle("🔒Passward Strength Generator")
st.write("Enter your passward below to check its security level.🔎")

#FUNCTION TO CHECK PASSWARD STRENGTH

def check_passward_strength(passward):
    score = 0
    feedback = []

    if len(passward) >= 8
         score += 1 #INCREASED SCORE BY 1
     else:
        feedback.append("❌Passward should be "atleast 8 characters long."")
    if re.search(r"[A-Z]",passward )and re.search(r"[a-z]",passward):
        score+= 1
    else:
        feedback.append("❌Passward should include ** both uppercase(A-Z) and lowercase(a-z) letters**.") 

    if re.search(r"\d", passward):
        score +=1
    else:feedback.append("❌Passward should include **atleast one number(1-9)** .")

#SPECIAL CHARACTER
if re.search(r"[!@#$%^&*/*]",passward):
    score += 1
else:
    feedback.append("❌Passward should include **atleast one special character(!@#$%^&*/*)**.")    

#DISPLAY PASSWARD STRENGTH RESULTS
 if score ==4:
    st.success("✅**Strong Passward** - Your passward is secure")
 elif score ==3:
    st.info("⚠️ **Moderate Passward** - Consider improving security by adding more features")   
else:
    st.error("❌**Week Passward**- Follow the suggestion below to strength it.")

#FEEDBACK
if feedback:
    with st.expander("🔍**Improve Your Passward"):
        for item in feedback:
            st.write(item)
            passward= st.text_input("Enter Your Passward:",type="passward",help="ensure your passward is strong .🔐") 

#BUTTON WORKING               
if st.button("Check Strength"):
    if passward :
        check_passward_strength(passward)
    else:
        st.warning("⚠️Please enter a passward first!")
