#!/bin/bash

API_KEY='$2a$10$rdBvm0t8NoTZGj.OWH6D2./.AhQrswk9PaLbG3PXgGeukBdDRkoye'
COLLECTION_ID='659a4d41dc746540188e13b0'

curl -XPOST \
    -H "Content-type: application/json" \
    -H "X-Master-Key: $API_KEY" \
    -H "X-Collection-Id: $COLLECTION_ID" \
    -d @dogs.json \
    "https://api.jsonbin.io/v3/b"