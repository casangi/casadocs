.. container::
   :name: viewlet-above-content-title

simulator
=========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   tool simulator description

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

      **simulator** provides a unified interface for simulation of
      telescope processing. It can create a MeasurementSet from scratch
      or read in an existing MeasurementSet, it can predict synthesis
      data onto the (u,v) coordinates or single dish data onto (ra,dec)
      points, and it can corrupt this data through Gaussian errors, an
      atmospheric model, or through specific errors residing in (anti-)
      calibration tables.

      .. container:: casa-input-box

         | #Import simulator:
         | import simulator as sm

      #. In **sm.observe**, **simulator** creates a MeasurementSet and
         calculates uvw values. You first make a **simulator** tool,
         with the name of the MeasurementSet that you wish to construct.
         Next you use the various parameters to set up the observing
         details (*sourcename*, *spwname*, *starttime, stoptime*, etc.).
         Then you call the **sm.observe** method for each observing scan
         you wish to make, or **sm.observemany** to create several
         scans. You specify the *sourcename*, *spwname*, *starttime,*
         and *stoptime*. After this, you have a MeasurementSet that is
         complete but *visibilities=0*.
      #. In **sm.predict**, you fill a MeasurementSet (either one newly
         created or a pre-existing one, perhaps from a real telescope)
         with data from a model or componentlist, and then corrupt the
         measurements (if desired).

      .. container:: info-box

         Info: **sm.predict** assumes model image units are Jy/pixel,
         and in fact will overwrite the brightness units of the image
         itself!

      The ft method of the imager tool can also be used to calculate the
      model visibility for a model image or componentlist.

      | To apply errors, first set up the various effects using the
        relevant **simulator** methods, and then call **sm.corrupt**.
      | Some important details:

      -  One call to **sm.observe** generates one scan (all rows have
         the same *SCAN_NUMBER*).
      -  The *starttime* and *stoptime* parameters specified to
         **sm.observe** need not be contiguous and so one can simulate
         antenna drive times or other gaps.
      -  Currently there is no facility to calculate patterns of
         observing, such as mosaicing, since it is easy to do this via
         sequences of calls of **sm.observe**, or
         **simutil.calcpointings,** or the **simobserve** task
      -  The heavy duty columns (*DATA, FLAG*, *IMAGING_WEIGHT*, etc.
         are tiled. New tiles are generated for each scan. Thus the TSM
         files will not get very large.
      -  **sm.predict**\ (*incremental=False*) calculates new
         visibilities and replaces the *DATA* column,
      -  **sm.predict**\ (*incremental=True*) calculates new
         visibilities, adds them to the *DATA* column
      -  **sm.predict** for any value of incremental then sets
         *CORRECTED_DATA* equal to *DATA*, and *MODEL_DATA* to 1

      Numerous methods to facilitate dealing with antenna configuration
      files, geodetic conversions, mosaic pointing files, etc, can also
      be found in the simutil class.

       

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   tool_simulator/about
   tool_simulator/examples
