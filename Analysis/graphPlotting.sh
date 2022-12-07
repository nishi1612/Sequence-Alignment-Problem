#!/bin/sh

mkdir -p datapoints_output_basic
mkdir -p datapoints_output_efficient

for FILE in `ls datapoints/| sort -V`; do 
    python3 ../basic_3.py datapoints/$(basename ${FILE}) datapoints_output_basic/$(basename ${FILE});
    python3 ../efficient_3.py datapoints/$(basename ${FILE}) datapoints_output_efficient/$(basename ${FILE});
    echo "Completed Processing: ${FILE}" 
done

python3 graphPlotting.py