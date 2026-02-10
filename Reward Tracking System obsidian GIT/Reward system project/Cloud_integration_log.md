A
## 03.02.2026 - AWS Focus

- Prepare local machine for AWS access via boto3 and CLI

Changes:
- Created a mental mind-map for the uploading process, read about AWS SDK and AWS Python


### 05.02.2026

- Added cloud_sync.py with a function to upload csv files to S3 bucket

### 09.02.2026
- Phase 2 v2 - AWS API Gateway + Lambda wired, inspected event

### 10.02.2026
- After doing some research on API's and AWS Lambda functions, which means watching some videos, did some API's crash courses, and creating an API's call with python from the scratch, it is now time to start implementing this small back-end pipeline to my project. The goal is to upload a single and simple .csv file into `S3` bucket on AWS through a API call and a Lambda function. Now, i have exported my `API_URL`, and `API_KEY` through terminal as a temporary variables used for testing and safety, they are safely stored in my AWS account, not hard-coded in the files or pushed to git.
- The API client is working, it is linked to a `Cloud Sync` button in the app, it does have required parameters, and it is shown in the AWS Lambda logs.
- The AWS API Usage plan has also been set very strictly, 1 request per second / 10 requests per day totally, just to be absolutely safe.