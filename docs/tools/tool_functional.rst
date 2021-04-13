

.. _Description:

Description
   A functional is a function with parameters, defined as
   :math:`f(p;x)`, where :math:`p` are the parameters, and :math:`x`
   the arguments. Methods are available to calculate the value of a
   function for a series of argument values for the given set of
   parameters, and for the automatic calculation of the derivatives
   with respect to the parameters.
   
   The created functionals can be used in the fitting \\tool\ or in
   any other \\tool\ that needs to have generic function values or
   their derivatives.
   
   A functional has a mask associated with it, to indicate if certain
   parameters have to be solved for. See <link
   anchor="functionals:functionals.masks.function">masks</link> for
   details.
   
   Functionals are created in a variety of ways, in general by
   specifying the name of the functional, together with some
   necessary information like e.g. the order of a polynomial, or the
   code needed to compile your privately defined function. Parameters
   can be set at creation time or later.
   
   | 
   | - a = fs.gaussian1d() # creates a 1D Gaussian, default arguments
   | - b = fs.open('gaussian1') # creates the same one
   | - a.state() # the 'state' of the functional
   | [type=0, order=-1, ndim=1, npar=3, params=[1 0 1] ]
   | - a.type() # its type
   | gaussian1d
   | - a.ndim() # its dimension (number of arguments)
   | 1
   | - a.npar() # its number of parameters
   | 3
   | - b.state()
   | [type=0, order=-1, ndim=1, npar=3, params=[1 0 1] ]
   | - a.f(1); # the value at x=1
   | 0.0625
   | - a.fdf([0,0.5]); # value and derivatives
   | [[1:2,]
   | 1 1 0 0
   | 0.5 0.5 1.38629 0.693147]
   
   In some cases an {\em order} can be specified as well (e.g. for
   polynomials):
   
   | 
   | - a := dfs.poly(3) # creates a 3rd order polynomial
   | - b := dfs.functional('polyn',3) # creates the same one, but
     with
   | # original defaults
   | - a.state()
   | [type=5, order=3, ndim=1, npar=4, params=[1 1 1 1] ]
   | - b.state()
   | [type=5, order=3, ndim=1, npar=4, params=[0 0 0 0] ]
   
   An extremely valuable aspect of the Functionals module is the
   ability to create a functional from a compiled string specifying
   an arbitrary function. For example, let us make our own polynomial
   :math:`1 + 2*x + 3*x^2` and evaluate it at a few abcissa locations
   
   | 
   | - a := dfs.compiled ('p0 + p1*x + p2*x*x', [1,2,3]) # Define
   | - a.f([0,10,20]) # Evaluate at x=[0,10,20]
   | [1 321 1241]
   
   The functions created can also be used to specify the function to
   be fitted in a least squares fit (see the fitting \\tool\ ).
   

.. _Examples:

Examples
   None

.. _Development:

Development
   No additional development details
