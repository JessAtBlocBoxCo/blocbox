from billing import gateway
from django.conf import settings
from billing import CreditCard

# Added the Following to /blocbox/billig'views.py or wherever you want to use it
#Django-Merchan stuff - from http://django-merchant.readthedocs.org/en/latest/overview.html#overview
g1 = get_gateway("authorize_net")
cc = CreditCard(first_name= "Test", last_name = "User", month=10, year=2011, number="4222222222222", verification_value="100")
response1 = g1.purchase(100, cc, options = {...})
#response1
#{"status": "SUCCESS", "response": <AuthorizeNetAIMResponse object>}
g2 = get_gateway("pay_pal")
response2 = g2.purchase(100, cc, options = {...})
#response2
#{"status": "SUCCESS", "response": <PayPalNVP object>}