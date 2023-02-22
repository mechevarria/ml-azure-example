import numpy as np
import pandas as pd
import os
from azure.storage.blob import BlobServiceClient
from sklearn.linear_model import LinearRegression
from dotenv import load_dotenv

# Load the data
load_dotenv()
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client('csv')
data_file='housing_data.csv'
blob_client = container_client.get_blob_client(data_file)

with open(data_file, 'wb') as local_blob:
  blob_data = blob_client.download_blob()
  blob_data.readinto(local_blob)

housing_data = pd.read_csv(data_file)
# print(housing_data.head())
X = housing_data[['Sq ft', 'Burglaries']]
y = housing_data['Rent']

# Create the model
reg = LinearRegression()

# Train the model
reg.fit(X, y)

# do prediction
square_footage = 2800
number_of_burglaries = 1

y_pred = reg.predict(np.array([square_footage, number_of_burglaries]).reshape(1, 2))

print(y_pred)

# cleanup local file
os.remove(data_file)