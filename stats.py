#!/bin/env python3

import mailbox
from collections import Counter

MDIR='/home/mulander/pg/var/vmail/tintagel.pl/mulander/Maildir/OpenBSD/Misc'

m = mailbox.Maildir(MDIR)

emails = 0
multipart = 0
types = Counter()

for email in m.itervalues():
    emails += 1
    if email.is_multipart():
        multipart += 1
        for part in email.walk():
            types[part.get_content_type()] += 1

print(emails)
print(multipart)
print(types)
