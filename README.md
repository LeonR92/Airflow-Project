# Airflow-Project

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

2. **Data Transformation**: Python script 'transformation' in the `/dags` directory use pandas for data transformation and modeling.

3. **Data Loading**: Processed data is loaded back into the AWS S3 bucket.

4. **Data Ochestration**: This workflow is ochestrated by Apache Airflow and is set to run daily.

### Technologies Used

- **Docker**: Containerization platform used for running the data pipeline.

- **Python**: Programming language used for data transformation and modeling.

- **pandas**: Python library for data manipulation and analysis.

- **AWS S3**: Cloud storage service used for data storage.
  
- **Apache Airflow**: A popular data ochestration tool.

![B3C523BD-EBB6-45D3-B212-C361992B463E](https://github.com/LeonR92/Airflow-Project/assets/127194165/5a6814ce-d10b-4fc6-bbae-c2450dcd3100)

