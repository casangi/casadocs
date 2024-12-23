

.. _Description:

Description
Msuvbinflag is an automatic flagging algorithm for the identification of Radio Frequency Interference (RFI)
in the UV plane. The visibilities in input CASA Measurements Set (MS) has to be gridded into an uniformed UV plane
with the msuvbin task.
The principle undelying this task is that any interference that has effects on a large scale in the image domain will appear
as a compact structure in UV-domain. No astronomical source will have that behavior especially not centred around (U=0, V=0).

.. _Examples:

Examples
    Here we run msuvbin then run msuvbinflag on the binned data twice with reduction in the nsigma level

.. code-block :: python
msuvbin(vis='evla_15A-397_spw1_7_scan_4_6.ms',field='1',spw='0',taql='',outputvis='test_flag_uvgrid.ms',phasecenter='',
imsize=300,cell='0.5arcsec',ncorr=2,nchan=10,start='',width='',wproject=False,memfrac=0.5,mode='bin',flagbackup=False )

msuvbinflag(binnedvis='test_flag_uvgrid.ms', method='radial_per_plane', nsigma=10)
msuvbinflag(binnedvis='test_flag_uvgrid.ms', method='radial_per_plane', nsigma=5)

##please not you have to run msuvbin with the same exact paramenters except for mode to transfer the flags back to original ms
msuvbin(vis='evla_15A-397_spw1_7_scan_4_6.ms',field='1',spw='0',taql='',outputvis='test_flag_uvgrid.ms',phasecenter='',
imsize=300,cell='0.5arcsec',ncorr=2,nchan=10,start='',width='',wproject=False,memfrac=0.5,mode='write_flags_back',flagbackup=False )

.. _Development:

Development
   A couple of more algorithms will be added

