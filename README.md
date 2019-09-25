# 《剑指offer》第二版 Python 实现
[题3.1-找出数组中重复的数字](题3.1-找出数组中重复的数字.py)   
**要求时间复杂度 O(N)，空间复杂度 O(1)** 。因此不能使用排序的方法，也不能使用额外的标记数组。对于这种数组元素在 [0, n-1] 范围内的问题，可以将值为 i 的元素调整到第 i 个位置上进行求解。以 (2, 3, 1, 0, 2, 5) 为例，遍历到位置 4 时，该位置上的数为 2，但是第 2 个位置上已经有一个 2 的值了，因此可以知道 2 重复

[题3.2-不修改数组找出重复的数字](题3.2-不修改数组找出重复的数字.py)   
**时间复杂度 O(NlogN)，空间复杂度 O(1)** 。二分查找方法。以长度为 8 的数组 {2, 3, 5, 4, 3, 2, 6, 7} 为例，那么所有数字都在 1-7 的范围内。中间的数字 4 将 1-7 分为 1-4 和 5-7。统计 1-4 内数字的出现次数，它们一共出现了 5 次，说明 1-4 内必要重复的数字；反之，若小于等于 4 次，则说明 5-7 内必有重复的数字。因为不能使用额外的空间，所以每次统计次数都要重新遍历整个数组一次

[题4-二维数组中的查找](题4-二维数组中的查找.py)
**时间复杂度 O(M+N)** 。从数组右上角或者左下角开始查找 array[i][j]

[题5-替换空格](题5-替换空格.py)
**时间复杂度 O(N)** 。如果直接每次遇到空格添加 "%20"，那么空格后面的数字就需要频繁向后移动。遇到这种移动问题，可以尝试先遍历一次，找出空格的数量，得到替换后的长度，然后从后往前扫描替换。逆向思维

[题6-从尾到头打印链表](题6-从尾到头打印链表.py)
（1）从头到尾遍历链表，并用栈存储每个结点的值，之后出栈输出
（2）使用递归方法

[题7-重构二叉树](题7-重构二叉树.py)
利用二叉树前序遍历和中序遍历的特性。前序遍历的第一个值为根节点的值，使用这个值将中序遍历结果分成两部分，左部分为树的左子树中序遍历结果，右部分为树的右子树中序遍历的结果。然后递归

[题8-二叉树的下一个结点](题8-二叉树的下一个结点.py)
若该节点存在右子树：则下个节点为右子树最左子节点；
若该节点不存在右子树：这时分两种情况：该节点为父节点的左子节点，则下一个节点为其父节点。该节点为父节点的右子节点，则沿着父节点向上遍历，直到找到一个节点，该结点是其父节点的左子节点，则该节点的父节点就是下一个节点

[题9-用两个栈实现队列](题9-用两个栈实现队列.py)
假设 stack_in 用于处理入栈操作，stack_out 用于处理出栈操作，stack_in 按栈的方式正常处理入栈数据。关键在于出栈操作。当 stack_out 为空时，需要先将每个 stack_in 中的数据出栈后压入 stack_out。反之，每次弹出 stack_out 栈顶元素即可

[题10.1-斐波那契数列](题10.1-斐波那契数列.py)    
三种思路（1）递归（2）循环，**时间复杂度O(N)** （3）求矩阵的乘方，**时间复杂度O(logN)**

[题10.2-青蛙跳台阶问题](题10.2-青蛙跳台阶问题.py)    
斐波那契数列问题

[题21-调整数组顺序使奇数位于偶数前面](题21-调整数组顺序使奇数位于偶数前面.py)
（1）使用新列表，奇数存一个列表，偶数存一个列表，合并
（2）使用冒泡的思想

[题22-链表中倒数第K个节点](题22-链表中倒数第K个节点.py)
如果输入链表为空，K 小于等于 0，K 大于链表的长度，返回 None；如果正常情况，设置两个指针 p1, p2 分别指向头节点，p1 指针先向前走 K-1 步，走到正数第 K 个节点，然后两指针分别往前移动，直到 p1 走到最后一个节点

[题23-链表中环的入口节点](题23-链表中环的入口节点.py)
使用双指针，一个指针 fast 每次移动两个节点，一个指针 slow 每次移动一个节点。因为存在环，所以两个指针必定相遇在环中的某个节点上。假设相遇点在下图的 z1 位置（图片这里没放），此时 fast 移动的节点数为 x+2y+z，slow 为 x+y，由于 fast 速度比 slow 快一倍，因此 x+2y+z=2(x+y)，得到 x=z。在相遇点，slow 要到环的入口点还需要移动 z 个节点，如果让 fast 重新从头开始移动，并且速度变为每次移动一个节点，那么它到环入口点还需要移动 x 个节点。在上面已经推导出 x=z，因此 fast 和 slow 将在环入口点相遇



