from django.conf import settings
from django.core.mail import send_mail


send_mail('Subject here - test test', 'This is a test message from my gmail (first address) to admin@blocbox.co (second).', 
					'jessica.yeats@gmail.com',
    ['admin@blocbox.co'], fail_silently=False)
