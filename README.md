# Tool for scaling synchronous mix networks

Tool allowing to get insights on how to scale and design mix networks from given resources.

Usage to simulate a mix network with the following characteristics:
* 400 queries per second
* 4 mixes in total
* 2 layers
* 1 second of latency added by each mix
* 1 second for the server to compute the response
* 3 split factor to divide the response (not implemented yet)

```
python simulate_mix.py -u 400 -n 4 -l 2 -tl 1 -ts 1 -s 3
```

Master Thesis, June 2019.
