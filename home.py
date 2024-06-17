import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "💻"),
        Section("Machine Learning UI App", "🧙‍♂️"),
        Page("pages/crop_recom_streamlitapp.py", "Crop Recommendation ML Model", "1️⃣", in_section=True),
        Page("pages/basic_sentiment_analyzer.py", "Basic Sentiment Analyzer", "2️⃣", in_section=True),
        Page("pages/img_classification.py", "Image Classification ", "3️⃣", in_section=True),

    ]
)

hide_pages(["Thank you"])

st.markdown("### 👨‍🔧 ML Learning by [koalatech](https://github.com/koalatech)")

st.image("./back.jpg")
st.markdown("""<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",unsafe_allow_html=True,)

st.info("Visit the project [Github](https://github.com/koalatech/machine_learning_portfolio_streamlit_web_app)")
st.info("Issues are now fixed with Streamlit 1.35.0")
st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

with st.expander("Sample ""st.expander"""):
    st.markdown("""
    
    <a href=""><img src="https://user-images.githubusercontent.com/875246/185755203-17945fd1-6b64-46f2-8377-1011dcb1a444.png" height="50" /></a>

    #

        Gwapo si sir Pabelona
        
    #""", unsafe_allow_html=True)

st.markdown("""
### 👨‍🎓 Sample Header Title

##### 👨‍👦‍👦 Subheader Title

* Bullet 1
* Bullet 2
* Bullet 3


##### 👨‍🔧 About Me

   I am Jovyck C. Gegantoni
   
       Hello there reader, I am Jovyck C. Gegantoni, a 3rd year college student at 
    Carlos Hilado Memorial State College, also known as CHMSU. I am pursuing 
    Bachelor of Science in Information Systems. I live in E. B.Magalona and been
    there since senior high school. This is my ITEQMT ENDTERM- FINAL REQUIREMENT 
    under the guidance of Mr. Richard Pabelona (a handsome guy) serving as our 
    instructor for the subject ITEQMT.

       
### 🔎 Overview""", unsafe_allow_html=True)


st.image("./back.jpg")


st.markdown("""
This Streamlit.app serves as a compilation of our work for the subject 
including Crop Recommendation ML Model, Basic Sentiment Analyzer,
and Image Classifier
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
