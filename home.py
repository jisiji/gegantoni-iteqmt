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
   
       Hello there reader, I am Jovyck C. Gegantoni, a 3rd year college student 
       at Carlos Hilado Memorial State College, also known as CHMSU. I am 
       pursuing Bachelor of Science in Information Systems. I live in E. B.
       Magalona and been there since senior high school. This is my ITEQMT ENDTERM
       - FINAL REQUIREMENT under the guidance of Mr. Richard Pabelona (a handsome guy)
       serving as our instructor

       
### 🔎 Overview""", unsafe_allow_html=True)


st.image("./back.jpg")


st.markdown("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Id neque aliquam vestibulum morbi blandit cursus risus. Sagittis nisl rhoncus mattis rhoncus. 
Purus viverra accumsan in nisl nisi scelerisque eu. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit amet. 
Eleifend quam adipiscing vitae proin. Neque convallis a cras semper auctor neque. Et tortor consequat id porta nibh. 
Vitae nunc sed velit dignissim sodales ut eu. Bibendum ut tristique et egestas quis ipsum suspendisse. 
Pharetra massa massa ultricies mi. In nulla posuere sollicitudin aliquam ultrices sagittis. Et pharetra pharetra massa massa. 
Pretium viverra suspendisse potenti nullam ac. Viverra accumsan in nisl nisi scelerisque eu ultrices vitae auctor. 
Nibh mauris cursus mattis molestie a iaculis at erat. Diam sit amet nisl suscipit. 
Urna molestie at elementum eu facilisis sed odio morbi quis. Arcu non sodales neque sodales.
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
