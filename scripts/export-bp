#!/usr/bin/env bash

# Check LOGIK_URL
if [[ -z "${LOGIK_URL}" ]]; then
    echo "LOGIK_URL is not set" >&2
    exit 1
fi

# Check LOGIK_TOKEN
if [[ -z "${LOGIK_TOKEN}" ]]; then
    echo "LOGIK_TOKEN is not set" >&2
    exit 1
fi

curl_args=(
    -H "Authorization: Bearer ${LOGIK_TOKEN}"
)

# WIP to support mutliple args
join_args () {
    local IFS=","
    echo "\"$*\""
}

init_export() {
    local url="${LOGIK_URL}api/admin/v1/bulk/blueprints/export"
    curl -fsSL -X POST "${curl_args[@]}" -H 'accept:application/json' -H 'content-type:application/json' "$url" -d "[\"$@\"]"
}

poll_job() {
    local MAX_ITER=5
    local LOOP_COUNT=0
    local status
    local url="${LOGIK_URL}api/admin/v1/job/${JOB_ID}"

    until [ $LOOP_COUNT -eq $MAX_ITER ]; do
        status=$(curl -fsSL "${curl_args[@]}" -H 'accept:application/json' "$url" | jq '.. | .status?')
       
        if [[ "$status" == *"COMPLETED"* ]]; then
            echo "Blueprint export complete"
            break
        fi
        
        (( LOOP_COUNT++ ))
        echo "Waiting for export to complete..."
        sleep 5
    done
    # echo "Blueprint export is taking a long time, check Job Id: $JOB_ID later" 
}

download_blueprint() {
    local url="${LOGIK_URL}api/admin/v2/bulk/export/${JOB_ID}"
    local NOW=$(date +'%Y-%m-%dT%H.%M.%S')
    local filename="export.zip"

    echo "Saving to $filename"
    curl -fsSL "${curl_args[@]}" -H 'accept:application/octet-stream' "$url" -o "$filename"
}

BP_VAR_NAMES=$@
# Run job to start export
HTTP_RESPONSE=$(init_export $@)

echo "Started export for $@"

# Extract JOB ID from HTTP
JOB_ID=$(echo $HTTP_RESPONSE | jq '.. | .id?')
echo "Export job: $JOB_ID"

# poll job until complete
poll_job

# download BP use args as var name
download_blueprint $@