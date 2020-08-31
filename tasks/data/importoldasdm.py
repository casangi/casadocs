#
# stub function definition file for docstring parsing
#

def importoldasdm(asdm, corr_mode='all', srt='all', time_sampling='all', ocorr_mode='co', compression=False):
    r"""
Convert an ALMA Science Data Model observation into a CASA visibility file

Parameters
   - **asdm** (string) - 
   - **corr_mode** (string='all') - 
   - **srt** (string='all') - 
   - **time_sampling** (string='all') - 
   - **ocorr_mode** (string='co') - 
   - **compression** (bool=False) - 


Description
      | Task **importnro** enables one to convert the data obtained with
        the NRO45m telescope into the CASA MS2 format. Usage of this
        task is very simple. Set *infile* and *outputvis*, then run the
        task. At this moment, only the OTF data (NOSTAR data) obtained
        with the SAM45 spectrometer is supported, and the OTF data
        obtained with the other spectrometers (e.g., AOS) and the PSW
        data (NEWSTAR data) are outside of scope (Jan./25/2017)
      | An important point in using **importnro** is the treatment of
        the beams of the multi-beam receiver such as FOREST, where
        different beams are assigned to different antennas (not
        beam!). When using other tasks such as **plotms** or
        **sdbaseline**, individual beams can be specified in the
        following ways:

      | (When you specify beam 1,)
      | antenna = ‘0&&&’,
      | antenna = ‘0&&0’, or
      | antenna = ‘NRO-BEAM0’.
      | Another important point is about the array of SAM45. Except for
        FOREST, **importnro** assigns SAM45’s sixteen arrays labelled
        A01-A16 to spw of 0-15 in ascending order, even if some
        different arrays share the same frequency setting. As a
        result, every MS2 file generated via **importnro** has sixteen
        spw IDs due to the high flexibility of the frequency setting in
        SAM45.

      | On the other hand, in the data obtained using FOREST,
        assignments of four beams, two polarizations, and two sidebands
        (4 x 2 x 2 = 16) to SAM45’s sixteen arrays are fixed, and there
        is no flexibility for users in choosing arrays when preparing
        the observation tables. Hence **importnro** generates a MS2 file
        which contains only two spw IDs (0 and 1) when importing FOREST
        OTF data. This is also the case in the so-called spectral window
        mode of FOREST, which enables one to use thirty-two arrays and
        to set four frequency settings. In this case **importnro**
        returns a MS2 file having four spw IDs (0-3).
      | The other parameters can be specified in the same manner as in
        the ALMA data. The results of the data import can be checked
        using task **listobs**.

    """
    pass
