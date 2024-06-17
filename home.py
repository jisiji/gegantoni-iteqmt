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
    
    Facebook  <a href="https://www.facebook.com/jovyck.gegantoni"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMwAAADACAMAAAB/Pny7AAAAYFBMVEU7V53///80Upv19/pQZ6XQ1eRXbKd3h7b5+vwiRpY2VJvByNxFX6GdqMh6ibYwT5lrfbDr7fQYQZNidawTP5SGlL0mSZaPnMLIzd+msM0KO5Hh5O7a3uq0vNWttdBLY6NLDS/9AAADXUlEQVR4nO3d7W6qQBSF4emgAsPHiBZEEb3/uzza5CSnJ6UD6mYvzHp/l4QnyoAzQM1HkZq3KC0+TPSpvRev6jMy2ftgMlM32jvxqprabKz2Trwqu9HeA8YYY4wxxhhjjI3L+ibdfStN06bx3lunvW9Tcn736Tfxobj0Wda22a2+7y/Hojgcyni7yX16+wPtvRyTa04+PrZdV0VR8vFPSRLdqqqq67rzut3jzyT5U1O31XfFz5XoGH9aZVHYsQSM99vzSAk6xrv9ejwFGuOaTTGFgoyxtpzwDcPGeFOMPe7hMT7vR4zFy8D4PJtuAcVYk02noGLS/hELJmY3cUhGxjTbxyyIGO8eOPZRMelDBz8mJq0f/WDwMM5MvYgBxqTTr2JgMS6fdNGPjXnmg4HDuIeHMjxMU1ZvhLk8YQHD2NUThz8axsfPfMvQMIdnLFgYl0/4HfM1LfutKEbC2M24S5moLe6z5f8X50hrAX4/5pCpDpvc+J9CshhfjrBcrFvEaoytw5YyXYLk3jFoOSzlzuQRg1kLdYz/lsvbgCUpF7HSd8/loZF5vUI6k/yau3YBzHExFmOvodPMYg7/2yezCvzKrMo3wnTbxRz/Ycx5AQv9fwti1gt6/oUY1IhBjRjUiEGNGNSIQY0Y1IhBjRjUlohxdiB/DWFWzdC29zQw+3ioOjQ7Uw9ueu86+6S6u4Zmxx9NYVbd5c/cUPJbClOEchiF4UEOk13fCNOb+QcAMcxx/ll1OUwx/3qHGCZSeEWWGKaK3+hrdt7Ofz0jhtFYiRbDZPOPzHKYXmHxVgxzUXirpBQm0XhFphRG4zQjhukUTjNiGJV7BKQwa4WRWQzTarwiVwqT7d4Hk2icZqQwkcqtaEIYnVvRpDAqd28JYTqVe4SFMGeVl5cLYdYqL/wWwvQap5kvTDJUaJcHN4yU3pGfl8VQoecauuPgpgqzGV/5dKCdCS025buhbeGW1Gx4GXApz2gsc01zMGJQIwY1YlAjBjViUCMGNWJQIwY1YlAjBjViUCMGNWJQIwY1YlAjBjViUCMGNWJQIwY1YlAjBjViUCMGNWJQIwY1YlAjBjViUCMGNWJQIwY1ecyMj9kKY+zezPieDWFMU5vs9LKdDSWMOWUmme+/V8liXJr8ARIETmu39x9NAAAAAElFTkSuQmCC" height="50" /></a>

     Github   <a href="https://github.com/jisiji/"><img src="data:image/jpeg;base64,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" height="50" /></a>
   
        
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
