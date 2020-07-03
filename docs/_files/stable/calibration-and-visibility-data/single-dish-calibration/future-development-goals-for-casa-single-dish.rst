.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Future Development Goals
========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Ongoing software development goals for CASA single-dish

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      | The top development priority for CASA single-dish data reduction
        is the conversion to the MeasurementSet format for the full
        reduction process. Dispensing with the ASAP (scan table) format
        will help unify data processing by providing a more homogenous
        basis for data processing, reduction, and analysis, as well as
        streamline and make more versatile the development aspects;
        current and future developers need only be familiar with one
        overall format of data. As such, ASAP will be gone in 5.1.
        However, please note that the **importasap** task is the only
        exception and will not go away even after removing ASAP. This
        task supports importing existing scantables in CASA for backward
        compatibility.
      | There is also significant active development to add header
        information to plots made by **plotms**. While preserving the
        multi-plot capability and building a layout that will not cramp
        or obfuscate the plot output, header information (i.e. target
        name, frequency, integration time, etc.) can be optionally added
        to the plots output by **plotms**.
      | There are a number of additional improvements that we do not
        detail here. ALMA-related development requests and bug notices
        can be sent to the CASA Single Dish Team via the `ALMA
        Helpdesk <https://help.almascience.org/>`__.

.. container:: section
   :name: viewlet-below-content-body
