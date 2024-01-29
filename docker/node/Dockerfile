FROM node:17

WORKDIR /var
RUN mkdir app
WORKDIR /var/app
RUN npm install express

COPY ./  .
CMD node app.js
#CMD sleep 10000
