#start a psql program
psql django

#DELET A ROW IN A TABLE - E.G., DROP HISTORY ASSOCIATED WITH TRANSACTIONS TABLE FROM SOUTH_MIGRATION HISTORY
DELETE FROM south_migrationhistory WHERE app_name = 'transactions';

    
#update a particular value on the table for a particular person
UPDATE core_userinfo SET hostrating=.99 WHERE id = 4;

#NOTE - BETTER TO HAVE SEPARATE APPS FOR EACH MODEL - I AM GOING TO CREATE A TRANSACTIONS APP
python manage.py startapp transaction

#TO CHANGE A FIELD FROM NOT NULL TO NULL:
If you’ve already created your database, and didn’t use null=True, you’ll need to execute a tiny bit of SQL to get rid of the NOT NULL Django set up for you; the syntax varies from database to database, but for Postgres it would look like this: 

ALTER TABLE core_transaction ALTER COLUMN price DROP NOT NULL;

#MOVED TRANSACTION TABLE TO TRANSACTIONS APP - but need to clean up references in plaes like
core.forms.py, core.views.py, testing.views.py, billing.views.py

#IF YOU ALTER TABLE, NEED TO UPDATE THE ADMIN SITE IF YOU'RE CONFIGURED IT SEPARATE -
#THIS IS A REASON KIDN OF A BAD IDEA TO DO THAT AT START - JUST LET THE DEFAULT ADMIN SETTINGS GOVERN

#RECREATING TABLES THAT WERE DROPPED MANUALLY (I DROPPED TRANSACTION)
#Normally to drop the db_tables for the app that is managed by south you should use:
python manage.py migrate appname zero
#But if you dropped them manually in the db let south know about it
python manage.py migrate appname zero --fake
#And of course to recreate the tables
python manage.py migrate core

#THAT DOESN'T ANSWER MY QUESTION - WANT A TABLE ON A LARGER DB



#Update a table type
ALTER TABLE core_userinfo ALTER COLUMN hostrating TYPE decimal; #chnages it to type=numeric
ALTER TABLE core_userinfo ALTER COLUMN userrating TYPE decimal; #changes it to type=numeric
ALTER TABLE core_uesrinfo ALTER COLUMN favorscompleted TYPE numeric;
ALTER TABLE core_userinfo ADD favorsrequested numeric; #adds a new field - type numeric
ALTER TABLE core_userinfo ADD neighborhood character;
UPDATE core_userinfo SET hostrating=.99; #edit data withina table

#add a new row to a table
INSERT INTO core_userinfo (id, email, first_name, last_name, email, st_address1, st_address2, neighborhood, city, state)
    VALUES (, , Neda, Ulaby, NedaUlaby@Gmail.com 'Yojimbo', 106, '1961-06-16', 'Drama');


#primary key on the core_userinfo table


#DEFAULT DATABASE CONFIG IN blocblox/blocbox/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': '3xsRDPTuG1',
        'HOST': 'localhost',
        'PORT': '',
    }
}

#-------------------------------------------------------------"""

#to list the databases
\l

#connect to database named django
\c django

#list the tables
\dt  #lists the relations

#create a table
CREATE TABLE tablename (field1 int, field2 varchar(255);
#drop table
DROP TABLE tablename;

#SHOW COLUMSN in psql
\d tablename
\d core_user

#DROP Column
ALTER TABLE tablename DROP columnname;

#view postgres useres
\du

#Create user outside of command promt
createuser username
createuser username --superuser

#allow user django to createdb;
ALTER USER django CREATEDB;


#CREATE USERS - WITHIN THE COMMAND PROMPT
CREATE ROLE username; #says cannot login
#ALTER LOGIN WITH
ALTER ROLE username WITH LOGIN;

CREATE ROLE username PASSWORD password;
#BUT THIS PERSON WONT HAVE PRIVILEGES

#CREATE A SUPERUSER
-s
--superuser
CREATE ROLE username PASSWORD
#DROP A USER
DROP ROLE username;

#GIVE ROOT PRIVELEGES
createuser --superuser root
