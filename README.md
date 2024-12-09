# Python

---

## Question 1: Parse and Summarise Log Files

### Problem:

Write a script that reads a server log file, extracts errors, and outputs a summary of errors grouped by error type and
how many times each error occurred.

Log lines follow this format:

```log
2024-09-18 12:35:22 ERROR ConnectionTimeout: Connection to database failed
2024-09-18 12:36:01 INFO Connection restored
2024-09-18 12:36:55 ERROR IOError: Unable to read file /etc/config.cfg
```

### Requirements:

1. Parse the log file and find all lines that contain the word "ERROR."
2. Group errors by their error type (e.g., ConnectionTimeout, IOError) and count their occurrences.
3. Store the summary on to a database (sqlight setup function provided).
4. Output the summary as a dictionary

## Question 2: Auto Scaling Decision Script

### Problem:

Write a script that simulates a simple auto-scaling decision mechanism for a cloud service. The script will receive CPU
utilisation as input of a list of instance and decide whether to scale up or scale down the number of servers.

1. If the average CPU utilisation is greater than 75% over the last 10 data points, scale up by increasing the number of
   servers by 1.
2. If the average CPU utilisation is below 25% over the last 10 data points, scale down by reducing the number of
   servers by 1.
3. Otherwise, maintain the current number of servers.

### Requirements:

1. Input: List of CPU utilisation percentages for the last 10 data points.
2. Output: A decision (scale up, scale down, or maintain current).

# Terraform

---

## Question 1: AWS Lambda Function Creation with Terraform

Write a Terraform configuration that creates an AWS Lambda function using Python 3.10.

1. Be triggered by an S3 event (when an object is uploaded to a specific bucket).
2. Log the file name of the uploaded object to CloudWatch Logs.
3. The Lambda function's code should be provided in a local file lambda_function.py.
4. Add a CloudWatch log group with a retention policy of 7 days.

## Question 2: Dynamic VPC and Subnet Creation with Terraform

How can we use terraform to dynamically deploy a VPC with 1 subnet in each availability zone.
    Region value and VPC CIDR block will be given as input.
    Terraform should dynamically provision a subnet for each availability Zone.

Example 1 – 
    N California – us-west-1 – 2 availability zones
    VPC CIDR – 10.0.0.0/16
    Subnet CIDRs – [ 10.0.0.0/17, 10.0.128.0/17 ]

Example 2 – 
    Oregon – us-west-2 – 4 availability zones
    VPC CIDR – 10.0.0.0/16
    Subnet CIDRs – [ 10.0.0.0/18, 10.0.64.0/18, 10.0.128.0/18, 10.0.192.0/18 ]
