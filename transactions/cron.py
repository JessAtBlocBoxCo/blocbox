from django_cron import CronJobBase, Schedule

class Watch_Packages_Cron(CronJobBase):
    RUN_EVERY_MINS = 20 # mintes - right now do 5 minutes, eventually update to 30

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transactions.watch_packages'    # a unique code

    def do(self):
        pass    # do your thing here

class Test_Mail_Cron(CronJobBase):
    RUN_EVERY_MINS = 1 # mintes - right now do 5 minutes, eventually update to 30

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transactions.watch_packages.test_send_email(1,2,184'

    #code = 'transactions.watch_packages.test_send_email(1,2,184)'    # a unique code

    def do(self):
        pass    # do your thing here
        