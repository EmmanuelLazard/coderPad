# coderPad
Some solutions to coderpad problem

https://app.coderpad.io/sandbox?question_id=230552

https://twitter.com/CoderPad/status/1578398272129060867

The original solution seems to work as it's a simple loop BUT the remove() method is also a loop ecause it has to loop through the list to find the 0. Two nested loops is too much...

So an easy way is not to remove the zeros but to build a new list without the zeros and add them at the end. That's easily done with a simple loop that copies the value if it's non zero and increments a counter otherwise. See solution 1. 

But the creation of a new list will always add some RAM usage and I wasn't able to get below 325MB. So we have to find a way of moving the elements directly in the original list.

To do so, we use two indexes: the first one loops through all elements of the list, the second one is ahead of the first one and each time we encouter a zero, that index advances to find the next non zero digit that will be exchange with the zero. See solution 2.
