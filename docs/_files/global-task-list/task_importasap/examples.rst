Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To convert an ASAP (scantable) based format file into
      MeasurementSet format:

      .. container:: casa-input-box

         importasap(infile='mydata.asap',
             outputvis='mydata.ms',
             flagbackup=True,
             overwrite=False,
             parallel=False)

      By default, importasap preserves flags, will not overwrite any
      existing files with the output, and will not engage parallel
      processing in the conversion (which would otherwise make the
      conversion faster).

.. container:: section
   :name: viewlet-below-content-body
