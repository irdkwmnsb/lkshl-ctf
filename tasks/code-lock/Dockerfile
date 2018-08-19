FROM base/archlinux
WORKDIR /usr
ADD out /srv/http
ADD lighttpd.conf /lighty.conf
RUN [ "pacman", "-Sy", "--noconfirm" ]
RUN [ "pacman", "-S", "lighttpd", "php-cgi", "--noconfirm" ]
# RUN [ "groupadd", "http" ]
# RUN [ "useradd", "http", "-g", "http" ]
RUN [ "chown", "http:http", "-R", "/srv/http" ]
CMD [ "bash", "-c", "rm -f /var/run/lighttpd/lighttpd-angel.pid; lighttpd -Df /lighty.conf" ]
EXPOSE 81
