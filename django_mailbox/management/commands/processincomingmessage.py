import email
import logging
import rfc822
import sys

from django.core.management.base import BaseCommand

from django_mailbox.models import Mailbox


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):
    args = "<[Mailbox Name (optional)]>"
    command = "Receive incoming mail via stdin"

    def handle(self, mailbox_name=None, *args, **options):
        message = email.message_from_string(sys.stdin.read())
        if message:
            if mailbox_name:
                mailbox = self.get_mailbox_by_name(mailbox_name)
            else:
                mailbox = self.get_mailbox_for_message(message)
            mailbox.process_incoming_message(message)
            logger.info(
                "Message received from %s",
                message['from']
            )
        else:
            logger.warning("Message not processable.")

    def get_mailbox_by_name(self, name):
        mailbox, created = Mailbox.objects.get_or_create(
            name=name,
        )
        return mailbox

    def get_mailbox_for_message(self, message):
        email_address = rfc822.parseaddr(message['to'])[1][0:255]
        return self.get_mailbox_by_name(email_address)
