import streamlit as st
st.set_page_config(layout="wide")

from multiapp import MultiApp
# import apps here
import reference
# comment placeholder
import introduction
import time_series_analysis
import time_series_forecasting_techniques
import coding_demonstrations
import visualization

# initiate multiple app sidebar interface
app = MultiApp()

# add apps here, order matters
app.add_app("I. Introduction",introduction.app)
app.add_app("II. Time Series Analysis", time_series_analysis.app)
app.add_app("III. Time Series Forecasting Techniques", time_series_forecasting_techniques.app)
app.add_app("IV. Coding Demonstration", coding_demonstrations.app)
app.add_app("V. Visualization", visualization.app)
# app.add_app("VI. Conclusion", reference.app)


# run apps
app.run()