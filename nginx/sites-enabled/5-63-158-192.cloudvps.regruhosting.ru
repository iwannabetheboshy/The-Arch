upstream django_server { server 
    unix:/home/django/django_venv/var/django_project.sock 
    fail_timeout=0;
}

server {
    listen 80;
    server_name the-arch.ru;
    return 301 https://the-arch.ru$request_uri;

}

server { 
    listen 443 ssl;  

    # ipv6only=on;
    server_name the-arch.ru; ssl_certificate /etc/ssl/the-arch.crt; 
    ssl_certificate_key /etc/ssl/the-arch.key;
	
    ssl_session_cache shared:SSL:10m; ssl_session_timeout 10m; 
    keepalive_timeout 35;
	
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; ssl_prefer_server_ciphers on;
	
    ssl_stapling on; ssl_trusted_certificate /etc/ssl/ca.crt; resolver 
    8.8.8.8; gzip on; gzip_comp_level 6; gzip_min_length 256; 
    gzip_proxied any; gzip_vary on;
	
	
    root /usr/share/nginx/html; location /static { alias 
        /home/django/django_venv/src/static;
    }
    location / { include proxy_params; proxy_pass http://django_server;
    }
}
