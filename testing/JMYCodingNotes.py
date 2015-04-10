##South Migraiton: How to fix/ delete taable restart when screwing up
"for core users we dont delete because wed have to recreate all the users
- but the migraiton history is clearly messedup, two things:"
1. deleted everything in the migraiton history folder, including the folder
2. delete the recors inthe south_migrationhistory table
DELETE FROM south_migrationhistory WHERE app_name='core'; (have to use singl qutations)

test test