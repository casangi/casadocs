

# LEL Interface 

Python and C++ interfaces to LEL

\--CASA Developer\--

There are two interfaces to LEL. One is from Python and the other from C++. It depends upon your needs which one you access. Most high level users of CASA will access LEL only via the Python interface.

 

## Simple String Expressions

 The **ia.imagecalc** method evaluates the expression and stores the result and mask in an output image. If you specify the output image name, it is written to a disk file of that name. If you don\'t give it, the output image is never written out; it is evaluated every time an action (like **ia.statistics**) is requested.

    im = ia.imagecalc(outfile='outimage', pixels='inimage1+inimage2');
    im.statistics();

The first command creates an image file `outimage` filling it with the sum of the input images. The second command does statistics on that new image. Writing it as

    im = ia.imagecalc(pixels='inimage1+inimage2');
    im.statistics();

would do the same with the exception of creating the output image. Instead the created image is transient; it only lives as an expression and each time it is used the expression is evaluated.

We can use the method **ia.calc** on an already existing image. Thus

     ia.open('ngc1213');
     ia.calc('ngc1213^2');

would replace the pixels by the square of their value in the opened image.

Sometimes you need to double quote the file names in your expression. For example, if the images reside in a different directory as in this example.

    im = ia.imagecalc ('"dir1/im1" + "/nfs/data/im2"');

## C++ interface

This consists of 2 parts.

1\. The function `command` in Images/ImageExprParse.h can be used to execute a LEL command. The result is a LatticeExprNode object. This example does the same as the Python one shown above. E.g.

      LatticeExprNode seltab1 = ImageExprParse::command
      ("imagein1 + imagein2");

2\. The other interface is a true C++ interface having the advantage that C++ variables can be used. Class LatticeExprNode contains functions to form an expression. The same operators and functions as in the command interface are available. For example:

      Float clipValue = 10;
      PagedImage<Float> image("imagein");
      LatticeExpr<Float> expr(min(image,clipValue));

forms an expression to clip the image. Note that the expression is written as a normal C++ expression. The overloaded operators and functions in class LatticeExprNode ensure that the expression is formed in the correct way. Note that a `LatticeExprNode` object is usually automatically converted to a templated `LatticeExpr` object, which makes it possible to use it as a normal `Lattice`. So far the expression is only formed, but not evaluated. Evaluation is only done when the expression is used in an operation, e.g. as the source of the copy operation shown below.

      PagedImage<Float> imout("imageout");
      imout.copyData (expr);

 

