import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Sample data for lifesupabase table
entry = {
    "name": "John Doe",
    "number": "9876543210",
    "subject": "Test Entry",
    "message": f"Inserted from VS Code at {datetime.utcnow().isoformat()}"
}

# Insert into Supabase
response = supabase.table("lifesupabase").insert(entry).execute()
print("Inserted:", response.data)
