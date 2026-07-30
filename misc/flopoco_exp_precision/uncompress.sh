#!/bin/bash

cd "$(dirname "$0")" || exit 1
find . -name "*.gz" -execdir gunzip -k {} \;
