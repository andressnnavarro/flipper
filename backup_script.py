import shutil
import os
from datetime import datetime

def backup_database():
    # Define paths
    db_path = 'gimnasio.db'  # Path to your database file
    backup_dir = 'backups'  # Directory to store backups
    os.makedirs(backup_dir, exist_ok=True)  # Create backup directory if it doesn't exist

    # Create a backup file name with the current date
    backup_file = os.path.join(backup_dir, f'gimnasio_backup_{datetime.now().strftime("%Y%m%d")}.db')

    # Copy the database file to the backup location
    try:
        shutil.copy2(db_path, backup_file)
        print(f"Backup created successfully: {backup_file}")
    except Exception as e:
        print(f"Error creating backup: {e}")

# Call the backup function
backup_database()
