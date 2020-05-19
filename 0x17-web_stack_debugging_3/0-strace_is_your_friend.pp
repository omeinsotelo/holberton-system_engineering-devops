# SED to change ".phpp" to ".php"
exec { 'fixing':
    command    => '/bin/sed -i s"/phpp/php/" /var/www/html/wp-settings.php',
}

# Restart service
service { 'restart-apache2':
  name       => 'apache2',
  hasrestart => true,
}

