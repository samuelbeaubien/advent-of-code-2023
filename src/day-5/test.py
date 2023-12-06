from shapely import LineString, intersection, difference
from collections import deque

# line_1 = LineString([[0, 0], [10, 0]])
# line_2 = LineString([[13, 0], [17, 0]])
# line_1 = LineString([[0, 0], [10, 0]])
# line_2 = LineString([[13, 0], [17, 0]])

before = []
after = deque()

line_1 = LineString([[0, 0], [10, 0]])
line_2 = LineString([[3, 0], [7, 0]])
intersec = intersection(line_1, line_2)
if not intersec.is_empty:
    intersect_range = [intersec.coords.xy[0][0], intersec.length]
segments = difference(line_1, line_2)
for segment in segments.geoms:
    start = segment.coords.xy[0][0]
    segment_range = [segment.coords.xy[0][0], segment.length]
    if (start < 3):
        before.append(segment_range)
    else:
        after.append(segment_range)
print("hello")
