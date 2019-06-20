#!/bin/bash

DIR=$(dirname $0)
source "$DIR/../report_tools.sh"

performance_summary $DIR/latencies-*

{
# General information:
FILE=$(ls $DIR/latencies-* | head -n 1)
hardware_summary $FILE $DIR/config-*
performance_header $FILE

# Comparison of selected test results:
performance_data "No ACPI idle machine" idle.png  data:isolcpu $DIR/latencies-*176-0[34]*-idle-*
performance_data "No ACPI full load" full.png data:isolcpu $DIR/latencies-*176-0[34]*-*-cimn-*
performance_data "Full ACPI idle machine" acpiidle.png  data:latency $DIR/latencies-*176-05*-idle-*
performance_data "Full ACPI full load" acpifull.png data:latency $DIR/latencies-*176-05*-*-cimn-*
} > "$DIR/report.md"
