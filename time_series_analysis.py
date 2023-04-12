import streamlit as st

def app():

    st.title('Time Series Analysis')
    st.caption('Author: Muskan, Zaid')
    st.caption('2023 April')
    
    st.header('A. Stationarity')
    
    st.markdown(
    """
    In time series analysis, stationarity refers to the property of a time series where the statistical properties of the data do not change over time. This means that the mean, variance, and covariance of the time series remain constant over time. In other words, the distribution of the data remains the same over time, and there are no trends or patterns that are dependent on time.

    Stationarity is important in time series analysis because many time series forecasting methods assume that the data is stationary. If the data is not stationary, the forecasting models may not be accurate, leading to incorrect predictions.

    There are two types of stationarity that are important in time series analysis: strict stationarity and weak stationarity. Strict stationarity requires that the joint probability distribution of any set of time series values is invariant to time shifts. Weak stationarity only requires that the mean, variance, and covariance of the time series are constant over time.

    There are several tests that can be used to determine if a time series is stationary, including the Augmented Dickey-Fuller (ADF) test and the Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test. If a time series is not stationary, it can be made stationary through a process called differencing, where the data is transformed by taking the difference between consecutive observations.

    In summary, stationarity is a key concept in time series analysis as it ensures that the statistical properties of the data remain constant over time, allowing for accurate forecasting and modeling.


    """
    )
    st.header("B. Autocorrelation")
    st.header("C. Seasonality")