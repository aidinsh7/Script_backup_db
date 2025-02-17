import os
import shutil
import subprocess
from datetime import datetime



#setup db
backup_dir = '/path/to/backup'  
db_name = 'your_database_name'
db_user = 'your_database_user'
db_password = 'your_database_password'
db_host = 'localhost'
files_to_backup = ['/path/to/file1', '/path/to/file2']  




# Create a backup directory with date and time
def create_backup_directory():
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'backup_{now}')
    os.makedirs(backup_path, exist_ok=True)
    return backup_path



def backup_database(backup_path):
    dump_file = os.path.join(backup_path, f'{db_name}.sql')
    command = f'mysqldump -u {db_user} -p{db_password} -h {db_host} {db_name} > {dump_file}'
    subprocess.run(command, shell=True)



def backup_files(backup_path):
    for file_path in files_to_backup:
        if os.path.exists(file_path):
            shutil.copy(file_path, backup_path)



# Main function to run backup
def main():
    backup_path = create_backup_directory()
    backup_database(backup_path)
    backup_files(backup_path)
    print(f'Backup completed and stored in: {backup_path}')

if __name__ == '__main__':
    main()