import streamlit as st
import streamlit.components.v1 as components


st.title('Evaluation of Time Series Models')
st.caption('Author: Shravani, Kashin')
st.caption('2023 April')

st.header('Coding Demonstration')
st.markdown(
    """
    - Train-Test Split
    
    - Error Metrics
    
    This outline covers the key concepts and techniques of time series forecasting and includes a coding demonstration in Python. The focus is on implementing the techniques and evaluating the models using error metrics. The conclusion provides a summary of the key takeaways and highlights future directions in the field. The coding demonstration provides a practical example of how to implement the techniques discussed in the presentation.

    """
)

components.html("""<script src='https://gist.github.com/UmbraVenus/2d5de6d990ff5cb30fba712a520d19bb.js'></script>""", height=2000)