
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


### 12.02.2026
- Today i will be creating the actual functionality of uploading a file through API Client and Lambda Service. First i had to create a custom `IAM` policy to be able to PUT and GET an object from `S3` bucket, then i had to attach to the policy to the Lambda execution role. After that things got a bit complicated, my local app was sending the csv file through the API as a HTTP request, which contains the formatted body where the file is, then i had to strip the format because Lambda receives raw multipart data, after it was stripped, i was able to upload the file successfully to S3 with simple, yet functional AWS Back-end pipeline. 
- The HTTP request is not as simple as it seems at first. The API Gateway received the HTTP request and transformed it into a JSON format for lambda which contained binary data, which were base64-encoded. 
- Inside the lambda:
	-  Decoded the base64-encoded body.
	- Parsed the multipart structure manually by splitting on the boundary.
	- Identified the file part using the `name="file"` marker.
	- Separated multipart headers from the file payload using the `\r\n\r\n` delimiter.
	- Removed protocol framing (trailing CRLF).
	- Extracted the raw CSV bytes.
	- Uploaded the cleaned file bytes to S3 using the Lambda execution role.
- So the final architecture looks like this now:
	- **Desktop App -> API Gateway -> Lambda -> S3**

### 17.02.2026
- After the last session, i extended the backend pipeline to support structured session storage in **DynamoDB**
- I created a new API Gateway : **POST** /session. This route sends JSON data to AWS Lambda instead of multipart file data like to S3.
- Inside the lambda:
	- I implemented route-based handling using `event["routeKey"]`
	- Parsed JSON body (non-base64)
	- Validated required primary keys (`user_id`, `timestamp`)
	- Used `boto3.resource("dynamodb")`
	- Inserted items using `put_item`
- During the implementation i encountered two important issues:
		-  **DynamoDB** does not support `python float` types, so i had to convert the values from `float` type to decimal type
		- **DynamoDB** strictly enforces primary key schema, i have made a typo in partition key(`used_id` instead of `user_id`) which led to ValidationException
- I also have created a custom IAM policy allowing `dynamodb:PutItem`, attached to the lambda execution role.
		- created a small python script to test the functionality using `requests` and `os` libraries
		- and successfully confirmed data insertion via **DynamoDB** console
- Next session will be to refactor both AWS Lambda and Local application code to reduce technical debt and clarify the architecture more.