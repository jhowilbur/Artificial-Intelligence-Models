# Linear Regression

- Algorithm with the purpose of drawing a future profile based on data from the past, a sequence of dataset to statistically predict a new result from results already seen in previous cases.

![1200px-Linear_regression svg](https://user-images.githubusercontent.com/59379254/104529366-59111f00-55e8-11eb-9ba2-dac4fef856ef.png)

---------------------
## Farthest example

Separated between ALGORITHM and MODEL, we have on the left side (ALGORITHM) the management of information, in this case take the number of items, add and divide by the number of existing elements:

- MEDIA = (ADD ALL VALUES) / (AMOUNT OF VALUES)

Finally my MODEL will be the final value of MEDIA

after this step a line can be drawn on the graph, the problem with this alternative is that the residuals are large given the distance of the values ​​to the average line

---------------------
## More accurate example

Through the average of this information (dataset), by the linear regression formula, in a Cartesian plane we can draw a line with its closest linear points and having a more accurate result, that is, we reduce the distance between the residuals (points in the graph) with the real values ​​(drawn line)

- Y = A + B * X

Summing up the advantage is that a line will be drawn that best suits the data set under study

In our table we have dependent and independent value, to find the line

REGRESSION STRAIGHT:

- Y = (INDEPENDENT COEFFICIENT) + (DEPENDENT COEFFICIENT) * X
- (Y = A + B * X)

---------------------

## Project
#### In this project, we will train a linear regression model for predicting continuous values.

for this model, I take a dataset from file .csv in project, and distributed values with training data for 20% of the data contained in the csv.

![Figure_1](https://user-images.githubusercontent.com/59379254/104532645-73023000-55ef-11eb-8557-0e8a5cb14ce9.png)

now with the data established and showing your points on the Cartesian plane, we will plot the linear regression line, given the sum of the squares of the differences
#### ~ (that is, we will reduce our residual value) ~

![Figure_1](https://user-images.githubusercontent.com/59379254/104532580-4d752680-55ef-11eb-8922-169aeedf12f3.png)

for the end we need to apply a model of the data we train (the 20% taken from the table in code {line 73})

```
predicoesCo2 = model.predict(engines_training)
```

an example of a model for having an idea

![Screenshot from 2021-01-13 23-14-52](https://user-images.githubusercontent.com/59379254/104535559-2f122980-55f5-11eb-94c5-4aaccc5a7c9d.png)

and after we have to make predictions using the model and test base

(as we know visually given the graph generated, the observation of differences is abstract, but mathematically we know that it exists and has high importance)

![Figure_1](https://user-images.githubusercontent.com/59379254/104536982-dabc7900-55f7-11eb-81b2-52698cc4ffff.png)

-------------------------

### finally we have some parameters that indicate the reliability of a certain form of the analysis, and a special highlight (R2-score) for the value of the variance (on variable Y in relation to variable X) in percentage

```
Sum of Errors squared (SSE): 799078.47
Mean Quadratic Error (MSE): 936.79
Mean Absolute Error (MAE): 23.20
Root of the Mean Square Error (RMSE): 30.61
R2-score: 0.76
```

--------------

Thanks for your attention!

~ 🅦🅘🅛🅑🅤🅡 ~

https://github.com/jhowilbur

https://www.linkedin.com/in/jwilbur