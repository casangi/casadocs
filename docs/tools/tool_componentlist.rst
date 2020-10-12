

.. _Description:

Description
   tool componentlist description
   
   A componentlist is a tool that contains functions that
   manipulate components. A component is a functional
   representation of the sky brightness - point source, disk,
   Gaussian, etc.
   
    
   
   Note for those new to CASA: components are not used explicitly
   in cleaning, rather the model is stored as an image. 
   Components are useful for e.g.
   `simulation <https://casa.nrao.edu/casadocs-devel/stable/simulation>`__
   and modifying images
   (`ia.modify <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list/tool_image>`__),
   but one will not in general have a clean component list
   associated with cleaning data.
   The simplest way to make a componentlist tool is to use
   cl.addcomponent:
   
   cl.done()   # since the tool is persistent, it is safest to
   close it before beginning
   
   cl.addcomponent(dir='J2000 10h30m00 -20d00m00.0',
   flux=[2.3,0,0,0])  # add a single point source component with
   Stokes I=2.3Jy and other Stokes parameters 0
   
   cl.rename("myList.cl")  # associate with table on disk
   
   cl.done() # flush buffers and ensure the table is written.
   
    
   
   One can open a list on disk with cl.open(filename).
   
    
   
   Componentlists can be converted to/from records (python
   dictionaries) with cl.torecord() and cl.fromrecord(record).
   

.. _Examples:

Examples
   tool componentlist example
   
   include 'componentlist.g' newcl := componentlist('core',
   readonly=F); othercl := componentlist('centarusA.cl', readonly=T);
   newcl.replace(1:2, othercl, [10,13]);
   

.. _Development:

Development
   --CASA Developer--
   