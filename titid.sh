#!/bin/bash

# URL yang akan diambil datanya
URL="https://www.usercheck.com/provider/emailfake.com"

# Mengambil konten halaman
content=$(curl -s $URL)

# Mengambil semua entri domain dan tanggal "added" menggunakan awk
domains=$(echo "$content" | awk -F'[<>]' '/<h2 class="domain"/{getline; print $3}')
added_dates=$(echo "$content" | awk -F'[<>]' '/<div class="added"/{getline; print $3}')

# Menampilkan domain dan tanggal "added" dalam satu baris
IFS=$'\n' read -r -d '' -a domains_array <<< "$domains"
IFS=$'\n' read -r -d '' -a added_array <<< "$added_dates"

# Memeriksa apakah jumlah domain dan tanggal "added" sama
if [ ${#domains_array[@]} -eq ${#added_array[@]} ]; then
  for (( i=0; i<${#domains_array[@]}; i++ )); do
    echo "${domains_array[i]} - Added: ${added_array[i]}"
  done
else
  echo "Jumlah domain dan tanggal 'added' tidak cocok."
fi
