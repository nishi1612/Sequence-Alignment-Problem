#!/bin/sh

for FILE in `ls datapoints/| sort -V`; do 
    python3 basicAnalysis.py datapoints/$(basename ${FILE});
    python3 efficientAnalysis.py datapoints/$(basename ${FILE});
done

python3 graphPlotting.py