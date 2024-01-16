import os
from Google import Create_Service

CLIENT_SECRET_FILE = 'testsecret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)


spreadsheet_id = '1tbe3W7KeBmyrjJ46OFN8vusJR7u40_v2xEWoLhMTIaE'
"""test 1"""
response = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, majorDimension='ROWS', range='Sheet1!A4:F6').execute()
print(response)