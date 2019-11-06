# Cron for python Beta
Cron for python (work with PyCharm)

How work:
1. Create or edit file "cron.txt"
2. Add text line in "cron.txt"
3. Line must be like "* * * * * test.py" where "minute hour day month day_of_week your_file"
4. from main.py import Cron_Stable in your project
5. Start cron:\
  cron = Cron_Stable()\
  cron.load_tasks()\
  cron.run()



Trade-offs of use:
1. Work for now only with python files
2. Now not work day_of_week
3. Maybe contain few bugs
