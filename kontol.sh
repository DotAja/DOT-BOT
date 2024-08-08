#!/bin/bash

# URL dari halaman yang akan diambil datanya
URL="https://www.usercheck.com/provider/generator.email"

# Mengambil dan memproses data dari halaman
curl -s $URL | grep -oP '<tr>.*?</tr>' | while read -r line; do
    domain=$(echo $line | grep -oP '(?<=<td class="domain-name">)[^<]+')
    date=$(echo $line | grep -oP '(?<=<td class="added-date">)[^<]+')
    if [[ -n "$domain" && -n "$date" ]]; then
        echo "$domain - $date"
    fi
done
