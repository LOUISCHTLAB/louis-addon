# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

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
RUN chmod -R +x /etc/services.d /etc/cont-init.d /etc/cont-finish.d /run.sh

# Run the add-on entrypoint
CMD ["/run.sh"]