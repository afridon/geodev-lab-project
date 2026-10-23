### Research Question
Which areas of Bridgwater, Somerset are exposed to surface-water flooding, and which buildings and roads are located within these areas?

### Operation Executed & Justification
Buffered a distance parameter of 100 metres on three distinct surface water risk tiers (High, Medium, and Low), dissolved, select by location intersection query was run against both the master building footprint dataset and the road network dataset to extract comparative exposure statistics.

### Expectations vs. Final Results
Expected: I initially expected a minor parts of the town's buildings and roads to intersect the risk zone.
Received: The analysis revealed almost all the geographic location of the town is exposed to surface-water flooding.
Baseline: 5,929 Buildings | 1,739 Roads
High Risk (1-in-30 Year Zone): 5,265 buildings and 1,631 roads.
Medium Risk (1-in-100 Year Zone): 5,802 buildings and 1,719 roads.
Low Risk (1-in-1000 Year Zone): 5,879 buildings and 1,726 roads.

### Project Surprises
I was highly surprised that majority of the road network sits inside the 100m risk zone. This shows local transport network is in vulnerable state during a high-risk flooding.  

### Remaining Data Needs
Drainage and Elevations data.
