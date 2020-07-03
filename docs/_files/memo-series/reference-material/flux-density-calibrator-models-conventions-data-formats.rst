.. container::
   :name: viewlet-above-content-title

Flux Calibrator Models - Data Formats
=====================================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Conventions and Data Formats

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

      This section describes the conventions, the formats as well as the
      locations of the data of the flux density calibrator models used
      in setjy. The detailed descriptions of specific flux standards and
      list of the calibrators are found in `Flux Calibrator
      Models <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-calibrator-models>`__
      in the Reference Material section.

      .. rubric:: Extragalactic flux calibrator source models
         :name: extragalactic-flux-calibrator-source-models

      | The spectral flux density models are expressed in a polynomial
        in the form
      | \\begin{equation}
      | log S[Jy] = a + b*log\nu + c*log^2\nu + …
      | \\end{equation}
      | where $\nu$ is a frequency either in MHz or GHz depending on the
        standard. In setjy, the point source model is constructed as a
        *componentlist* scaled by the spectral flux density model. For
        the standards, Baars, Perley 90, Perley-Taylor 95, Perley-Taylor
        99, Perley-Butler 2010, and Stevens-Reynolds 2016,the polynomial
        coefficients are hard-coded in the code.

      For Perley-Butler 2013 and Scaife-Heald 2012, the coefficients are
      stored in CASA tables called PerleyButler2013Coeffs and
      ScaifeHeald2012Coeffs, respectively located in
      ~/nrao/VLA/standards/ in the CASA data directory(from CASA prompt,
      you can find the data root path by typing casa[‘dirs’][‘data’]).
      The separation of the data from the flux calibration code makes
      the maintenace easy and enable a user to acces the informaiton
      directly. Your can access these tables using the table tool
      (**tb**) and **browsetable** task. The list of the column header
      for PerleyButler2013Coeffs is shown below:

      .. container:: casa-output-box

         | CASA <8>: tb.colnames
         | --------> tb.colnames()
         | Out[8]:
         | ['Epoch',
         | '3C48_coeffs',
         | '3C48_coefferrs',
         | '3C138_coeffs',
         | '3C138_coefferrs',
         | '3C147_coeffs',
         | '3C147_coefferrs',
         | '3C286_coeffs',
         | '3C286_coefferrs',
         | '3C123_coeffs',
         | '3C123_coefferrs',
         | '3C295_coeffs',
         | '3C295_coefferrs',
         | '3C196_coeffs',
         | '3C196_coefferrs']

      The coefficients of each source are stored in a column as a vector
      and the corresponding errors are stored in a seperate column. The
      different row represents the corresponding coefficinets at that
      epoch for the time variable sources while for the steady
      sources each row contains identical information. The frequency is
      assumed in GHz.

      The list of the column header for ScaifeHeald2012Coeffs is shown
      below:

      .. container:: casa-output-box

         | CASA <11>: tb.colnames
         | ---------> tb.colnames()
         | Out[11]:
         | ['Epoch',
         | '3C48_coeffs',
         | '3C48_coefferrs',
         | '3C147_coeffs',
         | '3C147_coefferrs',
         | '3C196_coeffs',
         | '3C196_coefferrs',
         | '3C286_coeffs',
         | '3C286_coefferrs',can b
         | '3C295_coeffs',
         | '3C295_coefferrs',
         | '3C380_coeffs',
         | '3C380_coefferrs']

       The reference frequnecy for Scaife-Heald 2012 is 150MHz. 

       

      .. rubric:: Solar System objects
         :name: solar-system-objects

      For the solar system object used as a flux calibrator, **setjy**
      contstruct a model visibiity of the calibrator with the (averaged)
      brightness temperature model and ephemeris data of the sources as
      described in `ALMA Memo
      #594 <https://library.nrao.edu/public/memos/alma/memo594.pdf>`__.
      While the older Bulter-JPL-Horizons 2010 standard, hard-coded the
      brightness temperature models in the code, the models for
      Butler-JPL-Horizons 2012 are tabulated in ASCII files
      (SSobject_name_Tb.dat) located in the CASA data directory under
      ~/alma/SolarSystemModels. With an exception of Mars, the data for
      the brightness temparature models are stored in a simple format:
      1st column - source frequency in GHz; 2nd column - the brightness
      temperature in Kelvin.  The follow example script shows how it can
      be plotted for Titan.

      .. container:: casa-input-box

         import numpy as np

         | rootdatapath=casa['dirs']['data']
         | source='Titan'
         | datapath=rootdatapath+'/alma/SolarSystemModels/'+source+'_Tb.dat'
         | data=np.genfromtxt(datapath)
         | data=data.transpose()

         | freq=data[0]
         | temp=data[1]
         | pl.plot(freq,temp)
         | pl.title(source+' Tb model')
         | pl.xlabel('Frequency (GHz)')
         | pl.ylabel('Tb (K)')

          

      And the following is the output plot by executing the script
      above.

      |image1|

       

      The Tb model for Mars (Mars_Tb.dat) is calculated as a function of
      time and frequency, with tabulations every hour and at frequencies
      of: 30, 80, 115, 150, 200, 230, 260, 300, 330, 360, 425, 650, 800,
      950, and 1000 GHz. The first line of the file contain frequencies
      in GHz. The data starts at the second line of the file with the
      format:    YYYY MM DD HH MJD Tb for at each frequency sepearated
      by a space.

       

      .. rubric:: New Asteroid models
         :name: new-asteroid-models

      Ceres_fd_time.dat, Luthetia_fd_time.dat, Pallas_fd_time.dat, and
      Vesta_fd_time.dat contain thermophysical models by Th. Mueller
      (private communication). These time variable models are already
      converted to flux densities and are tabulated for 30, 80, 115,
      150, 200, 230, 260, 300, 330, 360, 425, 650, 800, 950, and 1000
      GHz. Time intevals are 1 hr. for Ceres and 15min. for Luthetia,
      Pallas, and Vesta with the data available from 2015 01 01 0UT to
      2021 01 01 0 UT.  In **setjy** task,these models are automatically
      selected for the data with the observation dates falls within this
      time range. 

       

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/titan-tb-model.png/@@images/5e99b969-c3ce-4f0c-8758-e48eeec2d360.png
   :class: image-inline
