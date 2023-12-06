class MappingRange:
    def __init__(self, dest_range_start, source_range_start, range_size):
        self.dest_range_start = dest_range_start
        self.source_range_start = source_range_start
        self.range_size = range_size

    def is_in_range(self, source_num):
        """In range if in [source_range_start, source_range_start + range_size -1]

        Args:
            source_num (int): Source number

        Returns:
            bool: True if in range, false otherwise.
        """
        return (source_num >= self.source_range_start and 
                source_num < (self.source_range_start + self.range_size)
        )
    
    def get_dest_num(self, source_num):
        if (self.is_in_range(source_num)):
            diff = source_num - self.source_range_start
            return self.dest_range_start + diff
        else:
            return source_num
    
class FilterMap:
    def __init__(self, raw_input):
        self.name = ""
        self.ranges = []
        self.add_ranges_from_lines(raw_input)
        self.sort_ranges_increasing()

    def add_range_from_list(self, l):
        dest_start_range = l[0]
        source_start_range = l[1]
        range_size = l[2]
        self.ranges.append(MappingRange(dest_start_range, source_start_range, range_size))

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
        l = self.ranges
        l.sort(key=lambda range: range.source_range_start)


    def get_dest_num(self, source_num):
        # Find the first mapping range that starts after the source_num
        for i in range(len(self.ranges)):
            cur_range = self.ranges[i]
            if source_num < cur_range.source_range_start:
                if i > 0:
                    prev_range = self.ranges[i-1]
                    return prev_range.get_dest_num(source_num)
                else:
                    return source_num
            else:
                pass
        return cur_range.get_dest_num(source_num)
        




### Script ###

file = open("src/day-5/input.txt", 'r')
all = file.read()
all = all.split('\n\n')
seeds = all[0]
all = all[1:]
seeds = seeds.split(': ')
seeds = [int(s) for s in seeds[1].split(' ')]

filters=[]
for filter_input in all:
    lines = filter_input.split('\n')
    filter = FilterMap(lines)
    filters.append(filter)

final_destinations = []
for seed in seeds:
    for filter in filters:
        seed = filter.get_dest_num(seed)
    final_destinations.append(seed)
answer = min(final_destinations)
print("hello")
