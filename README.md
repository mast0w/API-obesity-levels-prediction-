# API-obesity-levels-prediction-
Report of project during the course Python for data analysis at ESILV (M2)

The purpose of this project was to create an intelligent tool to identify obesity levels. 

The source of data was found here : https://www.sciencedirect.com/science/article/pii/S2352340919306985?via%3Dihub

It contains eating habits and physical activity of 2111 persons from Perou, Coloumbia and Mexico (data mainly generated with Weka & Smote)

We found correlation between physical activity like means of transport to go to work and the corpulence. We also found correlation with eating habits (like the cosumption of alcohol.

Our solution is an API which runs a Random Forest Classifier (best model found) on a Django server. 

In this repository you can find :
-Our notebook to find the best model & see data visualisation
-Source code of Django API
