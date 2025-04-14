Max Heap: Parent ≥ Children
Min Heap: Parent ≤ Children

**Always fills left to right in each level (complete tree)**

Operation|	Time Complexity|	Description
|---|---|---|
Insert|	O(log n)|	Bubble-up to restore heap
Delete| Max/Min	O(log n)|	Remove root and heapify down
Heapify|	O(n)|	Build heap from array
Peek|	O(1)|	Look at top without removing


### How is a Heap Stored?
Heaps are stored in arrays, not pointer trees.

For node at index i:

Left child = 2*i + 1
Right child = 2*i + 2
Parent = (i - 1)/2