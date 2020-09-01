Description
      This is the task to convert single-dish scantable data format
      (ATNF Spectral Analysis Package, ASAP) into a CASA visibility data
      format (MeasurementSet, MS) to enable processing of
      scantable-format datasets (e.g. Parkes, Mopra Telescopes at ATNF).

      Prior to CASA 4.5, most of the ALMA data reduction process was
      done in Scantable format. Later CASA versions shifted towards
      eliminating the dependence on Scantable format. From CASA 5.0, no
      processing/reduction is done in Scantable format, and data with
      Scantable format must be transformed into MS format before
      reduction.
