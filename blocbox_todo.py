
"PRIORITIES: MUST HAPPEN BEFORE JOHN-ONLY BETA"
2. NEXT DOOR POST. 
3. BODEGA - APPROACH SOME -- tomorow en route out of how / 
4. BRAINSTORMING next step for user acquisition: handing out at post office
1. LANDING/SIGN IN
2. SHIPMENT PROCESS AND PAYMENT PROCESS
3. SIGNUP PROCESS
4. DASHBAORD
5. MESSAGING/NOTIFICATIONS
6. SEARCH
7. USER PROFILE
8. HOST PROFILE
9. HOST SIGN UP
10. MYBLOCK
11. OTHER FAVORS

"""JESS QUESTIONS/ISSUES FOR JOHN TO ADDRESS"""
1. on baseorange.html on like 425-ish it says "limitless possibilities" but links to the "privacy" page -- what is it supposed to link to? 
...likewise "trust and safety" links to "signuphost" and "invite your neighbors" also to "signuphost"
-- what pages should they be linking to?
2. also - do we have a contactus page?                           
3. created page: contactus - the support and contactus url both point to the same pag
4. created 'account' page --not convinced we need this in addition to dashboard and profile but i will let you sort that out. no strong opinions
5. what does the messages settings page entail?

	
"PRIORITIES POST JOHN BETA"
13. SHARING MECHANISMS.
12. INSURANCE 


"JESS TO-DO"


1.    
JESS: landing - fix anchor links to "how it works"
	JESS: add pages: Messages settings

2.
JESS: signin - fix invalid login credentials plac e- redirect to a forgot password
JESS: signin - Remove sign in after welcome page
JESS: signin - Link to become a host (on nav) - When signed in presents message, "Looks like you're already signed in! Sign out if you'd like to register as a new user Or, you can visit your dashboard or search for a new host to connect with.”

3.
fold tolgether first two pages of shipment into one: 
fix expected delivery window: number of days
JESS: shipment - Fix the shipment message to user 
JESS: shipment - availalbility days - change ot business days - update availability app so that its business days
JESS: shipment - availability - change button logic if have conflict button says "i accept accountability" or whatever.
JESS: shipment - pass the host_package-conflict indicator to the transaction table\\-
JESS: shipment - fix the day in week/warning thing - it need to be day of month
JESS: shipment - calendar: define a function when user enters date from and date to that forces date to to be after date_from]]
JESS: shipment - issue with payment option (bundled vers speciifc) and per-package items like "status" - thse are difference sorts.. so paypal shoudl just be for the money, transactions table for the favor/shipment/transaction
JESS: shipment - tracking information - automate that/connect to carrier - also figure out which tracking number code matched to what carrier
JESS: shipment - figure out what to do with conflicts that end more in more than the next month out - add a new month?
JESS: shipment - select a host - then the process - LOAD - to connect to a host...
JESS: shipment - shippackage: connect the host address fields to data table so populate,
JESS: shipment - paypal PDT
JESS: shipment - paypal PRO	
JESS: shipment - NOTE: when i implement the PRO version, need to update URL to /pro/ rather than /ipn/ -
JESS: shipment - update readme to describe navstaratshipment, et

4.
JESS: signup - after completing sign up page, it directs to a page that thanks them and asks them to sign in. Can they go directly to their dashboard? If not, the link to sign in on the thank you page should trigger the sign in modal, not take them to a stand-alone sign in page.
JESS: signup - page - add additional required fields (name, adddress, etc)
JESS: signup - request to connect - add errors if already connected
JESS: signup - fix the connect/host2 thing - connecting if already a user - make sure the emails are sending to thoe host, add a field for confirmed, right now its logging as connected een before host confirms

5.
JESS: dashbaord - Upload a picture not working
JESS: dashboard - finish for other transactions
JESS: dashbaord - stop error message if people visit the dashboard without login - just re-rout them to login or sign up
JESS: dashboard - create a field for profilepic links - the NULL/DEFAULT value is images/profilepics/blankprofilepic.png
JESS: dashboard - connect to transactions table to populate actually transactions

6.
JESS: messages - connection success email to user - add link in email to sign in
JESS: messages - Change {{ message.sender }} to first and last name instead of email
JESS: messages - Inbox - Change {{ message.sent_at|date:_("DATETIME_FORMAT") }} to month and date (ex. May 7)
JESS: messages - notification prefeernces defaul - profile
JESS: messages - notice preference by package - dashboard
JESS: messages - discuss with john: SMS notifications for aftership? 4 cents per SMS.. may not be worth it since meail is so close
JESS: messages - email notifications - allow users to opt in or out
JESS: messages - Inbox: call a snippet from the message, like {{ message.snippet }}, change delete and trash to “archive”?, Change {{ message.sender }} to the user name (e.g. “John”)?
JESS: messages - add to email sent to host - the text they fill in for when they usually get packages

7.
JESS: search - search bar placement
JESS: search - after entering new search address, host pin disappears, also zooms in very close
JESS: search - page is taking a reall long time to load with the urls
JESS: search - update search page for host pics
JESS: search - google map - link the search page to the fields in table so it automatically popualtes with hosts nearby (e.g., not hard coded)
JESS: search - later: figure out how to make it automatically register lat/long - right now we need to manually enter it for hosts

8.
JESS: user profile - make an upload picture modal
JESS: user profile - pics: make individualized/link to specific hosts
        
9.
JESS: host profile - make the process for hosts to enter their availability
JESS: host profile process
JESS: host profile:  verified info: if not connected, say "Verified Info" --
JESS: host profile - verified info on HPV - only show symbol if verified, then in connect version show the DATA.
JESS: host profile - update "when i'm home" informatiorfn for host profile... visitor
JESS: host profile - update table to have fields for what other services they are offering

10.
JESS: myblock - : fill this in = sjpw who you are connected to- just do basic list
JESS: myblock - update back-end of "my block" page after john adds themap and after youve fixed the search page to populate from the table

11.
JESS: other favors -  to form and table - add need_meals
JESS: other favors - add two use cases (1) wifi sharing; (2) community dinners/food as a use-case.. add this totable adn then also update the checkboxes: add NEED_MEALS
        
        
        
"JOHN TO-DO"


2.    
JOHN: landing - there should be a direct tlink to signing up as a host on the landing page. i think it shoudl say "esarch for a host in your neighborhood to get started" (less verbose though) and then a separate button saying "sign up to be a host"

4.    
JOHN: dashboard - Styling boxes
JOHN: dashboard - Style fonts
JOHN: dashboard - Placeholders or hide boxes when now shipments in process
JOHN: dashboard - Legend for the calendar
JOHN: dashbaord - the profile pictures ar enow upload-able and linked to the folder /home/django/blocbox/blocbox/static/user_uploads
this is true on the profile and dashboard page on profle - you need to appply the sahe "dashpic" and "Dashcoainter" type of styles you did to the dashboard if you want it to look better
JOHN: dashbaord - style the profile pic - so the user uplaodssimplepic, and then converted to glossy bubble

5.    
JOHN: messages - Style when no messages
JOHN: messages - inboxpic
    
6.
JOHN: search - host box on mobile

7.
JOHN: user profile -  page - style

8.
JOHN: host profile - style profile page
JOHN: host profile - create HOSTdashboard - or version of this for this host.
JOHN: host prpfile - add green check box next to verified info
JOHN: host profile - create the host profile or dashboard with things like options for setting prices

9.
JOHN: myblock - update "my block" p age with th enice map that you first crated

10.
JOHN: other favors - add process/for other favors


"BOTH TO-DO"
BOTH: need to re-think "start a favor" - need a better term
        
"NOTES"
8. SIGN-UP: two bowls of shit, one bowl, then sneaky second bowl of shit

"""JESS NOTES/QUESTIONS FOR JOHN"""
1. do we need to split up dashboard containers by type of transaction or can we just have a field/colum for that (e.g, shipments and dog walkign one)
2. dashboard: HOW DO WE WANT THESE TABLES TO LOOK ON MOBILE?-->            
3. dashboard: -THE TABLE FORMAT MAY BE TOO RESTRICTIVE - AMAZON, ETC - IN THE RECENT ORDERS, THEY ALL USE BOXES RATHER THAN TALE FORMAT-->

"""Jess - transaction tasks"""
1. allow the user to modify the paypalIPN table - add fields later - like tracking, 
2. add tracking
1. update the startashipmetn process so reload based on selected host
2. add a bunch of fields to the IPN table to correspond with waht john wants in dashboard
2. dashboard - need to split up those tables and variable calls according to whether the paymet is done or not (current vs recent)
1. LOG THE USER information on admit from the transacion table -- right now, the payers is whoeverl ogs into paypal - 
- we need to log that AND TEH user that was logged in that went to paypal..
2. create testdashboard with transaction talbe - link IPN table to dashboard
3. sort out receiver_email - is this admin@blocbox.co or is this the host?
1. set up IPN (instant payment notifiation) - this kind of sucks b/c drops customers off at paypla.. but easiers
2. set up "pro" -- enabling users to pay on the website
3. oce i've set up the blocbox.co/payment/ipn and blocbox.co/payment/pro - merge the base view (blocbox.co/payment) with pro.. rmoeve the other two'
5. dashboard - way down road: have recent transactions limited to last 60 days, with archie option - or multiple pages

"""longer term to-do- add to trello"""
1. host sign-up for users that are already registered - should this process be different?
2. tracing - instead of using that widget, use UPS, USPS etc APIs - 
3. create notification to users automatically when its delivered  - will need ot integrate those APIs first
4. current shipments  better word?
5. implement pay later policy/ pay once package is received

"""JESS NOTES ON HOW TO ISNTALL DJANGO PACKAGES"""
#they install at:

#3. footer is cropping up

#4. landing page may be broken.


# build out the process for a non-package transaction



6. Email Confirmation (not a page)

(user receives confirmation email indicating the host has accepted them. Links in email to �Start a shipment with John�, �John�s Host Profile Page�, Your dashboard�? )




A. Should we design the email to show as part of demo?




7. Start a Shipment

A. Push

Host name

Host address

Shipping Options

Host availability




B. Pull

Host Choice

Shipping Options




8. Payment




A. Push

Package pricing

Paypal Account (If linked)




B. Pull

Payment plan selection




9. Ship Your Order




A. Push

Host Name

Host Address




10. User Dashboard
"""
	A. Push
		User picture
		User name
		User address
		User phone
		Current Shipments (tracking number, host, host address, delivery date)
		Current Favors (description, host, host address, expiration date)
		Recent Shipments (tracking number, host, host address, delivery date)
"""

#add a field to the user_info that shows the first host the user connected to - NULl is OK for this b/c sometimes wont have connected to anyone...

#. finish paypal/payment thing
https://github.com/spookylukey/django-paypal
# views.py
...
from paypal.standard.forms import PayPalPaymentsForm

def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "https://www.example.com" + reverse('paypal-ipn'),
        "return_url": "https://www.example.com/your-return-location/",
        "cancel_return": "https://www.example.com/your-cancel-location/",

    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render_to_response("payment.html", context)

<!-- payment.html -->
...
<h1>Show me the money!</h1>
<!-- writes out the form tag automatically -->
{{ form.render }}



1. create superuser accounts for john, also maybe me so we dont need to log in as root
2. clean up messaging system - create structure/dashboard/
3. figur eout django-dash/dashboard app




1. EDIT host profile page so it looks different if youre  connnecte d- like {%if registered}

3. START A SHIPMENT process -if connected - start programming that

3. create host table - subset of core_userinfo
4. create pickup_from and pickup_to, see if we can use time field types


#Long Term
 -- add a thank you/confirmation email for the users that signup with WITHOUT CONNECTING
--Fix the admin site/ can be more intuitive/cleaner
--Particularly need to updat the Connections mode view in admin - want to see the connectiosn from each host
-- ADD FIELD: phone_number
-- embed SMS notificaitons
1. Approximate Address right now we have address in... it should be a APPROXIMATE ADDRESS, : address_approx, neighborhood, city, state
					say "cross-strees... connect with john to see address"


Update Git so that we can push to two remotes, so it automatically pushes to github and it pushes to the server?
	git remote set-url --add --push origin git://another/repo.git
	git remote set-url --add --push origin git://one_more/repo.git
So when you push to origin, it will push to both repositories








"""SOME NOTES"""
1. revoles the reverse() function -- it matches urls in blocbox/urls.py but doenst match names in other url docs
			ISSUE IS NAMESPACING
			"URL namespaces allow you to uniquely reverse named URL patterns even if different applications use the same URL names. 
			It’s a good practice for third-party apps to always use namespaced URLs (as we did in the tutorial). 
			Similarly, it also allows you to reverse URLs if multiple instances of an application are deployed. In other words, since multiple instances of a 
			single application will share named URLs, namespaces provide a way to tell these named URLs apart.
			Django applications that make proper use of URL namespacing can be deployed more than once for a particular site. 
			For example django.contrib.admin has an AdminSite class which allows you to easily deploy more than once instance of the admin. 
			In a later example, we’ll discuss the idea of deploying the polls application from the tutorial 
			in two different locations so we can serve the same functionality to two different audiences (authors and publishers)."
			






#done
1. transfer the host for blocbox.co to the digitalocean server:
2. add a forgot password/chnage password
1. JESS: beta.html: fix that shit with the margin padding on right-hand side
			- add "start a shipment" to navbar
			- nabbar needs to be drop0down is totally fucked - the list shows up to left
			HPV-- remove "this is test host_aboutme message" - change the text a bit

2. JESS: base.html -  Navbar  navbar height should be bigger on desktop
		--JESS HPV - count number of connections... - - MAKE A FUNCTION TO COUNT NEIGHBORS YOU ARE HELPING
1. JOHN: add his profile picture to HPV.
23. JOHN shippackage: add weights
16. JOHN: startashipment -

		-- select ta host - merge thea ddress into drop-down .. wider button - and get rid of the address and get directions
			-- have button say "select" and have an option..for john, with address, have an option "select host"
			-- consider resizing text
			-- confirm availability - fill out drop down menu (fedex, ups, etc)..
				--confirem availability - ONE dropdown - e.g., "fedex, 2 day", "USPS priority (2 day", usps 7-10 days..
				-- john add note around aviability: "Here's our avaiability policy: hosts are required to regularly update their availability.
																							Hosts are accountable for all packages delivered on days that they commmited to being available.
																							If they miss the package, you will not be charged, and the host is responsible for tracking down the missed delivery.
																							However, if you send a packaget to a host that might arrive on a day when they have stated they are unavailable,
																							you will be charged even if the host misses the delivery.  You're likely to still get the package, but it may not be available for pickup
																							until a later date."
15. JOHN dashbaord: add a "start a shipment" action button or link or wahtever to dashboard
			-- Add "wghen i'm home" field..... connect to availability
 		-- to userinfo: whenimhome_days
 										whenimhome_hours

3. when connected to the user, dont say "sign up to connect" -so edit that languager
2. JESS HPV - rather tha 'If authenticated' show approx address etc.. say if connected.. remember how to do that

- remove week numbers
	- create a two-month version (this month and next)
	- do a two-month version OR  one-month showing next week of folowing month
7. JOHN MYBLOCK: code a basic version of this
4. JOHN: payment pagee
			-- update payment options in first block
			-- add link to shipapackage from the payment page
-- HPV,
2. JOHN waitlist: fix the colors
3. JOHN: start a shipment: add a hyperlink to the payment page when the user "submits"

"#Test tracking nos to add"

TBA001951235001  - xlear refil (AMZN PARCEL?), delivered  - NOT SUPPORTED BY AFTERSHIP
9400115901531302012915 - tile for parents

#ALREADY TRACKED
1ZE6E4990234405990  = iphone armband and gum, delivered
1Z88Y70A0244854175  - ankar keyboard and mouse
9205599999975642680357 - pillow case, delivered 
591099350463 -- headbands, celivered
1Z2W6185YW01658200  = laptop case, delivered
9449009699938097189973 - johns - not yet delivered?
9374869903500264240007 - DHL global mail,  not delivered?
1ZX1A509YW10497241 - neti pot, not delivered (UPS)
9405509699939563285640 - black boots, already arrivedUSPS priority, already arrived - wnat to see if the type is updated
615774528257  - sleeping mask, not delivered
1ZA3225FYW43921778 - bars
