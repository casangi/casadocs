

# LEL Regions 

Regions of interest

\--CASA Developer\--

A region-of-interest generally specifies a portion of a lattice which you are interested in for some astronomical purpose (e.g. what is the flux density of this source). Quite a rich variety of regions are supported in CASA. There are simple regions like a box or a polygon, and compound regions like unions and intersections. Regions may contain their own \`\`region masks\'\'. For example, with a 2-d polygon, the region is defined by the vertices, the bounding box and a mask which says whether a pixel inside the bounding box is inside of the polygon or outside of the polygon.

In addition, although masks and regions are used somewhat differently by the user, a mask is really a special kind of region; they are implemented with the same underlying code.

Like masks, regions can be persistently stored in image. Within Python, regions can be created using the various methods of the rg tool. Regions can also be defined in plain text files (see [Region File Format](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-file-format)).

We saw in the previous section how the condition operator `[]` could be used to generate masks with logical expressions. This operator has a further talent. A region of any type can be applied to a lattice with the `[]` operator. You can think of the region as also effectively being a logical expression. The only difference with what we have seen before is that it results in a lattice with the shape of the region\'s bounding box. If the lattice or the region (as in the polygon above) has a mask, they are and-ed to form the result\'s mask.

All types of regions supported in CASA can be used, thus:

-   regions in pixel or world coordinates
-   in absolute, relative and/or fractional units
-   basic regions box, ellipsoid, and polygon
-   compound regions union, intersection, difference, and complement.
-   extension of a region or group of regions to higher dimensions
-   masks

The documentation in the classes LCRegion, LCSlicer, and WCRegion gives you more information about the various regions.

At this moment a region can not be defined in LEL itself. It is only possible to use regions predefined in an image or another table.

A predefined region can be used by specifying its name. There are three ways to specify a region name:

1.  `tablename::regionname` The region is looked up in the given table (which will usually be an image) in which it is stored.
2.  `::regionname` The region is looked up in the last table used in the expression.
3.  `regionname` Is usually equivalent to above. However, there is no syntactical difference between the name of a region and a lattice/image. Therefore LEL will first try if the name represents a lattice or image. If not, the name is supposed to be a region name. The prefix `::` in the previous way tells that the name should only be looked up as a region. 

Examples are

      myimage.data[reg1]
      (myimage.data - otherimage)[::reg1]
      (myimage.data - otherimage)[myimage.data::reg1]
      myimage.data:nomask[myotherimage::othermask]

In the first example region `reg1` is looked up in image `myimage.data`. It is assumed that `reg1` is not the name of an image or lattice. It results in a lattice whose shape is the shape of the bounding box of the region. The mask of the result is the and of the region mask and the lattice mask.

In the second example it is stated explicitly that `reg1` is a region by using the :: syntax. The region is looked up in `otherimage`, because that is the last table used in the expression. The result is a lattice with the shape of the bounding box of the region.

In the third example the region is looked up in `myimage.data`. Note that the this and the previous example also show that a region can be applied to a subexpression.

In the fourth example we have been very cunning. We have taken advantage of the fact that masks are special sorts of regions. We have told the image `myimage.data` not to apply any of its own masks. We have then used the `[]` operator to generate a mask from the mask stored in a different image, `myotherimage`. This effectively applies the mask from one image to another. Apart from copying the mask, this is the only way to do this.

Unions, intersections, differences and complements of regions can be generated and stored (in C++ and Python). However, it is also possible to form a union, etc. in LEL itself. However, that can only be done if the regions have the same type (i.e. both in world or in pixel coordinates).The following operators can be used:

-   `reg1 || reg2` to form the union.
-   `reg1 && reg2` to form the intersection.
-   `reg1 - reg2` to form the difference.
-   `!reg1` to form the complement.

The normal CASA rules are used when a region is applied:

-   A region in world or relative coordinates can only be applied to an image (or a subexpression resulting in an image). Otherwise there is no way to convert it to absolute pixel coordinates.
-   The axes of a region in world coordinates have to be axes in the image (subexpression). However, the region can have fewer axes.
-   If a region has fewer axes than the image or lattice the region is automatically extended to the full image by taking the full length of the missing axes.

