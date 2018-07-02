# abbott: rtai-5.1 on 4.4.115 linux kernel

tested on 2018-06-14

## Machine

Linux kernel version *4.4.115* patched with *hal-linux-4.4.115-x86-10.patch* of *rtai-5.1*

*Intel(R) Core(TM) i5-6600K CPU @ 3.50GHz* on a *ASUSTeK Z170-K* motherboard (version *COMPUTER INC. Rev X.0x*)

## Kernel parameter:
* idle=poll
* tsc=reliable

## Performance

kern/latency test for 1988 seconds.
Reported is the mean, standard deviation and the maximum value of the jitter (`lat max - lat min`) in nanoseconds.

### Idle machine

| isolcpus | mean | stdev | max   |
|----------|------------:|------:|------:|
| none     |         797 |   396 | 10808 |
| 1        |         231 |   122 |  1713 |

![idle.png](idle.png)


### Full load

| isolcpus | mean | stdev | max   |
|----------|------------:|------:|------:|
| none     |        2471 |   811 | 23088 |
| 1        |        1397 |   145 |  2831 |

![full.png](full.png)


