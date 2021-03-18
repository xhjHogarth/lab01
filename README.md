Students should implement the selected data structure in two way:
• as a mutable object (interaction with an object should modify it if applicable)
• as an immutable object (interaction with an object cannot change it).

For each version of a library (mutable and immutable) you should implement the following
features (in the brackets you can see examples of muttable and immutable API for single-linked
list):
• Add a new element (lst.add(3), cons(lst, 3))
• Remove an element by value (lst.remove(3), remove(lst, 3))
• Size (lst.size(), size(lst)), member, reverse (if applicable), intersection
• Conversion from/to built-in list (you should avoid of usage these function into your library):
– from (lst.from_list([12, 99, 37]), from_list([12, 99, 37]))
– to (lst.to_list(), to_list(lst)).
• Find element by specific predicate (lst.find(is_even), find(lst, is_even))
• Filter data structure by specific predicate (lst.filter(is_even), filter(lst, is_even))
• Map (link) structure by specific function (lst.map(increment), map(lst, increment))
• Reduce (link)– process structure elements to build a return value by specific functions (lst.reduce(sum),
reduce(lst, sum))
• Data structure should be an iterator (link)
– for the mutable version in Python style [10, Chapter 7. Classes & Iterators]ho
– for the immutable version by closure [47c], see example ahead.
• Data structure should be a monoid and implement mempty and mconcat.

Unrolled linked list (link)
• You can use the built-in list inside nodes
• You need to check that your implementation correctly works with None value
• A user should specify node size
• You need to implement functions/methods for getting/setting value by index.


precautions:
To insert a new element, we simply find the node the element should be in and insert the element into the elements array, incrementing numElements. If the array is already full, we first insert a new node either preceding or following the current one and move half of the elements in the current node into it.
To remove an element, we simply find the node it is in and delete it from the elements array, decrementing numElements. If this reduces the node to less than half-full, then we move elements from the next node to fill it back up above half. If this leaves the next node less than half full, then we move all its remaining elements into the current node, then bypass and delete it.
