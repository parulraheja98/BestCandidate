FROM node:8 as react-build
WORKDIR /lib
COPY . .
RUN npm install
RUN npm run build
FROM nginx:alpine
COPY --from=react-build /lib/build /var/www
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 3000
ENTRYPOINT ["nginx","-g","daemon off;"]
