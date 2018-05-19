# Manipulating CSV Files

In this activity, you will use list comprehensions to compose a wedding invitation to send to every name on your mailing list.

## Instructions

* Create a new file called `comprehensions.py`.

* Create a list that prompts the user for the names of five people they know.

* Run your program. Note that nothing forces you to write the name "properly"—e.g., as "Jane" instead of "jAnE". You will use list comprehensions to fix this.

  * First, use list comprehensions to create a new list that contains the lowercase version of each of the names your user provided.

  * Then, use list comprehensions to create a new list that contains the title=cased versions of each of the names in your lowercased list.

* Use a list comprehension that creates a list of "invitations" to the wedding.

  * For this exercise, keep it simple: `f"Dear <name>, please come to the wedding this Saturday!"`

* Finally, use a `for` loop to print each entry in your list of invitations.

## Bonuses

* Instead of creating a lowercased list and _then_ a titlecased list, create the titlecased list in a single comprehension.

## Hints

* See the documentation for the [title](https://docs.python.org/3/library/stdtypes.html#str.title) method.

- - -

### Copyright

Coding Boot Camp © 2017. All Rights Reserved.
