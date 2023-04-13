import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import streamlit as st
from plotly import graph_objs as go
from prophet import Prophet

st.cache()
def get_data():
    df = pd.read_csv("assets/medium_posts.csv", sep="\t")
    df = df[['published', 'url']].dropna().drop_duplicates()
    df['published'] = pd.to_datetime(df['published'])
    df = df[(df['published'] > '2012-08-15') & (df['published'] < '2017-06-26')].sort_values(by=['published'])
    aggr_df = df.groupby('published')[['url']].count()
    aggr_df.columns = ['posts']
    daily_df = aggr_df.resample('D').apply(sum)
    return daily_df


def app():

    st.title('Visualization(Prophet)')
    st.caption('Author: Sage')
    st.caption('2023 April')
    
    st.header('Predicting Daily Number of Posts Published on Medium')
    st.caption('Reference: https://www.kaggle.com/code/kashnitsky/topic-9-part-2-time-series-with-facebook-prophet/notebook')
    
    daily_df = get_data()
    def plotly_df(df, title=''):
        """Visualize all the dataframe columns as line plots."""
        common_kw = dict(x=df.index, mode='lines')
        data = [go.Scatter(y=df[c], name=c, **common_kw) for c in df.columns]
        layout = dict(title=title)
        fig = dict(data=data, layout=layout)
        st.plotly_chart(fig)
    plotly_df(daily_df, title='Posts on Medium (daily)')
    weekly_df = daily_df.resample('W').apply(sum)
    plotly_df(weekly_df, title='Posts on Medium (weekly)')
    df = daily_df.reset_index()
    df.columns = ['ds', 'y']
    # converting timezones (issue https://github.com/facebook/prophet/issues/831)
    df['ds'] = df['ds'].dt.tz_convert(None)
    prediction_size = 30
    train_df = df[:-prediction_size]
    m = Prophet()
    m.fit(train_df);
    future = m.make_future_dataframe(periods=prediction_size)
    forecast = m.predict(future)
    def make_comparison_dataframe(historical, forecast):
        return forecast.set_index('ds')[['yhat', 'yhat_lower', 'yhat_upper']].join(historical.set_index('ds'))
    cmp_df = make_comparison_dataframe(df, forecast)
    def calculate_forecast_errors(df, prediction_size):
        # Make a copy
        df = df.copy()
        
        # Now we calculate the values of e_i and p_i according to the formulas given in the article above.
        df['e'] = df['y'] - df['yhat']
        df['p'] = 100 * df['e'] / df['y']
        
        # Recall that we held out the values of the last `prediction_size` days
        # in order to predict them and measure the quality of the model. 
        
        # Now cut out the part of the data which we made our prediction for.
        predicted_part = df[-prediction_size:]
        
        # Define the function that averages absolute error values over the predicted part.
        error_mean = lambda error_name: np.mean(np.abs(predicted_part[error_name]))
        
        # Now we can calculate MAPE and MAE and return the resulting dictionary of errors.
        return {'MAPE': error_mean('p'), 'MAE': error_mean('e')}
    
    def show_forecast(cmp_df, num_predictions, num_values, title):
        def create_go(name, column, num, **kwargs):
            points = cmp_df.tail(num)
            args = dict(name=name, x=points.index, y=points[column], mode='lines')
            args.update(kwargs)
            return go.Scatter(**args)
        
        lower_bound = create_go('Lower Bound', 'yhat_lower', num_predictions,
                                line=dict(width=0),
                                marker=dict(color="gray"))
        upper_bound = create_go('Upper Bound', 'yhat_upper', num_predictions,
                                line=dict(width=0),
                                marker=dict(color="gray"),
                                fillcolor='rgba(68, 68, 68, 0.3)', 
                                fill='tonexty')
        forecast = create_go('Forecast', 'yhat', num_predictions,
                            line=dict(color='rgb(31, 119, 180)'))
        actual = create_go('Actual', 'y', num_values,
                        marker=dict(color="red"))
        
        # In this case the order of the series is important because of the filling
        data = [lower_bound, upper_bound, forecast, actual]

        layout = go.Layout(yaxis=dict(title='Posts'), title=title, showlegend = False)
        fig = go.Figure(data=data, layout=layout)
        st.plotly_chart(fig)
        
    code = """
    df = daily_df.reset_index()
    df.columns = ['ds', 'y']
    # converting timezones (issue https://github.com/facebook/prophet/issues/831)
    df['ds'] = df['ds'].dt.tz_convert(None)
    prediction_size = 30
    train_df = df[:-prediction_size]
    m = Prophet()
    m.fit(train_df);
    future = m.make_future_dataframe(periods=prediction_size)
    forecast = m.predict(future)
    def make_comparison_dataframe(historical, forecast):
        return forecast.set_index('ds')[['yhat', 'yhat_lower', 'yhat_upper']].join(historical.set_index('ds'))
    cmp_df = make_comparison_dataframe(df, forecast)
    def calculate_forecast_errors(df, prediction_size):
        # Make a copy
        df = df.copy()
        
        # Now we calculate the values of e_i and p_i according to the formulas given in the article above.
        df['e'] = df['y'] - df['yhat']
        df['p'] = 100 * df['e'] / df['y']
        
        # Recall that we held out the values of the last `prediction_size` days
        # in order to predict them and measure the quality of the model. 
        
        # Now cut out the part of the data which we made our prediction for.
        predicted_part = df[-prediction_size:]
        
        # Define the function that averages absolute error values over the predicted part.
        error_mean = lambda error_name: np.mean(np.abs(predicted_part[error_name]))
        
        # Now we can calculate MAPE and MAE and return the resulting dictionary of errors.
        return {'MAPE': error_mean('p'), 'MAE': error_mean('e')}
    
    def show_forecast(cmp_df, num_predictions, num_values, title):
        def create_go(name, column, num, **kwargs):
            points = cmp_df.tail(num)
            args = dict(name=name, x=points.index, y=points[column], mode='lines')
            args.update(kwargs)
            return go.Scatter(**args)
        
        lower_bound = create_go('Lower Bound', 'yhat_lower', num_predictions,
                                line=dict(width=0),
                                marker=dict(color="gray"))
        upper_bound = create_go('Upper Bound', 'yhat_upper', num_predictions,
                                line=dict(width=0),
                                marker=dict(color="gray"),
                                fillcolor='rgba(68, 68, 68, 0.3)', 
                                fill='tonexty')
        forecast = create_go('Forecast', 'yhat', num_predictions,
                            line=dict(color='rgb(31, 119, 180)'))
        actual = create_go('Actual', 'y', num_values,
                        marker=dict(color="red"))
        
        # In this case the order of the series is important because of the filling
        data = [lower_bound, upper_bound, forecast, actual]

        layout = go.Layout(yaxis=dict(title='Posts'), title=title, showlegend = False)
        fig = go.Figure(data=data, layout=layout)
        st.plotly_chart(fig)

    show_forecast(cmp_df, prediction_size, 100, 'New posts on Medium')

    """
    st.code(code, language='python')
    show_forecast(cmp_df, prediction_size, 100, 'New posts on Medium')

    st.markdown("""
    As we have seen, the Prophet library does not make wonders, and its predictions out-of-box are not ideal. It is still up to the data scientist to explore the forecast results, tune model parameters and transform data when necessary.

    However, this library is user-friendly and easily customizable. The sole ability to take into account abnormal days that are known to the analyst beforehand might make a difference in some cases.

    All in all, the Prophet library is worth being a part of your analytical toolbox.
    """)
    
    
    
    