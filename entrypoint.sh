#!/bin/sh
if [ ! -f /app/config/config.yaml ]; then
  echo "Copying default config file"
  cp /app/exemple-config.yaml /app/config/config.yaml
fi

exec "$@"