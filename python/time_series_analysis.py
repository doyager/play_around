

"""
Link : https://towardsdatascience.com/the-complete-guide-to-time-series-analysis-and-forecasting-70d476bfe775
Whether we wish to predict the trend in financial markets or electricity consumption, time is an important factor that must now be considered in our models. For example, it would be interesting to forecast at what hour during the day is there going to be a peak consumption in electricity, such as to adjust the price or the production of electricity.
Enter time series. A time series is simply a series of data points ordered in time. In a time series, time is often the independent variable and the goal is usually to make a forecast for the future.
However, there are other aspects that come into play when dealing with time series.
Is it stationary?
Is there a seasonality?
Is the target variable autocorrelated?


####Autocorrelation
Informally, autocorrelation is the similarity between observations as a function of the time lag between them.

Above is an example of an autocorrelation plot. Looking closely, you realize that the first value and the 24th
value have a high autocorrelation. Similarly, the 12th and 36th observations are highly correlated. This means
that we will find a very similar value at every 24 unit of time.
Notice how the plot looks like sinusoidal function. This is a hint for seasonality, and you can find its value by 
finding the period in the plot above, which would give 24h.


####Seasonality
Seasonality refers to periodic fluctuations. For example, electricity consumption is high during the day and 
low during night, or online sales increase during Christmas before slowing down again.

####Stationarity
Stationarity is an important characteristic of time series. A time series is said to be stationary if its statistical 
properties do not change over time. In other words, it has constant mean and variance, and covariance is independent of time.

Example of a stationary process
Looking again at the same plot, we see that the process above is stationary. The mean and variance do not vary over time.
Often, stock prices are not a stationary process, since we might see a growing trend, or its volatility might increase over
time (meaning that variance is changing).
Ideally, we want to have a stationary time series for modelling. Of course, not all of them are stationary, but we can make 
different transformations to make them stationary.


#####How to test if a process is stationary
You may have noticed in the title of the plot above Dickey-Fuller. This is the statistical test that we run to determine
if a time series is stationary or not.
Without going into the technicalities of the Dickey-Fuller test, it test the null hypothesis that a unit root is present.
If it is, then p > 0, and the process is not stationary.
Otherwise, p = 0, the null hypothesis is rejected, and the process is considered to be stationary.
As an example, the process below is not stationary. Notice how the mean is not constant through time.


##### Modelling time series
There are many ways to model a time series in order to make predictions. Here, I will present:
#moving average
#exponential smoothing
#ARIMA


##### Moving average
The moving average model is probably the most naive approach to time series modelling. This model simply states that
the next observation is the mean of all past observations.
Although simple, this model might be surprisingly good and it represents a good starting point.
Otherwise, the moving average can be used to identify interesting trends in the data. We can define a window to 
apply the moving average model to smooth the time series, and highlight different trends.

Example of a moving average on a 24h window
In the plot above, we applied the moving average model to a 24h window. The green line smoothed the time series, and 
we can see that there are 2 peaks in a 24h period.
Of course, the longer the window, the smoother the trend will be. Below is an example of moving average on a smaller window.


##### Exponential smoothing

Exponential smoothing uses a similar logic to moving average, but this time, a different decreasing weight is assigned to
each observations. In other words, less importance is given to observations as we move further from the present.
Mathematically, exponential smoothing is expressed as:

Exponential smoothing expression
Here, alpha is a smoothing factor that takes values between 0 and 1. It determines how fast the weight decreases for 
previous observations.

Example of exponential smoothing
From the plot above, the dark blue line represents the exponential smoothing of the time series using a smoothing factor
of 0.3, while the orange line uses a smoothing factor of 0.05.
As you can see, the smaller the smoothing factor, the smoother the time series will be. This makes sense, because 
as the smoothing factor approaches 0, we approach the moving average model.


Double exponential smoothing
Double exponential smoothing is used when there is a trend in the time series. In that case, we use this technique, which is simply a recursive use of exponential smoothing twice.
Mathematically:

Double exponential smoothing expression
Here, beta is the trend smoothing factor, and it takes values between 0 and 1.
Below, you can see how different values of alpha and beta affect the shape of the time series.

Example of double exponential smoothing
Tripe exponential smoothing
This method extends double exponential smoothing, by adding a seasonal smoothing factor. Of course, this is useful if you notice seasonality in your time series.
Mathematically, triple exponential smoothing is expressed as:

Triple exponential smoothing expression
Where gamma is the seasonal smoothing factor and L is the length of the season.


##### Seasonal autoregressive integraded moving average model (SARIMA)
SARIMA is actually the combination of simpler models to make a complex model that can model time series exhibiting
non-stationary properties and seasonality.
At first, we have the autoregression model AR(p). This is basically a regression of the time series onto itself.
Here, we assume that the current value depends on its previous values with some lag. It takes a parameter p which 
represents the maximum lag. To find it, we look at the partial autocorrelation plot and identify the lag after which 
most lags are not significant.
In the example below, p would be 4.

Example of a partial autocorrelation plot
Then, we add the moving average model MA(q). This takes a parameter q which represents the biggest 
lag after which other lags are not significant on the autocorrelation plot.
Below, q would be 4.

Example of an autocorrelation plot
After, we add the order of integration I(d). The parameter d represents the number of differences required to make the series stationary.
Finally, we add the final component: seasonality S(P, D, Q, s), where s is simply the season’s length. Furthermore, this component requires the parameters P and Q which are the same as p and q, but for the seasonal component. Finally, D is the order of seasonal integration representing the number of differences required to remove seasonality from the series.
Combining all, we get the SARIMA(p, d, q)(P, D, Q, s) model.
The main takeaway is: before modelling with SARIMA, we must apply transformations to our time series to remove 
seasonality and any non-stationary behaviors.



####Resampling
Let’s begin with simple resampling techniques. Resampling involves changing the frequency of your time series observations. 
One reason why you may be interested in resampling your time series data is feature engineering. Indeed, it can be used 
to provide additional structure or insight into the learning problem for supervised learning models. The resample method 
in pandas is similar to its groupby method as you are essentially grouping by a certain time span. You then specify a 
method of how you would like to resample. Let’s make resampling more concrete by looking at some examples. We’ll start 
with a weekly summary and:
data.resample() will be used to resample the kWh column of our DataFrame
The ‘W’ indicates we want to resample by week.
sum() is used to indicate we want the sum kWh during this period.

weekly = data.resample('W').sum()
weekly.plot(style=[':','--','-']



"""
