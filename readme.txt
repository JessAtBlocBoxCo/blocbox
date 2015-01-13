this is blocbox/readme.txt

The templates (.html files) that you will edit are all stored at blocbox/core/templates/blocbox

If you ever need to figure out teh path to a file, you cal right-clik on the apge and "vewi source" - at the top of the file i try to include the path to all html tempatles


The URLs for this site, and the corresponding files are as follows:

*-----------------------------------------------------------------------*
1. WAITLIST, BETA, GETTING STARTED PAGES
*-----------------------------------------------------------------------*
1A. blocbox.co
	- this is the waitlist page
	- the template is at blocbox/core/templates/blocbox/index.html

1B. blocbox.co/beta/
	- this is the beta page
	- the template is at blocbox/core/templates/blocbox/beta.html

1C. blocbox.co/search/
	- this is the search page (after clikign on "Get started")
	- the tempalte is at core/templates/blocbox/search.shtml
	- teh styles/css need to be fixed
	- aboiut latitude, longtidue: latitude first, longitude second  e.g., john is 40.686529, -73.949413
			to find latitude or longitude on google maps, right-click ont he icon and press "what is here"
			- the first number in lattitude coordinate is between -90 and 90 and 
			- the first number in your longitude coordinate is between -180 and 180.
	
1D. blocbox.co/abouthosting/, template is at core/blocbox/templates/blocbox/abouthosting.html, view is core/views/abouthosting

1E. blocbox.co/aboutblocbox (also accessible at www.blocbox.co/about) 
		- template is core/blocbox/templates/blocbox/aboutblocbox.html, view is core/views/aboutblocbox

*-----------------------------------------------------------------------*
2. REGISTRATION AND AUTHENTICATION PAGES
*-----------------------------------------------------------------------*
2A. blocbox.co/signupconnect/host2/
	- this is the page to sign-up and connect to John - "3" corresponds to USERid=3, but you can replace with "1", eg.,. to connect to jess. same as above
	- teh template is at blocbox/core/templates/blocbox/sign-up-connect.html,but it extends a template at basesignup.html (via sign-up-withtoutconnect.html)
	- if you want to change the basic form structure, you need to edit basesignup.html
	
	- What happens when a user submits/clicks "Sign up and REquest to Connect"
			- They are registered as a user on user_info table
			- the user is kept at same URL but page says "Thank you for registering.. you will be noified.. etc.. this is defined in welcome block			
			- An email is sent to the host asking if they want to accept,
						- Email template is at: \core\templates\emails\requestconnect.txt
						- Function for sending email is defined at \core\views.py\confirmconnect_mail  (this last part of that path is the def defined in views.py)
			- An email is sent to the user telling them a 
						- Email template is at: \core\templates\emails\requesthasbeensent.txt
						- Function for sending email is defined at \core\views.py\requesthasbeensent
			- When the host accepts the request, an email is sent to the user to confirm
						- Email template is at: \core\templates\emails\notifyconnectionconfirmed.txt
						- Function for sending email is defined at \core\views.py\notifyconnectionconfirmed 
			- NOTE ABOUT EMAILS: emails are sent from admin@blocbox.co - in blocbox/blocbox/settings.py - settings at bottom MUST UPDATE IF PWD CHANGES
			
	- Data requested 
		-User info: User email, User Zip, User Password, User address, User intro, User pick up times, Other services, Service requests
		- Register as host, Interested in learning about hosting, etc...

2B. blocbox.co/signup/
	- this is the page to sign-up WITHOUT CONNECTING to a particular host - so it passes no arguments in the url
	- template is at core/templates/blocbox/sign-up-withoutconnect.html; view is core/views/signupnoconnect
	- extends baseesignup.html

2C. blocbox.co/hostsignup/  (Host sign up)
	- template is at core/templates/blocbox/sign-host.html; view is core.views.signuphost
	- you'kll want to populate the "additionalfields" block - this is empty right now, but whatever you put there will be added on to the generic
		sign up form - so this should be host-specific stuff; analgous to the "introduce yourself" fields when connecting to someone
	- note that i had to remove "interst in hosting" from generic basesignup because we dont want that on host sign up, so i added that to specific pages
	- issue: right now we dont really discriminate between users that are already registered as end-useres.. e.g., the process isn't different for them. 
				should it be? if so, how? this is somewhat complicdated and i think it may be a thing to add to the
	- should it say "apply" rather than "sign up"? whats the right verb?
	- i also included a link to this page on the regular sign up pages
	- general issues with sign-up page: aligning and spacing is kinda weird
	- also - there should be a direct tlink to signing up as a host on the landing page. i think it shoudl say "esarch for a host in your neighborhood to get started" 
			(less verbose though) and then a separate button saying "sign up to be a host"
	
2D blocbox.co/login/ (template: blocbox/core/templates/blocbox/sign-in.html)
	- requests email and password
	- goes to dashboard after user logs in

2E blocbox.co/nudgeaneighbor; template: core/templates/blocbox/nudge-a-neighbor.html; view at core.views.nudgeaneighbor

2F. blocbox/connect/host2  - request to connect if already regsitered (e.g., sign up connect without sign up)
		template: core/blocbox/connect-already-registered.html; view is core.views.connectnewhost
		
*-----------------------------------------------------------------------*
3. PROFILE PAGES AND ACCOUNT PAGES
*-----------------------------------------------------------------------*



3A. blocbox.co/hostprofile/host2 - template is core/templates/blocbox/host-profile.html, view is core/views/hostprofile
	- NOTE - this is an outside view - so what other users see about the host, rather than  what the host sees about themselves, which will be on profil
	- the "3" corresponds to John because he is ID #3, you can repliace this with any number (there are like 15 users in the database)
				corresponding to a user ID, and it will render the page with their information
	- the template is at blocbox/core/templates/blocbox/host-profile-visitor.html
	- Data presented
		-Host first name (done)
		-Host address (done)
		-Host favors requested (done)
		-Host about me (needs to be edited to strike last sentence)
		-Host currently helping
		-Host availability
		-Host other offers

3B. blocbox.co/profile - template is core/templates/blocbox/profile.html, view is core/views/profile
		- would like to have this apply to all users regardless of whether hosts or not
		
3C. blcobox.co/dashboard (template: core/templates/dashboard.html)
	- view is core.views.dashboard
	- form for tracking (modal) is in transactions.forms.trackingform
	
	-Actions
		-Share via social
		-Share via email
		-Share via postcard
		-Share via flyers
		-Share via link

3C. blocbox.co/scheduling: access the schedule app. templates are at /schedule/templates/schedule
		Main URL (blocbox.co/schedule) pulls the template calendar_list.hmtl, which extends /schedule/templates/site_base.html (one level up)
		http://www.blocbox.co/scheduling/calendar/tri_month/testcalendar1/: is the tri_month calendar view for testcalendar1, template at:  ca
		Yearly View: www.blocbox.co/scheduling/calendar/year/[calendarname], template at calendar_year.html, it loads the _monthly_table.html per month		

*-----------------------------------------------------------------------*
4. TRANSACTION PAGES
*-----------------------------------------------------------------------*

4A. blocbox.co/startashipment (template: core/templates/blocbox/startashipment.html, view is core/views/startafavor
	- links to a host site if you only have one: blocbox.co/starashipment/host10 (if only connected to 10)
	- if connected to multiple, givesyou the option to pick
	- once the host is connected, you select the shipment speed - this links to
			blocbox.co/startashipment/host10/days3to4 where 3 = dayrangestart and 4 = dayrangeend

4B. 	blocbox.co/startafavor (template: core/templates/blocbox/startafavor.html, view is core/views/startafavor
			- issue: if they are connected to multiple hosts do they really need to "select" one or is it more of a bid? e.g., who will take? this may b ea next-level step 
				since at beta people will only have one host. but this is an issue unique to other favors, since "start a shipment" host sleection is deterined by 
				user preference (where they want the shipment to go) but that doesn't really apply to other favors as much, which may be more like a bid - 
				thats also true because everyone presumably will do shipping, but not everyone wil do the other favors
			- need a better phrase

4C. 	blocbox.co/payment (no form - just base template) + blocbox.co/payment/ipn (instant payment notifcaiont - shittier) and blocbox.co/payment/pro (better)
			Template: core/templates/payment.html; URL patterns defined in blocbox/billing/urls.py
			View: /blocbox/billing/views.py, which passes a form called PaypalPaymentsForm defined in paypal/standard/forms.py
			For IPN or PRO The template loads the form with the statement	{{ form.render }} 
			blocbox.co/payment/ipn/notify is the notify_url
			Paypal app documentation: /blocbox/paypal/documentation/README.md -- i am annotating that documentation
			
			Transaction table entries are creted by the view blocbox.paypal.standard.ipn.views.ask_for_money
			this view is called by two URLS, both defined in blocbox.billing.urls.py
						shipment: blocbox.co/payment/host<host_id>/days<dayrangestart>to<dayrangeend>/ipn/package/<paymentoption>
						other favor: blocbox.co/payment/hos<host_id>/ipn/<favortype>/<paymentoption>
	
	
			ISSUE: this is creating transactions prior to the submit button being pressed - i want the transactino to only be created once they've gon to paypal
			
	
			Payment table entires are created by that view, which calls the blocbox.paypal.standard.ipn.views.ipn view, when the "pay with paypal" puttin is submitted
			
			PAYPAL IPN BASE TABLE IS AT: paypal.standard.models.py - cann add fields there
						
			NOTES ON THE PAYMENT PAGE (was formerly on the html page)
        <p>There is currently no form at blocbox/payment - there a form at blocbox.co/payment/ipn and a PRO form at blocbox.co/payment/pro</p>
        <p>The button image was intially a really disgusting 'buy it now' picture with credit cards I updated it to link to your paypal image but i modified the CSS paypal style bcit was too wide relative to height and the margins weren't working within a form.</p>
        <p>This currently links to a 'Sandbox' paypal account, a cool development feature that allows you to link to fake paypal accounts</p>
			
		

4D. blocbox.co/shippackage (template: core/templates/shippackage.html)

	- Data presented
		-Host Name
		-Host Address


*-----------------------------------------------------------------------*
5. MESSAGING RELATED PAGES
*-----------------------------------------------------------------------*

5A. blocbox.co/messages: access the django_messages app
		this automatically goes to blocbox.co/message/inbox - template is at django_messages/tempaltes/django_messages/inbox.html, extends base.html in smae dir


*-----------------------------------------------------------------------*
6. SCHEDULE/CALENDAR APP - HOW IT WORKS
*-----------------------------------------------------------------------*
6a. Schedule templates: blocbox/schedule/templates/schedule
			calendarbase.html extends base.html extends schedule/templates/site_base.html extends blocbox/core/tempaltes/blocbox/base.html
6B. Schedule Tables:
		Calendar: lists each of the calendars,
				fields: "name" and "slug' - dont know the difference
				i think we need separate one for each user, so name should be tied to user
		Calendar relations: lists relationship between a calendar and a user
			
		Events
		Rules
6C. Views: most called by schedule.views.calendar_by_periods	
6D. Schedul tAgs: schedule.template.scheduletags.py - has lots of the naming convetions for referencing scheduling tags

timezones: to see them all, python > print.pytz.all_timezones

*-----------------------------------------------------------------------*
7. AFTERSHIP STUFF
*-----------------------------------------------------------------------*
- API key is in settings.py
- https://www.aftership.com/trackings - is the list of trackings, our account is admin@blocbox.co pwd 123G**
- need to add trackings from dashboard or from other programs that post it to afteership - if add from admin, wont register
- what i'm trying to do when tracking numbe ris added (core.views.dashboard defines this) is add it to the aftership site AND
		grab the afterhsip data and put it into our own tracking table. The issue is that the aftership API is slow.. doesn't immediately update-
		so it doesn't immediately update shipment_type of expected_delivery or 
- so, need a way to automatically update our transaction table with the afters hip stuff OR.. we just always pull form afterhip API and dont update our trans table
- isntead, dont update trans tablw tih all that information immediately -
- but, once transaction is completed - grab updated data from aftership so we can store it

*-----------------------------------------------------------------------*
END: DJANGO ADMIN SITES
*-----------------------------------------------------------------------*
- core apps are defined in blocbox.core.admin.py - but this creates issues when you update models
- admin site for paypal is paypal.standard.ipn.admin.py

END-USER NARRATIVE

1. Land on home page
2. Select “get started” to navigate to search page
3. Choose host to navigate to host page
4. User reviews host - selects “connect” to navigate to sign up
5. User fills in info - hits submit to navigate to welcome page
6. Welcome page explains the wait to get confirmation - encourages user to share with friends and complete profile
7.User receives email confirmation of host connection - email provides link to dashboard or multiple links also to include “start a shipment” and to connected host profile
8.User selects to start a shipment (from email or host page or dashboard)
9. User confirms host, host address
10. User selects shipping option
11. User confirms host available in shipping window and hits next to navigate to payment page
12. User selects payment option (per package vs subscription)
13. User confirms or activates paypal payment and hits next to navigate to order shipment page
14. User is notified that the host has been notified of incoming package
14. User copies host address into e-commerce site, completes purchase, hits next on BB site to navigate to dashboard
15. Dashboard displays incoming package information, with option to provide tracking information
16. User receives shipping confirmation from e-commerce site
17. BB sends user a email prompt to enter tracking info two days after entry(?)
18. User enters tracking information into dashboard.
19. User receives notification that host has received package with reminder of host availability
20. User travels to host address to pick up package.
21. User receives confirmation of receipt of package (after host has confirmed handoff) and request to review experience.


 	