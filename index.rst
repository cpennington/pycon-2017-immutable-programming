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
            (and common) to modify the values of variables (especially on objects).


    .. revealjs::

        What can we learn?

.. revealjs:: The Setup

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v1_mutable.py
            :language: python
            :start-after: STORAGE-START
            :end-before: STORAGE-END

    .. revealjs:: Action
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v1_mutable.py
            :language: python
            :start-after: ACTION-START
            :end-before: ACTION-END

    .. revealjs:: Loop
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v1_mutable.py
            :language: python
            :start-after: LOOP-START
            :end-before: LOOP-END

.. revealjs:: Restrict Values

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v2_enums.py
            :language: python
            :start-after: STORAGE-START
            :end-before: STORAGE-END

    .. revealjs::
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v2_enums.py
            :language: python
            :start-after: ENUM-START
            :end-before: ENUM-END

    .. revealjs:: Action
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v2_enums.py
            :language: python
            :start-after: ACTION-START
            :end-before: ACTION-END

.. revealjs:: Store Locally

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v3_game_object.py
            :language: python
            :start-after: STORAGE-START
            :end-before: STORAGE-END

    .. revealjs:: Action
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v3_game_object.py
            :language: python
            :start-after: ACTION-START
            :end-before: ACTION-END
            :dedent: 4

    .. revealjs:: Loop
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v3_game_object.py
            :language: python
            :start-after: LOOP-START
            :end-before: LOOP-END

    .. revealjs:: A Bug!
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v3_game_object.py
            :language: python
            :start-after: BUG-START
            :end-before: BUG-END
            :dedent: 4

    .. revealjs:: A Bug!
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v3_game_object.py
            :language: python
            :start-after: BUG-START
            :end-before: BUG-END
            :emphasize-lines: 6
            :dedent: 4


.. revealjs:: Compute

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: STORAGE-START
            :end-before: STORAGE-END

    .. revealjs:: Action
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: ACTION-START
            :end-before: ACTION-END
            :dedent: 4

    .. revealjs:: Property
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: PROPERTY-START
            :end-before: PROPERTY-END
            :dedent: 4

    .. revealjs:: Enum
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: ENUM-START
            :end-before: ENUM-END

.. revealjs:: Immutable

    .. revealjs:: Storage
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: STORAGE-START
            :end-before: STORAGE-END

    .. revealjs:: Action
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: ACTION-START
            :end-before: ACTION-END

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v4_properties.py
            :language: python
            :start-after: TEST-START
            :end-before: TEST-END
            :dedent: 4

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: TEST-START
            :end-before: TEST-END
            :dedent: 4

    .. revealjs:: Tests
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: TEST-2-START
            :end-before: TEST-2-END
            :dedent: 16

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

.. revealjs:: Commands

    .. revealjs::
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: COMMAND-START
            :end-before: COMMAND-END

    .. revealjs:: Loop
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: LOOP-START
            :end-before: LOOP-END

    .. revealjs:: Player
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: PLAYER-START
            :end-before: PLAYER-END
            :dedent: 8

    .. revealjs:: Random
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v7_command.py
            :language: python
            :start-after: RANDOM-START
            :end-before: RANDOM-END