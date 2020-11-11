# префиксное дерево
from collections import deque
from collections import defaultdict


class Node:
    def __init__(self, label=''):
        self._children = defaultdict()
        self._final = False # является ли концом слова
        self._count = 0 # в скольких словах используется
        self._label = label # ключ


class Trie:
    def __init__(self):
        self._root = Node()

    def add(self, word=''): # добавить слово
        if word == '':
            return
        if word in self:
            return
        d = self._root
        d._count += 1
        for w in word:
            d = d._children
            d.setdefault(w, Node(w))
            d = d[w]
            d._count += 1
        d._final = True

    def __contains__(self, word=''): # слово in дерево
        d = self._root
        for w in word:
            if w not in d._children:
                return False
            d = d._children[w]
        return d._final is True

    def __len__(self): # len(дерево)
        return self._root._count

    def pop(self, word=''): # удалить слово из дерева
        if word == '':
            return
        if word not in self:
            raise KeyError(word)
        d = self._root
        d._count -= 1
        if d._count == 0:
            del d._children[word[0]]
            return
        for w in word:
            d._children[w]._count -= 1
            if d._children[w]._count == 0:
                del d._children[w]
                return
            d = d._children[w]
        d._final = False

    def __iter__(self): # обход в ширину
        return TrieIterator(self._root)

    def starts_with(self, prefix=''): # вывод слов с соответствующим префиксом 
        pos = self._root
        for w in prefix:
            if w not in pos._children:
                return TrieIterator(Node())
            pos = pos._children[w]
        return TrieIterator(pos, prefix[:-1])


class TrieIterator:
    def __init__(self, root, prefix=''):
        self.iter = deque([root])
        self.prefix = prefix

    def __iter__(self):
        return self

    def __next__(self):
        while (len(self.iter)):
            cur = self.iter.popleft()
            self.prefix = self.prefix + cur._label
            cur._label = self.prefix[-1] if self.prefix else ''
            for key in sorted(cur._children.keys()):
                cur._children[key]._label = self.prefix + cur._children[key]._label
                self.iter.append(cur._children[key])
            prefix = self.prefix
            self.prefix = ''
            if cur._final:
                return prefix
        if self.prefix:
            prefix = self.prefix
            self.prefix = ''
            return prefix
        raise StopIteration
