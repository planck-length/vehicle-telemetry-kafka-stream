FROM confluentinc/cp-server-connect-base:7.5.0

ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"

ARG CONNECTOR_OWNER=confluentinc
ARG CONNECTOR_NAME
ARG CONNECTOR_VERSION=latest
RUN confluent-hub install --no-prompt ${CONNECTOR_OWNER}/${CONNECTOR_NAME}:${CONNECTOR_VERSION}