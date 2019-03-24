#!/bin/env python3

import mailbox
import psycopg2

MDIR='./var/vmail/tintagel.pl/mulander/Maildir/OpenBSD/Misc'

index_email = """
    INSERT INTO
         emails(file_path, subject   , body,
                document)
         VALUES(%(path)s, %(subject)s, %(body)s  ,
                setweight(to_tsvector('english', %(subject)s), 'A') ||
                setweight(to_tsvector('english', %(body)s), 'B'))
                ;
"""

conn = psycopg2.connect(user="postgres")

m = mailbox.Maildir(MDIR)

fail_decode = 0

with conn.cursor() as cur:
    for path, email in m.iteritems():
        try:
            body = email.get_payload(decode=True)
            if body is None:
                body = ''
            else:
                body = body.decode('UTF-8')
            cur.execute(
                    index_email,
                    {
                        'path': path,
                        'subject': email.get('subject'),
                        'body': body,
                    })
            print("OK : {}".format(path))
        except UnicodeDecodeError:
            fail_decode += 1
            print("ERR: {}".format(path))

conn.commit()
conn.close()

print(fail_decode)

