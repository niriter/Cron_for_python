#!/usr/bin/python3

import datetime
import time
import os

from threading import Thread


# - - - - - * * * * * выполняемый файл python
# | | | | |
# | | | | ----- день недели(0—7) (воскресенье = 0 или 7)
# | | | ------- месяц(1—12)
# | | --------- день(1—31)
# | ----------- час(0—23)
# ------------- минута(0—59)

class Cron_Stable():
    def __init__(self, quick_run=False):
        if quick_run == True:
            self.quick_run = True
            self.load_tasks()
            self.run()
        else:
            self.quick_run = False

    def run(self):
        process = Thread(target=self.start)
        process.start()

    def start(self):
        if not hasattr(self, 'tasks'):
            self.load_tasks()
        while True:
            process = Thread(target=self.needs_start)
            process.start()
            self.time_now = datetime.datetime.now()
            seconds_now = float(self.time_now.strftime('%S.%f')) / 10
            seconds_left = 60 - float(str(seconds_now - int(seconds_now))[1:])
            time.sleep(seconds_left)

    def load_tasks(self):
        if self.quick_run:
            with open("libraries/cron_stable/cron.txt", "r") as myfile:
                self.tasks = myfile.readlines()
        else:
            with open("cron.txt", "r") as myfile:
                self.tasks = myfile.readlines()
        for indx, task in enumerate(self.tasks):
            self.tasks[indx] = task.replace('\n', '')


    def needs_start(self):
        for task in self.tasks:
            if self.is_task_callable(task):
                task_file = task.split()
                task_file = str(task_file[-1])
                if self.quick_run:
                    task_file = task_file.replace('../../', '')
                os.system("python "+task_file)
        return

    def is_task_callable(self, task):
        tmp = task.split()

        if tmp[0] == '*' or ( ('/' in tmp[0]) and (int(self.time_now.strftime("%M")) % int(tmp[0].split('/')[-1]) == 0)) or (not ('/' in tmp[0]) and int(self.time_now.strftime("%M")) == int(tmp[0])): #minute
            if tmp[1] == '*' or (('/' in tmp[1]) and (int(self.time_now.strftime("%H")) % int(tmp[1].split('/')[-1]) == 0)) or (not ('/' in tmp[0]) and int(self.time_now.strftime("%H")) == int(tmp[0])): #hour
                if tmp[2] == '*' or (('/' in tmp[2]) and (int(self.time_now.strftime("%d")) % int(tmp[2].split('/')[-1]) == 0)) or (not ('/' in tmp[0]) and int(self.time_now.strftime("%d")) == int(tmp[0])): #day
                    if tmp[3] == '*' or (('/' in tmp[3]) and (int(self.time_now.strftime("%m")) % int(tmp[3].split('/')[-1]) == 0)) or (not ('/' in tmp[0]) and int(self.time_now.strftime("%m")) == int(tmp[0])): #month
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

    def delete_modules_tasks(self):
        if os.path.exists('modules_cron.txt'):
            return


if __name__ == "__main__":
    cron = Cron_Stable()
    cron.load_tasks()
    cron.run()