def answer(l):
    split = [v.split('.') for v in l]
    split = [[int(part) for part in parts] for parts in split]
    for parts in split:
        while len(parts) < 3:
            parts.append(-1)
            
    split.sort(key=lambda x:(x[0],x[1],x[2]))

    split = [[part for part in parts if part != -1] for parts in split]
    split = [[str(part) for part in parts] for parts in split]
    return ['.'.join(parts) for parts in split]

input = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
correct = ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]
assert(answer(input) == correct)
