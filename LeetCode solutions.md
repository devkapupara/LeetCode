### [Lowest Common Ancestor](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

```java
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    TreeNode current = root;
    while (current != null){
        if (p.val < current.val && q.val < current.val)		// Both located in left side.
            current = current.left;
        else if (p.val > current.val && q.val > current.val)	// Both located in right side
            current = current.right;
        else
            return current;		// Seperate branches, therefore current is lca.
    }
    return null;
}
```



### [Count And Say](https://leetcode.com/problems/count-and-say/)

```java
public String countAndSay(int n) {
    String result = "1";			// First letter
    for (int i = 1; i < n; i++){	// To get the nth string.
    	int startIndex = 0;
    	String temp = "";
    	while (startIndex < result.length()){	// While the previous string is unfinished
        	char ch = result.charAt(startIndex)
        	int count = 0;
        	while (ch == result.charAt(startIndex)){	// While ch is same
            	count++;		// record the count
            	startIndex++;	// increment the index to keep track of current
            	if (startIndex >= result.length())	// If out of bounds, break.
                	break;
       	 	}
    	    temp += count + String.valueOf(ch);		// Add the frequency and ch to temp.
  		}
  	    result = temp;			// Update result to temp to generate the next "say"
    }
	return result;
}
```



### [Maximum SubArray](https://leetcode.com/problems/maximum-subarray/)

```java
public int maxSubArray(int[] nums) {
    int localMax = nums[0];		// keeps track of max sum between the previous and current
    int globalMax = nums[0];	// keeps track of global max sum.

    /*
    The idea is as follows:
    If the current element is greater than the previous local max, then we found an element that is a better option then before.
    Then, if that localmax changed and is greater than our global max, update our global max.
    */

    for (int i = 1; i < nums.length; i++){
        localMax = Math.max(localMax + nums[i], nums[i]);
        globalMax = Math.max(localMax, globalMax);
    }

    return globalMax;
}
```



### [Plus One](https://leetcode.com/problems/plus-one/)

```java
public int[] plusOne(int[] digits)
{
    digits[digits.length-1]++;			// Add one to the last place.
    if (digits[digits.length-1] == 10)	// If it became 10,
    {
        for (int i = digits.length-1; i > 0; i--)	// Then add one to its previous place
        {
            if (digits[i] == 10){	// If that also results in 10, keep propogating that 1
                digits[i-1]++;		// upstream
                digits[i] = 0;
            }
        }
        if (digits[0] == 10){	// If the index 0 is 10, then the number is a multiple of 10.
            digits = new int[digits.length+1];
            digits[0] = 1;		// So increase length by 1 and set index 0 to 1.
        }
    }
    return digits;
}
```



### [Sqrt of X](https://leetcode.com/problems/sqrtx/)

```java
public int mySqrt(int x) {
    long x1 = 10 - (100 - x)/20;		// Using Newton's method of computing square roots.
    boolean done = false;
    while (!done)
    {
        long x2 = x1 - (x1*x1 - x)/(2*x1);
        if (x2 == x1)
            done = true;
        else
            x1 = x2;
    }
    return (int)x1-1;
}
```



### [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

```java
public int climbStairs(int n) {
    if (n < 4)		// I chose n < 4 because climbStairs(0 <= n <= 3) = n
        return n;
    int[] dp = new int[n+1];
    for (int i = 0; i < 4; i++)
        dp[i] = i;
    //return naiveDP(n, dp);
    return efficientDP(n);
}

public int naiveDP(int n, int dp[]){
    if (dp[n] != 0)		// If already computed, return it.
        return dp[n];
    int ways =  naiveDP(n-1, dp) + naiveDP(n-2, dp);	// Just like Fibonacci.
    dp[n] = ways;		// Save it.
    return ways;
}

public int efficientDP(int n){
    if (n < 4)
        return n;
    int[] dp = new int[n+1];		// Initialize dp of length n+1 to store n'th way.
    for (int i = 0; i < 4; i++)
        dp[i] = i;					// climbStairs(0 <= n <= 3) = n
    for (int i = 3; i <= n; i++)	// climbStairs(n) = climbStairs(n-1) + climbstairs(n-2);
        dp[i] = dp[i-1] + dp[i-2];  // So fetch those values from the dp array.
    return dp[n];
}
```



### [Remove Duplicates from sorted list](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

```java
public ListNode deleteDuplicates(ListNode head){
    ListNode current = head;
    // while we haven't reached the tail
    while (current != null && current.next != null)
    {
        // if current's next is the same as current, skip and update its next
        while (current.next != null && current.val == current.next.val)
            current.next = current.next.next;
        current = current.next;
    }
    return head;
}
```



### [Same Tree](https://leetcode.com/problems/same-tree/)

```java
public boolean isSameTree(TreeNode p, TreeNode q)
{
    if (p == null && q == null)		// Two empty trees
        return true;
    // If one of the node is null, the two trees can't be equal.
    if ((p == null && q != null) || (p != null && q == null))
        return false;
    // If the values in the two nodes are same, compare its's left and right sub-tree.
    if (p.val == q.val)
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    return false;		// If nothing worked out, they can't be same.
}
```



### [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

```java
public boolean isSymmetric(TreeNode root)
{
    return isSymmetricIterative(root);
}

public boolean isSymmetricIterative(TreeNode root)
{
    Queue<TreeNode> track = new LinkedList<>();
    track.add(root);		// Add the root twice so we can compare its left and right
    track.add(root);
    while (!track.isEmpty())
    {
        TreeNode x = track.poll();		// Remove 2 nodes
        TreeNode y = track.poll();

        if (x == null && y == null)		// If they are both null, skip it.
            continue;
        if (x == null || y == null || x.val != y.val)
            return false;				// If values don't match or one is null
        track.add(x.left);		// Otherwise add them in this order -> LRRL
        track.add(y.right);		// because we need to compare left most with the
        track.add(x.right);		// right most, then inner left with inner right.
        track.add(y.left);
    }
    return true;		// Everything's all right, so they must be symmetric.
}

public boolean isSymmetricRecursive(TreeNode root)
{
    return helperRecursive(root, root);
}

private boolean helperRecursive(TreeNode x, TreeNode y)
{
    if (x == null || y == null)		// Base Case: Both or one is null, so true
        return true;
    return (x.val == y.val && helperRecursive(x.left, y.right) && helperRecursive(x.right, y.left));
    // Check if values match and 1.left matches with the 2.right and 1.right matches with 2.left
}
```



### [Max Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

```java
/*
If root is null, height is 0 else add 1 and find if the left or the right has a greater depth.
*/
public int maxDepth(TreeNode root) {
    return root == null ? 0 : 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```



### [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

```java
public TreeNode sortedArrayToBST(int[] nums)
{
    return aux(nums, 0, nums.length-1);
}

private TreeNode aux(int[] n, int left, int right)
{
    if (left > right)					// Either empty, or return a null node
        return null;

    int mid = (left+right+1)/2;			// Create a node with the middle value
    TreeNode root = new TreeNode(n[mid]);
    root.left = aux(n, left, mid-1);	// Compute the left (which is the mid in left side)
    root.right = aux(n, mid+1, right);	// Compute the right (which is the mid in right side)
    return root;
}
```



### [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

```java
public boolean isBalanced(TreeNode root)
{
    return isBalancedBottomUp(root);
}

public boolean isBalancedTopDown(TreeNode root)
{
    if (root == null)
        return true;
    // if difference between root's left and right is > 1, they're not balanced
    if (Math.abs((getHeight(root.left) - getHeight(root.right))) > 1)
        return false;
    // otherwise, we need to check if the left and right subtree are also balanced.
    return isBalanced(root.left) && isBalanced(root.right);
}

private int getHeight(TreeNode node)
{
    // Standard height of a binary tree calculator
    if (node == null)
        return 0;
    return 1 + Math.max(getHeight(node.left), getHeight(node.right));
}

public boolean isBalancedBottomUp(TreeNode root)
{
    return getHeight2(root) != -1;	// -1 means not balanced.
}

private int getHeight2(TreeNode node)
{
    if (node == null)
        return 0;

    int lHeight = getHeight2(node.left);	// Get the height of left and right tree
    int rHeight = getHeight2(node.right);

    // If at any point there was a height difference of more than 1 or previous node's leftheight || rightheight returned -1, return -1 to let the next node know there was an imbalance.
    if ((Math.abs(lHeight-rHeight) > 1) || lHeight == -1 || rHeight == -1)
        return -1;

    return 1 + Math.max(lHeight, rHeight); // Else carry on with the normal procedure
}

```



### [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

```java
public int minDepth(TreeNode root) {
    // Base case
    if (root == null) return 0;
    // Left is null, find minheight from right side
    if (root.left == null) return 1 + minDepth(root.right);
    // Right is null, find minheight from left side
    if (root.right == null) return 1 + minDepth(root.left);
    // Else, both are not null, so compute min height from the two sides.
    return 1 + Math.min(minDepth(root.left), minDepth(root.right));
}
```



### [Path Sum](https://leetcode.com/problems/path-sum/)

```java
public boolean hasPathSum(TreeNode root, int sum) {
    if (root == null)
        return false;	// No sum exist
    sum -= root.val;	// Sum decreases
    if (root.left == null && root.right == null)	// If we are at a leaf
        return sum == 0;	// Check if the sum is 0.
    return hasPathSum(root.left, sum) || hasPathSum(root.right, sum);
    // Otherwise look if you can make sum = 0 by exploring the left or right side.
}
```



### [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

```java
public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> pt = new ArrayList<>();
    for (int i = 0; i < numRows; i++)	// Need to add all n rows
    {
        List<Integer> temp = new ArrayList<>();		// temp list to store values
        for (int j = 0; j <= i; j++)
        {
            if (j == 0 || i == j)		// First and last values are always 1.
                temp.add(1);
            else	// Else, get the previous row and surrounding two values and add them
                temp.add(pt.get(i-1).get(j-1) + pt.get(i-1).get(j));
        }
        pt.add(temp);		// Add it to pt.
    }
    return pt;
}
```



### [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

```java
public boolean isPalindrome(String s) {
    if (s.length() > 0){		// Only do this is s is not empty
        s = s.toLowerCase();	// Convert it to lowercase
        int left = 0;			// Initialize left and right pointers
        int right = s.length()-1;
        while (left < right)	// continue while we haven't hit the middle of the string
        {
            // If char at left is not a letter or a number, skip it.
            if (!Character.isLetter(s.charAt(left)) && !Character.isDigit(s.charAt(left)))
                left++;
            // Same with char at right.
            else if (!Character.isLetter(s.charAt(right)) && !Character.isDigit(s.charAt(right)))
                right--;
            //Char's are now alphanumeric.
            else if (s.charAt(left) != s.charAt(right))	// If they don't match
                return false;	// return false
            else	// They matched, so try to match the inner string
            {
                left++;
                right--;
            }
        }
    }
    return true;	// No mismatch found, return true.
}
```



### [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

```java
public List<Integer> getRow(int rowIndex)
{
    ArrayList<Integer> row = new ArrayList<>();
    row.add(1);	// First is always 1.
	// Using the nth row formula to compute the coeeficients. You can google "nth row Pascal"
    for (int i = 0; i < rowIndex; i++)
        row.add((int)(1.0*row.get(i)*(rowIndex-i)/(i+1)));
    return row;
}
```



### [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```Java
/*
The general idea is that if the price you are looking at right now in the array minus the minimum observed so far is greater than the maximum profit you recorded, update the max.
*/
public int maxProfit(int[] prices) {
    if (prices.length == 0)		// Empty array
        return 0;
    int min = prices[0];

    int max = 0;
    for (int i = 1; i < prices.length; i++)
    {
        if (prices[i] < min)
            min = prices[i];
        else if (prices[i] - min > max)
            max = prices[i]-min;
    }
    return max;
}
```



### [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

```java
/*
The general idea is that the moment you observe a valley and consecutive peak, make the trade by buying the stock on the valley day and selling it on the peak day.
*/
public int maxProfit(int[] prices) {
    int sum = 0;
    for (int i = 0; i < prices.length-1; i++)
        if (prices[i+1] > prices[i])
            sum += (prices[i+1] - prices[i]);
    return sum;
}
```



### [Single Number](https://leetcode.com/problems/single-number/)

```java
/*
The general idea is that XOR of two same numbers returns 0 and XOR with 0 returns the same number. So if there is only one element that doesn't have a pair, all the remaining will XOR with themselves at one point and give 0 but not the singleton element.
*/
public int singleNumber(int[] nums) {
    int num = nums[0];
    for (int i = 1; i < nums.length; i++)
        num ^= nums[i];
    return num;
}
```



### [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

```java
// Using the slow-fast runner technique.
public boolean hasCycle(ListNode head) {
    if (head == null)
        return false;
    ListNode first = head;	// Slow runner
    ListNode second = first.next;		// Fast Runner
    // while second is not at the end or it isn't the tail
    while (second != null && second.next != null)
    {
        if (second == first)	// If fast made a full loop and met up with slow
            return true;		// We got a cycle
        first = first.next;		// Slow moves one step
        second = second.next.next;	// Second advances two.
    }
    return false;		// We don't have a cycle
}
```



### [Min Stack](https://leetcode.com/problems/min-stack/)

```Java
class MinStack {

    int min;
    Stack<Integer> stack;

    public MinStack() {
        min = Integer.MAX_VALUE;
        stack = new Stack<>();
    }

    public void push(int x) {
        stack.push(x);		// Push the value
        if (x < min)		// If that value is minimum than we have, update min
            min = x;
        stack.push(min);	// Push the minimum on top of the stack for constant time
    }						// minimum retrieval.

    public void pop() {
        stack.pop();		// Pop the minimum.
        stack.pop();		// Pop the actual element meant to be popped
        if (stack.isEmpty())	// If empty, min is Max int value
            min = Integer.MAX_VALUE;
        else
            min = stack.peek();	// Otherwise, min would be the top most element since we
    }							// always push the minimum on top of any element we push.

    public int top() {
        return stack.elementAt(stack.size()-2);	// Top element is actually at second last
    }				// index since the last element is the minimum.

    public int getMin() {
        return min;
    }
}
```



### [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

```java
/*
The general idea is that if you are done traversing any of the lists, make it's pointer point to the head of the other list and start iterating. The reasoning is that the second time they iterate, they will have traversed exactly the same distance (it's length plus the other list's head to the intersecting node) and will meet at the intersecting node.
*/
public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    int count = 0;
    ListNode pA = headA;
    ListNode pB = headB;
    while (pA != pB){
        pA = pA == null ? headB : pA.next;
        pB = pB == null ? headA : pB.next;
    }
    return pA;
}
```



### [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

```java
public int[] twoSum(int[] numbers, int target) {
    int left = 0, right = numbers.length-1;
    while (left < right)	// Narrow down the window from both sides until they add up.
    {
        int sum = numbers[left] + numbers[right];
        if (sum > target)	// We overshot, so decrease the window from right
            right--;
        else if (sum < target)	// Undershot, increase windows from left so next sum is more
            left++;
        else
            break;				// Found the two numbers
    }
    return new int[] {left+1, right+1};	// +1 because LeetCode followed 1-n indexing.
}
```



### [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)

```java
public String convertToTitle(int n) {
    String res = "";
    while (n > 0)
    {
        /* 1 is A and 26 is Z, so n-1 to change it to 0-25 scheme. Then, % 26 to find how
        much it is off on a full alphabet cycle, add 65 (ASCII for A) and convert it to char
        */
        res = String.valueOf((char)(65+((n-1)%26))) + res;
        n = (n-1) / 26;	// Subtract 1 and divide by 26 to get prepare for the next character
    }
    return res;
}
```



### [Majority Element](https://leetcode.com/problems/majority-element/)

Uses [Moore's Algorithm](https://www.geeksforgeeks.org/majority-element/)

```java
// This is the implementation of Moore's Algorithm for O(n) complexity.
public int majorityElement(int[] nums) {
    int major = nums[0];
    int count = 1;

   for (int i = 0; i < nums.length; i++){
        if (major == nums[i])
            count++;
        else
            count--;
        if (count == 0){
            major = nums[i];
            count = 1;
        }
    }
    return major;
}
```



### [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

```java
/*
Start from the end of String s, compute the ASCII for the char, +1 for 1-26 Alphabet-Scheme (hence -64 instead of -65) and multiply it to 26^{distance from the end of the string}
*/
public int titleToNumber(String s) {
    int length = s.length()-1;
    int total = 0;
    for (int i = length; i > -1; i--)
        total += (int)(s.charAt(i)-64) * Math.pow(26,length-i);
    return total;
}
```



### [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)

```java
/*
The general idea is that every factorial that has 5 as a multiple also has 2 to multiply to 10. So if we can count the number of times we can divide n by 5, should gives us the number of trailing zeroes. O(log(n) base 5) complexity.
*/
public int trailingZeroes(int n) {
    int res = 0;
    while (n > 4)
    {
        res += n / 5;
        n /= 5;
    }
    return res;
}
```



### [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)

```mysql
select FirstName, LastName, City, State
from Person left join Address on Address.personId = person.personId;
```



### [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)

```mysql
select max(salary) as SecondHighestSalary
from Employee
where salary not in (select max(salary) from employee);
```



### [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

```mysql
select emp.Name as Employee
from Employee emp, Employee man
where emp.managerId = man.Id and emp.salary > man.salary;
```



### [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)

```mysql
select email
from person
group by (email)
having count(*) > 1;
```



### [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/)

```mysql
select name as Customers
from Customers
where customers.id not in (select customerId from orders);
```



### [Rotate Array](https://leetcode.com/problems/rotate-array/)

```java
public void rotate(int[] nums, int k) {
    k %= nums.length;		// k == nums.length ? Then it's a full rotation and no change
    if (k == 0)
        return;
    reverse(nums, 0 , nums.length-1);	// First reverse the full array
    reverse(nums, 0, k-1);				// Then reverse element from index 0 to k-1
    reverse(nums, k, nums.length-1);	// Then reverse all elements from k to end of Array
}

// Reverse function that reverses the array from specified indices.
public void reverse(int[] nums, int start, int end)
{
    while (start < end){
        int temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
}
```



### [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/)

```mysql
delete from Person
where Id not in (select min_id from
(select min(Id) as min_id from Person group by Email) as a)
```



### [Rising Temperature](https://leetcode.com/problems/rising-temperature/)

```mysql
select w2.id
from weather w1, weather w2
where Datediff(w2.recorddate, w1.recorddate) = 1 and w2.temperature > w1.temperature;
```



### [X of a Kind in a Deck of Cards](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/)

```java
public boolean hasGroupsSizeX(int[] deck) {
    HashMap<Integer, Integer> freq = new HashMap<>();

    for (int i = 0; i < deck.length; i++)		// Record the frequencies
        freq.put(deck[i],freq.getOrDefault(deck[i],0)+1);

/*
deck = [1,1,2,2,2,2,3,3,3,3,3,3]
number 1 has len of 2, number 2 has len of 4, number 3 has len of 6, they share a Greatest common divisor of 2, which means diving them into group of size X = 2, will be valid. Thus we just have to ensure each length (of a number) shares a Greatest Common Divisor that's >= 2.
*/
    int hcf = 0;
    for (int i: freq.keySet())
        hcf = gcd(hcf, freq.get(i));

    return hcf > 1;
}

private static int gcd(int x, int y)
{
    int temp = 0;
    while (y != 0){
        temp = y;
        y = x % y;
        x = temp;
    }
    return x;
}
```



### [Reverse Integer](https://leetcode.com/problems/reverse-integer/solution/)

```Java
public int reverse(int x) {
    int sign = x < 0 ? -1 : 1;
    x = x * sign;							// Make x positive
    long n = 0;
    while (x > 0){
        n = n * 10 + x % 10;				// Start adding from the end.
        x /= 10;
    }
    return (int)n == n ? (int)n*sign : 0;	// Try converting to int from long, if no change,
}											// Return n * sign, else 0 cause overflow.
```



### [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/submissions/)

```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    int carry = 0;							// To record the carry
    int sum = 0;							// To record the total of two vals
    ListNode dummy = new ListNode(0);		// Dummy's next is the actual head
    ListNode curr = dummy;
    do{
        if (l1 == null)						// If one of the node is null, we set it to a
            l1 = new ListNode(0);			// dummy value of 0 so we can adjust for
        if (l2 == null)						// different length of the two lists.
            l2 = new ListNode(0);
        sum = l1.val + l2.val + carry;		// Add the two vals and the carry.
        carry = sum < 10 ? 0 : 1;			// Record the carry for the next iteration
        curr.next = new ListNode(sum % 10);	// next node's value is sum % 10.
        curr = curr.next;					// advance current, l1 and l2.
        l1 = l1.next;
        l2 = l2.next;
    } while(l1 != null || l2 != null);
    if (carry == 1)							// In the end, if carry is 1, it was from
        curr.next = new ListNode(carry);	// from adding last terms, so make next node 1

    return dummy.next;						// Return the actual head.
}
```



### [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

```java
public int lengthOfLongestSubstring(String s) {
    if (s == null || s.length() == 0)
        return 0;

    int[] hash = new int[128];					// To store the occurence of characters
    int maxLength = 0;
    for (int i = 0, j = 0; j < s.length(); j++){
        i = Math.max(hash[s.charAt(j)], i);		// Check the most recent index of character.
        maxLength = Math.max(maxLength, j-i+1);	// That minus current pointer gives length
        hash[s.charAt(j)] = j+1;				// Record the index of the next character.
    }
    return maxLength;
}
```



### [House Robber](https://leetcode.com/problems/house-robber)

```java
/*
The basic idea is that if you are robbing house i, the maximum loot may come from by robbing the i-2th house or by robbing the i-3th house. Therefore rob both and then find the path that gave the maximum profit.
Example: loot = [1,9,3,8,4,3,6,4,3,5,7,6]
Profit DP = [1,9,4,17,13,20,23,24,26,29,33,35]
Here,
	dp[2] = loot[2] + loot[1]
	dp[4] = loot[4] + max(dp[2], dp[1])
	dp[5] = loot[5] + max(dp[3], dp[2]) and so on.
In the end, just compare the last two elements to check which path gave us the maximum profit.
Some people might not prefer modifying the original nums array. In that case, you can initialize another dp array of same length, initialize the first two elements as dp[0] = nums[0] and dp[1] = nums[1] and dp[3] = nums[0] + nums[2] and then performing the same loop. In that case, you would be using O(n) space.
*/
public int rob(int[] nums) {
    if (nums.length == 0 || nums == null)			// 3 Base Case
        return 0;
    if (nums.length == 1)
        return nums[0];
    else if (nums.length == 2)
        return Math.max(nums[0], nums[1]);
    else{
        nums[2] = nums[0] + nums[2];				// House 3 profit is rob House 1 and 3.
        for (int i = 3; i < nums.length; i++)
            nums[i] = nums[i] + Math.max(nums[i-2], nums[i-3]);
        return Math.max(nums[nums.length-1], nums[nums.length-2]);
    }
}
```



### [Happy Number](https://leetcode.com/problems/happy-number/submissions/)

```java
public boolean isHappy(int n) {
        return isHappyConstantSpace(n);		// Much faster than set method
        //return isHappySet(n);
    }

    private boolean isHappyConstantSpace(int n){
        int numSeenLessThan10 = 0;		// If I see 10 single digits, then it means that I am
        while (n != 1){					// now starting to see repititions.
            if (n < 10)					// Each time I see a num < 10, increment the counter
                numSeenLessThan10++;
            if (numSeenLessThan10 > 9)
                return false;
            n = getSquare(n);			// Get the total of square of its digits.
        }
        return true;
    }

/*
The general idea is that the moment you see a repition, it can't be a happy number, so keep track of digit square obtained so far. If they hit 1, well and good, otherwise there will be some repition, so return false.
*/
    private boolean isHappySet(int n){
        HashSet<Integer> seen = new HashSet<>();		// Keep track of numbers
        while (true){
            n = getSquare(n);							// Get the sum of digits square
            if (n == 1)									// If it's 1, it's a happy number
                return true;
            else if (seen.contains(n))					// If it's a repition of something
                return false;							// seen before, it's not a happy no.
            else
                seen.add(n);							// If not seen, add it.
        }
    }

    private int getSquare(int n){		// Add the squares of the digits.
        int total = 0;
        while (n != 0){
            int digit = n % 10;
            total += digit * digit;
            n /= 10;
        }
        return total;
    }
}
```



### [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

```java
public ListNode removeElements(ListNode head, int val) {
    while (head != null && head.val == val)				// While head contains the val, skip
        head = head.next;								// the head
    ListNode current = head;
    while (current != null && current.next != null){	// While we have something to iterate
        if (current.next.val == val)					// If current's val match, skip the
            current.next = current.next.next;			// next node.
        else
            current = current.next;						// Else advance to the next node.
    }
    return head;
}
```



### [Count Primes](https://leetcode.com/problems/count-primes/submissions/)

```java
public int countPrimes(int n) {
    if (n < 2)
        return 0;							// No prime numbers for numbers < 2
    boolean[] store = new boolean[n];		// Using Sieve of Eratosthenes
    for (int i = 2; i*i <= n; i++)			// Start from i = 2 to sqrt(n)
        if (!store[i])						// If store[i] = false, then mark all its
            for (int j = i*i; j < n; j += i)// multiples in the store as true
                store[j] = true;			// True = not a prime, false = prime
    int count = 0;
    for (int i = 2; i < n; i++)				// Loop through the array, count
        if (!store[i])
            count++;
    return count;
}
```



### [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/submissions/)

```Java
public boolean isIsomorphic(String s, String t) {
    if (s.length() != t.length())			// Can't be isomorphic is string lengths do not
        return false;						// match
    char[] hashS = new char[128];			// To store String s' match
    char[] hashT = new char[128];			// To store String t's match
    for (int i = 0; i < s.length(); i++){
        char charS = s.charAt(i), charT = t.charAt(i);
        if (hashS[charS] != hashT[charT])	// If the values at respective characters index
            return false;					// do not match, return false
        hashS[charS] = (char)(i+1);			// Otherwise, mark those index with the same
        hashT[charT] = (char)(i+1);			// arbitrary value. I chose a simple (i+1) to
    }										// to mark both the hash with the same value.
    return true;							// Everything worked out, return true;
}
```



### [Reverse LinkedList](https://leetcode.com/problems/reverse-linked-list/solution/)

```java
// Recursive
public ListNode reverseList(ListNode head) {	// Very tricky. Refer to the demo below
    if (head == null || head.next == null)
        return head;
    ListNode node = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return node;
}

//Iterative
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null)
        return head;						// No point in reversing empty or 1-sized list
    ListNode curr = head, prev = null;
    ListNode nextNode;
    while (curr != null){					// While we haven't reached the tail
        nextNode = curr.next;				// Store the next node
        curr.next = prev;					// Current's next becomes it's previous
        prev = curr;						// Advance previous to current.
        curr = nextNode;					// Make current the actual next node
    }
    return prev;							// Current is at null, so it's previous is the
}											// new head.
```

![reverse Linked list](/Users/devkapupara/Desktop/Notes/dependencies/reverse Linked list.jpg)



### [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/submissions/)

```java
public boolean containsDuplicate(int[] nums) {
    if (nums.length < 2)
        return false;							// There can't be any duplicates.
    HashSet<Integer> store = new HashSet<>();	// Store unique values.
    for (int n: nums){
        if (!store.add(n))						// Add func returns true if n was'nt present,
            return true;						// false if duplicate. Therefore if it was a
    }											// duplicate, return true.
    return false;								// No duplicates, so return false
}
```



### [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

```java
public boolean containsNearbyDuplicate(int[] nums, int k) {
    if (nums.length < 2)
        return false;
    int left = 0, right = 0;
    HashSet<Integer> store = new HashSet<>();	// Use a rotating window of size k
    while (right < nums.length){				// While we haven't processed everything
        if (store.contains(nums[right]))		// If our current window contains duplicate
            return true;
        store.add(nums[right]);					// No duplicates in the window
        right++;								// Increase right to visit the new element
        if (right - left > k){					// If window becomes > k
            store.remove(nums[left]);			// remove the number on the left side of
            left++;								// the window and increase the left counter
        }										// for new window from the next index
    }
    return false;								// No duplicates found in any window.
}
```



### [Implement Stack Using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

```java
class MyStack {
    Deque<Integer> stack;
    /** Initialize your data structure here. */
    public MyStack() {
        stack = new ArrayDeque<>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        stack.add(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return stack.removeLast();
    }

    /** Get the top element. */
    public int top() {
        return stack.peekLast();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return stack.isEmpty();
    }
}
```



### [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

```java
public TreeNode invertTree(TreeNode root) {
    if (root == null)
        return null;
    TreeNode temp = root.left;		// Swap the left and right nodes
    root.left = root.right;
    root.right = temp;
    invertTree(root.left);			// Then swap the subsequent trees of those nodes.
    invertTree(root.right);
    return root;					// Return the original root.
}
```



### [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

```java
// Iterative
public int fib(int N) {
    if (N < 2)						// fib(0) = 0; fib(1) = 1
        return N;
    int f0 = 0, f1 = 1, fn = 0;
    for (int i = 2; i <= N; i++){
        fn = f0 + f1;				// fib(n) = fib(n-1) + fib(n-2)
        f0 = f1;					// f0 becomes f1
        f1 = fn;					// f1 becomes fn
    }
    return f1;
}

// Dynamic Programming
private int fibDP(int N){
    if (N < 2)
        return N;
    int[] dp = new int[N+1];		// To store intermediate result
    dp[1] = 1;						// fib(0) = 0; fib(1) = 1
    for (int i = 2; i <= N; i++)
        dp[i] = dp[i-1]+dp[i-2];	// fib(i) = fib(i-1) + fib(i-2)
    return dp[N];					// Return the last number in the array
}
```



### [kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/)

1.	The minheap algorithm has $O(n lg n) $ complexity and $O(1)$ space. The idea here is that we use a minheap to keep only the k greatest elements. If size becomes more than k, we remove the smallest element at the top of the heap. Thereby, at the end, our kth largest element will be at the top.
2.	2.QuickSelect Algorithm performs in $O(n)$ best case, $O(n^2)​$ worst case when the pivot chosen is always the largest, so we use a random pivot.


```java
// MinHeap Algorithm
public int kthLargest(int[] nums, int k){
    PriorityQueue<Integer> q = new PriorityQueue<>((n1,n2) -> n1 - n2);	// Initialize minheap
    for (int n: nums){
        q.add(n);				// Add number one by one
        if (q.size() > k)		// If size is greater than k
            q.poll();			// Remove the topmost element
    }
    return q.poll();			// The topmost element is
}

// QuickSelect Algorithm - Hoare's Partition Scheme

private int[] arr;

public int kthLargest(int[] nums, int k){
arr = nums;
return quickselect(0, nums.length-1, nums.length-k);	// kth largest is (n-k)th largest
}

private int quickselect(int left, int right, int k){
if (left == right)						// Array contains only 1 element, that's the answer
  return arr[left];
Random rand = new Random();				// Choose a random pivot between left and right
int pivotIndex = left + rand.nextInt(right-left);	// but not left
pivotIndex = partition(left, right, pivotIndex);	// Partition, and find it's correct index
if (k == pivotIndex)					// That index is equal to kth statistic
  return arr[pivotIndex];
else if (k < pivotIndex)				// If it's less than the index, our ans lies in the
  return quickselect(left, pivotIndex-1, k);	// left side
else
  return quickselect(pivotIndex+1, right, k);	// Otherwise, it's on the right side.
}

private int partition(int left, int right, int pivotIndex){
int pivot = arr[pivotIndex];			// Partition element
swap(pivotIndex, right);				// Move that element to the end
int wall = left - 1;					// wall is initially before everything
for (int i = left; i < right; i++){
  if (arr[i] < pivot)					// If the current element is < than the pivot, then
    swap(i, ++wall);					// we need to swap it with the element next to wall.
}
swap(right, ++wall);					// Lastly, swap the element at wall and the end.
return wall;
}

private void swap(int i, int j){
int temp = arr[i];
arr[i] = arr[j];
arr[j] = temp;
}
```



### [Power Of Two](https://leetcode.com/problems/power-of-two/)

```java
public boolean isPowerOfTwo(int n) {
    if (n < 1)
        return false;		// n < 0 cannot be powers of 2
    while (n > 2){
        if (n % 2 != 0)		// If n is odd, it can't be a power of 2.
            return false;
        n = n / 2;			// It is a multiple of 2, so divide it by 2.
    }
    return true;			// n came out to be 1 which is a power of 2, so return true.
}
```



### [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

```java
private char[][] board;
public boolean isValidSudoku(char[][] board){
this.board = board;
return rowCheck() && colCheck() && boxCheck();	// Check row first, then column and at
}												// last, boxes because they are time
                                                // consuming.
  
private boolean onePassCheck(){
  HashSet<Integer>[] rows = new HashSet[9];		// 1 HashSet for each row
  HashSet<Integer>[] columns = new HashSet[9];	// 1 HashSet for each column
  HashSet<Integer>[] boxes = new HashSet[9];	// 1 HashSet for each box.

  for (int i = 0; i < 9; i++){
      rows[i] = new HashSet<>();
      columns[i] = new HashSet<>();
      boxes[i] = new HashSet<>();
  }

  for (int i = 0; i < 9; i++){
      for (int j = 0; j < 9; j++){
          int n = (int)(board[i][j]);
          if (n != -2){							// -2 = '.'		
              int boxIndex = (i/3) * 3 + j/3;	// Calculate which box we are in.
              if (!rows[i].add(n) || !columns[j].add(n) || !boxes[boxIndex].add(n))
                  return false;					// If the row set or the column set or the
          }										// box set contains that val, return false.
      }
  }

  return true;
}

private boolean rowCheck(){						// Horizontal check
    boolean[] arr;
    for (char[] row: board){
      arr = new boolean[9];
      for (char c: row){
        int val = c-'0';
        if (val != -2){								// val = -2 means '.' in the board
          if (arr[val-1])							// If val already seen, invalid sudoku
            return false;
          arr[val-1] = true;						// else, Mark that index as seen.
        }
      }
    }
    return true;
  }

  private boolean colCheck(){						// Vertical Check.
    boolean[] arr;
    for (int col = 0; col < board.length; col++){
      arr = new boolean[9];
      for (int row = 0; row < board[0].length; row++){
        int val = board[row][col]-'0';
        if (val != -2){
          if (arr[val-1])
            return false;
          arr[val-1] = true;
        }
      }
    }
    return true;
  }

  private boolean boxCheck(){					// For the 9 sub boxes, let the single
    for (int i = 0; i < 9; i+=3){				// box checker check it's validity.
      for (int j = 0; j < 9; j+=3)				// If any of the subbox was invalid,
        if (!singleBoxCheck(i,j))				// we abort and return false.
          return false;
    }
    return true;
  }

  private boolean singleBoxCheck(int topRightRow, int topRightCol){
    boolean[] arr = new boolean[9];
    for (int i = 0; i < 3; i++){				// Each sub box has 3 rows and 3 columns
      for (int j = 0; j < 3; j++){
        int val = board[topRightRow+i][topRightCol+j]-'0';	// This gives us the value at 
        if (val != -2){							// each cell in the sub box and we fill the
          if (arr[val-1])						// arr with all values that are seen.
            return false;						// If seen twice, return false;
          arr[val-1] = true;
        }
      }
    }
    return true;
  }
}
```



### [Implement Queue Using Stack](https://leetcode.com/problems/implement-queue-using-stacks/submissions/)

```java
/*
Since we reverse stack1 into stack2, stack2 is basically our queue, so if stack2 isn't empty, then the topmost element is what we need when we pop or peek. If it is empty, then again fill it with whatever's there is stack1, and it again becomes the correct queue.
*/
Stack<Integer> stack1;
Stack<Integer> stack2;

public MyQueue() {
    stack1 = new Stack<>();
    stack2 = new Stack<>();
}

public void push(int x) {
    stack1.push(x);			// Push onto stack1
}

public int pop() {
    peek();					// First call the peek function, to make sure stack 2 isn't
    return stack2.pop();	// empty. Then, the topmost element of stack2 is what we want
}

/** Get the front element. */
public int peek() {
    if (stack2.isEmpty()){			
        while (!stack1.isEmpty())
            stack2.push(stack1.pop());
    }
    return stack2.peek();	// stack2 is basically the queue, so return whatever's on the top
}

/** Returns whether the queue is empty. */
public boolean empty() {
    return stack1.isEmpty() && stack2.isEmpty();
}
```



### [Palindrome LinkedList](https://leetcode.com/problems/palindrome-linked-list/submissions/)

```JAVA
public boolean isPalindrome(ListNode head) {
    if (head == null || head.next == null)		// Size 0 or 1 list, must be unique.
        return true;
    if (head.next.next == null)					// Size 2 list, compare the head and tail
        return head.val == head.next.val;		// values

    ListNode middleNode = head;					// Standard Rabbit-Tortoise pointers.
    ListNode fastPointer = head;				// Fast pointer jumps twice so by the time
												// it reaches the end of the list, middlenode
    ListNode curr = head;						// is at the middle of the linkedlist.
    ListNode prev = null;
    ListNode nextNode;							// These three nodes are for reversing the 
												// first half of the list
    while (fastPointer != null && fastPointer.next != null){
        middleNode = middleNode.next;			// Advance middle once, fastpointer twice
        fastPointer = fastPointer.next.next;

        nextNode = curr.next;					// Reverse the curr node, but first store the
        curr.next = prev;						// next newNode. By doing this, we would have
        prev = curr;							// reversed exactly half of the list because
        curr = nextNode;						// fastpointer advacnes at double the speed.
    }

    if (fastPointer != null)					// If faspointer isn't null, then we have an
        middleNode = middleNode.next;			// odd length list, so advance middle once,
												// List looks like 1->2->3->2->1 instead of
    while (middleNode != null){					// 1->2->3->3->2->1
        if (middleNode.val != prev.val)			// While middle isn't null, check middlenode
            return false;						// val and prev val. Prev is basically the
        middleNode = middleNode.next;			// the point where the list reverses.
        prev = prev.next;						// Advance middle and next.
    }
    return true;								// Values matched, so return true.
}												// Reversed list looks like this:
												// 1<-2<-3<-prev middle->3->2->1 in even len
												// 1<-2<-prev middle->2->1 in odd lengths.
```



### [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/)

```java
public void deleteNode(ListNode node) {
    node.val = node.next.val;		// Node's value becomes its next node's value
    node.next = node.next.next;  	// Node's next is it's next's next.
}
```



### [Is Anagram](https://leetcode.com/problems/valid-anagram/submissions/)

```java
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length())			// Can't be anagram if size aren't the same
        return false;
    int[] store = new int[26];				// Acts like a hashmap
    for (int i = 0; i < s.length(); i++)	// Increment the count by 1 in the store for the
        store[s.charAt(i)-'a']++;			// index = position of char in the alphabet
    for (int i = 0; i < t.length(); i++){	// Loop throught the second string, decrement
        if (--store[t.charAt(i)-'a'] < 0)	// count of each character in store by 1, but if
            return false;					// it goes below 0, then it means that character
    }										// occurred more than it did in s. So false.
    return true;							// Everything matched, so return true.
}
```



### [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

```java
List<String> paths = new ArrayList<>();
public List<String> binaryTreePaths(TreeNode root) {
    if (root == null)					// No paths
        return paths;
    String rootval = root.val + "";		// Converting int to string.
    traverse(root, rootval);
    return paths;
}

private void traverse(TreeNode root, String s){
    if (root.left == null && root.right == null)		// It's a leaf, and you found a path
        paths.add(s);									// so add it to the list
    if (root.left != null)								// Left side is traversable, so
        traverse(root.left, s + "->" + root.left.val);	// visit it and record its value.
    if (root.right != null)								// Same as above, but for right side.
        traverse(root.right, s + "->" + root.right.val);
}
```



### [Add Digits](https://leetcode.com/problems/add-digits/)

```java
private int constantTime(int n){
    if (n < 10)
        return n;			// Already a single digit
    int result = n % 9;
    if (result == 0)		// If perfectly divisible by 9, then sum will be 9.
        return 9;
    return result;			// Otherwise, the result is going to be n % 9.
}

private int iterative(int num){
    while (num > 9){				// While number isn't between 2-9
        num = sumOfDigits(num);		// make num = sum of it's digits.
    }
    return num;
}

private int sumOfDigits(int n){		// Standard method to add the digits of a number.
    int sum = 0;
    while (n != 0){
        sum += n % 10;				// Extract the last digit, add it to sum.
        n /= 10;					// Divide the num by 10.
    }
    return sum;
}
```



### [Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/)

```java
public int largestPerimeter(int[] A) {
    Arrays.sort(A);							// Sort so the largest sides are at the end.
    for (int i = A.length-3; i >= 0; --i)	// Triangle inequality Theorem : a + b > c
        if (A[i] + A[i+1] > A[i+2])			// If sum of last two is greater than the last
            return A[i] + A[i+1] + A[i+2];	// we found out max perimeter, otherwise
    return 0;								// decrease i by i, then check the next three
}											// triplets
											// In the end if nothing works out, we return 0.
```



### [Ugly Number](https://leetcode.com/problems/ugly-number/submissions/)

```java
public boolean isUgly(int num) {
    if (num < 1)
        return false;		// Negative numbers are automatically non ugly
    while (num % 2 == 0)	// Keep dividing number by 2 till it is divisible
        num /= 2;
    while (num % 3 == 0)	// Keep dividing by 3
        num /= 3;
    while (num % 5 == 0)	// and 5
        num /= 5;
    return num == 1;		// If num isn't 1, that means that there are other prime factors
}							// except 2,3 and 5.
```



### [Missing Number](https://leetcode.com/problems/missing-number/)

```java
public int missingNumber(int[] nums) {			// Since it's given that the array contains
    int nsum = (nums.length*(nums.length+1))/2;	// all numbers from 0-n, we use the formula
    int arraySum = nums[0];						// to compute sum of n numbers.
    for (int i = 1; i < nums.length; i++)		// Then we loop through the array to compute
        arraySum += nums[i];					// the sum of the array.
    return nsum - arraySum;						// Subtract the array sum from the required
}												// sum, and that gives us the missing number
```



### [Is Bad Version](https://leetcode.com/problems/first-bad-version/submissions/)

```java
public int firstBadVersion(int n) {		// Basic Binary Search Algorithm
    int low = 1, high = n;
    int mid;
    while (low < high){
        mid = low + (high - low)/2;		// high - low to prefent integer overflow.
        if (isBadVersion(mid))			// if the model at mid was bad version, then we
            high = mid;					// could possibly have a bad version before it
        else
            low = mid+1;				// If it wasn't, then our first bad version lies
    }									// beyond the middle element.
    return low;
}
```



### [Move Zeroes](https://leetcode.com/problems/move-zeroes/solution/)

```java
/*
The general idea is that we know the end of the array is going to contain zeroes. So first, iterate over the array, if you find any non-zero value, copy it down to the front of the array. Then we you are done, length of the array minus the last index where you copied the non-zero element is the number of zeroes you need to fill in. So iterate from that last non-zero index to the end of the array and fill in zeroes.
*/
public void moveZeroes(int[] nums) {
    int lastNonZeroIndex = 0;
    for (int i = 0; i < nums.length; i++)
        if (nums[i] != 0)
            nums[lastNonZeroIndex++] = nums[i];
    for (int i = lastNonZeroIndex; i < nums.length; i++)
        nums[i] = 0;
}

/*
This solution is an extension of the above, but a better one because we only swap elements when needed and do not do any unnecessary writes. Start from the beginning of the array, maintain the last position of non-zero value you saw, and the current element. If you see a non-zero value, swap the current value with the index just after the last non-zero index you have, and then increment the non-zero index by 1 because you just found a new non-zero value. This helps us prepare for the next non-zero value we find and copy it at this index+1. By doing so, we are basically partitioning the array into non-zeroes and zero values.
*/
public void moveZeroes(int[] nums) {
    for (int lastNonZeroIndex = 0, i = 0; i < nums.length; i++){
        if (nums[i] != 0)
            swap(nums, i , lastNonZeroIndex++);
    }
}

private void swap(int[] a, int i, int j){
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}
```



### [Word Pattern](https://leetcode.com/problems/word-pattern/)

```java
public boolean wordPattern(String pattern, String str) {
    String[] words = str.split(" ");		// Split str into words
    if (pattern.length() != words.length)	// If length of pattern and words mismatch
        return false;						// then pattern do not match
    HashMap<Character, String> patternStore = new HashMap<>();	// Map pattern char to word
    HashMap<String, Character> wordMap = new HashMap<>();		// Map word to pattern char
    for (int i = 0; i < words.length; i++){
        char c = pattern.charAt(i);					// Get the char
        patternStore.putIfAbsent(c, words[i]);		// Put it in patternStore if absent
        if (!patternStore.get(c).equals(words[i]))	// If it was already there and it doesn't
            return false;							// map to words[i], we have a violation
        wordMap.putIfAbsent(words[i], c);			// Now check the other way around. If
        if (wordMap.get(words[i]) != c)				// words is absent in the map, map it to
            return false;							// the char. If present, then fetch it's
    }												// mapping and check if both match to c.
    return true;							// No violation, so return true
}
```



### [Can Win Nim](https://leetcode.com/problems/nim-game/)

```java
public boolean canWinNim(int n) {
    return n % 4 != 0;			// You can always win the game if n is not divisible by 4.
}
```



### [Power Of Three](https://leetcode.com/problems/power-of-three/)

```java
public boolean isPowerOfThree(int n) {
    if (n < 1)				// If negative, it can't be a power of 3.
        return false;
    while (n % 3 == 0)		// While n is divisible by 3, keep dividing it.
        n /= 3;
    return n == 1;			// In the end, if it was a power of 3, then n should be 1.
}
```



### [Power of Four](https://leetcode.com/problems/power-of-four/submissions/)

```java
/*
You can also use the iterative method that I have used in Power of Two and Power of Three problems. I just wanted to try a different approach here. This is a constant time function.
*/
public boolean isPowerOfFour(int num) {
    double pow = Math.log(num)/Math.log(4);	// Calculate x in 4^x = num using logs.
    return pow == (int)pow;					// Making sure that x is an integer and not a
}											// fractional exponent.
```



### [Reverse String](https://leetcode.com/problems/reverse-string/)

```java
/*
1 Liner solution. Basically, create a StringBuilder of the string, the builder already has a reverse method, so reverse it and then return it's toString.
*/

public String reverseString(String s) {
    return new StringBuilder(s).reverse().toString();
}

/*
Golfing aside, here is how one is expected to solve it in an interview.
*/

public String reverseString(String s) {
	char[] array = s.toCharArray();		// Create a char array of the string
	int len = array.length;				// length of the array
	for (int i = 0; i < len/2; i++){	// We only need to iterate over half the array.
		char temp = array[i];			// Swap the 0th index element with (len-1)th,
		array[i] = array[len-i-1];		// 1st index element with (len-2)th, until you get
		array[len-i-1] = temp;			// to the middle element.
	}
	return new String(array);			// Return a new string with the reversed array.
}
```



### [Implement strStr()](https://leetcode.com/problems/implement-strstr/submissions/)

```java
/*
The basic idea here is that you only need to iterate haystack length - needle length, and then check the substring of size = needle length in haystack from each index. If you are successfully able to match each character of the needle in the corresponding substring in haystack, return the index you start from. 
*/
public int strStr(String haystack, String needle) {
    if (needle.length() > haystack.length())	// Needle length can't be > than haystack
        return -1;
    int hl = haystack.length();
    int nl = needle.length();
    if (nl == 0)								// Empty strings are always a match starting
        return 0;								// from 0.
    for (int i = 0; i <= hl-nl; i++){			// Iterate haystack length - needle length.
        for (int j = 0; j < nl && haystack.charAt(i+j) == needle.charAt(j); ++j)}
            if (j == nl-1)						// We are checking how far from i can we
                return i;						// match. If i matched with j, increment j
        }										// and then match the character i+1 to j.
    }											// If that matches, increment j and match i+2
    return -1;									// j == n-1 checked wether or not if we were
}												// able to match the full needle string, if
												// yes, then i is our index
												// in the end, nothing matched, so return -1
```



### [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

```java
public String reverseVowels(String s) {
    if (s.length() < 2)
        return s;					// No need to reverse a string of length 0 or 1
    char[] str = s.toCharArray();	// Get the char array

    int left = 0;
    int right = str.length-1;

    while (left < right){
        while (left < right && !isVowel(str[left]))		// While left is pointing to a
            left++;										// consonant, increment it/
        while (left < right && !isVowel(str[right]))	// While right is pointing to a
            right--;									// consonant, decrement it.

        char temp = str[left];							// Left and right are now pointing
        str[left] = str[right];							// to vowels, so swap it.
        str[right] = temp;								// And then increment left and
        left++;											// decrement right to process the
        right--;										// inner string
    }
    return new String(str);			// Return a string from the reveresed array.
}

private boolean isVowel(char c){	// Function to check if a character is a vowel.
    switch (c) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
            return true;
        default:
            return false;
    }
}
```



### [Intersection of two arrays](https://leetcode.com/problems/intersection-of-two-arrays/)

```java
public int[] intersection(int[] nums1, int[] nums2) {
    Set<Integer> set1 = new HashSet<Integer>();		// Record all unique values in set 1
    for (int i: nums1)
        set1.add(i);
    Set<Integer> intersect = new HashSet<>();		// We will use it to record intersection
    for (int i: nums2)								// For each value in nums2 array
        if (set1.contains(i))						// If set1 contains it, we found an
            intersect.add(i);						// intersecting element, so add it.
    int[] res = new int[intersect.size()];			// We will now convert the set to an
    int i = 0;										// array and then return the array.
    for (int n: intersect)
        res[i++] = n;
    return res;
}
```



### [Is Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

```java
/**
The basic idea here is to close in on the square root using binary search algorithm. 
I handle 4 seperately because it's root is the only one where 4/3 < it's square root. 
All other numbers square root is greater than its value/3.
So we create a lowerBound of 1 and an upperBound of num/3. Then if the middle value's square
overshoots, we make upperBound = mid-1, otherwise increment lowerBound to mid+1. This way, we
close on the square root from both sides, and if the middle values is the square root, it's
square will yield num.
*/
public boolean isPerfectSquare(int num) {
    if (num < 2 || num == 4)
        return true;
    long lowerBound = 1;
    long upperBound = num/3;
    long mid;
    long square;
    while (lowerBound <= upperBound){
        mid = lowerBound + (upperBound-lowerBound)/2;
        square = mid*mid;
        if (square == num)
            return true;
        if (square > num)
            upperBound = mid-1;
        else
            lowerBound = mid+1;
    }
    return false;
}
```



### [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)

I cannot explain it better than this [post](https://leetcode.com/problems/sum-of-two-integers/discuss/132479/Simple-explanation-on-how-to-arrive-at-the-solution).

```java
public int getSum(int a, int b) {
    if (a == 0)
        return b;
    if (b == 0)
        return a;
    int sum = a ^ b;
    int carry = a & b;
    if (carry == 0)
        return sum;
    return getSum(sum, carry << 1);
}
```



### [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

```java
public int guessNumber(int n) {				// Standard binary search algorithm
    int low = 1, high = n, result = -2;		// Arbitrary result, but not 0
    int mid = 0;
    while (result != 0){
        mid = low + (high-low)/2;			// Check the mid.
        result = guess(mid);				// Check if our guess is correct
        if (result == -1)					// If result == -1, then we overshot
            high = mid-1;					// So we can discard all values > mid
        else if (result == 1)				// If result == 1, we undershot
            low = mid+1;					// Need to discard all the values < mid
    }
    return mid;								// Result == 0, so return the mid.
}
```



### [Ransom Note](https://leetcode.com/problems/ransom-note/submissions/)

```java
public boolean canConstruct(String ransomNote, String magazine) {
    int[] store = new int[26];
    for (char c: magazine.toCharArray())		// First, fill the store with available
        store[c-'a']++;							// characters from the magazine
    for (char c: ransomNote.toCharArray())		// Then, scan through the note, decrement
        if (--store[c-'a'] < 0)					// each char's index by 1 because we used
            return false;						// it. If it's frequency drops below 0,
    return true;								// then it means that we need more chars
}												// than available. In the end, return
												// true if everything worked out.
```



### [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/submissions/)

```java
public int firstUniqChar(String s) {
    int[] freq = new int[26];			// Preprocess freq array to maintain freq of each
    char[] chars = s.toCharArray();		// character in the string s
    for (char c: chars)
        ++freq[c-'a'];
    for (int i = 0; i < chars.length; i++)	// Make a second pass through the chars of the
        if (freq[chars[i]-'a'] == 1)		// string in order, and if any of the char's
            return i;						// frequency is 1, that's our unique char
    return -1;								// Otherwise, no unique character
}
```



### [Find the Difference](https://leetcode.com/problems/find-the-difference/)

```java
/**
The general idea here is same as the problem where we are required to find a unique int
in an array containing duplicates except one. We use the xor operator between each character
of the string s and t, and the ones that are duplicate will xor to give 0. XOR of any element
with 0 is the element itself, and XOR of two same elements gives 0. This way, since string s
and t basically has pairs of repeating characters except one, the unique element will XOR
with 0 and give us it's ASCII code. The only thing we need to take care of is to now shift it
up by 26, so we add 'a' and convert it to char.
*/
public char findTheDifference(String s, String t) {
    int xor = 0;
    for (char c: s.toCharArray())
        xor ^= c-'a';
    for (char c: t.toCharArray())
        xor ^= c-'a';
    return (char)(xor+'a');
}
```



### [Nth Digit](https://leetcode.com/problems/nth-digit/)

```java
/**
Notice that # of digits between 0-9 is 1*9, 10-99 is 2*90, 100-999 is 3*900. If we generalize
it, it is exactly equal to 9 * (num of digits in the number) * 10^{# of digits - 1}.
*/
public int findNthDigit(int n) {
    if (n < 10)
        return n;
    int pow = 1;				// First we need to figure out how many digits there are
    long upperBound = 9;		// in the number.
    while (n > upperBound){
        n -= upperBound;		// If n is a two digit number, subtract the 9 single digit
        ++pow;					// numbers, if 3 digit, subtract the first 189 digits.
        upperBound = (long)Math.pow(10, pow-1) * pow * 9;
    }							// pow allows us to track how many digits there are in num.

    int num = (int)Math.pow(10,pow-1) + (n-1)/pow;		// Calculate which number we want
    int position = pow - 1 - (n-1) % pow;				// Calculate which index we want
    for (int i = 0; i < position; i++)					// Divide num that many times
        num /= 10;
    return num % 10;									// num % 10 gives us that digit.
}
```



### [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/)

```java
public int sumOfLeftLeaves(TreeNode root) {
    if (root == null)		// Empty tree, therefore total is 0.
        return 0;
    int sum = 0;			// Initialize sum.
    // Look ahead and check. If left is not null but left is a leaf, then sum is the value of the left leaf.
    // But if left is null or left is an inner node, then we need to explore it, so sum is whatever the subtree from the left node returns.
    if (root.left != null && root.left.left == null && root.left.right == null)
        sum = root.left.val;
    else
        sum = sumOfLeftLeaves(root.left);
    // We computed the sum of the left side. Now we need to traverse the right side and fetch
    // the sum, so total sum is sum of the left side as computed above + sum returned by
    // traversing the right side.
    return sum + sumOfLeftLeaves(root.right);
}
```



### [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

```java
public int longestPalindrome(String s) {
    int[] freq = new int[128];		// To record the frequency of each char
    for (char c: s.toCharArray())
        freq[c]++;					// Increment count by 1 for each character observed
    int len = 0;					// length of the longest palindrome
    boolean isOdd = false;			// Check if our palindrome length is odd
    for (int i = 0; i < 128; i++){	// Go through each character's index
        if (freq[i] != 0){			// Only if it has been observed atleast once
            int val = freq[i];		// Store it's frequency
            int used;				// Record how many of it's occurrences we will use
            if (val % 2 == 0)		// If a perfect multiple of 2, we will use all
                used = val;
            else{
                used = val-1;		// If odd occurrences, then the max we can use to form a
                isOdd = true;		// valid palindrome is val-1. It also tells us that the
            }						// palindrome is going to be of odd length.
            len += used;			// Finally, increment length by the number of chars used
        }
    }
    if (isOdd)						// If length is odd, we can always insert any single
        return len+1;				// character in the middle to keep the palindrome valid.
    return len;						// If the length is even, then we can't do anything.
}
```



### [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)

```java
public List<String> fizzBuzz(int n) {
    List<String> nums = new ArrayList<String>();
    for (int i = 1; i <= n; ++i){				// Loop from 1 to n
        if (i % 15 == 0)						// If i divisible by 15, add "FizzBuzz"
            nums.add("FizzBuzz");
        else if (i % 5 == 0)					// i's not a multiple of 15, check if it's a
            nums.add("Buzz");					// multiple of 5. If so, add "Buzz"
        else if (i % 3 == 0)					// i's not a multiple of 5, check if it's a
            nums.add("Fizz");					// multiple of 3, if so, add "Fizz"
        else
            nums.add(i+"");						// Otherwise, just add the String type of the
    }											// number
    return nums;
}
```



### [Third maximum Number](https://leetcode.com/problems/third-maximum-number/)

```java
public int thirdMax(int[] nums) {
    if (nums.length == 0)		// Empty array
        return 0;
    if (nums.length == 1)		// Size 1 array
        return nums[0];
    if (nums.length == 2)		// Size 2 array, check between 0th element or 1st element
        return nums[0] > nums[1] ? nums[0] : nums[1];
    long firstMax = Long.MIN_VALUE;		// Lowest values for all three
    long secondMax = Long.MIN_VALUE;
    long thirdMax = Long.MIN_VALUE;
    for (int i: nums){					// For each number in the array
        if (i > firstMax){				// If num > than the largest, then old largest
            thirdMax = secondMax;		// becomes second largest and second largest becomes
            secondMax = firstMax;		// first largest, then update the largest.
            firstMax = i;
        }
        else if (i > secondMax && i != firstMax){	// If num > second and num is not is the
            thirdMax = secondMax;					// same as first, first largets becomes
            secondMax = i;							// second largest and update the second
        }
        else if (i > thirdMax && i != secondMax && i != firstMax) // // If num > third, we
            	thirdMax = i;						// need to check that it is not the same
    }												// as the first and second largest.
    if (thirdMax == Long.MIN_VALUE)					// This check allows us to make sure that
        return (int)firstMax;						// we do indeed have a third max and is
    return (int)thirdMax;							// not what we initialized initially.
}
```



### [Add Two Strings](https://leetcode.com/problems/add-strings/)

```java
public String addStrings(String num1, String num2) {
    if (num1.equals("0"))
        return num2;
    if (num2.equals("0"))
        return num1;
    
    /** We use a char array to maintain the digit at each index. We want the array to be of
    the size of the largest string + 1 to handle carry bit if any at the end. We start
    adding each digit of the string from the end, and place it in it's correct index at the
    end of the sum array. This way, we avoid reversing it and return the answer in constant
    time. Take care to convert the digit you compute by adding '0'. Lastly, if the carry bit
    is 1, we need to make the 0th index as 1, and return the string by using the sum array.
    If it's not 1, then the sum array has a leading 0 which we don't want. So we use Java's
    String constructor that takes in the char array, startingIndex in that array and the
    number of elements of that array we want. So if the carry isn't 1, we technically want
    everything from index 1 and # of elements = sum.length - 1 because we discard 0 index.
    */
    char[] sum = new char[1 + Math.max(num1.length(), num2.length())];
    int index = sum.length-1, idx1 = num1.length()-1, idx2 = num2.length()-1, carry = 0, total = 0;
    int n1, n2;
    while (idx1 >= 0 || idx2 >= 0){
        n1 = idx1 < 0 ? 0 : num1.charAt(idx1--)-'0';
        n2 = idx2 < 0 ? 0 : num2.charAt(idx2--)-'0';
        total = n1 + n2 + carry;
        carry = total/10;
        sum[index--] = (char)(total % 10 + '0');
    }
    if (carry == 1){
        sum[0] = '1';
        return new String(sum);
    }
    return new String(sum, 1, sum.length-1);
}
```



### [Construct Quad Tree](https://leetcode.com/problems/construct-quad-tree/)

```java
private int[][] grid;					// Store it once, instead of passing it over & over.
public Node construct(int[][] _grid) {
    grid = _grid;
    return helper(0,0,grid.length);		// Ask helper to build the tree.
}

private Node helper(int top, int left, int len){
    if (len <= 0)						// Base case: if empty grid or if we are done
        return null;					// checking the full grid, return null
    int key = grid[top][left];			// Get the topleft value, and start checking the box
    for (int i = 0; i < len; ++i){		// of len*len. If at any point, the value doesn't
        for (int j = 0; j < len; ++j){	// match the key, we have found a breakpoint from
            if (grid[top+i][left+j] != key){	// where we need to break the grid into four
                int offset = len/2;		// grids, each of len = len/2. The topleft grid has
                return new Node(true, false, 	// the same top and left point, the topright
                                helper(top,left, offset),	// grid has left point shifted to
                                helper(top, left + offset, offset),	// the right by offset.
                                helper(top+offset, left, offset),	// The bottom left grid
                                helper(top+offset, left+offset, offset));	// is shifted
            }	// downwards by offset with the same left point. The bottom right grid will
        }		// have an index where it's top is shifted down by len/2 and left by left/2.
    }			// We know that the node will have a value = true if 1 else false and it won't be a leaf, so true, false, topleft, topright, bottomleft, bottomright.
    return new Node(key == 1, true, null, null, null, null);	// Everything passed, so we return a new Node whose value is true if key is 1, else false and it will be a leaf, with
// no children, so 4 nulls.
}
```



### [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

```java
public List<List<Integer>> levelOrder(Node root) {
    List<List<Integer>> res = new ArrayList<>();	// Result list
    if (root == null)								// If root is null, return empty list.
        return res;
    Queue<Node> q = new LinkedList<>();				// BFS Queue. Add the root.
    q.add(root);
    while (!q.isEmpty()){							// While q isn't empty
        int size = q.size();						// Check how many elements in that level
        List<Integer> level = new ArrayList<>(size);// level list to store elements.

        for (int i = 0; i < size; i++){				// Remove each node for whatever the size
            Node n = q.poll();						// Add that node's value and add all of
            level.add(n.val);						// its children to the queue.
            for (Node child: n.children)
                q.add(child);
        }
        res.add(level);								// Add the level array to the result
    }
    return res;										// Return the result list.
}
```



### [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/)

```java
public int countSegments(String s) {
    if (s.length() == 0)					// Empty String
        return 0;

    int segments = 0;						// Record segments

    char prev = s.charAt(0);				// We will compare adjacent characters.
    for (int i = 1; i < s.length(); ++i){	// Start looking at chars from index 0
        char curr = s.charAt(i);			// Get the current char
        if (prev != ' ' && curr == ' ')		// If previous char wasn't a space but the
            ++segments;						// current char is, we found a segment.
        prev = curr;						// Make previous = current for next iteration
    }
/**
This line is important. If prev was an empty space, that means that all we have been looking
at was empty spaces towards the end. So return whatever segments we found in the beginning
of the string. But if prev wasn't a space, that means the char next to prev might have been
an empty space or just a normal character. In any case, we would want to include that last
segment, so we return segment+1.
*/
    return prev == ' ' ? segments : segments+1;
}
```



### [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

```java
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null)						// Empty Tree
        return result;
    Queue<TreeNode> q = new LinkedList<>();	// BFS Queue
    q.add(root);
    while (!q.isEmpty()){					// While we have something to process
        List<Integer> level = new ArrayList<>();
        int size = q.size();				// Check how many elements at the current level
        for (int i = 0; i < size; i++){
            TreeNode node = q.poll();		// Remove one element each time
            if (node != null){				// If not null, add it's val to the level list,
                level.add(node.val);		// and it's left and right children to the queue
                q.add(node.left);			// to process in order
                q.add(node.right);
            }
        }
        if (!level.isEmpty())				// If level list wasn't empty,
            result.add(level);				// add it to the result list.
    }
    return result;
}
```



### [Path Sum III](https://leetcode.com/problems/path-sum-iii/submissions/)

```java
HashMap<Integer, Integer> sumToWays;			// Record how many ways there are to form sum
int ways;										// Total number of ways.
public int pathSum(TreeNode root, int sum) {
    sumToWays = new HashMap<>();
    ways = 0;
    sumToWays.put(0,1);							// 1 way to form a sum of 0.
    helper(root, 0, sum);
    return ways;
}

/**
The idea here is as follows. Start with the root node, and keep a running total. We maintain
how many ways there to form a running sum. Then we check how many ways there are to form
(running sum) - (sum we are looking for). If there is a way to form it, then we increase the
number of ways to form sum. We then have to update the map to record how many ways can the
running sum be formed. If it's something we could form before, increment it, or else set it
to 1. Now, traverse the left side and then the right side. In the end, for each time we
incremented the count for a running sum, we need to decrement it because we are backtracking.
We are first going down, incrementing the count for runningSum, then we move up and decrement
it by 1 for each time we observed it. This is to maintain the Pre-Order traversal.
*/
private void helper(TreeNode node, int runningSum, int sum){
    if (node == null)
        return;
    runningSum += node.val;
    ways += sumToWays.getOrDefault(runningSum-sum, 0);
    sumToWays.put(runningSum, sumToWays.getOrDefault(runningSum, 0)+1);

    helper(node.left, runningSum, sum);
    helper(node.right, runningSum, sum);

    sumToWays.put(runningSum, sumToWays.get(runningSum)-1);
}
```



### [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

```java
public List<Integer> findAnagrams(String s, String p) {
    List<Integer> result = new ArrayList<>();
    int start = 0, end = 0, slen = s.length(), plen = p.length();
    if (slen == 0 || slen < plen || plen == 0)
        return result;
    int[] freq = new int[26];				// Store the freq of chars in p
    for (char c: p.toCharArray())
        freq[c-'a']++;
    char[] sArr = s.toCharArray();			// Get the chars of the string s as an array
    while (end < slen){						// While everything is not processed
        if (--freq[sArr[end]-'a'] >= 0)		// decrease the freq of the char at index end
            plen--;							// if it's > 0, then we matched something in p
											// so decrease plen by 1.
        while (plen == 0){					// If plen goes to 0, we were able to match all
            if (end-start+1 == p.length())	// chars of p. If length of the matched chars is
                result.add(start);			// equal to length p, we found a start point.
            if (freq[sArr[start]-'a'] >= 0)	// Check if the freq of char at start index is
                plen++;						// >= 0. If it is, shift the window to the right
            ++freq[sArr[start++]-'a'];		// but first restore the frequency of the char
        }									// at the index start.

        end++;								// Get ready to inspect the new element
    }

    return result;							// Return the answer.
}
```



### [Arranging Coins](https://leetcode.com/problems/arranging-coins/)

The idea is as follows. Sum of first n numbers is given by $\frac{n^2+n}{2}​$. We need to find $n​$ such that sum of $n​$ numbers is closest to the number of coins we have. That is, $\frac{n^2+n}{2} = k​$ where $k​$ is the number of coins we have. So, everything boils down to solving the quadratic equation $n^2 + n - 2k = 0​$. We use the quadratic formula where for any quadratic equation $ax^2 -bx + c​$ is solved substituting for $a​$, $b​$ and $c​$ in $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2}​$. Here, $a​$ and $b​$ are always going to be 1, while $c​$ is always going to be $2k​$. Substitute those, and solve the equation.

```java
public int arrangeCoins(int n) {
    // return solveQuadratic(n);
    return iterative(n);
}

private int solveQuadratic(int n){
    return (int)(Math.sqrt(1 + 8*(long)n)-1)/2;
}

private int iterative(int n){
    int used = 1, level = 0;		// Coins used, and level completed.
    while (n > 0){					// While coins left are greater than 0.
        n-=used;					// Calculcate remaining coins.
        if (n > -1)					// If there are still some coins left,
            ++level;				// we were able to fill the level.
        ++used;						// Prepare used for the next level, which is plus 1.
    }
    return level;					// Return level
}
```



### [Hamming Distance](https://leetcode.com/problems/hamming-distance/)

```java
public int hammingDistance(int x, int y) {
    int diff = 0;				// Track differences
    while (x != 0 || y != 0) {	// While both of them aren't 0
        if (x % 2 != y % 2)		// Check the bit of x and y by mod 2. If they are unequal
            diff++;				// increment difference.
        x /= 2;					// Divide x and y by 2.
        y /= 2;
    }
    return diff;
}
```



### [String Compression](https://leetcode.com/problems/string-compression/)

```java
public int compress(char[] chars) {
    int len = chars.length;			// No need to reverse array of length 0 or 1
    if (len < 2)
        return len;
    int arrayIndex = 0;				// To maintain the length of new array.
    int start = 0;					// start index
    int end = 0;					// end index
    while (end < len){
        char first = chars[start];	// Record the char we are looking at.
        int count = 0;				// count is 0.
        while (end < len && chars[end] == first){	// while the char is the same
            ++end;					// increment end to check next char
            ++count;				// and increment the count.
        }
        start = end;				// shift start to end to check next sequence of chars
        chars[arrayIndex++] = first;	// our arrayIndex points to to the new array's 
        if (count != 1){				// indices. So copy the first char to arrayIndex.
            if (count > 1 && count < 10)	//Only if count isn't 1, if count is less than 10
                chars[arrayIndex++] = (char)(count+'0');	// then we simply convert count to char and write it next to the char we just overwrote.
            else						// Otherwise, it has many digits. So convert it to
                for (char c: String.valueOf(count).toCharArray()){	// string and add all it's digit to the array one by one while increment arrayIndex.
                    chars[arrayIndex++] = c;
            }
        }
    }
    return arrayIndex;			// Wherever arrayIndex is, is the new length for the array.
}
```



### [Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/)

```java
public int numberOfBoomerangs(int[][] points) {
    int boomerangs = 0;
    HashMap<Double, Integer> map = new HashMap<>();	// To record points with same dist
    for (int[] i: points){		// Compute distance between one point and every other.
        map.clear()				// clear map before each relative distance computation
        for (int[] j: points){	// Compute distance with other points
            if (i == j)			// Don't compare the same two points.
                continue;
            double dist = Math.sqrt(Math.pow(i[0]-j[0],2) + Math.pow(i[1]-j[1],2));
            int prevCount = map.getOrDefault(dist, 0);	// Check how many points are equidistant from point i.
            boomerangs += prevCount * 2;	//  Number of boomerangs = whatever pairs there were before times 2, because you can form twice the number of different orders.
            map.put(dist, prevCount+1);	// Increase the count of points observed for that distance.
        }
    }
    return boomerangs;	// return number of boomerangs
}
```

