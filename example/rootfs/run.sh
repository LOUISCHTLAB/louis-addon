#!/usr/bin/with-contenv bashio
# ==============================================================================
# Entry point to start the S6 supervision tree
# ==============================================================================

bashio::log.info "Starting ESPHome Log Viewer add-on..."
exec /init