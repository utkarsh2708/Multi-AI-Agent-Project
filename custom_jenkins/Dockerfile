# Base Docker-in-Docker image (rootful)
FROM docker:24-dind

# Install Jenkins dependencies
RUN apk add --no-cache openjdk17 bash git curl

# Add Jenkins user
RUN adduser -D -u 1000 jenkins && \
    mkdir -p /var/jenkins_home && \
    chown -R jenkins:jenkins /var/jenkins_home

ENV JENKINS_HOME=/var/jenkins_home
VOLUME /var/jenkins_home

USER jenkins
