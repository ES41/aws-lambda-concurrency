# aws-lambda-concurrency
A small Python script that allows you to get better understanding of your current AWS account lambda status

## Basic terms :

**AWS Lambda concurrency limit** - determines how many function invocations can run simultaneously in one region.by default its set to 1000.

**Reserve concurrency** - set the wanted concurrency limit for the specified Lambda function.

**Unreserved account concurrency** - exactly what it sounds like - a 'pool' of unreserverd concurrency that a function can use.Lambda requires at least 100 unreserved concurrent executions per account.

![This is an image](https://i.ibb.co/rwVRxYb/Screen-Shot-2021-09-20-at-10-41-03.png)


## Exmaple usage & outpot :
Use wanted AWS Region ( by default us-east-2 )
```
Line 10 : region="us-east-2"
```

Run in CLI :
```
Python3 script.py
```
Sample output (Sorted ) : 
- Takes ~ 1.2sec/1 Function 
```
+---------------------------------+-------------------+
|           Lambda-name           | concurrency value |
+---------------------------------+-------------------+
|           lambda_name_1         |         0         |
+---------------------------------+-------------------+
|           lambda_name_2         |         3         |
+---------------------------------+-------------------+
|           lambda_name_3         |         7         |  
+---------------------------------+-------------------+
|           lambda_name_4         |    unreserved     |
+---------------------------------+-------------------+
```
