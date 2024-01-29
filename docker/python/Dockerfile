FROM centos:7

# Install necessary dependencies
RUN yum update -y && \
    yum install -y \
    wget \
    gcc \
    openssl-devel \
    bzip2-devel \
    libffi-devel \
    make \
    zlib-devel \
    ca-certificates \
    epel-release

# Download and install Python 3.11
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz && \
    tar xzf Python-3.11.0.tgz && \
    cd Python-3.11.0 && \
    ./configure --enable-optimizations && \
    make && \
    make install

# Clean up unnecessary files
RUN rm -rf /tmp/Python-3.11.0*

# Set the default Python version
RUN ln -s /usr/local/bin/python3 /usr/local/bin/python

# Verify Python installation
RUN python --version && pip3 --version

# Set the working directory
WORKDIR /var




# Install project dependencies

#RUN pipenv install --deploy --ignore-pipfile

EXPOSE 8000
CMD sleep 1000
#CMD ["pipenv", "run", "uvicorn", "main:app", "--reload"]
