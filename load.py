import boto3
import os


def s3_load():
    # AWS credentials and S3 bucket information
    aws_access_key_id = ''
    aws_secret_access_key = ''
    bucket_name = 'airflow-project-lr'
    s3_folder = 'Processed/'  # Optional: You can specify a folder in the S3 bucket

    # Local directory containing CSV files
    local_directory = '/opt/airflow/dags/'

    # Initialize an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)

    # Iterate through files in the local directory
    for filename in os.listdir(local_directory):
        if filename.endswith('.csv') and filename != 'raw.csv':
            # Full path to the local file
            local_file_path = os.path.join(local_directory, filename)

            # Key (name) for the S3 object
            s3_object_key = s3_folder + filename

            try:
                # Upload the file to S3
                s3.upload_file(local_file_path, bucket_name, s3_object_key)
                print(f"Uploaded {filename} to S3 as {s3_object_key}")
            except Exception as e:
                print(f"Error uploading {filename} to S3: {str(e)}")
