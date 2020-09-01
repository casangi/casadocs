

# LEL Examples 

Examples for LEL in C++ and Glish.

\--CASA Developer\--

The following examples show some LEL expressions (equally valid in C++ or Glish).

Note that LEL is readonly; i.e. it does not change any value in the images given. A function in the `image` client has to be used to do something with the result (e.g. storing in another image).

-   `lat1+lat2` \-- adds 2 lattices
-   `mean(myimage:nomask) -- `results in a scalar value giving the mean of the image. No mask is used for the image, thus all pixels are used. The scalar value can be used as a lattice. E.g. it can be used as the source in the `image` function `replacemaskedpixels` to set all masked-off elements of a lattice to the mean.
-   `complex(lat1,lat2) -- `results in a complex lattice formed by `lat1` as the real part and `lat2` as the imaginary part.
-   `min(lat1, 2*mean(lat1)) -- `results in a lattice where `lat1` is clipped at twice its mean value.
-   `min(myimage, 2*mean(mymage[myregion])) -- `results in an image where `myimage` is clipped at twice the mean value of region `myregion` in the image..
-   `lat1[lat1>2*min(lat1)]` \-- results in a lattice with a mask. Only the pixels greater than twice the minimum are valid.
-   `replace(lat1)`  \-- results in a lattice where each masked-off element in `lat1` is replaced by 0.
-   `iif(lat1<mean(lat1),lat1*2,lat1/2) -- `results in a lattice where the elements less than the mean are doubled and the elements greater or equal to the mean are divided by 2.

Here follows a sample Glish session showing some of the LEL capabilities and how Glish variables can be used in LEL.

    duw01> glish -l image.g
    - a := array(1:50,5,10)              # make some data
    - global im1 := imagefromarray('im1', a);   # fill an image with it
    - im1.shape()
    [5 10]
    - local pixels, mask
    - im1.getregion(pixels, mask);       # get pixels and mask
    - mask[1,1] := F                     # set some mask elements to False
    - mask[3,4] := F
    - im1.putregion(mask=mask);          # put new mask back
    - global reg:=drm.box([1,1],[4,4]);  # a box region
    - im2 := imagecalc(pixels='$im1[$reg]')     # read-only image applying region
    - local pixels2, mask2
    - im2.getregion(pixels2, mask2);     # get the pixels and mask
    - print pixels2
    [[1:4,]
        1 6 11 16
        2 7 12 17
        3 8 13 18
        4 9 14 19] 
    - print mask2
    [[1:4,]
        F T T T
        T T T T
        T T T F
        T T T T] 
    - im1.replacemaskedpixels ('mean(im2)'); # replace masked-off values
    - im1.getregion (pixels2, mask2);        # by mean of masked-on in im2
    - print pixels2
    [[1:5,]
        10.0714283 6  11 16         21 26 31 36 41 46
        2          7  12 17         22 27 32 37 42 47
        3          8  13 10.0714283 23 28 33 38 43 48
        4          9  14 19         24 29 34 39 44 49
        5          10 15 20         25 30 35 40 45 50]

