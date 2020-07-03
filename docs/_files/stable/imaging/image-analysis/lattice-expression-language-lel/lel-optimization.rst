.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

LEL Optimization
================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Performance issues in LEL.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

      When giving a LEL expression, it is important to keep an eye on
      performance issues.

      .. rubric:: LEL itself will do some optimization:
         :name: lel-itself-will-do-some-optimization

      -  As said in the introduction a LEL expression is evaluated in
         chunks. However, a scalar subexpression is executed only once
         when getting the first chunk. E.g. in

         ::

              lat1 + mean(lat2)

         the subexpression ``mean(lat2)`` is executed only once and not
         over and over again when the user gets chunks. 

      -  Often the exponent 2 is used in the ``pow`` function (or
         operator ``^``). This is optimized by using multiplication
         instead of using the system pow function. 

      -  When LEL finds a `masked-off
         scalar <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-expressions>`__
         in a subexpression, it does not evaluate the other operand.
         Instead it sets the result immediately to a masked-off scalar.
         Exceptions are the operators AND and OR and function ``iif``,
         because their masks depend on the operand values.

      .. rubric:: The user can optimize by specifying the expression
         carefully.
         :name: the-user-can-optimize-by-specifying-the-expression-carefully.

      -  It is strongly recommended to combine scalars into a
         subexpression to avoid unnecessary scalar-lattice operations.
         E.g.

         ::

              2 * lat1 * pi()

         should be written as

         ::

              lat1 * (2 * pi())
              #or
              2 * pi() * lat1

         | because in that way the scalars form a scalar subexpression
           which is calculated only once. Note that the subexpression
           parentheses are needed in the first case, because
           multiplications are done from left to right.
         | In the future LEL will be optimized to shuffle the operands
           when possible and needed.

      -  It is important to be careful with the automatic data type
         promotion of single precision lattices. Several scalar
         functions (e.g. pi) produce a double precision value, so using
         ``pi`` with a single precision lattice causes the lattice to be
         promoted to double precision. If accuracy allows it, it is much
         better to convert ``pi`` to single precision. E.g. assume
         ``lat1`` and ``lat2`` are single precision lattices.

         ::

              atan2(lat1,lat2) + pi()/2

         The result of ``atan2`` is single precision, because both
         operands are single precision. However, ``pi`` is double
         precision, so the result of ``atan2`` is promoted to double
         precision to make the addition possible. Specifying the
         expression as:

         ::

              atan2(lat1,lat2) + float(pi())/2

         avoids that (expensive) data type promotion. 

      -  ``POW(LAT,2)`` or ``LAT``\ ``^``\ ``2`` is faster than
         ``LAT*LAT``, because it accesses lattice ``LAT`` only once.

      -  ``SQRT(LAT)`` is faster than ``LAT``\ ``^``\ ``0.5`` or
         ``POW(LAT,0.5)`` 

      -  ``POW(U,2) + POW(V,2) < 1000``\ ``^``\ ``2`` is considerably
         faster than
         ``SQRT(SQUARE(U) + SQUARE(V)) < 1000``, because it avoids the
         ``SQRT`` function.

      -  LEL can be used with disk-based lattices and/or memory-based
         lattices. When used with memory-based lattices it is better to
         make subexpressions the first operand in another subexpression
         or a function. E.g.
         ``lat1*lat2 + lat3``
         is better than
         ``lat3 + lat1*lat2``
         The reason is that in the first case no copy needs to be made
         of the lattice data which already reside in memory. All LEL
         operators and functions try to reference the data of their
         latter operands instead of making a copy.
         In general this optimization does not apply to LEL expression.
         However, when using the true `C++
         interface <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-interface>`__
         to classes like ``LatticeExprNode``, one can easily use
         memory-based lattices. In that case it can be advantageous to
         pay attention to this optimization.

.. container:: section
   :name: viewlet-below-content-body
