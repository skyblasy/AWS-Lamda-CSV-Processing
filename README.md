# Automated CSV Processing With AWS Lambda
### Schuyler Blasy

#### -- Project Status: Completed

## Project Description
This project uses AWS Lambda to create a function which processes csv files, pefromes data manipulation and simple analysis to generate new, processed csv files placed in their respective buckets in a dynamic way. The project takes raw csv files from an S3 Bucket and uses a Lambda trigger to take each new file, process and transform it using python and pandas, and places the transformed data as new objects into their respective S3 Buckets. 

The data used in this example is sales order data set from kaggle, but can be easily adapted to any use case. For this dataset and example, I created some goupby’s for some simple analysis, but the options can go far beyond that. 

This project would be an example of a possible intermediary step within a data pipeline with further endpoints possibly being AWS QuickSight, Athena, SQS, or DynamoDB. The flexibility of using AWS SDK allows for many options and combinations. Or, simply changing the endpoint of this function to send processed data directly to the aforementioned endpoints. 

The Lambda Function and AWS were created and deployed using The Serverless Framework, and this repos includes the Yaml File and CloudFormation stack for generating the additional S3 Buckets. Please note that S3 Bucket names must be globally unique, so reproducing this stack will require changing the bucket names both in the Yaml file and in referencing them within the Python code. 

This project is only an example of many combinations and possible applications of using AWS Lambda to process raw csv files for automated transformations and data analysis. 



### Methods Used
* Data Analysis
* Data Processing
* Data Munging
* Data Automation
* Business Analysis


### Technologies
* Python, Boto3
* Yaml
* Serverless Framework
* AWS Lambda
* AWS S3
* AWS CloudFormation
