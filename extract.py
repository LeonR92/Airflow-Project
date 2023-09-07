import boto3
import os


def download_csv_from_s3():

    # Predefined AWS credentials and file information
    aws_access_key_id = ''
    aws_secret_access_key = ''
    bucket_name = 'airflow-project-lr'
    file_key = 'Raw/uber_data.csv'
    local_file_path = '/opt/airflow/dags/raw.csv'

    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)

    # Download the file from S3
    try:
        s3.download_file(bucket_name, file_key, local_file_path)
        print(
            f"File '{file_key}' downloaded to '{local_file_path}' successfully.")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
