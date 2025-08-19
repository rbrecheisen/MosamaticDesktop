#!/bin/bash

for line in $(cat requirements-macos.txt); do
    echo $line
    poetry add $line
done