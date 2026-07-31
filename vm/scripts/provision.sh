#!/usr/bin/env bash
set -euo pipefail

user=vagrant home=/home/vagrant
uid=$(id -u "$user")
gid=$(id -g "$user")
export DEBIAN_FRONTEND=noninteractive
export NEEDRESTART_MODE=l

mkdir -p /etc/needrestart/conf.d
cat >/etc/needrestart/conf.d/vagrant.conf <<'EOF'
$nrconf{restart} = 'l';
EOF
apt-get update
apt-get -o Dpkg::Options::=--force-confold install -y --no-install-recommends \
  firefox gnome-terminal expect python3-venv rsync build-essential mc mesa-utils neovim parted tmux wget libgtk2.0-0t64 \
  libx11-6 libxext6 libxrender1 libxtst6 libxi6 libxft2 \
  libsm6 libice6 libfontconfig1 libfreetype6 libncurses6 libncursesw6 libtinfo6
apt-get -o Dpkg::Options::=--force-confold install -y --no-install-recommends \
  fdisk g++ git graphviz libc6-dev-i386 libasound2t64 libgdk-pixbuf-2.0-dev \
  libgtk-3-dev libncurses-dev libnss3-dev libsecret-1-dev libxss-dev make \
  net-tools unzip xvfb zip htop

mount_xilinx_disk() {
  local disk part fs uuid root_source
  local -a links
  mapfile -t links < <(find /dev/disk/by-path -maxdepth 1 -type l -name '*-ata-2' ! -name '*-part*' -print)
  [ "${#links[@]}" -eq 1 ] || {
    echo "Expected one persistent Xilinx disk at VirtualBox SATA port 1, found ${#links[@]}"
    exit 1
  }
  disk=$(readlink -f "${links[0]}")
  part=${disk}1
  [[ $disk =~ [0-9]$ ]] && part=${disk}p1
  root_source=$(readlink -f "$(findmnt -nro SOURCE /)")
  ! lsblk -sno PATH "$root_source" | grep -qxF "$disk" || { echo "Refusing to format root disk $disk"; exit 1; }
  if [ ! -b "$part" ]; then
    [ -z "$(wipefs -n "$disk")" ] || { echo "$disk is not blank; refusing to partition it"; exit 1; }
    parted -s "$disk" mklabel gpt mkpart primary ext4 1MiB 100%
    partprobe "$disk"
    udevadm settle
  fi
  fs=$(blkid -s TYPE -o value "$part" 2>/dev/null || true)
  if [ -z "$fs" ]; then
    [ -z "$(wipefs -n "$part")" ] || { echo "$part has an unknown signature; refusing to format it"; exit 1; }
    mkfs.ext4 -L XILINX "$part"
    fs=ext4
  fi
  [ "$fs" = ext4 ] || { echo "Expected ext4 on $part, found $fs"; exit 1; }
  uuid=$(blkid -s UUID -o value "$part")
  mkdir -p /opt/Xilinx
  sed -i '\|[[:space:]]/opt/Xilinx[[:space:]]|d' /etc/fstab
  printf 'UUID=%s /opt/Xilinx ext4 defaults,nofail,discard 0 2\n' "$uuid" >>/etc/fstab
  if mountpoint -q /opt/Xilinx; then
    mount -o remount,discard /opt/Xilinx
  else
    mount /opt/Xilinx
  fi
}
mount_xilinx_disk

passwd -d "$user"
chown -R "$uid:$gid" "$home"

[ ! -f "$home/install-vivado" ] || install -m 0755 -o "$uid" -g "$gid" "$home/install-vivado" /usr/local/bin/install-vivado
[ ! -f "$home/download-vivado-installer.py" ] || install -m 0755 -o "$uid" -g "$gid" "$home/download-vivado-installer.py" /usr/local/bin/download-vivado-installer
[ ! -f "$home/project-gui" ] || install -m 0755 -o "$uid" -g "$gid" "$home/project-gui" /usr/local/bin/project-gui
test -x /usr/local/bin/install-vivado
test -x /usr/local/bin/download-vivado-installer
test -x /usr/local/bin/project-gui
wget --https-only --secure-protocol=TLSv1_2 -qO- https://just.systems/install.sh | bash -s -- --to /usr/bin --force
install -d -o "$uid" -g "$gid" "$home/.local/share/bash-completion/completions"
sudo -u "$user" env HOME="$home" /usr/bin/just --completions bash >"$home/.local/share/bash-completion/completions/just"
chown "$uid:$gid" "$home/.local/share/bash-completion/completions/just"
completion_line='test -r "$HOME/.local/share/bash-completion/completions/just" && . "$HOME/.local/share/bash-completion/completions/just"'
touch "$home/.bashrc"
grep -qxF "$completion_line" "$home/.bashrc" || printf '\n%s\n' "$completion_line" >>"$home/.bashrc"
chown "$uid:$gid" "$home/.bashrc"
install -d -o "$uid" -g "$gid" /opt/Xilinx /opt/Xilinx/.installer "$home/Desktop" "$home/.config" "$home/Downloads"
chown -R "$uid:$gid" /opt/Xilinx/.installer
printf yes >"$home/.config/gnome-initial-setup-done"
if [ -L "$home/Downloads/vivado_installer" ]; then
  rm -f "$home/Downloads/vivado_installer"
fi
install -d -o "$uid" -g "$gid" "$home/Downloads/vivado_installer"
venv="$home/.local/share/vivado-downloader"
if [ ! -x "$venv/bin/python" ] || ! "$venv/bin/python" -c 'import selenium' 2>/dev/null; then
  rm -rf "$venv"
  python3 -m venv "$venv"
  "$venv/bin/pip" install --disable-pip-version-check 'selenium==4.34.2'
fi
chown -R "$uid:$gid" "$home/.local" "$home/Downloads"
[ ! -f "$home/.vivado-credentials" ] || { chown "$uid:$gid" "$home/.vivado-credentials"; chmod 600 "$home/.vivado-credentials"; }

lib=/usr/lib/x86_64-linux-gnu
for name in libtinfo libncurses libncursesw; do
  [ -e "$lib/$name.so.5" ] || ln -s "$lib/$name.so.6" "$lib/$name.so.5"
done

rm -f "$home/Desktop/Project-Vivado.desktop"
rm -f "$home/Desktop/Install-Vivado.desktop"
rm -f "$home/.config/autostart/install-vivado.desktop"
chown -R "$uid:$gid" "$home/Desktop" "$home/.config"

test -d /etc/gdm3 || { echo "Ubuntu GNOME desktop base is missing GDM"; exit 1; }
cat >/etc/gdm3/custom.conf <<'EOF'
[daemon]
WaylandEnable=false
AutomaticLoginEnable=true
AutomaticLogin=vagrant
InitialSetupEnable=false
EOF
install -d /var/lib/AccountsService/users
cat >/var/lib/AccountsService/users/vagrant <<'EOF'
[User]
Session=ubuntu-xorg
XSession=ubuntu-xorg
SystemAccount=false
EOF
chmod 0600 /var/lib/AccountsService/users/vagrant
install -d -o "$uid" -g "$gid" "$home/.config/dconf"
gsettings_as_user() {
  sudo -u "$user" env HOME="$home" XDG_RUNTIME_DIR="/run/user/$uid" \
    dbus-run-session gsettings set "$@"
}
gsettings_as_user org.gnome.desktop.session idle-delay 0
gsettings_as_user org.gnome.desktop.screensaver lock-enabled false
gsettings_as_user org.gnome.desktop.screensaver ubuntu-lock-on-suspend false 2>/dev/null || true

systemctl set-default graphical.target

if [ ! -r /opt/Xilinx/2025.1/Vivado/settings64.sh ]; then
  session=$(loginctl list-sessions --no-legend | awk -v uid="$uid" '$2 == uid && $4 == "seat0" {print $1; exit}')
  [ -n "$session" ] || systemctl restart gdm3
  runtime=/run/user/$uid
  auth=$runtime/gdm/Xauthority
  for _ in $(seq 1 60); do
    test -r "$auth" && break
    sleep 2
  done
  test -r "$auth" || { echo "No vagrant desktop session available for Firefox"; exit 1; }
  sudo -u "$user" env HOME="$home" USER="$user" LOGNAME="$user" \
    DISPLAY=:0 XAUTHORITY="$auth" XDG_RUNTIME_DIR="$runtime" \
    DBUS_SESSION_BUS_ADDRESS="unix:path=$runtime/bus" \
    /usr/local/bin/install-vivado
else
  /usr/local/bin/install-vivado
fi
test -r /opt/Xilinx/2025.1/Vivado/settings64.sh
cat >/etc/profile.d/vivado-2025.1.sh <<'EOF'
if [ -z "${XILINX_VIVADO:-}" ]; then
  . /opt/Xilinx/2025.1/Vivado/settings64.sh
fi
EOF
chmod 0644 /etc/profile.d/vivado-2025.1.sh

session=$(loginctl list-sessions --no-legend | awk -v uid="$uid" '$2 == uid && $4 == "seat0" {print $1; exit}')
[ -n "$session" ] || systemctl restart gdm3
for _ in $(seq 1 30); do
  session=$(loginctl list-sessions --no-legend | awk -v uid="$uid" '$2 == uid && $4 == "seat0" {print $1; exit}')
  [ -z "$session" ] || break
  sleep 1
done
[ -n "${session:-}" ] || { echo "GDM did not automatically log in $user"; exit 1; }
[ "$(loginctl show-session "$session" -p Name --value)" = "$user" ]
runtime=/run/user/$uid
auth=$runtime/gdm/Xauthority
test -r "$auth"
glx=$(sudo -u "$user" env HOME="$home" DISPLAY=:0 XAUTHORITY="$auth" \
  XDG_RUNTIME_DIR="$runtime" glxinfo -B)
grep -q '^direct rendering: Yes$' <<<"$glx"
renderer=$(sed -n 's/^OpenGL renderer string: //p' <<<"$glx")
[ -n "$renderer" ] || { echo "No OpenGL renderer available"; exit 1; }
echo "VirtualBox OpenGL renderer: $renderer"
fstrim -av

echo "Provisioning done!"
