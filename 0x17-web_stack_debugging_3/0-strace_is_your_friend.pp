# Fixes bad filename
exec { 'fix-wordpress':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure    => running,
  restart   => true,
  subscribe => Exec['fix-wordpress'],
}

