# Visualization-Of-Optimization-functions
Visualization of Momentum, RMSProp and Adam Optimization Functions.

Getting intuitions on workings of these algorithms. 

## Intuitions:

- The First Exponentially Weighted Moving Average is Sensitive towards the change in direction of the plot,
which is a little smoothened due to the Weighted average more focusing on the historical values of the Original plot,
which in terms retains the overall "momentum" of the plot. 
    
- Whereas the Second EWMA is particularly sensitive towards the Overall direction of the Original plot,
while smoothing and averaging out all the nearby change in directions.
    
- The Adam Curve is Sensitive Towards all the big changes in the directions of the original plot 
as well as the curve moves along the overall direction of the Original plot. 
    
*P.S while using the bias correction the graph explodes in certain regions(mostly when x unit is small).*
