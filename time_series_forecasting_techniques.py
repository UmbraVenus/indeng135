import streamlit as st

def app():

    st.title('Time Series Forecasting Techniques')
    st.caption('Author: Richard, David')
    st.caption('2023 April')
    
    st.image('assets/pursuing_stationary.png')
    st.image('assets/trend_modeling.png')
    st.image('assets/Differencing.png')
    st.image('assets/Seasonal_Differencing.png')
    
    st.markdown("Here we are going to predict Xt as we have removed both trend and seasonality")
    
    st.subheader('A. Moving Average')
    
    st.image('assets/moving_average.png')
    st.markdown("""
                Hence as we notice that the autocorreation is larger than 0 only when lag is between 0 and q

                Hence a quick check if the MA model will be a good model for our residual is if the acf plot has a sudden cutoff after lag q like the one shown below
                """)
    st.image('assets/ma.png')
    
    st.subheader('B. Exponential Smoothing')
    
    st.markdown("""
                Exponential smoothing is a technique that assigns exponentially decreasing weights to past observations, with more recent observations having a greater weight. It is useful for forecasting when there is a trend or seasonality in the data.

There are different types of exponential smoothing methods that can be used, depending on the characteristics of the data being analyzed. Here are some examples:

Simple Exponential Smoothing: Simple exponential smoothing is the most basic form of exponential smoothing. It is used to smooth out noise in the data and make short-term predictions. The method involves calculating a weighted average of past observations, where the weights decrease exponentially over time. The formula for simple exponential smoothing is:

**:blue[F(t+1) = α * Y(t) + (1-α) * F(t)]**

where F(t+1) is the forecast for the next period, Y(t) is the actual observation in the current period, F(t) is the forecast for the current period, and α is the smoothing parameter, which determines the weight given to the most recent observation.

Holt's Linear Exponential Smoothing: Holt's Linear Exponential Smoothing is an extension of simple exponential smoothing that can handle data with a trend. It involves calculating two sets of weights, one for the level of the series and one for the trend. The formula for Holt's Linear Exponential Smoothing is:

**:blue[F(t+1) = α * Y(t) + (1-α) * (L(t) + T(t))]**

**:blue[L(t) = α * Y(t) + (1-α) * (L(t-1) + T(t-1))]**

**:blue[T(t) = β * (L(t) - L(t-1)) + (1-β) * T(t-1)]**

where F(t+1) is the forecast for the next period, Y(t) is the actual observation in the current period, L(t) is the level of the series in the current period, T(t) is the trend in the current period, α is the smoothing parameter for the level, and β is the smoothing parameter for the trend.

Holt-Winters Exponential Smoothing: Holt-Winters Exponential Smoothing is an extension of Holt's Linear Exponential Smoothing that can handle data with both a trend and seasonality. It involves calculating three sets of weights, one for the level of the series, one for the trend, and one for the seasonal component. The formula for Holt-Winters Exponential Smoothing is:

**:blue[F(t+m) = L(t) + m * T(t) + S(t+m-k)]**

**:blue[L(t) = α * (Y(t) - S(t-m)) + (1-α) * (L(t-1) + T(t-1))]**

**:blue[T(t) = β * (L(t) - L(t-1)) + (1-β) * T(t-1)]**

**:blue[S(t) = γ * (Y(t) - L(t)) + (1-γ) * S(t-m)]**

where F(t+m) is the forecast for m periods ahead, Y(t) is the actual observation in the current period, L(t) is the level of the series in the current period, T(t) is the trend in the current period, S(t) is the seasonal component in the current period, α is the smoothing parameter for the level, β is the smoothing parameter for the trend, γ is the smoothing parameter for the seasonal component, m is the number of periods in a season
""")

    st.subheader('C. ARIMA')
    
    st.markdown("""
- Autoregression (AR): refers to a model that shows a changing variable that regresses on its own lagged, or prior, values.
- Integrated (I): represents the differencing of raw observations to allow the time series to become stationary (i.e., data values are replaced by the difference between the data values and the previous values).
- Moving average (MA):  incorporates the dependency between an observation and a residual error from a moving average model applied to lagged observations.

                """)
    
    
    st.image('assets/ar.png')
    st.markdown("""
                Similar to MA model AR(p) model will have a cut off for its PACF plot at lag = p
p: the number of lag observations in the model, also known as the lag order.
d: the number of times the raw observations are differenced; also known as the degree of differencing.
q: the size of the moving average window, also known as the order of the moving average.
AutoRegressive (AR): The parameter p tells us how many past values to consider for the expression of the current value. Essentially, we learn a model that predicts the value at time t as:
 Moving Average (MA): How many of the forecast errors in the past should be considered. A new value is computed as:""")
    st.markdown("""
                Hence this model is combining everything above together; the difference method, MA model and AR model since we can simply change the parameters to achieve the other model.
                """)
    st.image('assets/frontpage.jpeg')
    st.image('assets/acf.png')
    st.image('assets/pacf.png')
    st.image('assets/partial_acf.png')
    st.image('assets/code1.png')
    st.image('assets/code2.png')
    st.image('assets/umemp_rate.png')
    
    st.subheader('D. Prophet')
    st.markdown("""
                Prophet is a time series forecasting model developed by Facebook. It uses a decomposable time series model with three main components: trend, seasonality, and holidays. It is useful for forecasting data that has multiple seasonalities and non-linear trends.

The trend component is modeled using a piecewise linear function, while the seasonality component is modeled using Fourier series. The holidays component is designed to capture the effect of holidays and other events that may impact the time series.

Here are some examples of how Prophet can be used:
1. Forecasting Daily Sales Data: Suppose you are working for a retail company and you want to forecast daily sales data for the next year. You can use Prophet to create a forecast by fitting a model to historical sales data and making predictions for future dates. The code to do this in Python is as follows:
""")
    st.image('assets/code3.png')
    st.markdown("""
                2. Forecasting Hourly Website Traffic: Suppose you are working for a website and you want to forecast hourly website traffic for the next day. You can use Prophet to create a forecast by fitting a model to historical website traffic data and making predictions for future dates. The code to do this in Python is as follows:
                """)
    st.image('assets/code4.png')
    st.text("In both examples, Prophet is used to create a forecast by fitting a model to historical data and making predictions for future dates. The resulting forecasts can be used to make informed decisions about resource allocation, inventory management, and other business operations.")
    st.subheader('E. LSTM')
    st.markdown("""
                LSTM stands for Long short-term memory. LSTM cells are used in recurrent neural networks that learn to predict the future from sequences of variable lengths. Note that recurrent neural networks work with any kind of sequential data and, unlike ARIMA and Prophet, are not restricted to time series. 
The main idea behind LSTM cells is to learn the important parts of the sequence seen so far and forget the less important ones. This is achieved by the so-called gates as we learned in the class, i.e., functions that have different learning objectives such as: 
1. a compact representation of the time series seen so far
2. how to combine new input with the past representation of the series
3. what to forget about the series
4. what to output as a prediction for the next time step. 
""")
    st.image('assets/code5.png')
    st.image('assets/output.png')