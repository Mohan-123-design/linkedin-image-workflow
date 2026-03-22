from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv("config/.env")

SHEET_ID = os.getenv("GOOGLE_SHEET_ID")

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_service():
    creds = Credentials.from_service_account_file(
        "config/credentials.json", scopes=SCOPES
    )
    return build('sheets', 'v4', credentials=creds)

def read_rows():
    service = get_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=SHEET_ID,
        range="Sheet1"
    ).execute()
    return result.get("values", [])

def update_cell(range_name, values):
    service = get_service()
    sheet = service.spreadsheets()
    sheet.values().update(
        spreadsheetId=SHEET_ID,
        range=range_name,
        valueInputOption="RAW",
        body={"values": values}
    ).execute()
