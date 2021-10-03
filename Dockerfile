FROM node:lts-alpine as build
WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY ./public /app/
COPY ./ /app/
RUN npm run build

FROM nginx:mainline-alpine
COPY --from=build /app/dist/ /var/www/html/reborn-pokepedia/
COPY --from=build /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf