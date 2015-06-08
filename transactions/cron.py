from django_cron import CronJobBase, Schedule
from transactions import watch_packages
from transactions.watch_packages import test_send_email

class Watch_Packages_Cron(CronJobBase):
    RUN_EVERY_MINS = 20 # mintes - right now do 5 minutes, eventually update to 30

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transactions.cron.Watch_Packages_Cron'    # a unique code

    def do(self):
    	watch_packages.main()
        #pass    # do your thing here

class Test_Mail_Cron(CronJobBase):
    RUN_EVERY_MINS = 360 # 6 hours- make sure its running

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transactions.cron.Test_Mail_Cron'

    #code = 'transactions.watch_packages.test_send_email(1,2,184)'    # a unique code

    def do(self):
    	test_send_email(1,2,184)
        #watch_packages.main()
        #pass    # do your thing here
        