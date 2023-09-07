# Airflow-Project

Welcome to the Apache Airflow Project. This is a simple Data Engineering project that does not include advanced Airflow concepts such as SubDAGs, deadlocks, and encryption using a fernet key. Nor does it encompass advanced features such as log and monitoring implementations or API connections.

### Prerequisites

Before running the project, ensure you have the following prerequisites set up:

- **Docker**: You need to have Docker installed on your local machine or your AWS EC2 instance. You can download Docker from [here](https://www.docker.com/get-started).

- **Docker Compose File**: curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.0/docker-compose.yaml'

- **AWS S3**: You should have an AWS S3 bucket set up to store your raw and processed data. Ensure that you have your AWS credentials configured correctly to access the bucket.

### Usage

To run the data engineering project, follow these steps:

1. Open a terminal and navigate to the project directory.

2. Build and start the Docker containers using Docker Compose:

   ```bash
   docker-compose up -d
   ```

   This command will start the data extraction, transformation, and loading processes in Docker containers.

3. Monitor the project's progress by viewing the container logs:

   ```bash
   docker-compose logs -f
   ```

### Data Flow

The data flow in this project is as follows:

1. **Data Extraction**: Raw data is extracted from an AWS S3 bucket.

2. **Data Transformation**: Python script 'transformation' in the `/dags` directory uses pandas for data transformation and modeling.

3. **Data Loading**: Processed data is loaded back into the AWS S3 bucket.

4. **Data Orchestration**: This workflow is orchestrated by Apache Airflow and is set to run daily.

### Technologies Used

- **Docker**: Containerization platform used for running the data pipeline.

- **Python**: Programming language used for data transformation and modeling.

- **pandas**: Python library for data manipulation and analysis.

- **AWS S3**: Cloud storage service used for data storage.
  
- **Apache Airflow**: A popular data orchestration tool.

### Workflow examples

**Airflow Dags**:

![B3C523BD-EBB6-45D3-B212-C361992B463E](https://github.com/LeonR92/Airflow-Project/assets/127194165/5a6814ce-d10b-4fc6-bbae-c2450dcd3100)

**Folder Structure in AWS S3**:
![D710DA41-7BBF-49D5-A48C-12AE8DA524DB](https://github.com/LeonR92/Airflow-Project/assets/127194165/53def5fe-1d63-486a-8a79-0c8d74769c1e)

**Final Dim and Fact Tables in AWS S3**:
![A184AF94-BC55-4FA8-B501-515C1677405B](https://github.com/LeonR92/Airflow-Project/assets/127194165/04d8a339-4183-4774-8a3e-3dd26cf1d87b)

**Data Model**:
![D97BAF85-6E50-4067-A99E-B77FB9DB093E](https://github.com/LeonR92/Airflow-Project/assets/127194165/d70dd655-4ffa-48a1-a507-43815b66dfec)






