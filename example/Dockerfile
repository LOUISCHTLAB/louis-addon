ARG BUILD_FROM
FROM $BUILD_FROM

# Install S6 Overlay manually if not included
RUN curl -sSL https://github.com/just-containers/s6-overlay/releases/download/v3.1.6.2/s6-overlay-noarch.tar.xz | tar -C / -Jx \
    && curl -sSL https://github.com/just-containers/s6-overlay/releases/download/v3.1.6.2/s6-overlay-$(uname -m).tar.xz | tar -C / -Jx

# Execute during the build of the image
ARG TEMPIO_VERSION BUILD_ARCH
RUN \
    curl -sSLf -o /usr/bin/tempio \
    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}" \
    && chmod a+x /usr/bin/tempio

# Install Python and required libraries for ESPHome API
RUN apk add --no-cache python3 py3-pip \
    && pip3 install aioesphomeapi

# Copy root filesystem and set executable permissions
COPY rootfs /
RUN chmod -R +x /etc/s6/init /etc/services.d /etc/cont-init.d /etc/cont-finish.d /run.sh /tmp/esphome_log.py

# Run the S6 supervision tree
CMD ["/init"]