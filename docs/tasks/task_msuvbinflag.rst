

.. _Description:

Description
    `msuvbinflag` is an automatic flagging algorithm for the identification of radio frequency interference (RFI)
    in the UV plane. In order to use this task, the visibilities first have to be gridded using the msuvbin task.
    The principle underlying this task is that any interference that has an effect on a large scale in the image domain (such as systematic background ripples from RFI) will appear
    as a compact structure in UV-domain. This is in contrast to astronomical sources, which typically show the inverse behavior (compact in the image domain and large scale in the UV domain).

.. _Examples:

Examples
    Here we run msuvbin, then run msuvbinflag on the binned data twice - reducing the nsigma threshold on the second run.

.. code-block :: python

        msuvbin(vis='evla_15A-397_spw1_7_scan_4_6.ms',field='1',spw='0',taql='',outputvis='test_flag_uvgrid.ms',
                phasecenter='',imsize=300,cell='0.5arcsec',ncorr=2,nchan=10,start='',width='',wproject=False,memfrac=0.5,
                mode='bin',flagbackup=False )        
        msuvbinflag(binnedvis='test_flag_uvgrid.ms', method='radial_per_plane', nsigma=10)
        msuvbinflag(binnedvis='test_flag_uvgrid.ms', method='radial_per_plane', nsigma=5)

.. note:: 
    In order to transfer the flags back to the original (ungridded) MS, `msuvbin` will need to be called with the
    same parameters except for `mode` (example below)


.. code-block :: python

    msuvbin(vis='evla_15A-397_spw1_7_scan_4_6.ms',field='1',spw='0',taql='',
            outputvis='test_flag_uvgrid.ms',phasecenter='',imsize=300,cell='0.5arcsec',ncorr=2,nchan=10,start='',
            width='',wproject=False,memfrac=0.5,mode='write_flags_back',flagbackup=False )

.. _Development:

Development
    The first release of msuvbinflag contains two algorithms to identify RFI in the UV-domain. Future releases are expected to have more options for identifying RFI, as well as applying the flags back to the original MS.
