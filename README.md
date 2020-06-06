# Visualization-Of-Optimization-functions
Visualization of Momentum, RMSProp and Adam Optimization Functions.

Getting intuitions on workings of these algorithms. 

## Intuitions:

![Plots of these Algorithms](https://github.com/shambu09/visualization-of-optimization-functions/blob/master/Graphs/Intuitive_Vis.png?raw=true)

- The First Exponentially Weighted Moving Average is sensitive towards the change in direction of the plot,
which is a little smoothened due to the weighted average more focusing on the historical values of the original plot,
which in terms retains the overall "momentum" of the plot. 
    
- Whereas the Second EWMA(RMS) is particularly sensitive towards the overall direction of the original plot,
while smoothing and averaging out all the nearby change in directions.
    
- The Adam Curve is sensitive towards all the big changes in the directions of the original plot 
as well as the curve moves along the overall direction of the original plot. 
    
*P.S while using the bias correction the graph explodes in certain regions(mostly when x unit(year) is relatively small).*
