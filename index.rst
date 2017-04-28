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

    .. revealjs:: Python

        Mutable by default (mostly)

        .. rv_note::

            In Python, nearly everything is mutable.

    .. revealjs:: Haskell

        Immutable by default

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

    .. revealjs:: Loop
        :title-heading: h3
        :data-transition: slide

        .. literalinclude:: tictactoe_v5_immutable.py
            :language: python
            :start-after: LOOP-START
            :end-before: LOOP-END