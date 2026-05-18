import pandas as pd
import s3fs
import requests
def read_data():
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

    # Read parquet directly from URL
    df = pd.read_parquet(url)

    # Write to S3
    df.to_csv(
        's3://anirudh-nyc-taxi-experiment/NYC_Taxi_Data.csv',
        index=False
    )

    print("Data uploaded to S3 successfully")