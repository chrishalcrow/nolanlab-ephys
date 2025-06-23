#!/bin/bash

# CSV filepath lookup script
# Usage: ./script.sh <csv_file> <mouse> <day> <session1,session2,session3...>

# Check if correct number of arguments provided
if [ $# -ne 4 ]; then
    echo "Usage: $0 <csv_file> <mouse> <day> <sessions>"
    echo "Example: $0 data.csv mouse1 day1 session1,session2,session3"
    exit 1
fi

CSV_FILE="$1"
MOUSE="$2"
DAY="$3"
SESSIONS="$4"

# Check if CSV file exists
if [ ! -f "$CSV_FILE" ]; then
    echo "Error: CSV file '$CSV_FILE' not found"
    exit 1
fi

# Convert sessions to array
# Handle both comma-separated and space-separated sessions
if [[ "$SESSIONS" == *","* ]]; then
    # Comma-separated
    IFS=',' read -ra SESSION_ARRAY <<< "$SESSIONS"
else
    # Space-separated
    read -ra SESSION_ARRAY <<< "$SESSIONS"
fi

# Arrays to store results
FOUND_FILEPATHS=()
NOT_FOUND_SESSIONS=()

# Search for each session
for SESSION in "${SESSION_ARRAY[@]}"; do
    # Trim whitespace from session
    SESSION=$(echo "$SESSION" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    
    # Search for matching row and extract filepath
    FILEPATH=$(awk -F',' -v mouse="$MOUSE" -v day="$DAY" -v session="$SESSION" '
    NR > 1 {
        # Remove leading/trailing whitespace from each field
        gsub(/^[ \t]+|[ \t]+$/, "", $1)
        gsub(/^[ \t]+|[ \t]+$/, "", $2)
        gsub(/^[ \t]+|[ \t]+$/, "", $3)
        gsub(/^[ \t]+|[ \t]+$/, "", $4)
        
        if ($1 == mouse && $2 == day && $3 == session) {
            print $4
            exit
        }
    }' "$CSV_FILE")
    
    if [ -n "$FILEPATH" ]; then
        FOUND_FILEPATHS+=("$FILEPATH")
    else
        NOT_FOUND_SESSIONS+=("$SESSION")
    fi
done

# Output results

if [ ${#FOUND_FILEPATHS[@]} -gt 0 ]; then
    IFS=','
    echo "python sort.py --filepaths ${FOUND_FILEPATHS[*]}"
    IFS=' '
    #echo "Found filepaths:"
    #for filepath in "${FOUND_FILEPATHS[@]}"; do
    #    echo "$filepath"
    #done
fi

# Report any sessions that weren't found
if [ ${#NOT_FOUND_SESSIONS[@]} -gt 0 ]; then
    echo "No matching records found for mouse='$MOUSE', day='$DAY', sessions: ${NOT_FOUND_SESSIONS[*]}" >&2
fi

# Exit with error if no filepaths were found
if [ ${#FOUND_FILEPATHS[@]} -eq 0 ]; then
    exit 1
fi