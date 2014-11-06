#1.Build Welcome Page
"""

"""
#2.Build start-a-shipment page
"""
extend base.html


"""
#3. Build payment page
"""
extend base.html

"""
#4. Build Ship-package page
"""
extend base.html

"""
#5. Build User-Dashboard page
"""
extend base.hmtl

"""
#3. Build pages (Welcome, Start a Shipment, Payment, Ship package, User Dashboard) - all extended from base.html
"""

"""
#4. Write Pitch Draft - outline with timing and suggestions for what slide should accompany




3. Push/Pull for completed pages





4. HALP email




5. Navbar/ drop downs




6. Research carrier API for dashboard





7. Review stock questions (on gdrive) to ensure we have answers to all. NOT suggesting we write answers. We’ll review them this weekend.




JB Priorities:




1. Build pages (first, start a shipment page)

2. Once JY completes first draft of pitch outline, sketch outline/new deck slides







SITE/DEMO MAP




1. Landing (complete minus minor problems described in HALP email)




2. Search (complete)




3. Host Visitor Profile




A. Push

Host first name (done)

Host address (done)

Host favors requested (done)

Host about me (needs to be edited to strike last sentence)

Host currently helping

Host availability

Host other offers




4. Sign Up (complete)




A. Pull

User email

User Zip

User Password

User address

User intro

User pick up times

Other services

Service requests

Register as host

Interested in learning about hosting




5. Welcome to Blocbox




A. Push

User name (Nav Bar/"Welcome to Blocbox John!")

Host name ("an invitation has been sent to John”)




B. Pull

User personal introduction

User notification preferences




C. Functions (don’t need to be functional for demo)

Share via social

Share via email

Share via postcard

Share via flyers

Share via link

Profile picture upload

Paypal/payment activation




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




A. Push

User picture

User name

User address

User phone

Current Shipments (tracking number, host, host address, delivery date)

Current Favors (description, host, host address, expiration date)

Recent Shipments (tracking number, host, host address, delivery date)




1. finish paypal/payment thing
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