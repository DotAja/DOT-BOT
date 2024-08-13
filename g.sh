#!/bin/bash

# Gantilah ini dengan Token Akses Facebook Graph API Anda
ACCESS_TOKEN="EAAHc36AwJEUBO1poGQrWzOKbWN4GdaAJjszVZCuzqLMJwtSpUngqDtn5uDLMH4AjZB16GNVceKN2z98WhVmTbDNYZBESxCuppkVfNXxjIdbGInZABtYgEONuRyBggZBZAnlpOqtBmwIX91EFEFhL1IQdj1YIJJGpCuWJJNWcCC1vGjEBH2IterZBuZAi1PbPKZCr6ECj79D9IIQZDZD"

# Gantilah ini dengan ID Halaman Facebook Anda
PAGE_ID="436015940513248"

# Gantilah ini dengan jumlah postingan yang ingin Anda dapatkan (misalnya 100)
LIMIT=100

# URL yang ingin Anda cari dalam postingan
SEARCH_URL="https://chat.whatsapp.com"

# Panggil API Facebook Graph untuk mendapatkan daftar postingan
response=$(curl -s "https://graph.facebook.com/v13.0/$PAGE_ID/posts?access_token=$ACCESS_TOKEN&limit=$LIMIT")

# Ambil daftar postingan dan filter yang mengandung URL tertentu
echo "$response" | jq -r --arg url "$SEARCH_URL" '.data[] | select(.message | contains($url)) | "\(.message) - https://www.facebook.com/\(.id)"'
