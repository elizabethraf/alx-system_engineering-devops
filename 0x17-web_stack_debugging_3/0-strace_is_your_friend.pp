class apache_fix {
  file_line { 'modify_wp_settings':
    path    => '/var/www/html/wp-settings.php',
    line    => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
    replace => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.phpp\' );',
  }

  service { 'apache2':
    ensure => running,
    enable => true,
    subscribe => File_line['modify_wp_settings'],
    refreshonly => true,
  }
}
