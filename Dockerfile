FROM python:3.9

# Install psutil library
RUN pip install psutil

# Install Apache and Python 3 library for Apache
RUN apt-get update && apt-get install -y apache2 libapache2-mod-python

# Enable mod_python in Apache
RUN a2enmod python

# Create a directory for the application
WORKDIR /usr/src/app

# Copy Python script to container
COPY os_info_logger.py .

# Copy HTML file to Apache directory
COPY page.html /var/www/html/

# Set up logging directory
RUN mkdir /logs

RUN mkdir -p /var/log/my_logs/

# Configure Apache to serve logs
COPY apache_conf/my_logs.conf /etc/apache2/sites-available/
RUN a2ensite my_logs

# Set ServerName directive to suppress warning
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Expose port 80 for Apache
EXPOSE 80

# Start Apache in the foreground
CMD ["bash", "-c", "apachectl -D FOREGROUND & python os_info_logger.py"]