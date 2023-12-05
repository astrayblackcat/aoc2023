from functools import reduce

with open('input.txt') as f:
    input = [line for line in f.read().strip().split('\n\n') if line]

mappings = []
for mapping in input[1:]:
    cur = []
    for line in mapping.split('\n')[1:]:
        dst_st, src_st, rg_len = tuple(map(int, line.split()))
        cur.append([src_st, src_st + rg_len - 1, dst_st - src_st])
    mappings.append(sorted(cur))

def lookup(key, mapping):
    for source_st, source_end, delta in mapping:
        if key > source_end:
            continue
        elif key < source_st:
            return key
        else:
            return key + delta
    return key

def lookup_range(start, end, mapping):
    result = []
    for source_st, source_end, delta in mapping:
        if start > source_end or end < source_st:
            continue

        if start < source_st:
            result.extend([
                (start, source_st - 1),
                (source_st + delta, min(source_end, end) + delta)
            ])
        else: 
            result.append((start + delta, min(source_end, end) + delta))
        
        if source_end > end:
            return result
        start = source_end
    return result or [(start, end)]

def pairs(seeds):
    rg = [(seeds[0], seeds[0] + seeds[1])]
    for mapping in mappings:
        result = []
        for start, end in rg:
            result.extend(lookup_range(start, end, mapping))
        rg = result
    return min(result)[0]

seeds = list(map(int, input[0][7:].split()))
print(min(reduce(lookup, mappings, s) for s in seeds))
print(min([pairs(seeds[i:i+2]) for i in range(0, len(seeds), 2)]))

# this day sucks.