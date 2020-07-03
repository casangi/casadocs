.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   examples how to use sdms tool functions.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      If you already have your SD data in MS format, you can operate on
      that data as follows. Here is an example to fit 3rd order
      polynomials to spectra stored in the FLOAT_DATA column with
      *field='M100'* and with *spw=5* and *7*, subtract it, then
      save the residual spectra into another file:

      .. container:: casa-input-box

         sdms.open('foo.ms')

         sdms.set_selection(field='M100', spw='5,7')

         sdms.subtract_baseline(order=3, datacolumn='float_data',
         outfile='bar.ms')

         sdms.close()

      When importing SD data from other data formats than MS, do as
      follows:

      .. container:: casa-input-box

         sdms.importnro(infile='foo.Y', outfile='bar.ms')      # import
         from NOSTAR format

       or

      .. container:: casa-input-box

         sdms.importasap(infile='foo.asap', outfile='baz.ms')  # import
         from Scantable

      Once you get your data in MS format, you can process it as shown
      in the code sample at the top of this page.

.. container:: section
   :name: viewlet-below-content-body
