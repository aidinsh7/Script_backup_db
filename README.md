How to run script:

step 1 set permission:
     chmod +x  automation_backup_db.py

step 2 crontab:
    crontab -e

step 3 Add a new line to the cron to schedule the script. For example, to run the script every day at 2am:
       0 2 * * * /usr/bin/python3 /path/to/your/automation_backup_db.py
   
   
