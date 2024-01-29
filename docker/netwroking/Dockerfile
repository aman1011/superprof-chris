# Use the official Ubuntu base image
FROM ubuntu:latest

# Update the package lists and install Apache
RUN apt-get update && \
    apt-get install -y apache2

RUN apt-get install curl

# Expose port 80 for web traffic
#EXPOSE 80

# Set the default command to start Apache when the container runs
#CMD ["bash"]
CMD ["apache2ctl", "-D", "FOREGROUND"]
