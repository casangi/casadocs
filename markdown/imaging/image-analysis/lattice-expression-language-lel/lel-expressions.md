

# LEL Expressions 

LEL Expressions in detail

\--CASA Developer\--

A LEL expression can be as simple or as complex as one likes using the standard arithmetic, comparison, and logical operators. Parentheses can be used to group subexpressions. The operands in an expression can be lattices, constants, functions, and condition masks. 

> $lat1 + 10$
>
> $lat1 + 2 * max(lat2,1)$
>
> $amp(lat1, lat2)$
>
> $lat1 + mean(img[region1])$
>
> $lat1 + mean(lat2[lat2>5 \unicode{x20}\unicode{x20}\unicode{x26}\unicode{x26}\unicode{x20}\unicode{x20} lat2<10])$

The last example shows how a boolean expression can be used to form a mask on a lattice. Only the pixels fulfilling the boolean condition will be used when calculating the mean. In general the result of a LEL expression is a lattice, but it can be a scalar too. If is is a scalar, it will be handled correctly by C++ and Python functions using it as the source in, say, an assignment to another lattice. LEL fully supports masks. In most cases the mask of a subexpression is formed by AND-ing the masks of its operands. It is fully explained in a [later section](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-masks).

LEL supports the following data types:

> Bool
>
> Float - single precision real (which includes integers)
>
> Double - double precision real
>
> Complex - single precision complex
>
> DComplex - double precision complex

All these data types can be used for scalars and lattices.LEL will do automatic data type promotion when needed. E.g. when a Double and a Complex are used in an operation, they will be promoted to DComplex. It is also possible to promote explicitly using the conversion functions (FLOAT, DOUBLE, COMPLEX and DCOMPLEX). These functions can also be used to demote a data type (e.g. convert from Double to Float), which can sometimes be useful for better performance.

Region is a specific data type. It indicates a region of any type (in pixel or world coordinates, relative, fractional). A region can only be applied to a lattice subexpression using operator `[]`.

# Constants

Scalar constants of the various data types can be formed as follows (which is similar to Python):

-   A Bool constant can be given as True or False.

```{=html}
<!-- -->
```
-   A Float constant can be any integer or floating-point number. For example:

> $3$
>
> $3.14$
>
> $3.14e-2$

-   A Double constant is a floating-point number using a D for the exponent. One can also use the `DOUBLE` function. For example:

> $1d2$
>
> $3.14d-2$
>
> $double(2)$

-   The imaginary part of a Complex or DComplex constant is formed by a Float or Double constant immediately followed by a lowercase i. A full complex constant is formed by adding another constant as the real part. For example:

> $1.5 + 2i$
>
> $2i+1.5$ is identical

Note that a full complex constant has to be enclosed in parentheses when, say, a multiplication is performed on it. For example:

> $2 * (1.5+2i)$

The functions `pi()` and `e()` should be used to specify the constants pi and e. Note that they form a Double constant, so when using for example pi with a Float lattice, it could make a lot of sense to convert pi to a Float. Otherwise the lattice is converted to a Double, which is time-consuming. However, one may have very valid reasons to convert to Double, e.g. to ensure that the calculations are accurate enough.

# Operators

The following operators can be used (with their normal meaning and precedence):

> Unary + and -

> Can not be used with Bool operands.

> Unary !

> Logical NOT operator. Can only be used with Bool operands.

> For a region it forms the complement.

> Binary \^, \*, /, %, +, and -

> \% is the modulo operator. E.g. `3%1.4` results in `0.2` and `-10%3` results in `-1`.

> \^ is the power operator.

> All operators are left-associative, except \^ which is right-associative; thus `2`\^`1`\^`2` results in `2`.

> Operator % can only be used for real operands, while the others can be used for real and complex operands.

> Operator - can also be used for regions. It forms the difference of the left and right operand.

> ==, ! =, \>, \> =, \<,  and \< =

> For Bool operands only = = and ! = can be used. A Bool operand cannot be compared with a numeric operand. The comparison operators use the norm for complex values.

> && and \| \|  && and \|\|

> Logical AND and OR operator.

> These operators can only be used with Bool operands. When used on a region && forms the intersection, while \| \| forms the union.

> The precedence order is:

> \^

> unary `+, -, !``*, /, %`

> `+, -` 

> `= = ,! = , > , > = , < , < =`

> `&&`

> `| |`

Note that \^ has a higher precedence than the unary operators.`For example, -3`\^`2` results in `-9`.

The operands of these operators can be 2 scalars, 2 lattices, or a lattice and a scalar. When 2 lattices are used, they should in principle conform; i.e. they should have the same shape and coordinates. However, LEL will try if it can extend one lattice to make it conformant with the other. It can do that if both lattices have coordinates and if one lattice is a true subset of the other (thus if one lattice has all the coordinate axes of the other lattice and if those axes have the same length or have length 1). If so, LEL will add missing axes and/or stretch axes with length 1.

# Functions

In the following tables the function names are shown in uppercase, while the result and argument types are shown in lowercase. Note, however, that function names are case-insensitive. All functions can have scalar and/or lattice arguments.When a function can have multiple arguments (e.g. atan2), the operands are automatically promoted where needed.

## Mathematical functions

Several functions can operate on real or complex arguments. The data types of such arguments are given as \'numeric\'.

> `Double PI()`

Returns the value of pi.

> `Double E()`

Returns the value of e.

> `numeric SIN(numeric)`

> `numeric SINH(numeric)`

> `real ASIN(real)`

> `numeric COS(numeric)`

> `numeric COSH(numeric)`

> `real ACOS(real)`

> `real TAN(real)`

> `real TANH(real)`

> `real ATAN(real)`

> `real ATAN2(real y, real x)`

Returns `ATAN(y/x)` in correct quadrant.

> `numeric EXP(numeric)`

> `numeric LOG(numeric)`

Natural logarithm.

> `numeric LOG10(numeric)`

> `numeric POW(numeric, numeric)`

The same as operator \^.

> `numeric SQRT(numeric)`

> `complex COMPLEX(real, real)`

Create a complex number from two reals.

> `complex CONJ(complex)`

> `real REAL(numeric)`

Real value itself or real part of a complex number.

> `real IMAG(complex)`

Imaginary part of a complex number.

> `real NORM(numeric)`

> `real ABS(numeric), real AMPLITUDE(numeric)`

`B`oth find the amplitude of a complex number. If the numeric argument is real, imaginary part zero is assumed.

> `real ARG(complex), real PHASE(complex)`

`B`oth find the phase of a complex number.

> `numeric MIN(numeric, numeric)`

> `numeric MAX(numeric, numeric)`

> `Float SIGN(real)`

Returns -1 for a negative value, 0 for zero, 1 for a positive value.

> `real ROUND(real)`

Rounds the absolute value of the number. E.g. `ROUND(-1.6) = -2`.

> `real FLOOR(real)`

Works towards negative infinity. E.g. `FLOOR(-1.2) = -2`

> `real CEIL(real)`

Works towards positive infinity.

> `real FMOD(real, real)`

The same as operator %.

Note that the trigonometric functions need their arguments in radians.

## Scalar result functions

The result of these functions is a scalar.

> `double `$NELEMENTS(anytype)$

> Return number of elements in a lattice (1 for a scalar).

> `double `$NDIM(anytype)$

> Return dimensionality of a lattice (0 for a scalar).

> `double `$LENGTH(anytype, real axis)$

> Return length of a lattice axis (returns 1 for a scalar or if axis exceeds number of axes). Axis number is 1-relative.

> `Bool `$ANY(Bool)$

> Is any element true?

> `Bool `$ALL(Bool)$

> Are all elements true?

> `Double `$NTRUE(Bool)$

> Number of true elements.

> `Double `$NFALSE(Bool)$

> Number of false elements.

> `numeric `$SUM(numeric)$

> Return sum of all elements.

> `numeric `$MIN(numeric)$

> Return minimum of all elements.

> `numeric `$MAX(numeric)$
>
> Return maximum of all elements.

> `real `$MEDIAN(real)$
>
> Return median of a lattice. For smallish lattices (max. 512\*512 elements) the median can be found in 1 pass. Other lattices usually require 2 passes.

> `real `$FRACTILE(real,float)$

> Return the fractile of a lattice at the fraction given by the second argument. A fraction of 0.5 is the same as the median. The fraction has to be between 0 and 1. For smallish lattices (max. 512\*512 elements) the fractile can be found in 1 pass. Other lattices usually require 2 passes.

> `real `$FRACTILERANGE(real,float,float)$

> Return the range between the fractiles at the fraction given by the second and third argument. The fractions have to be between 0 and 1 and the second fraction has to be greater than the first one. The second fraction is optional and defaults to `1-fraction1`. Thus:

> $FRACTILERANGE(lat, 0.1)$

> ``$FRACTILERANGE(lat, 0.1, 0.9)$

> ``$FRACTILE(lat,0.9) - FRACTILE(lat,0.1)$

> are equal, be it that the last one is about twice as slow. For smallish lattices (max. 512\*512 elements) the fractile range can be found in 1 pass. Other lattices usually require 2 passes.

> `numeric MEAN(numeric)`

> Return mean of all elements.

> `numeric VARIANCE(numeric)`

> Return variance. 

> (`sum((a(i) - mean(a))**2) / (nelements(a) - 1)`). All calculations are done in double precision.

> `numeric STDDEV(numeric)`

> Return standard deviation (the square root of the variance).

> `real AVDEV(numeric)`

> Return average deviation.

> (`sum(abs(a(i) - mean(a))) / nelements(a)`). All calculations are done in double precision. 

## Miscellaneous functions

> `numeric `$REBIN(numeric,[f1,f2,...])$

> Rebins the image using the given (integer) factors. It averages the pixels in each bin with shape \[f1,f2,\...\]. Masked-off pixels are not taken into account. If all pixels in a bin are masked off, the resulting pixel will be masked off. The length of the factor list \[f1,f2,\...\] has to match the dimensionality of the image. The factors do not need to divide the axes lengths evenly. Each factor can be a literal value, but it can also be any expression resulting in a real scalar value. For instance, for a 3-dimensional image:
>
> $rebin(lat,[2,2,1])$
>
> will halve the size of axis 1 and 2.

> `real `$AMP(real,real)$

> It returns the square root of the quadrature sum of the two arguments. Thus:

> $amp(lat1,lat2)$

> gives $\sqrt{{lat}_1^2 + {lat}_2^2}$

> This can be used to form, for example, (biased) polarized intensity images when lat1 and lat2 are Stokes Q and U images.

> `real `$PA(real,real)$

> It returns a \`\`position angle\'\' (in degrees) from the two lattices. That is,

> $pa(lat1,lat2)$

> gives $180/\pi*atan2(lat1, lat2)/2$

> This can be used to form, for example, linear polarization position angle images when lat1 and lat2 are Stokes Q and U images, respectively.

> `real `$SPECTRALINDEX(real,real)$

> It returns a the spectral index made from the two lattices. That is,

> $log(s1/s2) / log(f1/f2)$

> where s1 and s2 are the source fluxes in the lattices and f1 and f2 are the frequencies of the spectral axes of both lattices. Similar to e.g. operator + the lattices do not need to have the same shape. One can be extended/stretched as needed.

> `anytype `$VALUE(anytype)$

> It returns the argument without its possible mask, thus it removes the mask from the argument. The section about [mask handling](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-masks) discusses it in more detail.

> `Bool `$MASK(anytype)$

> It returns the mask of the argument. The section about [mask handling](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-masks) discusses it in more detail.

> `Bool `$ISNAN(anytype)$

> It tests lattice elements on a NaN value and sets the corresponding output element to T if so; otherwise to F.

> `anytype REPLACE(anytype, anytype)`

> The first argument has to be a lattice (expression). The optional second argument can be a scalar or a lattice (expression). It defaults to 0. The result of the function is a copy of the first argument, where each masked-off element in the first argument is replaced by the corresponding element in the second argument. The result\'s mask is a copy of the mask of the first argument.
>
> $replace (lat1, 0)$
>
> $replace (lat1, lat2)$
>
> The first example replaces each masked-off element in `lat1` by 0. The second example replaces it by the corresponding element in `lat2`. A possible mask of `lat2` is not used.

> ``$anytype IIF(Bool, anytype, anytype)$

> The first argument is a boolean expression. If an element in it is true, the corresponding element from the second argument is taken, otherwise from the third argument. It is similar to the ternary `?:` construct in C++. E.g.

> $iif (lat1>0, lat1, 0)$ same as $max(lat1,0)$

> $iif (sum(lat1)>0, lat1, lat2)$

> The examples shows that scalars and lattices can be freely mixed. When all arguments are scalars, the result is a scalar. Otherwise the result is a lattice. Note that the mask of the result is formed by combining the mask of the arguments in an appropriate way as explained in the section about [mask handling](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-masks).

> ``$Bool INDEXIN(real axis, set indices)$

> The first argument is a 1-relative axis number. The second argument is a set of indices. It returns a Bool array telling for each lattice element if the index of the given axis is contained in the set of indices.

> The 1-relative indices have to be given as elements with integer values enclosed in square brackets and separated by commas. Each element can be a single index, an index range as `start:end`, or a strided index range as `start:end:stride`. The elements do not need to be ordered, but in a range start must be \< = end. For example:

> $image[indexin(2, [3,4:8,10:20:2])]$

> masks `image` such that only the pixels with an index 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, or 20 on the second axis are set to True.

> The following special syntax exists for this function.

> $INDEXi IN set$

> where `i` is the axis number. So the example above can also be written as:

> $image[index2 in [3,4:8,10:20:2]]$

> Negated versions of this function exist as:

> $INDEXNOTIN(axis, set)$

> $INDEXi NOT IN set$

## Conversion functions

> ``$Float FLOAT(real)$

> Convert to single precision.

> ``$Double DOUBLE(real)$

> Convert to double precision.

> ``$Complex COMPLEX(numeric)$

> Convert to single precision complex. If the argument is real, the imaginary part is set to 0.

> ``$DComplex DCOMPLEX(numeric)$

> Convert to double precision complex. If the argument is real, the imaginary part is set to 0.

> ``$Bool BOOLEAN(region)$

> Convert to boolean. This can be useful to convert a region to a boolean lattice. Only a region in pixel coordinates can be converted, so in practice only an image mask can be converted.

Note that, where necessary, up-conversions are done automatically. Usually it may only be needed to do a down-conversion (e.g. Double to Float).

## Lattice names

When a lattice (e.g. an image) is used in an expression, its name has to be given. The name can be given directly if it consists of the characters `-.$~ `and alphanumeric characters.

If the name contains other characters or if it is a reserved word (currently only T and F are reserved), it has to be escaped. Escaping can be done by preceeding the special characters with a backslash or by enclosing the string in single or double quotes. E.g.

      ~/myimage.data
      ~/myimage.data\-old
      '~/myimage.data-old'

 

