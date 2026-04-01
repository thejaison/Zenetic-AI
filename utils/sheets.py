import gspread
from google.oauth2.service_account import Credentials

scope = [
    "https://spreadsheets.google.com/feeds", # these links are for the google sheets api
    "https://www.googleapis.com/auth/drive" 
]

creds = Credentials.from_service_account_file(
    "credentials.json", scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open("Fitness Client").sheet1

def save_to_sheet(name, age, weight, email):
    sheet.append_row([name, age, weight, email])