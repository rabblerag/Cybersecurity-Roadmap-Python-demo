FROM python:3.9-slim

RUN apt-get update && apt-get install -y socat
RUN apt-get install -y ncat bash vim nano net-tools iputils-ping btop sudo 


# Set the working directory inside the container
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG PORT
ENV PORT=$PORT


# Accept a build argument for the challenge port
ARG CHALLENGE_PORT
ENV CHALLENGE_PORT=$CHALLENGE_PORT

# Create new user and group 

RUN useradd -ms /bin/bash user 
RUN groupadd challenge

# COPY ./challenge /usr/src/app/

# Accept a build argument for the challenge path
ARG CHALLENGE_PATH
COPY ./${CHALLENGE_PATH}/challenge /usr/src/app/

# Changing the permissions of specific files to minimize the damage 

RUN chmod 755 challenge.py
RUN chmod 744 flag.txt

RUN chmod 777 /usr/bin/bash
RUN chmod 777 /bin/bash
RUN chmod 777 /usr/local/bin/python


USER user


# Expose the dynamically assigned port
EXPOSE $CHALLENGE_PORT

# Start the challenge on the correct port
CMD ["sh", "-c", "socat -v TCP-LISTEN:${CHALLENGE_PORT},reuseaddr,fork EXEC:'python3 /usr/src/app/challenge.py',pty,echo=0,stderr"]

# Expose the port the server will run on
# EXPOSE 1337

# CMD ["socat", "-v","TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'python3 /usr/src/app/challenge.py',pty,echo=0,stderr"]

