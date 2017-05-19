.. title:: Immutable Programming: Writing Functional Python

.. revealjs:: Immutable Programming
    :subtitle: Writing Functional Python

    Cale Pennington

    @vengefulpickle

    github.com/cpennington

.. revealjs::

    .. revealjs:: Compare

        Python
            Mutable by default (mostly)

        Haskell
            Immutable by default

        .. rv_note::

            The difference I'm going to focus this talk on is mutability. In Python, it's possible
            (and common) to modify the values of variables (especially on objects). In Haskell, once
            you assign a value to a name, that value is fixed forever.

    .. revealjs:: Immutability allows Local Thinking
        :title-heading: h3

    .. revealjs:: Tools for Local Thinking
        :title-heading: h3

        * @property
        * tuple (and namedtuple)
        * Commands
        * Enum

        .. rv_note::

            In the rest of this talk, I'm going to take what's a fairly standard Python design for
            a game of Tic-Tac-Toe, and then explore what additional options moving to an Immutable
            design presents.

.. revealjs:: The Setup

    .. revealjs:: Game Loop
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: LOOP-START
            :end-before: LOOP-END
            :class: mutable
            :emphasize-lines: 9

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :class: mutable
            :start-after: INTRO-START
            :end-before: INTRO-END
            :emphasize-lines: 3, 7

        .. rv_note::

            This is a fairly standard game loop that gets player input, and then calls a method
            on the game to update its state.

            do_move modifies the state of the board, as long as there isn't already a piece
            in that position.


    .. revealjs:: Property
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: PROPERTY-START
            :end-before: PROPERTY-END
            :dedent: 4
            :class: mutable

        .. rv_note::

            Here we see a common Pythonic use of immutability. Rather than having a mutable
            player attribute that we have to update in sync with the board change, we
            use @property to compute the current player based on the board state.
            This helps eliminate a class of bugs where we update the board state without
            updating the player state at the same time.

    .. revealjs:: Enum
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: ENUM-START
            :end-before: ENUM-END
            :class: mutable

        .. rv_note::

            This also uses Enums to limit the set of valid values that our code has to
            consider. Rather than risk typo errors by just using strings, we can restrict
            our inputs to a known set of valid board positions.

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide-in fade-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: FAILED-TEST-START
            :end-before: FAILED-TEST-END
            :dedent: 4
            :class: mutable


    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: fade-in slide-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: FAILED-TEST-START
            :end-before: FAILED-TEST-END
            :dedent: 4
            :emphasize-lines: 4
            :class: mutable

        .. code-block:: python
            :class: mutable

            ================================================================
            FAIL: test_game_end (tictactoe_v4_properties.TestTicTacToe)
            ----------------------------------------------------------------
            Traceback (most recent call last):
            File ".../tictactoe_v4_properties.py", line 93, in test_game_end
                self.assertFalse(self.game.is_finished)
            AssertionError: True is not false

        .. rv_note::

            Uh oh! One of the tests failed. What happened?

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide-in fade-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: DEEP-TEST-START
            :end-before: DEEP-TEST-END
            :dedent: 4
            :class: mutable

        .. rv_note::

            Let's add a new test, that compares the full state of the board,
            before and after the move is made, and asserts that only the expected
            changes are made.

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: fade

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: DEEP-TEST-START
            :end-before: DEEP-TEST-END
            :dedent: 4
            :class: mutable
            :emphasize-lines: 3

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: fade-in slide-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: DEEP-TEST-START
            :end-before: DEEP-TEST-END
            :dedent: 4
            :class: mutable
            :emphasize-lines: 9


    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide

        .. code-block:: python
            :class: mutable

            =============================================================
            FAIL: test_moves_made (tictactoe_v4_properties.TestTicTacToe)
            -------------------------------------------------------------
            Traceback (most recent call last):
            File ".../tictactoe_v4_properties.py", line 116,
            in test_moves_made
                self.assertEqual(after - before, {(0, 0, Player.X)})
            AssertionError: Items in the first set but not the second:
            (1, 0, <Player.X: 'X'>)
            (2, 0, <Player.X: 'X'>)

        .. rv_note::

            That test fails, as you might expect, and shows us that somehow we're
            setting the entire first column to X, even though we were only trying
            to set a single square. Why?

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide-in fade-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :lines: 16-18
            :class: mutable

        .. literalinclude:: tictactoe_v4_properties.py
            :class: fragment mutable
            :language: python
            :start-after: FIXED-STORAGE-START
            :end-before: FIXED-STORAGE-END

        .. revealjs::
            :class: fragment saaad

            Spooky action at a distance

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: fade-in slide-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :lines: 16-18
            :class: mutable

        .. literalinclude:: tictactoe_v4_properties.py
            :class: mutable
            :language: python
            :start-after: FIXED-STORAGE-START
            :end-before: FIXED-STORAGE-END

        .. revealjs::
            :class: saaad

            Saaad... 🙁

        .. rv_note::

            Let's look back at where we store the board state. It turns out, using
            list multiplication returns multiple references to the *same* list contents.
            In this case, it means we actually only have one row, referenced 3 times,
            rather than having three independent rows.

            One fix is to be more careful about crafting our board state. But another
            option would be to make it so that having multiple references to the
            same row object wouldn't be an issue, by making the rows immutable.



.. revealjs:: Immutable

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide

        .. code-block:: python
            :class: immutable

            class Board():
                def __init__(self):
                     self.board = ((Player.NA, )*3, )*3

        .. rv_note::

            This change would prevent the earlier bug, but would also
            require rewriting all of our operations around modifying
            the board state (because we can't change it in-place anymore).
            If we're going to do that, maybe we can get some other benefits as well.
            Let's look back at the test we wrote to compare the before and after board
            states.

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide-in fade-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: DEEP-TEST-START
            :end-before: DEEP-TEST-END
            :dedent: 4
            :class: mutable

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: fade-in slide-out

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: TEST-START
            :end-before: TEST-END
            :dedent: 4
            :class: immutable
            :emphasize-lines: 3, 9

        .. rv_note::

            This version of the test is significantly clearer. Making a move
            on the board doesn't modify the board, it just returns a new board
            with the modified state. Now we can easily compare the before
            and after results.

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide-in fade-out

        .. code-block:: python
            :class: immutable

            class Board():
                def __init__(self):
                     self.board = ((Player.NA, )*3, )*3

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: fade-in slide-out

        .. code-block:: python
            :class: immutable
            :emphasize-lines: 1

            class BoardState(namedtuple('_BoardState', ['board'])):
                ...

            BoardState.__new__.__defaults__ = (((Player.NA, )*3, )*3, )

    .. revealjs:: namedtuple
        :title-heading: h3
        :data-transition: slide

        .. code-block:: python

            from collections import namedtuple

            Widgit = namedtuple('Widgit', ['height', 'weight'])
            x = Widgit(10, 20)
            x.height  # 10
            x.weight  # 20
            list(x)   # [10, 20]

        .. rv_note::

            namedtuple is a function that comes in the python standard library,
            in the collections package. Calling it generates a new subclass of
            tuple that has attribute accessors for each element in the tuple.
            Because it derives from tuple, the attributes are immutable. This
            makes it an easy drop-in way to add immutablity to an existing codebase.

            (It also gives you equality checking, __str__, and a number of other convenience
            methods for free).

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide

        .. code-block:: python
            :class: immutable
            :emphasize-lines: 4

            class BoardState(namedtuple('_BoardState', ['board'])):
                ...

            BoardState.__new__.__defaults__ = (((Player.NA, )*3, )*3, )

        .. rv_note::

            To implement do_move that way, we'll make Board immutable. My bread-and-butter for
            immutability in Python is namedtuple, from the collections package in the standard
            library. It gives you all of the nice properties of an object (named attribute access,
            equality checks, etc), without requiring much boilerplate.

            The second line works around a restriction in namedtuples, which is that normally,
            they don't have any default values. By setting the __defaults__ on __new__, you can
            inject default values for any trailing attributes in the namedtuple constructor.

            You can also see that we use the same storage layout as in the mutable case,
            but using tuples instead of lists so that they can't be modified.


    .. revealjs:: Action
        :title-heading: h3
        :data-transition: slide-in fade-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :lines: 20-22
            :dedent: 4
            :class: mutable

        .. rv_note::

            Just as a reminder, here's what the code looked like in the mutable case.

    .. revealjs:: Action
        :title-heading: h3
        :data-transition: fade-in slide-out

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: ACTION-START
            :end-before: ACTION-END
            :dedent: 4
            :class: immutable

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: REPLACE-START
            :end-before: REPLACE-END
            :class: immutable

        .. rv_note ::

            The implementation of do_move has the same conditional as before, but instead of
            modifying the state in-place, it creates another Board and returns that. If
            the move is invalid, it returns the current board. Because the board is immutable,
            there's no need to make a copy when return an new identical object.


.. revealjs:: Commands

    .. revealjs:: Player
        :title-heading: h3
        :data-transition: slide-in fade-out

        .. literalinclude:: tictactoe_v6_history.py
            :language: python
            :start-after: LOOP-START
            :end-before: LOOP-END
            :class: immutable

        .. rv_note::

            Instead, we can separate the logic into a function that presents the board
            to the player, and returns their action ...

    .. revealjs:: Player
        :title-heading: h3
        :data-transition: fade-in slide-out

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: PLAYER-START
            :end-before: PLAYER-END
            :class: immutable
            :emphasize-lines: 3, 9, 11, 15

        .. rv_note::

            Instead, we can separate the logic into a function that presents the board
            to the player, and returns their action ...

    .. revealjs::
        :title-heading: h3
        :data-transition: slide-in fade-out

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: COMMAND-START
            :end-before: COMMAND-END
            :class: immutable
            :emphasize-lines: 1, 5, 14

    .. revealjs::
        :title-heading: h3
        :data-transition: fade

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: COMMAND-START
            :end-before: COMMAND-END
            :class: immutable
            :emphasize-lines: 2, 6, 15

    .. revealjs::
        :title-heading: h3
        :data-transition: fade-in slide-out

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: COMMAND-START
            :end-before: COMMAND-END
            :class: immutable
            :emphasize-lines: 3, 8, 12, 16

        .. rv_note::

            and then a set of actions that can be performed, and how they affect the
            board state.

    .. revealjs:: Loop
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: LOOP-START
            :end-before: LOOP-END
            :class: immutable

        .. rv_note::

            The game loop ends up significantly simpler, because it just has to tie
            those two concepts together.

    .. revealjs:: Random
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: RANDOM-START
            :end-before: RANDOM-END
            :class: immutable

        .. rv_note::

            It also presents a clean interface for substituting other types of
            players (like a random-AI), or a player over a network interface.

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: TEST-START
            :end-before: TEST-END
            :dedent: 4
            :class: immutable

        .. rv_note::

            Lastly, separating out the commands from the main loop means that you
            can test them independently, and check that relationships between the
            moves hold.

.. revealjs:: Iteration

    .. revealjs:: Search
        :title-heading: h3
        :data-transition: slide-in fade-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: DEPTH-FIRST-START
            :end-before: DEPTH-FIRST-END
            :class: mutable

        .. revealjs::
            :class: saaad fragment

            Saaad... 🙁

        .. rv_note::

            Say now that we want to analyze TicTacToe. We could look through all
            possible games, and see how many X wins vs how many Y wins.

            This code does the trick, but what happens if the caller of depth_first
            makes a modification to the board? Or passes the board to something else
            that makes a modification? If that happens, the rest of the iteration will
            be over the modified board (and we'll miss some game states).

    .. revealjs:: Search
        :title-heading: h3
        :data-transition: fade-in fade-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: DEPTH-COPY-START
            :end-before: DEPTH-COPY-END
            :class: mutable

    .. revealjs:: Search
        :title-heading: h3
        :data-transition: fade-in fade-out

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: DEPTH-COPY-START
            :end-before: DEPTH-COPY-END
            :class: mutable

        .. revealjs::
            :class: saaad

            Saaad... 🙁

        .. rv_note::

            This code fixes that problem, by duplicating the list contents
            of the board at every step.

    .. revealjs:: Search
        :title-heading: h3
        :data-transition: fade-in slide-out

        .. literalinclude:: tictactoe_v8_all_games.py
            :language: python
            :start-after: SEARCH-START
            :end-before: SEARCH-END
            :class: immutable

        .. rv_note::

            With our immutable implementation, the code gets much simpler.

    .. revealjs:: Filter
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v8_all_games.py
            :language: python
            :start-after: FILTER-START
            :end-before: FILTER-END
            :class: immutable
            :emphasize-lines: 1, 12

        .. rv_note::

            Just iterating over all of the states is useful, but it's even
            better when you can direct the search. So, we can add a step that
            uses a provided function to filter (and order) the upcoming boards
            to be searched.

            For example, let's look at how many games are won by X rather than O.
            We can start by only exploring un-finished games.


    .. revealjs:: Filter Function
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v8_all_games.py
            :language: python
            :start-after: FILTER-FN-START
            :end-before: FILTER-FN-END
            :class: immutable

        .. rv_note::

            This stops the search after it finds a board that is finished.

    .. revealjs:: Main
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v8_all_games.py
            :language: python
            :start-after: MAIN-START
            :end-before: MAIN-END
            :dedent: 4
            :class: immutable

        .. rv_note::

            We catagorize the boards based on who won.

    .. revealjs:: Results
        :title-heading: h3
        :data-transition: slide

        .. code-block:: bash

            > python tictactoe_v8_all_games.py
            O wins 77904
            X wins 131184
            Tie 46080

        .. rv_note::

            And after churning away for a bit, get a result.

.. revealjs::

    .. revealjs:: Immutability allows Local Thinking
        :title-heading: h3

    .. revealjs:: Tools for Local Thinking
        :title-heading: h3

        * @property
        * tuple (and namedtuple)
        * Commands
        * Enum

.. revealjs:: Questions?

.. revealjs:: references

    Talk: `bit.ly/immutable-python-pres`_

    Source Code: `bit.ly/immutable-python-src`_

.. _bit.ly/immutable-python-pres: http://bit.ly/immutable-python-pres
.. _bit.ly/immutable-python-src: http://bit.ly/immutable-python-src
