FROM python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG sleekforum_environment
ARG sleekforum_user=sleekforum
ENV SLEEKFORUM_USER=$sleekforum_user
ENV SLEEKFORUM_PATH /srv/http/$SLEEKFORUM_USER
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated \
      nano \
      lynx \
      libffi-dev \
      libssl-dev \
      libjpeg-dev \
      libopenjp2-7-dev \
      locales \
      cron \
      psycopg2 \
      gettext && \
    apt-get clean
RUN useradd --create-home $sleekforum_user
COPY ../../src $SLEEKFORUM_PATH
WORKDIR $SLEEKFORUM_PATH
ENV SLEEKFORUM_ENVIRONMENT sleekforum.settings.$sleekforum_environment
RUN pip install -r sleekforum/requirements/$sleekforum_environment.txt --no-warn-script-location
EXPOSE 4042
CMD ["uwsgi", "uwsgi.ini"]
