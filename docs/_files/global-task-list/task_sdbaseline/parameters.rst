.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               infile : string

            name of input SD dataset

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = data

   name of data column to be used ["data", "float_data", or "corrected"]

Allowed Value(s)

data float_data corrected

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   select data by antenna name or ID, e.g. "PM03"

Example

.. container:: param

   .. container:: parameters2

      field : string

   select data by field IDs and names, e.g. "3C2*" (""=all)

Example

.. container:: param

   .. container:: parameters2

      spw : string

   select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see
   examples in help)

Example

.. container:: param

   .. container:: parameters2

      scan : string

   select data by scan numbers, e.g. "21~23" (""=all)

Example

.. container:: param

   .. container:: parameters2

      pol : string

   select data by polarization IDs, e.g. "XX,YY" (""=all)

Example

.. container:: param

   .. container:: parameters2

      intent : string

   select data by observational intent, e.g. "*ON_SOURCE*" (""=all)

Example

.. container:: param

   .. container:: parameters2

      reindex : bool = True

   Re-index indices in subtables based on data selection. Ignored when
   blmode='apply'.

Example

.. container:: param

   .. container:: parameters2

      maskmode : string = list

   mode of setting additional channel masks. "list" and "auto" are
   available now.

Allowed Value(s)

auto list

Example

.. container:: param

   .. container:: parameters2

      thresh : double = 5.0

   S/N threshold for linefinder

Example

.. container:: param

   .. container:: parameters2

      avg_limit : int = 4

   channel averaging for broad lines

Example

.. container:: param

   .. container:: parameters2

      minwidth : int = 4

   the minimum channel width to detect as a line

Example

.. container:: param

   .. container:: parameters2

      edge : intArray = 00

   channels to drop at beginning and end of spectrum

Example

.. container:: param

   .. container:: parameters2

      blmode : string = fit

   baselining mode ["fit" or "apply"]

Example

.. container:: param

   .. container:: parameters2

      dosubtract : bool = True

   subtract baseline from input data [True, False]

Example

.. container:: param

   .. container:: parameters2

      blformat : string stringArray = text

   format(s) of file(s) in which best-fit parameters are written
   ["text", "csv", "table" or ""]

Allowed Value(s)

table text csv

Example

.. container:: param

   .. container:: parameters2

      bloutput : string stringArray

   name(s) of file(s) in which best-fit parameters are written

Example

.. container:: param

   .. container:: parameters2

      bltable : string

   name of baseline table to apply

Example

.. container:: param

   .. container:: parameters2

      blfunc : string = poly

   baseline model function ["poly", "chebyshev", "cspline", "sinusoid",
   or "variable"(expert mode)]

Allowed Value(s)

poly chebyshev cspline sinusoid variable

Example

.. container:: param

   .. container:: parameters2

      order : int = 5

   order of baseline model function

Example

.. container:: param

   .. container:: parameters2

      npiece : int = 2

   number of element polynomials for cubic spline curve

Example

.. container:: param

   .. container:: parameters2

      applyfft : bool = True

   automatically set wave numbers of sinusoids

Example

.. container:: param

   .. container:: parameters2

      fftmethod : string = fft

   method for automatically set wave numbers of sinusoids

Allowed Value(s)

fft

Example

.. container:: param

   .. container:: parameters2

      fftthresh : undefined = 3.0

   threshold to select wave numbers of sinusoids

Example

.. container:: param

   .. container:: parameters2

      addwn : undefined = 0

   additional wave numbers to use

Example

.. container:: param

   .. container:: parameters2

      rejwn : undefined

   wave numbers NOT to use

Example

.. container:: param

   .. container:: parameters2

      clipthresh : double = 3.0

   clipping threshold for iterative fitting

Example

.. container:: param

   .. container:: parameters2

      clipniter : int = 0

   maximum iteration number for iterative fitting

Example

.. container:: param

   .. container:: parameters2

      blparam : string

   text file that stores per spectrum fit parameters

Example

.. container:: param

   .. container:: parameters2

      verbose : bool = False

   output fitting parameters to logger

Example

.. container:: param

   .. container:: parameters2

      showprogress : bool = False

   (NOT SUPPORTED YET) show progress status for large data

Example

.. container:: param

   .. container:: parameters2

      minnrow : int = 1000

   (NOT SUPPORTED YET) minimum number of input spectra to show progress
   status

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   name of output file

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   overwrite the output file if already exists

Example

.. container:: section
   :name: viewlet-below-content-body
