# Testing an Order Processor

In this project, you will write tests that check if a program is working correctly.

There are two parts of the project. First, you will explore the code for the Order Processor. Then, you will write a set of tests that check that the implementation is working correctly.

## Part One: Understanding the Order Processor

Part of managing an online store is handling inventory. The store receives orders, and some code has to update the inventory. For this online store, there is already an `OrderProcessor` class that can update the inventory based on the orders that come in.

This store has 3 types of merchandise: `jacket`, `slacks`, and `pair_of_shoes`.

There are 3 brands the store sells, `fruche`, `onalaja` and `kente`.

The store starts with a quantity of 20 of each of the different items for each brand. So, in the beginning, there will be

- 20 Fruche jackets
- 20 Onalaja jackets
- 20 Kente jackets
- 20 Fruche slacks
- 20 Onalaja slacks
- 20 Fruche pair\_of\_shoes
- 20 Onalaja pair\_of\_shoes
- 20 Kente pair\_of\_shoes

For simplicity, this project won't connect to a database or persist the results to a file - it will just print the results.

The other parts of the program send the `OrderProcessor` a json file with an order, and the order processor interprets it and deducts from the inventory.

An order is a JSON list of objects with a `type`, `brand`, and `quantity`.

An example order looks like this:

```json
[
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "1"}
]
```

When processing this order, the inventory would deduct 2 from the Fruche jackets, and deduct 1 from the Kente slacks.

The program should print this as a result:

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

### Explore the program

For Part 1, you don't need to write any code. Complete the following steps to understand what the program is doing:

* Run `main.py` and see the results.
* The sample orders are stored in json files named `example1.json`,  `example2.json`, and  `example3.json`. Edit `main.py` so that runs `example2.json`, and run `main.py` to see the results. Also try `example3.json`.
* Read through `implementations/store_order_processor.py` and trace through how it processes an order.
  * Find the part of code that raises an exception if the brand for an order is not one of the 3 supported brands.
  * Understand what the `search_in_list` method does.

In summary, here are the features that exist in `implementations/store_order_processor.py`:

* Ordering an item subtracts it from the inventory.
* An order that uses more than the available inventory is not valid.
* If input is not valid, raise an `StoreOrderProcessorException`.
* The inventory is displayed after each order.


## Part Two: Writing Tests

The next part of the assignment is to write tests that check that the `StoreOrderProcessor` implementation works correctly.

Edit `test_store_order_processor.py`. See the `TODO` comments in the file. For each `TODO` comment, write a test. The existing tests in the file show examples of how to set up and test the order processor.

Run the tests with `python test_store_order_processor.py`. All the tests should pass.

The next step is fun. Notice all of the files like `implementations/with_bugs_01.py`. These are different Store Order Processors that have realistic bugs. If the tests are working correctly, they will detect the bugs. In other words - if you pass a buggy implementation to your tests, you would expect one or more of the tests to fail! You can try this. Read the buggy implementations - a comment at the top of the file describes the problem.

We have provided a file `test_tests.py` - a Python program that tests the tests. It loops through every `with_bugs` file, runs the tests on it, and confirms that the tests have a failure. If the tests did not have a failure, they are allowing a buggy program to pass, which isn't right.

Test the tests you've written by running `test_tests.py`. If it runs with no errors, your tests are catching the right bugs. The `test_tests.py` tests are how the project will be autograded.

<img src="img/sh2.png" width="64" height="64" /> <img src="img/sh1.png" width="64" height="64" /> <img src="img/sla2.png" width="64" height="85" /> <img src="img/sla1.png" width="64" height="80" /> <img src="img/sui2.png" width="64" height="64" /> <img src="img/sui1.png" width="64" height="64" /> <img src="img/sh2.png" width="64" height="64" /> <img src="img/sh1.png" width="64" height="64" /> <img src="img/sla2.png" width="64" height="85" /> <img src="img/sla1.png" width="64" height="80" /> <img src="img/sui2.png" width="64" height="64" /> <img src="img/sui1.png" width="64" height="64" />
