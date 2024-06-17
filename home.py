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



st.image("./back.jpg")
 

with st.expander("Socials"""):
    st.markdown("""
    
    Facebook  
<a href="https://www.facebook.com/jovyck.gegantoni"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMwAAADACAMAAAB/Pny7AAAAYFBMVEU7V53///80Upv19/pQZ6XQ1eRXbKd3h7b5+vwiRpY2VJvByNxFX6GdqMh6ibYwT5lrfbDr7fQYQZNidawTP5SGlL0mSZaPnMLIzd+msM0KO5Hh5O7a3uq0vNWttdBLY6NLDS/9AAADXUlEQVR4nO3d7W6qQBSF4emgAsPHiBZEEb3/uzza5CSnJ6UD6mYvzHp/l4QnyoAzQM1HkZq3KC0+TPSpvRev6jMy2ftgMlM32jvxqprabKz2Trwqu9HeA8YYY4wxxhhjjI3L+ibdfStN06bx3lunvW9Tcn736Tfxobj0Wda22a2+7y/Hojgcyni7yX16+wPtvRyTa04+PrZdV0VR8vFPSRLdqqqq67rzut3jzyT5U1O31XfFz5XoGH9aZVHYsQSM99vzSAk6xrv9ejwFGuOaTTGFgoyxtpzwDcPGeFOMPe7hMT7vR4zFy8D4PJtuAcVYk02noGLS/hELJmY3cUhGxjTbxyyIGO8eOPZRMelDBz8mJq0f/WDwMM5MvYgBxqTTr2JgMS6fdNGPjXnmg4HDuIeHMjxMU1ZvhLk8YQHD2NUThz8axsfPfMvQMIdnLFgYl0/4HfM1LfutKEbC2M24S5moLe6z5f8X50hrAX4/5pCpDpvc+J9CshhfjrBcrFvEaoytw5YyXYLk3jFoOSzlzuQRg1kLdYz/lsvbgCUpF7HSd8/loZF5vUI6k/yau3YBzHExFmOvodPMYg7/2yezCvzKrMo3wnTbxRz/Ycx5AQv9fwti1gt6/oUY1IhBjRjUiEGNGNSIQY0Y1IhBjRjUlohxdiB/DWFWzdC29zQw+3ioOjQ7Uw9ueu86+6S6u4Zmxx9NYVbd5c/cUPJbClOEchiF4UEOk13fCNOb+QcAMcxx/ll1OUwx/3qHGCZSeEWWGKaK3+hrdt7Ofz0jhtFYiRbDZPOPzHKYXmHxVgxzUXirpBQm0XhFphRG4zQjhukUTjNiGJV7BKQwa4WRWQzTarwiVwqT7d4Hk2icZqQwkcqtaEIYnVvRpDAqd28JYTqVe4SFMGeVl5cLYdYqL/wWwvQap5kvTDJUaJcHN4yU3pGfl8VQoecauuPgpgqzGV/5dKCdCS025buhbeGW1Gx4GXApz2gsc01zMGJQIwY1YlAjBjViUCMGNWJQIwY1YlAjBjViUCMGNWJQIwY1YlAjBjViUCMGNWJQIwY1YlAjBjViUCMGNWJQIwY1YlAjBjViUCMGNWJQIwY1ecyMj9kKY+zezPieDWFMU5vs9LKdDSWMOWUmme+/V8liXJr8ARIETmu39x9NAAAAAElFTkSuQmCC" height="50" /></a>
    
   
   
        
    #""", unsafe_allow_html=True)

st.markdown("""


#

##### 👨‍🔧 About Me

   I am Jovyck C. Gegantoni
   
       Hello there reader, I am Jovyck C. Gegantoni, a 3rd year college student at 
    Carlos Hilado Memorial State College, also known as CHMSU. I am pursuing 
    Bachelor of Science in Information Systems. I live in E. B.Magalona and been
    there since senior high school. This is my ITEQMT ENDTERM- FINAL REQUIREMENT 
    under the guidance of Mr. Richard Pabelona (a handsome guy) serving as our 
    instructor for the subject ITEQMT.

 #
### 🔎 Overview""", unsafe_allow_html=True)





st.image("./back.jpg")


st.markdown("""
#
This Streamlit.app serves as a compilation of our work for the subject 
ITEQMT. It includes Crop Recommendation ML Model, Basic Sentiment Analyzer, and Image Classifier

#
#
#
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
