## Linear Regression Example

Downloads a CSV from from [Azure Blob storage](https://azure.microsoft.com/en-us/products/storage/blobs/) and runs a linear regression example

### Requirements
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Conda](https://docs.conda.io/en/latest/) already installed

* Install required packages
```bash
conda install numpy pandas scikit-learn python-dotenv azure-storage-blob azure-identity
```

* Create a local file, `.env` and copy the value of your Azure connection string found in your storage account. Format is similar to below
```properties
AZURE_STORAGE_CONNECTION_STRING='DefaultEndpointsProtocol=https;AccountName=<strorage_name>;AccountKey=<key_value>;EndpointSuffix=core.windows.net'
```

* Run the regression example with `python3 script.py`