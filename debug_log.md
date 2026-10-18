# debug_log.md
# Author: [Your Name]

## Bug 1
Error type: KeyError
File + line: week8_buggy.py + line 12
What the error means: This error means that we tried to access a key in a nonexistent dictionary
What I told the duck: We are trying to add the amounts in each record to get the total. We first set the total as 0, then for each record in our defined dictionary, we are adding the amounts. One of the amounts is misspelt.
What I tried: I used a debug command to check the actual output.
How I fixed it: There was a typo in the first record's key name which I fixed.

## Bug 2
Error type: TypeError
File + line: week8_buggy.py + line 16
What the error means: The error means that the two types of data we are using cannot be compared to eachother. One of the data types is incorrect.
How I fixed it: I changed the type of data of '1000' from string to int by removing the quotes.

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records
True
Did pytest pass? Yes

## AI Literacy Reflection
Did I use AI? No
If yes -- exact prompt I used: ___
What AI explained: ___
What I changed myself: I did not use AI for this assignment. I was able to understand the error and fix it myself without having to use AI to debug the code. 
Can I explain every fixed line? Yes

## What I learned
I learned the different types of errors, specifically how a keyerror and typeerror look like. I also learnt how to debug the code and understand what the debug output means. 