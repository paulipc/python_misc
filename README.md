# Python_misc

## Pythonilla tehtyjä sekalaisia skriptejä

Eka projekti on replaceallcommas, joka korvaa merkkijonossa olevat puolipisteet (;) pisteellä (.) jos puolipiste on kahden tagin välissä (start ja end). Helpottaa CSV:n käsittelyä kun CSV:ssä on ylimääräisiä puolipisteitä.

## time_calc

### ```to_hhmm(minutes)```
**usage:** ```to_hhmm(minutes)```

Converts minutes given to hours and minutes.

### ```to_min(hh,mm)```

**usage:** ```to_min(hh,mm)```

Converts hours and minutes given to minutes.

Does not care about days or 24h or something. Just converts both ways and the rest is for user.

### Example:

Calculate time difference with 04.45 - 17.00 and multiply by 5 (days)
```
(to_min(17,00)-to_min(4,45))*5          # You get minutes of differencies for five days.

to_hhmm((to_min(17,00)-to_min(4,45))*5) # You get hours and minutes for above minutes.
```

