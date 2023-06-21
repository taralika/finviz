#!/bin/bash
gcloud functions deploy quote --source . --runtime python39 --trigger-http --allow-unauthenticated
