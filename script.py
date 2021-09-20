from contextlib import redirect_stdout
import subprocess
import json
from beautifultable import BeautifulTable

# create table template
table = BeautifulTable()
table.columns.header = ["Lambda-name", "concurrency value"]
# deafult region is us-east-2
region="us-east-2"

# command for getting all lambdas lambdas in eu-east-2 
list_lambda_command = "aws lambda list-functions --region {region} --query 'Functions[].FunctionName' --output json"
# command for getting a specific lambda cuoncurrency  
lambda_concurrency="aws lambda get-function-concurrency --function-name {function_name}"

# running the first aws cli command on host and load to list object 
lambda_json_output = subprocess.check_output(['bash','-c', list_lambda_command.format(region=region)]).decode()
lambda_list=json.loads(lambda_json_output)

# empty list for incoming 'bad' lambda's results
concurrency_functions={}
unreserved_function={}

for function in lambda_list: 
    # getting lambda funcations with unreserved concurreny value into a dict
    try:
        output=subprocess.check_output(['bash','-c', lambda_concurrency.format(function_name=function)]).decode()
        current_lambda_concurrency=json.loads(output)
    except:
        unreserved_function[f'{function}']="unreserved"
        continue

    # getting lambda funcations with 'bad' concurreny value value into a dict
    current_concurrency=current_lambda_concurrency['ReservedConcurrentExecutions']
    if current_concurrency != 1:
        concurrency_functions[f'{function}']=int(current_concurrency)

# sorting the dic by value
bad_functions_sorted={k: v for k, v in sorted(concurrency_functions.items(), key=lambda item: item[1])}

# adding each dic pair to the table
for key, value in bad_functions_sorted.items():
    table.rows.append([f"{key}",f"{value}"])

for key, value in unreserved_function.items():
    table.rows.append([f"{key}",f"{value}"])

print(table)
