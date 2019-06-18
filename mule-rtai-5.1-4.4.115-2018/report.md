# mule: rtai-5.1 on 4.4.115 linux kernel

tested on 2018-06-14

## Kernel and machine

Linux kernel version *4.4.115* patched with *hal-linux-4.4.115-x86-10.patch* of *rtai-5.1*: [kernel configuration](config-4.4.115-rtai-5.1-mule-019-2018-06-14-polltscrel-plain-cpu1-idle-good)

*Intel(R) Core(TM) i5-3570 CPU @ 3.40GHz* on a *FUJITSU D3162-A1* motherboard (version *S26361-D3162-A1*)

## Kernel parameter:
* idle=poll
* tsc=reliable

## Performance

kern/latency test for 1988 seconds.
Reported is the mean, standard deviation and the maximum value of the jitter (`lat max - lat min`) in nanoseconds.

### Idle machine

| isolcpus | mean | stdev | max  | link                                                                                               |
|----------|------------:|------:|-----:|----------------------------------------------------------------------------------------------------|
| none     |         537 |   239 | 4322 | [test details](latencies-4.4.115-rtai-5.1-mule-019-2018-06-14-polltscrel-plain-cpu1-idle-good)     |
| 1        |         252 |   196 | 4476 | [test details](latencies-4.4.115-rtai-5.1-mule-021-2018-06-14-polltscrel-isolcpus1-cpu1-idle-good) |

![idle.png](idle.png)


### Full load

| isolcpus | mean | stdev | max   | link                                                                                               |
|----------|------------:|------:|------:|----------------------------------------------------------------------------------------------------|
| none     |        5539 |   737 | 10272 | [test details](latencies-4.4.115-rtai-5.1-mule-020-2018-06-14-polltscrel-plain-cpu1-cimn-ok)       |
| 1        |        5567 |   426 |  7839 | [test details](latencies-4.4.115-rtai-5.1-mule-022-2018-06-14-polltscrel-isolcpus1-cpu1-cimn-good) |

![full.png](full.png)


