from collections import deque
import shapely
from shapely import LineString, MultiLineString, intersection, difference

class FilterMapRange:
    def __init__(self, dest_range_start, source_range_start, range_length):
        self.dest_start = dest_range_start
        self.source_start = source_range_start
        self.length = range_length

class NormalRange:
    def __init__(self, range_start, range_length):
        self.start = range_start
        self.length = range_length

def go_through_one_filter(filter, normal_ranges):
    unprocessed = deque(normal_ranges)
    processed = []
    for filter_map_range in filter:
        after = None
        while(after == None):
            if unprocessed:
                normal_range = unprocessed.popleft()
            else:
                break
            line_1 = LineString([[normal_range.start, 0], [normal_range.start + normal_range.length, 0]])
            line_2 = LineString([[filter_map_range.source_start, 0], [filter_map_range.source_start+filter_map_range.length, 0]])
            # Difference (left - right)
            line_diff = difference(line_1, line_2)
            if not None and not line_diff.is_empty:
                segments = []
                if type(line_diff) == LineString:
                    segments.append(line_diff)
                else:
                    segments.append(line_diff.geoms)
                for segment in segments:
                    normal_range_segment = NormalRange(int(segment.coords.xy[0][0]), int(segment.length))
                    # Before
                    if (normal_range_segment.start < filter_map_range.source_start):
                        processed.append(normal_range_segment)
                    # After
                    else:
                        after = normal_range_segment
                        unprocessed.appendleft(normal_range_segment)
            intersec = intersection(line_1, line_2)
            # Intersection
            if not intersec.is_empty:
                normal_range_intersection = NormalRange(int(intersec.coords.xy[0][0]), int(intersec.length))
                # Map the intersection range.
                map_delta = filter_map_range.dest_start - filter_map_range.source_start
                mapped_intersect_range = NormalRange(normal_range_intersection.start + map_delta, normal_range_intersection.length)
                processed.append(mapped_intersect_range)
    processed.extend(unprocessed)
    processed.sort(key=lambda normal_range: normal_range.start)
    return processed

# filter = [FilterMapRange(*[52, 50, 48]), FilterMapRange(*[50, 98, 2])]
# source_ranges = [NormalRange(*[55, 13]), NormalRange(*[79, 14])]
# expected = [NormalRange(*[57, 13]), NormalRange(*[81, 14])]
# output = go_through_one_filter(filter, source_ranges)
# assert expected == output 


file = open("src/day-5/input.txt", 'r')
all = file.read()
all = all.split('\n\n')
seeds = all[0]
all = all[1:]
seeds = seeds.split(': ')
seeds = [int(s) for s in seeds[1].split(' ')]
seed_pairs = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
seed_pairs.sort(key = lambda seed: seed[0])
seed_normal_ranges = [NormalRange(*seed_pair) for seed_pair in seed_pairs]
filters=[]
for raw_filter in all:
    lines = raw_filter.split('\n')
    lines = lines[1:]
    lines = [FilterMapRange(*[int(num) for num in line.split(' ')]) for line in lines]
    lines.sort(key=lambda filter_map_range: filter_map_range.source_start)
    filters.append(lines)

processing = list(seed_normal_ranges)
for filter in filters:
    processing = go_through_one_filter(filter, processing)

end_ranges = processing

print("hello")

