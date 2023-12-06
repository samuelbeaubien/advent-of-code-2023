class NumRange:
    """A range of numbers. Inclusive on both ends.
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end

class MappingRange:
    def __init__(self, source_start, source_end, dest_start, dest_end, real_mapping):
        self.source_range = [source_start, source_end]
        self.dest_range = [dest_start, dest_end]
        self.real_mapping = real_mapping

        def map_number_range(self, n_range):
            """ Returns the mapped range that fell inside the mapping range
            and the remaining num range that fell outside the mapping range."""
            if (n_range[0] < self.source_range[0]):
                raise Exception("Input range starts before mapping range")
            intersection_range = range(max(n_range[0], self.source_range[0]), min(n_range[-1], self.source_range[-1])+1)
            if (intersection_range.start >= intersection_range.stop):
                return [[], n_range]
            intersection = [intersection_range[0], intersection_range[-1]]
            if (self.real_mapping):
                mapped_intersection = [intersection[0] - self.source_start + self.dest_start, intersection[1] - self.source_start + self.dest_start]
            else:
                mapped_intersection = intersection
            if (intersection[1] == n_range[1]):
                return [mapped_intersection, []]
            else:
                return [mapped_intersection, [intersection[1]+1, n_range[1]]]





















# class MappingRange:
#     def __init__(self, dest_range_start, source_range_start, range_size):
#         self.dest_range_start = dest_range_start
#         self.source_range_start = source_range_start
#         self.range_size = range_size

#     def is_in_range(self, source_num):
#         """In range if in [source_range_start, source_range_start + range_size -1]

#         Args:
#             source_num (int): Source number

#         Returns:
#             bool: True if in range, false otherwise.
#         """
#         return (source_num >= self.source_range_start and 
#                 source_num < (self.source_range_start + self.range_size)
#         )
    
#     def get_dest_num(self, source_num):
#         if (self.is_in_range(source_num)):
#             diff = source_num - self.source_range_start
#             return self.dest_range_start + diff
#         else:
#             return source_num
    
class FilterMap:
    def __init__(self, raw_input):
        self.name = ""
        self.mapping_ranges = []
        self.add_ranges_from_lines(raw_input)
        self.sort_ranges_increasing()

    def add_range_from_list(self, l):
        dest_start_range = l[0]
        source_start_range = l[1]
        range_size = l[2]
        self.mapping_ranges.append(MappingRange(
            source_start_range, 
            source_start_range + range_size -1,
            dest_start_range, 
            dest_start_range + range_size - 1))

    def add_ranges_from_lines(self, lines):
        """Get the raw text of one filter and creates a filter.
        Important: cannot contain newline characters

        Args:
            lines (List[string]): All the lines
        """
        self.name = lines[0][:-1]
        lines = lines[1:]
        lines = [l.split(' ') for l in lines]
        for line in lines:
            line = [int(v) for v in line]
            self.add_range_from_list(line)

    def sort_ranges_increasing(self):
        l = self.mapping_ranges
        l.sort(key=lambda range: range.source_range[0])

    def filter(self, source_ranges):
        dest_ranges = []
        for mapping in self.mapping_ranges:
            for source_range in source_ranges:
                unmapped = [None]
                while unmapped != []:
                    [mapped, unmapped] = mapping.map_number_range(source_range)
                    if mapped != []:
                        dest_ranges.append(mapped)
                    source_range = unmapped
            source_range = dest_ranges
        return source_range




### Script ###

file = open("src/day-5/input.txt", 'r')
all = file.read()
all = all.split('\n\n')
seeds = all[0]
all = all[1:]
seeds = seeds.split(': ')
seeds = [int(s) for s in seeds[1].split(' ')]
seed_pairs = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

filters=[]
for filter_input in all:
    lines = filter_input.split('\n')
    filter = FilterMap(lines)
    filters.append(filter)

final_destinations = []
smallest_destination = 1000000
for seed_pair in seed_pairs:
    for seed in range(seed_pair[0], seed_pair[0] + seed_pair[1], 1):
        for filter in filters:
            seed = filter.get_dest_num(seed)
        if seed < smallest_destination:
            smallest_destination = seed 
answer = smallest_destination
print("hello")
