#!/bin/bash

DB_NAME="lesson_9"
DB_USER="postgres"
DB_HOST="localhost"
DB_PORT="5432"
BACKUP_DIR="/tmp"
DB_PASSWORD="1"

DATE=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$DATE.tar"
export PGPASSWORD="$DB_PASSWORD"
pg_dump -U $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -F c -f $BACKUP_FILE