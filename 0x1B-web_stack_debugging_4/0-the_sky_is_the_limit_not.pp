# We are testing how well our web server setup featuring Nginx
exec { '/usr/bin/env sed -i s/15/2000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
