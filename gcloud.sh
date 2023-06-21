#!/bin/bash
gcloud functions deploy quote --runtime python39 --trigger-http --allow-unauthenticated
