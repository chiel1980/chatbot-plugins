FROM alpine:latest
MAINTAINER Michiel van Es <mve@pragmasec.nl>
# the works
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base
RUN rm -rf /var/cache/apk/*
RUN pip install will
# create user for running the bot
# create user and group that matches host UID and GID
RUN addgroup -g 5001 willbot
RUN adduser -h /home/willbot -s /bin/sh -u 5001 -G willbot -D willbot willbot
WORKDIR /home/willbot
RUN chown -R willbot /home/willbot
#
WORKDIR /home/willbot/
RUN generate_will_project
ADD config.py /home/willbot/
# add plugins
ADD chucknorris.py /home/willbot/plugins/
ADD rts.py /home/willbot/plugins/
#
ADD startup.sh /home/willbot/
RUN chmod +x /home/willbot/startup.sh /home/willbot/config.py
RUN chown willbot /home/willbot/config.py
RUN mkdir -p /var/run/will/settings/
RUN chown -R willbot.root /var/run/will/settings/
# move to user willbot
USER willbot
# start
ENTRYPOINT ["/home/willbot/startup.sh"]
