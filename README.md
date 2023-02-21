# Testing a Store Order Processor

In this project, you will write tests that check if a program is working correctly.

There are two steps to the project. First, you will write an implementation of an "order processor". Then, you will write a full set of tests that confirm that the implementation is working correctly.

## Part One: An Order Processor

Imagine that you are working on server code for an online store. The other parts of the program send the OrderProcessor a json file with an order, and the order processor interprets it and deducts from the inventory.

An example order looks like this,

```json
[
    {"type": "jacket", "brand": "Fruche", "quantity": "2"},
    {"type": "slacks", "brand": "Kente", "quantity": "1"}
]
```

The store has 3 types of merchandise: `jacket`, `slacks`, and `pair_of_shoes`. There are 3 brands the store sells, `Fruche`, `Onalaja` and `Kente`. (For this project these are the only attributes needed as part of the order).

Every item starts off with a quantity of 20 in the inventory. So, in the beginning, there will be 20 Fruche jackets, 20 Onalaja jackets, 20 Kente jackets, 20 Fruche slacks, 20 Onalaja slacks, etc. For simplicity, this project won't connect to a database or persist the results to a file - it will just print the results. The inventories reset to 20 each run.

For the example input, the program should print this as a result:

```
Processed the order.
Remaining inventory:
jacket Fruche 18
jacket Onalaja 20
jacket Kente 20
slacks Fruche 20
slacks Onalaja 20
slacks Kente 19
pair_of_shoes Fruche 20
pair_of_shoes Onalaja 20
pair_of_shoes Kente 20
```

If there is at least one jacket, slacks and pair_of_shoes from one brand in an order we will call this a full outfit. When an order contains one or more full outfits for a brand, the program should print "Contains full outfit for brand" at the end.

So for the example input:

```json
[
    {"type": "jacket", "brand": "Fruche", "quantity": "2"},
    {"type": "slacks", "brand": "Kente", "quantity": "1"},
    {"type": "slacks", "brand": "Fruche", "quantity": "1"},
    {"type": "pair_of_shoes", "brand": "Fruche", "quantity": "1"}
]

```

The output should be this:

```
Remaining inventory:
jacket Fruche 18
jacket Onalaja 20
jacket Kente 20
slacks Fruche 19
slacks Onalaja 20
slacks Kente 19
pair_of_shoes Fruche 19
pair_of_shoes Onalaja 20
pair_of_shoes Kente 20
Contains full outfit for brand
```


For this project, be careful: the input orders might have some bugs and sometimes does not send correct input. (Maybe there is a manual input available where a clerk types in the order, and sometimes they type the wrong thing). You should use `if` statements and `try/catch` statements so that the program does not crash if the input is not correct. If input is not valid, the program should ignore the order entirely, print "Invalid input", and stop.

An order that uses more than the available inventory is also not valid.

## Part Two: Writing Tests


