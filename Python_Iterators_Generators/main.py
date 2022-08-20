nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, list_):
        self.list_ = [item for item in flat_iterator(list_)]
        self.list_len = len(self.list_)

    def __iter__(self):
        # Place the cursor before the first element
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.list_len:
            raise StopIteration
        # If the last element wasn't reached return next element
        return self.list_[self.cursor]


def flat_iterator(list_):
    for item in list_:
        if isinstance(item, list):
            yield from flat_iterator(item)
        else:
            yield item


if __name__ == '__main__':
    print(f'ITERATORS: ')
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print(f'GENERATORS: ')
    for item in flat_iterator(nested_list):
        print(item)

    flat_list = [item for item in flat_iterator(nested_list)]
    print(flat_list)


