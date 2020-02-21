# Misc Python Scripts

## replacecommas.py

Replaces all semicolons (;) with a dot (.). If semicolon is between two tabs (start and end).

The idea is to make CSV munging easier when there are extra semicolons in rows.

## time_calc.py

### ```to_hhmm(minutes)```
**usage:** ```to_hhmm(minutes)```

Converts minutes given to hours and minutes.

### ```to_min(hh,mm)```

**usage:** ```to_min(hh,mm)```

Converts hours and minutes given to minutes.

Does not care about days or 24h or something. Just converts both ways and the rest is for user.

### Example:

Calculate time difference with 04.45 - 17.00 and multiply by 5 time (if difference same for instance for 5 days).
```
>>> (to_min(17,00)-to_min(4,45))*5          # You get minutes of differencies for five days.
3675
>>>
```
...and more:
```
>>> to_hhmm((to_min(17,00)-to_min(4,45))*5) # You get hours and minutes for above minutes.
(61, 15)
>>>
```
