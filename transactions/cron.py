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
        message = 'This is Watch_Packages_Cron - should run every 20 minutes on the hour - wondering why its executing twice'

class Test_Mail_Cron(CronJobBase):
    RUN_EVERY_MINS = 360 # 6 hours- make sure its running

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transactions.cron.Test_Mail_Cron'

    #code = 'transactions.watch_packages.test_send_email(1,2,184)'    # a unique code

    def do(self):
    	test_send_email(1,2,184)
        #watch_packages.main()
        #pass    # do your thing here
        message = 'This is test_send_mail - should run every 6 hours'

class Test_Every_Minute(CronJobBase):
    RUN_EVERY_MINS = 1 # 6 hours- make sure its running

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transactions.cron.Test_Every_Minute'

    #code = 'transactions.watch_packages.test_send_email(1,2,184)'    # a unique code

    def do(self):
        message = 'This is Test_Every_Minute - curious to see if it is also running twice'

        