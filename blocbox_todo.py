
"""WEB WORK: jOHN"""
1. add his profile picture to HPV.
2. fix mobile

"""WEBSITE WORK: JESS"""
1. fix that shit with the margin padding on right-hand side
2. Navbar 
		- is totally fucked - the list shows up to left
		- navbar height should be bigger on desktop
3. "done see a blocbox host in your hood"? -- MAKE IT LARGER
4. HPV -- remove "this is test host_aboutme message" - change the text a bit
5. HPV pricing - says "unlimited" BUT REALLY "10 PACKAGES/MONTH"
6. HPV - currently helping XX neighbors - fix XX
7. populate helpingneighbors filed for JOHN - - MAKE A FUNCTION TO COUNT NEIGHBORS YOU ARE HELPING
8. Add "when i'm home" field...
6. add an APPROXIMATE ADDRESS FIELD
5. HPV vs HP - we dont really need "visitor" site.. its just if-then.. just turn to hosprofile 
-- what differs when you are connected? 
				1. Approximate Address right now we have address in... it should be a APPROXIMATE ADDRESS, 
				2. verified info: if not connected, say "Verified Info" -- 
				3. when connected to the user, dont say "sign up to connect" -so edit that languager
7. jess: RE-LEARN SOUTH DATABASE MIGRATION.
6. dashboar d- add list of users connected

"""WEBSITE TASKS TO DO AFTER TUMML APP"""
1. JOHN: add green check box next to verified info
2. JESS: verified info on HPV - only show symbol if verified, then in connect version show the DATA.
3. JESS: update "when i'm home" information for host profile... visitor
4. JESS: update table to have fields for what other services they are offering
5. JESS: updating HPV so that it truly reflects what services you offer
# check oyt the pages john made

# fix the "beyond packages" text on baseorange


#3. footer is cropping up

#4. landing page may be broken.

"""PITCH WORK"""
#1. make an outline
#2. make the pitch
#3. 



# build out the process for a non-package transaction

# User Dashboard: rsearch carrier API embedd tracking capability ito the website

# Complete start-a-shipment

# Complete payment page

#4. Write Pitch Draft - outline with timing and suggestions for what slide should accompany

#5. HALP email

#6. Navbar/ drop downs

#7. Review stock questions (on gdrive) to ensure we have answers to all. NOT suggesting we write answers. We’ll review them this weekend.











6. Email Confirmation (not a page)

(user receives confirmation email indicating the host has accepted them. Links in email to “Start a shipment with John”, “John’s Host Profile Page”, Your dashboard”? )




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


Update Git so that we can push to two remotes, so it automatically pushes to github and it pushes to the server?
	git remote set-url --add --push origin git://another/repo.git
	git remote set-url --add --push origin git://one_more/repo.git
So when you push to origin, it will push to both repositories















#done
1. transfer the host for blocbox.co to the digitalocean server: 
2. add a forgot password/chnage password