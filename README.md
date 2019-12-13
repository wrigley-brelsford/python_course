# James' project - Identifying terraces in .ibw file AFM images

James Wrigley

## Overview of the Project

The resulting file, named ReadingIBWfiles.py, when supplied with the correct modules (not sure that I have on github), will read in .ibw files and flatten the surfaces. Subsequently, edges are identified by local gradients, and terraces are identified as enclosed regions of edges.

The final step in the program is a loop requiring user input to remove terraces from the final summary of the program. This is repeated by inputting an x,y pair for a single point in each terrace to be removed. 

After all required terraces are removed a user can type any non-numerical character to end the loop. The program then returns the proportion of area remaining in the image. This would be used to identify the coverage of a surface when two materials are present.

