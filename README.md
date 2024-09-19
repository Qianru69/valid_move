# Valid Move
Algorithm to check one valid move in chess

### Description 

Given a board in some representation (example here as a 2d array of strings but you are free to change this - the uppercase characters are WHITE), implement the function isValidMove()    

let cb = [    
    ['R', 'H', 'B', 'K', 'Q', 'B', 'H', 'R'],    
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],    
    ['.', '.', '.', '.', '.', '.', '.', '.'],    
    ['.', '.', '.', '.', '.', '.', '.', '.'],    
    ['.', '.', '.', '.', '.', '.', '.', '.'],    
    ['.', '.', '.', '.', '.', '.', '.', '.'],    
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],    
    ['r', 'h', 'b', 'k', 'q', 'b', 'h', 'r']    
  ]    

The function should take at least 3 parameters: 
* the board
* the starting position
* the ending position
and should answer the question “if i move the piece in the starting position to the ending position, would that be valid?”

Examples:     
js :     
    let start = [0,1]    
    let end = [2 2]    
    let canIDoThis = isValidMove(chessboard, start, end)    
java :     
    boolean isgood = isValidMove(char[][] cb, Position start, Position end);    

NOTES :     
The chess board is 8x8    
Pieces and movement:     
pawn (soldier) = move 1 forward, only captures forward diagonally. (On its first move it can move 2)    
knight (horse) = 1 + 2. 1 horiz + 2 vert, or vice versa. Can jump over pieces.    
Rook (elephant) = N spaces horiz and vertically    
Bishop (camel) = N spaces diagonally    
Queen = N spaces in any direction    
King = 1 space in any direction    
