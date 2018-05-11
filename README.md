# Mini Projects

#### Tyler Blevins
#### 2-14-2018

## Mathematical Expression Parser.

I went through a few ideas of how to solve this one. I ended up settling on an approach that builds a binary tree and then evaluates it recursively.  My solution assumes that there will be spaces between each parenthesis, operand, and operator.  If I had more time, I would add functionality that allows for no spacing in the expression and checks for matching parentheses.  Thinking about it further, I would like to add more operators as well. Please refer to '/problem_1.py'.  I really enjoyed solving this one!

## Common Strings between two files
* 1 million strings *
I chose a hash table approach for efficiency.  My program reads the first file line by line and assigns a key-value pair to a dicitonary.  The keys are the strings from the file and their values are set to 0. The second file is read line by line with each line attempting to access the dictionary using its string as a key.  If the string is a key, the value is set to 1 (indicating a match). If the string is not a key, then the call fails and the program continues.  After reading the file, the counts from the values are summed. Please refer to '/problem_2.py'.

I assume that we still consider it a single match if a file has duplicate lines that match a line in the second file.

* 1 billion strings *
If the file contained one billion strings instead, I would consider changing my approach. At one million 32 character strings, we are looking at around 32M of working memory. At one billion strings, we are looking at 32G of working memory.  That is too much to hold in memory and maybe we should consider tradeoffs with performance.

## Flagging overlapping event times
My solution for this one involves creating a list of the events, sorting the list using the 'start_time' as a key.  Then we can loop through the list comparing the 'end_time' of the current event to the 'start_time' of the next event.  If the 'start_time' of the next event falls before the 'end_time' of the current event, then we mark both events as having overlap. Please refer to 'problem_3.py' attached.

I assume that if an event starts at the exact time the previous event ends then there is no overlap.

* Streaming solution *
For an arbitrarily large stream of events, I would like to leverage a database. Events would be saved to a db as they stream in. Once events have subsided, we could query the db for overlap and adjust all overlap flags at once before returning events. 