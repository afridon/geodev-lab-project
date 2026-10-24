with open ("wards.csv") as f:
    lines = f.readlines()

for line in lines [1:]:  # Skip the header line
    parts = line.strip().split(",") # Split the line into parts using comma as the delimiter
    ward = parts[0]
    area_km2 = float(parts[1])
    if area_km2 > 9:
        size = "large"
    else:
        size = "small"
    print(ward, "is", size)