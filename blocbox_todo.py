
1. create superuser accounts for john, also maybe me so we dont need to log in as root
2. install django-messages, user-to-usermessages
		/tmp/pip_build_root/django-messages
			read about it: 	http://django-messages.readthedocs.org/en/latest/install.html
		#To enable django-messages in your Django project make sure it is installed. 
		#You can check if django-messages was successfully installed by opening a python shell and running:
>>> import django_messages #no error messages
		#install django_messages to installed apps
		#add to URL patters:
		(r'^messages/', include('django_messages.urls')),

>>>


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