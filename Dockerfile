FROM node as build
WORKDIR /app
COPY package*.json /app/
RUN npm install
RUN apt install git
COPY ./ /app/
RUN npm run build
RUN cd dist &&\
    git init &&\
    git add -A &&\
    git commit -m 'deploy' &&\
    git push -f git@github.com:brentspector/reborn-pokepedia.git master:gh-pages