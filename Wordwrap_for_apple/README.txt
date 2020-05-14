=====================================>REQUIREMENT<=====================================
Write a program in Python, that can accept a paragraph string and and page width and return an array of left AND right justified strings.
NOTE: No words should be broken, the beginning and end of the line should be characters).

You should provide instructions on how to execute your program and provide a sample output. 

Example:
 
Sample input:
 
Paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
Page Width = 20
 
 
Output should look like this:
 
Array [1] = "This  is  a   sample"
Array [2] = "text      but      a"
Array [3] = "complicated  problem"
Array [4] = "to be solved, so  we"
Array [5] = "are adding more text"
Array [6] = "to   see   that   it"
Array [7] = "actually      works.”

========================================================================================

==================================>BELOW IS THE ANSWER FOR THE REQUIREMENT<========================

There are two files/programs.
1. appleProjectSample1
2. appleProjectSample2 

appleProjectSample2 : is the which, who provide exact required output as asked as given below:

Paragraph =  This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.
Page_Width =  20
Below is the Output
_____________ ____________________ 

Array [1] = "This   is  a  sample"
Array [2] = "text      but      a"
Array [3] = "complicated  problem"
Array [4] = "to  be solved, so we"
Array [5] = "are adding more text"
Array [6] = "to   see   that   it"
Array [7] = "actually      works."

Process finished with exit code 0




appleProjectSample1: is very easy to write n understand. But it will not extend the line along the width else it also suit the requirement.

Paragraph =  This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.
Page_Width =  20
Below is the Output
_____________ ____________________ 

Array [1] = "This is a sample    "
Array [2] = "text but a          "
Array [3] = "complicated problem "
Array [4] = "to be solved, so we "
Array [5] = "are adding more text"
Array [6] = "to see that it      "
Array [7] = "actually works.     "

Process finished with exit code 0