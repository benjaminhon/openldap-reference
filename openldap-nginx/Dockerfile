FROM python:2-alpine

# Install required software
RUN \
    apk --no-cache add openldap-dev && \
    apk --no-cache add --virtual build-dependencies build-base && \
    pip install python-ldap && \
    apk del build-dependencies