from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from core.models import UserInfo, Transaction

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    zipcode = forms.CharField(label="Zip Code")

    class Meta:
        model = UserInfo
        fields = ('email', 'password', 'password2', 'zipcode', 'hostinterest', 
            'first_name', 'last_name', 'zipcode', 'st_address1', 'st_address2', 'city', 'state',
            'about_me', 'intro_message', 'pickup_time', 'FBlink', 'imageurl', 'userrating', 'host',
            'need_storage', 'need_petcare', 'need_housesitting', 'need_rentals', 'need_laundry', 'need_letin',
    				'need_childcare', 'need_plantcare', 'need_lawn', 'need_carsharing', 'need_housemaint', 'need_autocare', 'need_other'
            )

#The hostPRofileForm should include the UserProfileForm and other stuff specific to host
#Need a second about_me field for hosts that is required
class HostForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('host_aboutme', 'services_offered', 'availability', 'hostrating',)
      

#Create a form for confirming connections
#class ConfirmConnectForm(forms.ModelForm):
        

#CREATE A TRANSACTION FORM
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('host', 'enduser', 'payer', 'payee')
"""
class PayPalPaymentsForm(forms.Form):
    CMD_CHOICES = (
        ("_xclick", "Buy now or Donations"),
        ("_donations", "Donations"),
        ("_cart", "Shopping cart"),
        ("_xclick-subscriptions", "Subscribe")
    )
    SHIPPING_CHOICES = ((1, "No shipping"), (0, "Shipping"))
    NO_NOTE_CHOICES = ((1, "No Note"), (0, "Include Note"))
    RECURRING_PAYMENT_CHOICES = (
        (1, "Subscription Payments Recur"),
        (0, "Subscription payments do not recur")
    )
    REATTEMPT_ON_FAIL_CHOICES = (
        (1, "reattempt billing on Failure"),
        (0, "Do Not reattempt on failure")
    )

    BUY = 'buy'
    SUBSCRIBE = 'subscribe'
    DONATE = 'donate'

    # Where the money goes, 
    business = forms.CharField(widget=ValueHiddenInput(), initial=RECEIVER_EMAIL)
    
    # Item information.
    amount = forms.IntegerField(widget=ValueHiddenInput())
    item_name = forms.CharField(widget=ValueHiddenInput())
    item_number = forms.CharField(widget=ValueHiddenInput())
    quantity = forms.CharField(widget=ValueHiddenInput())

    # Subscription Related.
    a1 = forms.CharField(widget=ValueHiddenInput())  # Trial 1 Price
    p1 = forms.CharField(widget=ValueHiddenInput())  # Trial 1 Duration
    t1 = forms.CharField(widget=ValueHiddenInput())  # Trial 1 unit of Duration, default to Month
    a2 = forms.CharField(widget=ValueHiddenInput())  # Trial 2 Price
    p2 = forms.CharField(widget=ValueHiddenInput())  # Trial 2 Duration
    t2 = forms.CharField(widget=ValueHiddenInput())  # Trial 2 unit of Duration, default to Month    
    a3 = forms.CharField(widget=ValueHiddenInput())  # Subscription Price
    p3 = forms.CharField(widget=ValueHiddenInput())  # Subscription Duration
    t3 = forms.CharField(widget=ValueHiddenInput())  # Subscription unit of Duration, default to Month
    src = forms.CharField(widget=ValueHiddenInput()) # Is billing recurring? default to yes
    sra = forms.CharField(widget=ValueHiddenInput()) # Reattempt billing on failed cc transaction
    no_note = forms.CharField(widget=ValueHiddenInput())
    # Can be either 1 or 2. 1 = modify or allow new subscription creation, 2 = modify only
    modify = forms.IntegerField(widget=ValueHiddenInput()) # Are we modifying an existing subscription?

    # Localization / PayPal Setup
    lc = forms.CharField(widget=ValueHiddenInput())
    page_style = forms.CharField(widget=ValueHiddenInput())
    cbt = forms.CharField(widget=ValueHiddenInput())

    # IPN control.
    notify_url = forms.CharField(widget=ValueHiddenInput())
    cancel_return = forms.CharField(widget=ValueHiddenInput())
    return_url = forms.CharField(widget=ReservedValueHiddenInput(attrs={"name": "return"}))
    invoice = forms.CharField(widget=ValueHiddenInput())
		
		#adding host and enduser email form-- can't do  this.. not registered
    #host_email = forms.CharField(widget=ValueHiddenInput())
    #enduser_email = forms.CharField(widget=ValueHiddenInput())
    custom = forms.CharField(widget=ValueHiddenInput())
    receiver_id = forms.CharField(widget=ValueHiddenInput())
		
    # Default fields.
    cmd = forms.ChoiceField(widget=forms.HiddenInput(), initial=CMD_CHOICES[0][0])
    charset = forms.CharField(widget=forms.HiddenInput(), initial="utf-8")
    currency_code = forms.CharField(widget=forms.HiddenInput(), initial="USD")
    no_shipping = forms.ChoiceField(widget=forms.HiddenInput(), choices=SHIPPING_CHOICES,
                                    initial=SHIPPING_CHOICES[0][0])

    def __init__(self, button_type="buy", *args, **kwargs):
        super(PayPalPaymentsForm, self).__init__(*args, **kwargs)
        self.button_type = button_type
        if 'initial' in kwargs:
            # Dynamically create, so we can support everything PayPal does.
            for k, v in kwargs['initial'].items():
                if k not in self.base_fields:
                    self.fields[k] = forms.CharField(label=k, widget=ValueHiddenInput(), initial=v)

    def test_mode(self):
        return getattr(settings, 'PAYPAL_TEST', True)

    def get_endpoint(self):
        "Returns the endpoint url for the form."
        if self.test_mode():
            return SANDBOX_POSTBACK_ENDPOINT
        else:
            return POSTBACK_ENDPOINT


    def render(self):
        return mark_safe(u % (self.get_endpoint(), self.as_p(), self.get_image()))

		
    def sandbox(self):
        "Deprecated.  Use self.render() instead."
        import warnings
        warnings.warn(, DeprecationWarning)
        return self.render()

    def get_image(self):
        return {
            (True, self.SUBSCRIBE): SUBSCRIPTION_SANDBOX_IMAGE,
            (True, self.BUY): JB_PAYPAL_IMAGE, #SANDBOX_IMAGE, #defined in conf.py as "https://www.sandbox.paypal.com/en_US/i/btn/btn_buynowCC_LG.gif")
            (True, self.DONATE): DONATION_SANDBOX_IMAGE,
            (False, self.SUBSCRIBE): SUBSCRIPTION_IMAGE,
            (False, self.BUY): IMAGE,
            (False, self.DONATE): DONATION_IMAGE,
        }[self.test_mode(), self.button_type]

    def is_transaction(self):
        return not self.is_subscription()

    def is_donation(self):
        return self.button_type == self.DONATE

    def is_subscription(self):
        return self.button_type == self.SUBSCRIBE
"""
#end paypal form