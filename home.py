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

    Github   <a href="https://github.com/jisiji/"><img src="data:image/png;base64,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"/></a>
   
   
        
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
