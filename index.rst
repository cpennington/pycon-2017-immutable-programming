.. revealjs:: Immutable Python
    :subtitle: Writing Functional Python

.. revealjs:: Who Am I?

    .. revealjs::

        Cale Pennington

        edx.org

        .. rv_note::

            Hi! I'm Cale Pennington, and I work at edX, which is a non-profit online MOOC provider.
            My day-job is mostly Python, but I dabble with Haskell as well, and will be sharing some
            techniques that are common in Haskell, and other functional progamming languages,
            that are useful in Python too!

.. revealjs:: Background

    .. revealjs::

        Python
            Mutable by default (mostly)

        Haskell
            Immutable by default

        .. rv_note::

            The difference I'm going to focus this talk on is mutability. In Python, it's possible
            (and common) to modify the values of variables (especially on objects). In Haskell, once
            you assign a value to a name, that value is fixed forever.

    .. revealjs::

        What can we learn?

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

        .. rv_note::

            This is a fairly standard game loop that gets player input, and then calls a method
            on the game to update its state.

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: STORAGE-START
            :end-before: STORAGE-END

        .. rv_note::

            The board is stored as nested lists, so that we can easily index particular squares.

    .. revealjs:: Action
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: ACTION-START
            :end-before: ACTION-END
            :dedent: 4

        .. rv_note::

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

        .. rv_note::

            This also uses Enums to limit the set of valid values that our code has to
            consider. Rather than risk typo errors by just using strings, we can restrict
            our inputs to a known set of valid board positions.

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: TEST-START
            :end-before: TEST-END
            :dedent: 4

        .. rv_note::

            We can write some unittests, and validate that the turn changes when moves are
            played and that the move is actually recorded correctly.

.. revealjs:: Immutable

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: TEST-START
            :end-before: TEST-END
            :dedent: 4
            :emphasize-lines: 8-11

        .. rv_note::

            One downside to the unittests that we wrote up above is that once we actually
            call do_move, we lose access to the unmodified board to do comparisons. This makes
            it hard to validate that the move function is only changing the squares we expect it
            to.

            Here, we've got a unit test that assumes that do_move won't change the original
            Board that it was called on, and will instead return a modified Board. That way,
            we can diff the new and old board and verify that only the expect change was made.

            We can also easily chain multiple tests using subTest to verify that all first-moves
            are correct.

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide

        .. code-block:: python

            from collections import namedtuple

            class Board(namedtuple('_Board', ['board'])):
                ...

            Board.__new__.__defaults__ = (((Player.NA, )*3, )*3, )

        .. rv_note::

            To implement do_move that way, we'll make Board immutable. My bread-and-butter for
            immutability in Python is namedtuple, from the collections package in the standard
            library. It gives you all of the nice properties of an object (named attribute access,
            equality checks, etc), without requiring much boilerplate.


    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide

        .. code-block:: python
            :emphasize-lines: 6

            from collections import namedtuple

            class Board(namedtuple('_Board', ['board'])):
                ...

            Board.__new__.__defaults__ = (((Player.NA, )*3, )*3, )

        .. rv_note::

            The second line works around a restriction in namedtuples, which is that normally,
            they don't have any default values. By setting the __defaults__ on __new__, you can
            inject default values for any trailing attributes in the namedtuple constructor.

            You can also see that we use the same storage layout as in the mutable case,
            but using tuples instead of lists so that they can't be modified.


    .. revealjs:: Action
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: ACTION-START
            :end-before: ACTION-END

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: REPLACE-START
            :end-before: REPLACE-END

        .. rv_note ::

            The implementation of do_move has the same conditional as before, but instead of
            modifying the state in-place, it creates another Board and returns that. If
            the move is invalid, it returns the current board. Because the board is immutable,
            there's no need to make a copy when return an new identical object.


.. revealjs:: History

    .. revealjs:: Replay
        :title-heading: h3
        :data-transition: slide

        .. code-block:: python
            :emphasize-lines: 2, 10, 13-14

            def main():
                boards = [Board()]
                while not boards[-1].is_finished():
                    print(boards[-1])
                    move = input(f"... ")
                    x, y = move.split()
                    x = int(x)
                    y = int(y)

                    boards.append(boards[-1].do_move(x, y))

                print("Game Over!")
                for board in boards:
                    print(board)

        .. rv_note::

            Now that we've switch to an immutable style, we get some improvements to other aspects of
            the game as well. We can easily add tracking of the history of the game, by storing
            each of the board states that have occurred. That lets us display a replay of the game
            at the end, or ...

    .. revealjs:: Undo
        :title-heading: h3
        :data-transition: slide

        .. code-block:: python
            :emphasize-lines: 7, 9

            def main():
                boards = [Board()]
                while not boards[-1].is_finished():
                    print(boards[-1])
                    move = input(f"u to undo, gN to revert to move N? ")
                    if move == 'u':
                        boards.pop()
                    elif move.startswith('g'):
                        boards = boards[:int(move.replace('g',''))+1]
                    else:
                        ...

        .. rv_note::

            implement a couple of different kinds of undo commands, where we either undo the most recent move,
            or go back to a previous board state and pick up the game from there.

            This main function highlights another opportunity to learn from Haskell. As written,
            the logic of figuring out what the user is trying to do is mixed in with actually
            doing what they are asking for.

.. revealjs:: Commands

    .. revealjs:: Player
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: PLAYER-START
            :end-before: PLAYER-END

        .. rv_note::

            Instead, we can separate the logic into a function that presents the board
            to the player, and returns their action ...

    .. revealjs::
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: COMMAND-START
            :end-before: COMMAND-END

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

        .. rv_note::

            Lastly, separating out the commands from the main loop means that you
            can test them independently, and check that relationships between the
            moves hold.


.. revealjs::

    * Consider immutability

      * @properties, namedtuple

    * Limit your inputs

      * Commands, Enum

    * Separate logic and I/O

.. revealjs:: Questions?
