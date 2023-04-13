import streamlit as st

def app():
    st.title(":blue[IEOR 135/235: Time Series Analysis and Forecasting Tutorials]")
    st.markdown("---")
    st.subheader("Group Members:")
    st.subheader("Sage Ren, Zaid Jiwani, Richard Shi, Muskan Parnami, Kashin Shah, Shravani Nimbolkar, David Lu")
    
    st.caption("All rights reserved @IEOR135 2023")
    st.markdown("---")
    
    st.title('Introduction')
    st.caption('Author: Muskan, Zaid')
    st.caption('2023 April')
    
    st.header('Definition and Importance of Time Series Forecasting')
    
    st.markdown(
    """
    Time series forecasting is a branch of forecasting that deals with predicting future values of a sequence of data points over time, based on historical patterns and trends. It involves using past observations to make predictions about future outcomes.

    Time series forecasting is an important tool in many industries, including finance, economics, marketing, and manufacturing. It can be used to make predictions about sales, stock prices, production levels, and many other variables.

    The importance of time series forecasting lies in its ability to provide valuable insights into future trends and patterns. By analyzing historical data, businesses and organizations can make informed decisions about resource allocation, inventory management, and pricing strategies. For example, a retailer can use time series forecasting to predict demand for a particular product during a certain time of year, and adjust their inventory levels accordingly. Similarly, a manufacturer can use time series forecasting to predict production levels and adjust their operations accordingly, optimizing efficiency and reducing waste.

    Overall, time series forecasting is a valuable tool for businesses and organizations looking to make informed decisions based on past trends and patterns, ultimately helping to improve efficiency and profitability.

    """
    )
    
    st.image('assets/1.png')