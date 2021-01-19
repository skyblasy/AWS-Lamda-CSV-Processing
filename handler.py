#trying a different approach to importing data into Lambad
import boto3
import io 
import numpy as np
import pandas as pd
import datetime 
from datetime import datetime
from io import StringIO

s3_client = boto3.client("s3")
s3_resource = boto3.resource('s3')


csv_buffer1 = StringIO()
csv_buffer2 = StringIO()
csv_buffer3 = StringIO()


#creating the export buckets
bucket1 = 'segment-and-catagory-grouped'
bucket2 = 'productname-grouped'
bucket3 = 'productcatagory-and-orderpriority-grouped'

csv_file_1 = 'Segment_And_Catagory' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.csv'
csv_file_2 = 'Product' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.csv'
csv_file_3 = 'Order_Priority_Catagory' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.csv'


def dataprocessor(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name =  event['Records'][0]['s3']['object']['key']
    read_file = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
   
    #turning the CSV into a dataframe in AWS Lambda
    s3_data = io.BytesIO(read_file.get('Body').read())
    df = pd.read_csv(s3_data, encoding='unicode_escape')

    #creating a groupby of segment, category, and sub-category 
    SegmentMarket = df[['Segment','Category','Sub-Category','Sales', 'Quantity','Profit']]
    newrangegrouped = SegmentMarket.groupby(['Segment','Category','Sub-Category'])
    df1 = pd.DataFrame(newrangegrouped['Sales', 'Quantity','Profit'].agg([np.sum, np.mean, np.std, np.ma.count]))
    df1.to_csv(csv_buffer1)
    s3_resource.Object(bucket1, csv_file_1).put(Body=csv_buffer1.getvalue())

    #creating a groupby of products along with their respective clusters
    productclusters = df[['Product Name','Profit', 'Quantity','Sales','Discount','Shipping Cost']] #NUMBER 3
    newrangegrouped2 = productclusters.groupby(['Product Name'])
    df2 = pd.DataFrame(newrangegrouped2['Profit','Sales','Quantity','Discount','Shipping Cost'].agg([np.sum]))
    df2.to_csv(csv_buffer2)
    s3_resource.Object(bucket2, csv_file_2).put(Body=csv_buffer2.getvalue())

    #creating a groupby of product categories and their respective order order priority 
    OrderPriority = df[['Category','Order Priority','Profit','Sales','Quantity', 'Discount','Shipping Cost']]
    newrangegrouped3 = OrderPriority.groupby(['Category','Order Priority'])
    df3 = pd.DataFrame(newrangegrouped3['Sales', 'Quantity','Profit','Discount','Shipping Cost'].agg([np.sum, np.mean, np.std, np.ma.count]))
    df3.to_csv(csv_buffer3)
    s3_resource.Object(bucket3, csv_file_3).put(Body=csv_buffer3.getvalue())  

    return 'Completed'




