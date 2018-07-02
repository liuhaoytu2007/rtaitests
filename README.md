# RTAI Tests

Collection of RTAI test results.


## Instructions

 1. Clone [makertai](https://github.com/relacs/makertai) and
    [rtaitests](https://github.com/relacs/rtaitests.git) into the same
    directory:
    ```
    git clone https://github.com/relacs/makertai
    git clone https://github.com/relacs/rtaitests
    ```

 2. Make a directory for your latency test results. Idealy it should
    be named `HOSTNAME-RTAIVERSION-LINUXKERNEL` like the beginning of
    the `latencyes-*` file name:
    ```
    cd rtaitests
    mkdir HOSTNAME-RTAIVERSION-LINUXKERNEL
    ```

 3. Copy `latencies-*` and the corresponding `config-*` files into this directory:
    ```
    cd /path/to/your/test/results
    cp latencies-* config-* /path/to/rtaitests/HOSTNAME-RTAIVERSION-LINUXKERNEL/
    ```

 4. Copy from one of the other directories the `report.sh` file:
    ```
    cd /path/to/rtaitests
    cp OTHERTESTS/report.sh HOSTNAME-RTAIVERSION-LINUXKERNEL/
    cd HOSTNAME-RTAIVERSION-LINUXKERNEL/
    ```

 5. Modify the `report.sh` script if necessary...

 6. Run the `report.sh` script:
    ```
    ./report.sh
    ```

 7. Add your files to the git repository, commit and push:
    ```
    cd ..
    git add HOSTNAME-RTAIVERSION-LINUXKERNEL/
    git commit -a -m 'added test results for HOSTNAME-RTAIVERSION-LINUXKERNEL'
    git push origin master
    ```

--------------------------------------------------------------------------

## Test results

1. [abbott](abbott-rtai-5.1-4.4.115-2018/report.md)
2. [mule](mule-rtai-5.1-4.4.115-2018/report.md)


