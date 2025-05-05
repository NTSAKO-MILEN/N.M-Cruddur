FROM gitpod/workspace-full

RUN apt-get update && apt-get install -y python3-pip
RUN npm install -g npm