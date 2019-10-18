#!/bin/sh

sigint_handler() {
  kill $PID
  exit
}

trap sigint_handler SIGINT

cd /usr/src/app

while true; do
  # Start Pokealarm in the background
  python ./start_pokealarm.py --host 0.0.0.0 $@ &
  PID=$!
  # Wait until any config file changes
  inotifywait -e close_write config/config.ini $(python ./tools/watchfiles.py)
  echo "Configuration has changed, restarting PokeAlarm..."
  kill $PID
done
