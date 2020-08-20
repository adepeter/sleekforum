FROM archlinux
ARG sleekforum_environment=development
ARG sleekforum_user=sleekforum
ENV SLEEKFORUM_USER=$sleekforum_user
ENV SLEEKFORUM_PATH /srv/http/$SLEEKFORUM_USER
RUN pacman -Syu --noconfirm base-devel lynx nano postgresql git \
uwsgi uwsgi-plugin-python uwsgitop \
python python-{pip,setuptools,wheel} && \
pip install --upgrade pip setuptools wheel uwsgi && \
pacman -Scc --noconfirm
RUN useradd --create-home $sleekforum_user
COPY . $SLEEKFORUM_PATH
WORKDIR $SLEEKFORUM_PATH
ENV SLEEKFORUM_ENVIRONMENT sleekforum.settings.$sleekforum_environment
RUN pip install -r sleekforum/requirements/$sleekforum_environment.txt --no-warn-script-location
EXPOSE 4042
CMD ["uwsgi", "uwsgi.ini"]