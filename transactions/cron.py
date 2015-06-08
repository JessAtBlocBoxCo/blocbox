from django_cron import CronJobBase, Schedule

class Watch_Packages_Cron(CronJobBase):
    RUN_EVERY_MINS = 5 # mintes - right now do 5 minutes, eventually update to 30

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transactions.watch_packages'    # a unique code

    def do(self):
        pass    # do your thing here