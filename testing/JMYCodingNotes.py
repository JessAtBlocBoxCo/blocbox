"South Migraiton: How to fix/ delete taable restart when screwing up
for core users we dont delete because wed have to recreate all the users
- but the migraiton history is clearly messedup, two things:
Steps to Fix:"
#1. deleted everything in the migraiton history folder, including the folder
#2. delete the recors inthe south_migrationhistory table
#		DELETE FROM south_migrationhistory WHERE app_name='core'; (have to use singl qutations)

# THEN RUN
$ python manage.py convert_to_south core
$ python manage.py migrate core 0001 --fake


"PSQL - INSTALLATION LOCATION"
/etc/postgresql/9.3/main

"PSQL - IMPORT CSV"
#1. create the table (This is test table)
$ CREATE TABLE delmewaitlistusers (
		EMAIL_ADDRESS character varying(254), 
		first_name character varying(100), 
		last_name character varying(100),
	  zip_code character varying(5) );
#2. upload the CSV- TESTING
COPY delmewaitlistusers (EMAIL_ADDRESS, first_name, last_name, zip_code)
	FROM '/home/django/blocbox/core/mailchimp_imports/testcsvimport.csv'
	WITH DELIMITER ','
	CSV HEADER ;

#Drop the test table

# copy/UPLOAD - REAL ONE
DROP TABLE mailchimp_waitlist;
CREATE TABLE mailchimp_waitlist (
		EMAIL character varying(254),
	  first_name character varying(100), 
		last_name character varying(100),
	  zipcode character varying(5),
	  Subscribe_Date timestamp,
	  Referred_By character varying(254),
	  Untitled1 character varying(50),
	  Untitled2 character varying(50),
	  Website character varying(250),
	  Image_URL character varying(250),
	  Become_a_Host character varying(100),
	  Email_Opt_In boolean,
	  Member_Rating numeric,
	  optin_time timestamp,
	  optin_ip character varying(30),
	  date_joined_waitlist timestamp,
	  confirm_ip character varying(30),
	  latitude decimal,
	  longitude decimal,
	  GMTOFF numeric,
	  DSTOFF numeric,
	  TIMEZONE character varying(30),
	  Country character varying(5),
	  Region character varying(5),
	  Last_Changed timestamp,
	  LEID numeric,
	  EUID character varying(15),
	  NOTES character varying(250)
);

#COPY the real one
COPY mailchimp_waitlist (
		email,  first_name ,  last_name, zipcode ,
	  Subscribe_Date,  referred_by , Untitled1,  Untitled2,
	  Website,	Image_URL,  Become_a_Host ,  Email_Opt_In ,
	  Member_Rating,  optin_time, optin_ip, date_joined_waitlist, confirm_ip,
	  latitude, longitude, GMTOFF,  DSTOFF, TIMEZONE, Country,  Region,
	  Last_Changed,  LEID, EUID, NOTES )
	FROM '/home/django/blocbox/core/mailchimp_imports/mailchimp_waitlist_users_10april2015.csv'
	WITH DELIMITER ',' CSV HEADER ;

#make a hostinterest field based on "Become_a_Host" field
ALTER TABLE mailchimp_waitlist ADD COLUMN hostinterest boolean;
UPDATE mailchimp_waitlist SET hostinterest=True WHERE Become_A_Host is not null;

"MERGE components of two tables - so in this case merging the fields i want from waitlist into the user table"
#merge the mailchimp_waitlist info into core_userinfo
#TEST
DROP TABLE delmetest;
CREATE TABLE delmetest
	(EMAIL character varying(254), first_name character varying(100), zipcode character varying(5), 
	hostinterest boolean, date_joined_waitlist timestamp, referred_by character varying(254) );
INSERT INTO delmetest (email, zipcode, first_name, referred_by, date_joined_waitlist, hostinterest)
	SELECT email, zipcode, first_name, waitlist_referred_by, date_joined_waitlist, hostinterest FROM mailchimp_waitlist;
DROP TABLE delmetest;

#Actual
INSERT INTO core_userinfo (email, zipcode, first_name, referred_by, date_joined_waitlist, hostinterest)
	SELECT email, zipcode, first_name, referred_by, date_joined_waitlist, hostinterest FROM mailchimp_waitlist;


	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
);
	  
EMAIL ADDRESS	First Name	Last Name	ZIP CODE	Subscribe Date	Referred By	Untitled	Untitled	Website	Image URL	BECOME A HOST	Email_Opt_In	MEMBER_RATING	OPTIN_TIME	OPTIN_IP	CONFIRM_TIME	CONFIRM_IP	LATITUDE	LONGITUDE	GMTOFF	DSTOFF	TIMEZONE	CC	REGION	LAST_CHANGED	LEID	EUID	NOTES


FOR THE REAL ONE:
COPY delmewaitlistusers (EMAIL_ADDRESS, first_name, last_name, zip_code)
	FROM '/home/django/blocbox/core/mailchimp_imports/mailchimp_waitlist_users_10april2015.csv'
	WITH DELIMITER ','
	CSV HEADER ;
	

"FINDING LOCATION OF SOMETHING ON LINUX"
https://www.digitalocean.com/community/tutorials/how-to-use-find-and-locate-to-search-for-files-on-a-linux-vps