# Data notes
## Bridgwater administrative boundary
Source: https://www.data.gov.uk/dataset/273b0f96-cfc4-48c4-ba98-760f1e929e53/parishes-and-non-civil-parished-areas-may-2026-boundaries-ew-bfc
Downloaded: 12/09/2026
1 features, polygon.
Key columns: PARNCP26CD, PARNCP26NM, LAD26CD, LAD26NM, BNG_E, BNG_N, LONG, LAT, GloballD.
PARNCP26NM contains a NULL value.
Highlighted the location row and saved selected features.

## River and tidal flood zones
Source: https://www.data.gov.uk/dataset/104434b0-5263-4c90-9b1e-e43b1d57c750/flood-map-for-planning-flood-zones1
Downloaded: 12/09/2026
243 features, polygon.
Key columns: origin, flood_zone, flood_source.
None contains blank or NULL.
I clipped the layer to cover the boundary.

## Surface-water flooding
Source: https://www.data.gov.uk/dataset/dfd734fb-cc68-4229-b60d-8c0280398052/flood-map-for-planning-surface-water-spatial-planning-extents-present-day
Downloaded: 12/09/2026
19 features, polygon.
Key columns: aep, origin, flood_sour.
shape_leng and shape_area contain NULL values.
I used the 1 in 100 AEP surface-water layer  and clipped to the Bridgwater boundary.

## Buildings
Source: https://osdatahub.os.uk/data/downloads/open/OpenZoomstack
Downloaded: 12/09/2026
5929 features, polygon.
Key columns: id, uuid.
No blank or NULL in the id or uuid fields.
I used the local_buildings layer and clipped to the Bridgwater boundary.

## Roads
Source: https://osdatahub.os.uk/data/downloads/open/OpenRoads
Downloaded: 12/09/2026
1739 features, line.
Key columns: id, road_classification, road_function, form_of_way, road_classification_number, name_1, road_structure, length, primary_route, trunk_road, start_node, end_node.
Some name_1 values contain NULL values.
I clipped the layer to the Bridgwater boundary.

## CRS and preparation
All source layers arrived in EPSG:4326
Study area: Bridgwater Somerset, extracted from the administrative boundary
All layers clipped to study area, then reprojected to EPSG:27700
Working files in GeoDev/data/, raw files untouched 
