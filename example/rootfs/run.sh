#!/usr/bin/with-contenv bashio
# ==============================================================================
# Run ESPHome log viewer directly
# ==============================================================================

bashio::log.info "Starting ESPHome Log Viewer add-on..."
exec python3 /tmp/esphome_log.py