##South Migraiton: How to fix/ delete taable restart when screwing up
"for core users we dont delete because wed have to recreate all the users
- but the migraiton history is clearly messedup, two things:
Steps to Fix:"
#1. deleted everything in the migraiton history folder, including the folder
#2. delete the recors inthe south_migrationhistory table
#		DELETE FROM south_migrationhistory WHERE app_name='core'; (have to use singl qutations)

# THEN RUN
$ python manage.py convert_to_south core
$ python manage.py migrate core 0001 --fake

#ERROR: "core_userinfo" already exists
