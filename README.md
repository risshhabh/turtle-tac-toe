# turtle-tac-toe
A GUI version of the popular game Tic-Tac-Toe (Also known as Noughts and Crosses).

Pretty simple to play, just run the program and the only controls are the 1-9 keys and the `q` key.

`1-9` to place a piece, it alternates from X and O and is a 2-player-game.

`q` quits out of the turtle program and ends the program. It returns an error in the terminal- not sure why- but it still works perfectly fine.

Once you win, the title will change from `Tic-Tac-Toe` to `X is the winner!` or `O is the winner!`. I am yet to implement something for ties.

***

### TODO:
- Make the code a bit neater, especially that disgusting bit around line ~150.
- Get rid of the error after clicking the `q` key which activates `turtle.bye()`.
- Improve the main loop.
- Implement tie system.
- Exit out of program upon 5 seconds after win.
- New `turtle` window that showcases keybinds/instructions.
- More user-friendly UI.
