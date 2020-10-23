FROM nginx
ENV NGINX_DIR /etc/nginx
RUN rm -rf $NGINX_DIR/nginx.conf $NGINX_DIR/conf.d
COPY ./conf $NGINX_DIR