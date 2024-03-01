FROM node:lts AS development
WORKDIR /app

COPY package*.json ./
RUN npm install --platform=linuxmusl --arch=arm64
RUN npm install vite
RUN npm install rollup

CMD ["/bin/sh", "-c", "npm install && npm run dev"]


FROM development as build
COPY . .
RUN npm install -g vite
RUN npm run build

FROM nginx:stable-alpine as production
COPY --from=build /app/dist /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]