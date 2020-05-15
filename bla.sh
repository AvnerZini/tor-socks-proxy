#! /bin/bash

EXTERNAL=$(curl ifconfig.co)
echo "My external IP is: ${EXTERNAL}"

end=$((SECONDS + 120))

while [ $SECONDS -lt $end ]; do

  IP=$(curl --socks5-hostname 127.0.0.1:9150 https://ipinfo.tw/ip)
  echo "Tor IP is: $(ip)"
  sleep 10
done
