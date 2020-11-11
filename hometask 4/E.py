def chain_loop(args):
    iterators = list(map(iter, args))
    pos = list(range(len(args)))
    j = 0
    while len(pos) > 0:
        try:
            yield next(iterators[pos[j]])
        except StopIteration:
            pos.pop(j)
            j -= 1
        finally:
            j += 1
            if (j >= len(pos)):
                j = 0
