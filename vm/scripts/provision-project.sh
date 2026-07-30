#!/usr/bin/env bash
set -euo pipefail

uid=$1
target=$2
user=vagrant
home=/home/vagrant
session=
for _ in $(seq 1 60); do
  session=$(loginctl list-sessions --no-legend | awk -v uid="$uid" '$2 == uid {print $1}' | while read -r id; do
    [ "$(loginctl show-session "$id" -p Active --value)" = yes ] || continue
    [ "$(loginctl show-session "$id" -p Type --value)" = x11 ] || continue
    echo "$id"
    break
  done)
  [ -z "$session" ] || break
  sleep 2
done
[ -n "$session" ] || { echo "No active X11 session for $user"; exit 1; }

display=$(loginctl show-session "$session" -p Display --value)
runtime=/run/user/$uid
auth=$runtime/gdm/Xauthority
if [ -z "$display" ]; then
  pid=$(pgrep -u "$uid" -n Xorg || true)
  [ -z "$pid" ] || display=$(tr '\0' '\n' <"/proc/$pid/environ" | sed -n 's/^DISPLAY=//p')
fi
[ -n "$display" ] || display=:0
test -r "$auth"

sudo -u "$user" env HOME="$home" USER="$user" LOGNAME="$user" \
  DISPLAY="$display" XAUTHORITY="$auth" XDG_RUNTIME_DIR="$runtime" \
  DBUS_SESSION_BUS_ADDRESS="unix:path=$runtime/bus" \
  /usr/local/bin/project-gui "$target"
