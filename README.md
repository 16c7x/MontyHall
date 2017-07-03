# MontyHall
Trying to develop a model for the Monty Hall probelm

https://en.wikipedia.org/wiki/Monty_Hall_problem

To validate the results here is a state table showing the possible sequences of goats and car. It's showing that Sticking should give a 33.3% win rate vs 66.6% win rate.  

|                     |         |         |         | Stick       | Switch      | 
| -------             | ------- | ------- | ------- | -------     | -------     | 
| Sequence            | Car     | Goat    | Goat    |             |             | 
| Stick               | guess   | reveal  |         | 1           |             | 
| Switch              | guess   | reveal  | Switch  |             | 0           | 
|                     |         |         |         |             |             | 
| Sequence            | goat    | car     | goat    |             |             | 
| Stick               | guess   |         | Reveal  | 0           |             | 
| Switch              | guess   | Switch  | Reveal  |             | 1           | 
|                     |         |         |         |             |             | 
| Sequence            | goat    | goat    | car     |             |             | 
| Stick               | guess   | reveal  |         | 0           |             | 
| Switch              | guess   | reveal  | Switch  |             | 1           | 
|                     |         |         |         |             |             | 
| Sequence            | Car     | Goat    | Goat    |             |             | 
| Stick               |         | guess   | reveal  | 0           |             | 
| Switch              | Switch  | guess   | reveal  |             | 1           | 
|                     |         |         |         |             |             | 
| Sequence            | goat    | car     | goat    |             |             | 
| Stick               | reveal  | guess   |         | 1           |             | 
| Switch              | reveal  | guess   | Switch  |             | 0           | 
|                     |         |         |         |             |             | 
| Sequence            | goat    | goat    | car     |             |             | 
| Stick               | reveal  | guess   |         | 0           |             | 
| Switch              | reveal  | guess   | Switch  |             | 1           | 
|                     |         |         |         |             |             | 
| Sequence            | Car     | Goat    | Goat    |             |             | 
| Stick               |         | reveal  | guess   | 0           |             | 
| Switch              | Switch  | reveal  | guess   |             | 1           | 
|                     |         |         |         |             |             | 
| Sequence            | goat    | car     | goat    |             |             | 
| Stick               | reveal  |         | guess   | 0           |             | 
| Switch              | reveal  | Switch  | guess   |             | 1           | 
|                     |         |         |         |             |             | 
| Sequence            | goat    | goat    | car     |             |             | 
| Stick               | reveal  |         | guess   | 1           |             | 
| Switch              | reveal  | Switch  | guess   |             | 0           | 
| -------             | ------- | ------- | ------- | -------     | -------     | 
| Total               |         |         |         | 3           | 6           | 
| Percentage win rate |         |         |         | 33.33333333 | 66.66666667 |   

Here is the output from running the code:
```
How many games? 100000000
The result for stick is a 33.322797% win rate, the result for switch is a 66.663946% win rate out of 100000000 games.
```

