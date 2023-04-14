import streamlit as st



st.title('Time Series Analysis')
st.caption('Author: Muskan, Zaid')
st.caption('2023 April')

st.image('assets/time_series.jpg')

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
st.markdown("""
Autocorrelation as the name suggests is the degree of similarity between a given time series and a lagged version of itself over successive periods; in other words it measures the relationship between a variable’s value over the time.

We can calculate the correlation for a time series data with data from the previous time intervals also known as the lags. Because the correlation of the data is calculated with the values of the same data in the previous time frames, we call it “AUTOCORRELATION” or “Serial Correlation”. For example, we can observe autocorrelation in the “Prices” of a stock  by measuring the correlation between current price and the price of the stock k-periods ago.

The mathematical computation of Autocorrelation is as follows:
""")
st.image('assets/math1.png')
st.subheader('How does Autocorrelation affect our Machine Learning models?')
st.markdown("""
One of the most common models that we use in machine learning to predict the future values is the Linear Regression. One important underlying assumption of the model is the independence of the data. Any type of correlation between the random errors will decline the accuracy of our predictions. Therefore it is important to remove this before we build our model.

We can detect the autocorrelation in the time series data by plotting an Autocorrelation Function (ACF) graph. It is also known as the correlogram or an autocorrelation plot. This is a 2D plot of Lag Values vs Correlation (Note: The k th lag is the time period that happened “k” time points before time i). It also shades the confidence interval across the plot. The values outside of this shaded region have a very high chance of correlation. 

In python we can easily plot the ACF by importing an inbuilt function “plot_acf” from “statsmodel.graphics.tsaplots.” We are attaching a graph where you can clearly notice the lag values where we suspect correlation to exist:""")
st.image('assets/analysis_graph.png')
st.subheader('Partial AutoCorrelation')
st.markdown("""As we observed in the previous section we learnt that ACF measures the linear relationship between an observation at time t and previous time periods. But the Rk (correlation coefficient) only measures the correlation between y(t) to y(t-K) and filter out the linear influence of Random Variable before the K period which requires a transformation on the time series. If we calculate the correlation of the transformed series then we get the PACF.

To explain in simpler words,  partial autocorrelation for Lag 3 is merely the correlation that Lags 1 and Lags 2 do not explain that is the unique correlation between two observations after the intermediate correlations have been removed. The PACF plot is similar to the ACF plot but shows the correlation of a sequence with itself after a certain period of time has elapsed. Thus after all intermediary effects are removed direct effects are visible.
""")
st.image('assets/partial_cor.png')
st.header("C. Seasonality")
st.markdown("""
        As the name suggests Seasonality is any cyclical pattern that repeats itself regularly within a fixed time period. Understanding the seasonal components of our time series data can help us improve the performance of the models. We can use the following two approaches:

- Remove the seasonal components to examine a more clear relationship between the dependent and independent variables. 
        
- Incorporate any information that we gather from the seasonal components into our model which helps us better understand the time series data

Modeling of seasonality and removal from the data is a part of the data cleaning, that is we detect seasonality and incorporate changes before we actually start building our models. But extracting information from seasonality and using it as an input feature is usually done during feature engineering (i.e. after we build our baseline model).

There are different types of seasonality ranging from Time of Day to Daily, Weekly, Monthly or Yearly. A simple approach to identify seasonality is by plotting the data and reviewing at different time scales along with the trend lines to highlight seasonality.
""")
st.image('assets/season1.png')
st.image('assets/season2.png')
st.markdown("""
**Seasonal Adjustments**

The process of removing the seasonality from the time series data is known as the seasonal adjustment or Deseasonalising. A time series data in which the seasonal variables have been removed is called Seasonal Stationary, and a data with clear seasonal variables is called non stationary.
""")
st.image('assets/season_adjust.png')