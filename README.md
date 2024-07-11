## AIR QUALITY PREDICTION 
#### Introduction
The Air Quality Index (AQI) is used for reporting daily air quality. It tells you how clean or polluted your air is, and what associated health effects might be a concern for you. The AQI focuses on health effects you may experience within a few hours or days after breathing polluted air. EPA calculates the AQI for five major air pollutants regulated by the Clean Air Act: ground-level ozone, particle pollution (also known as particulate matter), carbon monoxide, sulfur dioxide, and nitrogen dioxide. For each of these pollutants, EPA has established national air quality standards to protect public health .Ground-level ozone and airborne particles are the two pollutants that pose the greatest threat to human health in this country.

The AQI is divided into various range according to their affect
![Reference image](/screenshot/Screenshot%20(87).png)
#### Dataset
In this, I have used the Air Quality dataset which is taken form kaggel dataset name as Air quality index(2015-2020). This is a dataset that reports on the weather and the level of pollution each day for five years in indian cities. The data includes the date-time, the pollution called PM2.5 concentration,PM10 concentration,CO,
NO,NO2 etc.
#### Step Followed
- Data preparation
- Data visualization
- Model selection 
- Model Building
- Evaluate model
- Model Deployment
#### Data preparation
- Handling missing value
- outlier Detection and removal
#### Data visualization 
- pie chart
- regplot
- correlation matrix
- Line plot
![Reference image](/screenshot/Screenshot%20(88).png)
#### model selection 
- cross val score
![Referncne iamge](/screenshot/Screenshot%20(89).png)
#### model Buliding 
- Gradient Descent 
#### Evaluate model
- Result
![Reference image](/screenshot/Screenshot%20(86).png)
#### Model Deployment
- flask
- html & css
### Demo
![Reference image](/screenshot/Screenshot%20(84).png)
![Reference image](/screenshot/Screenshot%20(85).png)
#### Reference
J. H. Friedman, “Greedy function approximation: A gradient boosting machine. Annals of Statistics, 29(5), 1189-123,” 2001.