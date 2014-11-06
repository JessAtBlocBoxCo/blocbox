this is blocbox/readme.txt

The templates (.html files) that you will edit are all stored at blocbox/core/templates/blocbox

If you ever need to figure out teh path to a file, you cal right-clik on the apge and "vewi source" - at the top of the file i try to include the path to all html tempatles


The URLs for this site, and the corresponding files are as follows:

1. blocbox.co
	- this is the waitlist page
	- the template is at blocbox/core/templates/blocbox/index.html

2. blocbox.co/beta/
	- this is the beta page
	- the template is at blocbox/core/templates/blocbox/beta.html

3. blocbox.co/search/
	- this is the search page (after clikign on "Get started")
	- the tempalte is at blocbox/core/templates/blocbox/search.shtml
	- teh styles/css need to be fixed
	
4. blocbox.co/3/hostprofilevisitor/ 
	- this is John's host profile profile. 
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

5. blocbox.co/3/signupconnect/
	- this is the page to sign-up and connect to John - "3" corresponds to USERid=3, but you can replace with "1", eg.,. to connect to jess. same as above
	- teh template is at blocbox/core/templates/blocbox/sign-up-connect.html,but it extends a template at basesignup.html (via sign-up-withtoutconnect.html)
	- if you want to change the basic form structure, you need to edit basesignup.html
	
	- What happens when a user submits/clicks "Sign up and REquest to Connect"
			- They are registered as a user on user_info table
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

6. blocbox.co/signup/
	- this is the page to sign-up WITHOUT CONNECTING to a particular host - so it passes no arguments in the url
	- the template is at blocbox/core/templates/blocbox/sign-up-withoutconnect.html
	
7. blocbox.co/login/
	- this is the login page
	- the template is at blocbox/core/templates/blocbox/sign-in.html

8. blocbox.co/startshipment !!! JESS NEEDS TO CREATE TEMPLTE !!!
	- Data presented
		-Host name
		-Host address
		-Shipping Options
		-Host availability

	- Data requested
		-Host Choice
		-Shipping Options

9. blcobox.co/payment !!! JESS NEEDS TO CREATE TEMPLATE !!!

	- Data presented
		-Package pricing
		-Paypal Account (If linked)

	- Data requested
		-Payment plan selection

10. blcobox.co/shiporder !!! JESS NEEDS TO CREATE TEMPLATE !!!

	- Data presented
		-Host Name
		-Host Address

11. blcobox.co/dashboard !!! JESS NEEDS TO CREATE TEMPLATE !!!
	- Data presented
		-User picture
		-User name
		-User address
		-User phone
		-Current Shipments (tracking number, host, host address, delivery date)
		-Current Favors (description, host, host address, expiration date)
		-Recent Shipments (tracking number, host, host address, delivery date)

12. blocbox.co/welcome !!! JESS NEEDS TO CREATE TEMPLATE !!!

	- Data presented
		-User name (Nav Bar/"Welcome to Blocbox John!")
		-Host name ("an invitation has been sent to John”)

	- Data requested
		-User personal introduction
		-User notification preferences
		-Profile picture upload
		-Paypal/payment activation
	-Actions
		-Share via social
		-Share via email
		-Share via postcard
		-Share via flyers
		-Share via link
		

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


 	