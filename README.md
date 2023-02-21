
# Testing a Store Order Processor

In this project, you will write tests that check if a program is working correctly.

There are two steps to the project. First, you will write an implementation of an "order processor". Then, you will write a full set of tests that confirm that the implementation is working correctly.

## Part One: An Order Processor

Imagine that you are working on server code for an online store. The other parts of the program send the OrderProcessor a json file with an order, and the order processor interprets it and deducts from the inventory.

An example order looks like this,

```json
[
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "1"}
]
```

The store has 3 types of merchandise: `jacket`, `slacks`, and `pair_of_shoes`. There are 3 brands the store sells, `fruche`, `onalaja` and `kente`. (For this project these are the only attributes needed as part of the order).

Every item starts off with a quantity of 20 in the inventory. So, in the beginning, there will be 20 Fruche jackets, 20 Onalaja jackets, 20 Kente jackets, 20 Fruche slacks, 20 Onalaja slacks, etc. For simplicity, this project won't connect to a database or persist the results to a file - it will just print the results. The inventories reset to 20 each run.

For the example input, the program should print this as a result:

```
Remaining inventory:
jacket fruche 18
jacket onalaja 20
jacket kente 20
slacks fruche 20
slacks onalaja 20
slacks kente 19
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 20
```

If there is at least one jacket, slacks, and pair\_of\_shoes from one brand in an order, we will call this a full outfit. When an order contains one or more full outfits for a brand, the program should print "Contains full outfit for a brand" at the end.

So for the example input:

```json
[
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "1"},
    {"type": "slacks", "brand": "fruche", "quantity": "1"},
    {"type": "pair_of_shoes", "brand": "fruche", "quantity": "1"}
]

```

The output should be this:

```
Remaining inventory:
jacket fruche 18
jacket onalaja 20
jacket kente 20
slacks fruche 19
slacks onalaja 20
slacks kente 19
pair_of_shoes fruche 19
pair_of_shoes onalaja 20
pair_of_shoes kente 20
Contains full outfit for a brand
```


For this project, be careful: the input JSON might have some bugs and sometimes does not send correct input. (Maybe sometimes a clerk is types in an order manually, and they might type incorrectly). You should use `if` statements and `try/catch` statements so that the program does not crash if the input is not correct. If input is not valid, the program should ignore the order entirely, print "Invalid input", and stop.

An order that uses more than the available inventory is also not valid.

## Part Two: Writing Tests

Please edit the file `test_store_order_processor.py` and add many unit tests.

The tests can call into either the `main process_list()` method, or a helper method you have added. The important part is to write lines like `assert (expected) == (received)`.

You should check for all features,
* including cases where the order would run out of inventory
* including cases where there is a complete outfit for a brand
* checking that invalid input will cause the output to be 'Invalid input'

(This project is autograded, and so you will see the GitHub actions turn green when your project is complete. We are using a script that goes through the test cases you have written and looks for completeness).

