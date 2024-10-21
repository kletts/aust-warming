---
title: Monthly weather 
---

# Monthly temperature anomaly

```js 
const obsdata = FileAttachment("data/au-current-obs.csv").csv({ typed: true });
```

```js 
const maxdate = d3.max(obsdata, d => d.Date);
```

```js 
const measure = view(Inputs.radio(new Map([
    [`Anomaly for ${d3.timeFormat("%B %Y")(maxdate)}`, "Anomaly"], 
    [`Average Temperatures for ${d3.timeFormat("%B %Y")(maxdate)}`, "ObsTemp"], 
    [`Long Run Average Temperatures (Average 1961 to 1990) for ${d3.timeFormat("%B")(maxdate)}`, "NormTemp"]]), 
{ value: "Anomaly" }))
```

```js 
Plot.plot({ 
    color: { legend: true },
    aspectRatio: true, 
    x: { axis: null },
    y: { axis: null }, 
    inset: 10,
    marks: [ 
    Plot.hexagon(obsdata.filter(d => d.ObsTemp > -100), 
    { x: "long", y: "lat", fill: measure, r: 8.3, tip: true, 
    title: d => d3.format("0.01f")(d[measure]) })
]})
```
