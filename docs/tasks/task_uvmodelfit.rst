

.. _Description:

Description

   .. warning:: There are `Known Issues <../../notebooks/introduction.html#Known-Issues>`__ for uvmodelfit.
   
   Fit a single component source model to the uv-data. Three
   models are available: P=point; G=Gaussian; D=Disk. Fitting
   parameters can be held fixed. The results are given in the CASA
   log and placed in a components file. More information can be found
   about uvmodelfit `here <../../notebooks/uv_manipulation.ipynb>`__ .
   
   .. note:: **INFO:** The Nordic ALMA Regional Center Node has developed
      tools for fitting multiple components of any shape to the
      visibilities. Their versatile
      uvmultifit [1]_ package is provided on their
      `software tools <https://www.oso.nordic-alma.se/software-tools.php>`__
      page.  
   
   .. rubric:: Parameter descriptions
   
   *vis*
   
   Name of input visibility file. Default: none. Examples:
   vis='ngc5921.ms'
   
   *field*
   
   Select data based on field id(s) or name(s). Default: '' (all).
   Examples: field='1'; field='0~2', field IDs inclusive from 0 to 2;
   field='3C*', all field names starting with 3C
   
   *spw*
   
   Select data based on spectral window. Default: '' (all). Examples:
   spw='1'; spw='<2' #spectral windows less than 2; spw='>1',
   spectral windows greater than 1
   
   *selectdata*
   
   Select a subset of the visibility using MSSelection. Default:
   False.  Examples: selectdata=True
   
   *timerange*
   
   Select data based on time range. Default = '' (all). Examples:
   timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
   
   .. note:: NOTE: YYYY/MM/DD can be dropped as needed.
   
   Further examples:* timerange='09:14:0~09:54:0'* yields the quoted
   time range; *timerange='09:44:00'* yields data within one
   integration of the specified time; *timerange='>10:24:00'*
   yields data after the specified time;
   *timerange='09:44:00+00:13:00'* yields data 13 minutes after the
   specified time
   
   *uvrange*
   
   Select data within uvrange (default units kilo-lambda). Default:
   '' (all). Examples: uvrange='0~1000klambda', uvrange from 0-1000
   kilo-lambda; uvrange='>4klambda', uvranges greater than 4 kilo
   lambda; uvrange='0~1000km', uvrange in kilometers
   
   *antenna*
   
   Select data based on antenna/baseline. Default: '' (all). 
   Examples: antenna='5&6', baseline 5-6; antenna='5&6;7&8',
   baselines 5-6 and 7-8; antenna='5', all baselines with antenna 5;
   antenna='5,6', all baselines with antennas 5 and 6
   
   *scan*
   
   Select data based on scan number. Default: '' (all). Examples:
   scan='>3'
   
   *msselect*
   
   Optional data selection (field,spw,time,etc). Default:'' means
   select all.  Examples: msselect='FIELD_ID==0'; msselect='FIELD_ID
   IN [0,1,2]' means select fields 0,1 and 2; msselect='FIELD_ID <=
   1' means select fields 0, 1; msselect='FIELD_ID==0 && ANTENNA1 IN
   [0] && ANTENNA2 IN [2:26]' means select field 0 and antennas 0 to
   26, except antenna 1. Other msselect fields are: 'DATA_DESC_ID',
   'SPECTRAL_WINDOW_ID', 'POLARIZATION_ID', 'SCAN_NUMBER', 'TIME',
   'UVW'.
   
   *niter*
   
   Number of fitting iterations to execute. Default: 5. Examples:
   niter=20
   
   *comptype*
   
   Component model type. Default: 'P'. Options: 'P' (point source),
   'G' (elliptical gaussian), 'D' (elliptical disk)
   
   *sourcepar*
   
   Starting guess for component parameters. Default: [1,0,0] (for
   comptype='P').
   
   If comptype = 'P', then sourcepar = [flux,xoff,yoff], where flux =
   flux (Jy), xoff = offset east (arcsec), yoff = offset north
   (arcsec).
   
   If comptype = 'G' or 'D', then sourcepar =
   [flux,xoff,yoff,majax,axrat,pos], where majax = FWHM along the
   major axis (arcsec), axrat < 1 is the ratio of minor to major
   axis, pos  = position angle (deg)
   
   *varypar*
   
   Control which parameters to let vary in the fit. Default: [ ] (all
   vary). Examples: varypar=[False,True,True]

   
   **Examples with comptype, sourcepar, and varypar**
   
   Fit a point: comptype = 'P', sourcepar = [0.4,0.2,-0.3], varypar =
   [True,True,True]
   
   Fit a circular Gaussian: comptype = 'G', sourcepar =
   [1.4,0.3,-0.2,0.3, 1, 0], varypar = [ True , True ,  True , True ,
   False, False]

   
   *outfile*
   
   Optional output component list table. Default: ''. Examples:
   outfile='componentlist.cl'
   
   How to get the output values:
   
   ::
   
         cl.open('componentlist.cl')        #open the componentlist 'componentlist.cl'
   
         fit = cl.getcomponent(0)           #stores component informationof the first component
   
         fit                                #to see the list
   
         flux = fit['flux']['value']        #to store the I,Q,U,V, flux
   
         print flux
   
   
         ra = fit['shape']['direction']['m0']['value']
   
         dec =fit['shape']['direction']['m1']['value']
   
         print ra, dec
   
   
         bmaj = fit['shape']['majoraxis']['value']     #to get major axis
   
         bmin = fit['shape']['minoraxis']['value']     #to get minor axis
   
   
   Bibliography

   .. [1] Marti-Vidal et al. 2014, A&A 563, 136 `arXiv:1401.4984 <http://arxiv.org/abs/1401.4984>`__
   

.. _Examples:

Examples
   More information on **uvmodelfit** can be found
   `here <../../notebooks/uv_manipulation.ipynb>`__.
   
   ::
   
      # Note: It's best to channel average the data if there are many channels before running a modelfit
      split('ngc5921.ms','1445+099_avg.ms', datacolumn='corrected',field='1445*',width='63')
   
      # Initial guess is that it's close to the phase center and has a flux of 2.0 (a priori we know it's 2.47)
      uvmodelfit('1445+099_avg.ms', # use averaged data
                 niter=5, # Do 5 iterations
                 comptype='P', # P=Point source, G=Gaussian, D=Disk
                 sourcepar=[2.0,.1,.1], # Source parameters for a point source
                 spw='0',
                 outfile='gcal.cl') # Output component list file
   

.. _Development:

Development
   No additional development details

