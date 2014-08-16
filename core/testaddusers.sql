/*
from core.models import User, Transaction
u = User(email="test1", password="pass1", date_join=timezone.now(), zipcode=)
u.save()
*/

/*To Drop tables use:
DROP TABLE core_transaction; DROP TABLE CORE_USERINFO; */

/*Using John's old BK Address:  360 Grand Ave, Brookly, NY 11238 */
INSERT INTO CORE_USERINFO (email, password, date_join, zipcode, st_address, city, state, fname, lname, host, hostinterest)
VALUES ('jburgeson@gmail.com', 'password', now(), '11238', '360 Grand Ave', 'Brooklyn', 'NY', 'John', 'Burgeson', True, True);


INSERT INTO CORE_USERINFO (email, password, date_join, zipcode, st_address, city, state, fname, lname, host, hostinterest)
VALUES ('BedStuy1@gmail.com', 'password', now(), '11205','','Brooklyn', 'NY', 'Fname1', 'Lname1', False, False);

INSERT INTO CORE_USERINFO (email, password, date_join, zipcode, st_address, city, state, fname, lname, host, hostinterest)
VALUES ('BedStuy2@gmail.com', 'password', now(), '11206','','Brooklyn', 'NY', 'Fname2', 'Lname2', False, False);

INSERT INTO CORE_USERINFO (email, password, date_join, zipcode, st_address, city, state, fname, lname, host, hostinterest)
VALUES ('BedStuy3@gmail.com', 'password', now(), '11216','','Brooklyn', 'NY', 'Fname3', 'Lname3', False, False);

INSERT INTO CORE_USERINFO (email, password, date_join, zipcode, st_address, city, state, fname, lname, host, hostinterest)
VALUES ('BedStuy4@gmail.com', 'password', now(), '11221','','Brooklyn', 'NY', 'Fname4', 'Lname4', False, True);

INSERT INTO CORE_USERINFO (email, password, date_join, zipcode, st_address, city, state, fname, lname, host, hostinterest)
VALUES ('BedStuy5@gmail.com', 'password', now(), '11233','','Brooklyn', 'NY', 'Fname5', 'Lname5', False, True);

/* williamsburg zip coes  11206, 11211, 11249 */
INSERT INTO CORE_USERINFO (email, password, date_join, zipcode, st_address, city, state, fname, lname, host, hostinterest)
VALUES ('Williamsburg1@gmail.com', 'password', now(), '11206','','Brooklyn', 'NY', 'Fname6', 'Lname6', False, False);

INSERT INTO CORE_USERINFO (email, password, date_join, zipcode, st_address, city, state, fname, lname, host, hostinterest)
VALUES ('Williamsburg2@gmail.com', 'password', now(), '11211','','Brooklyn', 'NY', 'Fname7', 'Lname7', False, False);

INSERT INTO CORE_USERINFO (email, password, date_join, zipcode, st_address, city, state, fname, lname, host, hostinterest)
VALUES ('Williamsburg3@gmail.com', 'password', now(), '11249','','Brooklyn', 'NY', 'Fname8', 'Lname8', False, False);



