# Automated CSV Processing With AWS Lambda
### Schuyler Blasy

#### -- Project Status: Completed

## Project Description
This project uses AWS Lambda to create a function which processes csv files, pefromes data transformation and simple analysis to generate new, processed csv files placed in their respective buckets in a dynamic way.

Raw csv files are placed in an intake S3 Bucket causing a Lambda trigger beginning an asynchronous invocation that uses pandas to transform the files into various groupby objects and statistics for analysis using pandas. The objects are then converted back into csv files and dynamically labelled using datetime to give them a unique name and chronological ordering, and then placed in their receiving S3 Buckets. 

This project would be an example of a possible intermediary step within a data pipeline with further endpoints possibly being AWS QuickSight, Athena, SQS, or DynamoDB. The flexibility of using AWS SDK allows for many options and combinations. Or, simply changing the endpoint of this function to send processed data directly to the aforementioned endpoints

The data used in this example is sales order data set from the Kaggle Global Super Store Dataset, which can be found [here](https://www.kaggle.com/apoorvaappz/global-super-store-dataset), but can be easily adapted to any use case. 

The Lambda Function and AWS resources were created and deployed using The Serverless Framework, and this repo includes the Yaml File and CloudFormation stack for generating the additional S3 Buckets. Please note that S3 Bucket names must be globally unique, so reproducing this stack will require changing the bucket names both in the Yaml file and in referencing them within the Python code. 

This project is only an example of many combinations and possible applications of using AWS Lambda to process raw csv files for automated transformations and data analysis. The possibilities for data processing go far beyond what is shown in this brief example, and can include possibilities such as automated EDA, imputation, or other BI techniques such as pivot tables. 



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


