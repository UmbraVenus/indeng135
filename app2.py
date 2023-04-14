import streamlit as st
st.set_page_config(layout="wide")

from multiapp import MultiApp
# import apps here
import reference
# comment placeholder
import introduction
import pages.time_series_analysis as time_series_analysis
import time_series_forecasting_techniques
import pages.coding_demonstrations as coding_demonstrations
import visualization

# initiate multiple app sidebar interface
introduction = MultiApp()

# add apps here, order matters
introduction.add_app("I. Introduction",introduction.app)
introduction.add_app("II. Time Series Analysis", time_series_analysis.app)
introduction.add_app("III. Time Series Forecasting Techniques", time_series_forecasting_techniques.app)
introduction.add_app("IV. Coding Demonstration", coding_demonstrations.app)
introduction.add_app("V. Visualization", visualization.app)
# app.add_app("VI. Conclusion", reference.app)


# run apps
introduction.run()