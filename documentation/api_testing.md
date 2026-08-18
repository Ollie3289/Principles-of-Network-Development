# Network Device API Testing Results

This document records REST API GET requests and responses completed
using Postman.

The API represents the enterprise network created in Lab 

## GET - Retrieve Home Devices
Endpoint: http://127.0.0.1:5000/home/devices
Method: GET
Purpose: Retrieve network device information from the REST API.
Result: API unavailable because the REST API has not yet been implemented.
Observed Error: Connection refused - no service running on port 5000.
Future Development: The REST API will be implemented in lab 6 using Python and
Flask.

# API Troubleshooting Expected Results
This section records REST API testing activities, errors identified
and solutions applied

## Expected Successful API Request
Resource:
/home/routers/R1
Method: GET
Expected Status: 200 OK
Purpose: Retrieve router information from the Network Device Management API.
Implementation: The API will be developed during Lab 6