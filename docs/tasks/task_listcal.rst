

.. _Description:

Description
   This task lists antenna gain solutions in tabular form. The table
   is organized as follows. Solutions are output by
   
   #. Spectral window
   #. Antenna
   #. Time
   #. Channel
   #. and Polarization
   
   where the inner-most loop is over polarization.
   
   The **listcal** output table contains two table headers. The
   top-level header is printed each time the spectral window
   changes. This header lists the spectral window ID (SpwID),
   the date of observation (Date), the calibration table name
   (CalTable), and the measurement set name (MS name).
   
   A lower-level header is printed when the top-level header is
   printed, when the antenna names change, and for every *pagerows*
   of output. The lower-level header columns are described here:
   
   =========== ===================================================
   Column name Description
   Ant         Antenna name (contains sub-columns: Amp, Phs, F)
   Time        Visibility timestamp corresponding to gain solution
   Field       Field name
   Chn         Channel number
   Amp         Complex solution amplitude
   Phs         Complex solution phase
   F           Flag
   =========== ===================================================
   
   Elements of the "F" column contain an 'F' when the datum is
   flagged, and '' (whitespace) when the datum is not flagged.
   Presently, the polarization mode names (for example: R, L) are not
   given, but the ordering of the polarization modes (left-to-right)
   is equivalent to the order output by task **listobs** (see "Feeds"
   in **listobs** output).

   
   .. rubric:: Parameter descriptions
   
   *vis*
   
   Name of input visibility file. Default: none. Examples:
   *vis='ngc5921.ms'*
   
   *caltable*
   
   Name of input calibration table. Default: none. Examples:
   *caltable='ngc5921.gcal'*
   
   *field*
   
   Select data based on field ID(s) or name(s). Default: '' => all.
   Examples: *field='1'*; *field='0~2'* field IDs inclusive from 0 to
   2; *field='3C*'* all field names starting with 3C
   
   *antenna*
   
   Select calibration data based on antenna. Default: '' => all.
   Examples: *antenna='5'*; *antenna='5,6'* antenna index 5 and 6
   solutions; *antenna='VA05','VA06'* VLA antenna 5 and 6
   
   *spw*
   
   Select spectral window, channel to list. Default: '' => all spws
   and channels. Examples: *spw='2:34'* spectral window 2, channel 34
   (will only list one spw, one channel at a time)
   
   *listfile*
   
   Write output to disk (will not overwrite). Default: '' => write to
   screen
   
   *pagerows*
   
   Rows per page of listing. Default: 50; *pagerows=0* => do not
   paginate
   

.. _Examples:

Examples
   ::
   
      # Get path to CASA home dir
      pathname=os.environ.get('CASAPATH').split()[0]

      # Select uv-data (FITS) file
      fitsdata=pathname+'/data/demo/NGC5921.fits'

      # MS name; write to current directory
      msdata='NGC5921.ms'

      # import FITS data to MS
      importuvfits(fitsfile=fitsdata, vis=msdata)

      # Create model data for flux calibrator
      setjy(vis=msdata)

      # Calibration table name
      caldata=msdata+'.bcal'

      # Bandpass calibration
      bandpass(vis=msdata, caltable=caldata)

      # List a subset of calibration factors
      listcal(vis=msdata, caltable=caldata, field='N5921_2, 0, 1',
              antenna='1,2,5;10~14', spw='0:1,0:22~25', pagerows=0)
   
   Example Output:
   
   ::
   
      SpwID = 0, Date = 1995/04/13,  CalTable = NGC5921.ms.bcal (B Jones), MS name = /users/jcrossle/NRAO/casa/NGC5921.ms
         
      -------------------------------------------------------------------------------------------------------------------------------------------------------
                                    \| Ant = 1 \| Ant = 2                     \| Ant = 5 \| Ant = 10                    \|
      Time       Field           Chn|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F\|
      ----------|---------------|---|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------\|
      09:21:46.0 1331+30500002_0   1|0.165    7.9   0.117   21.3 0.168   98.8   0.161 -116.8   0.146  -24.6   0.153 -109.7 0.163 -158.6   0.139    3.9
      10:05:27.9 1445+09900002_0   1|0.260   10.3   0.185   20.0 0.266  102.3   0.250 -116.1   0.233  -20.4   0.245 -108.6 0.255 -156.5   0.217    4.1
      10:09:05.3         N5921_2   1|0.047   54.2   0.030   50.7 0.057  -64.6   0.041   36.5   0.050   93.5   0.035  -13.9 0.079   97.5   0.048 -107.0
                                    \| Ant = 11 \| Ant = 12                    \| Ant = 13 \| Ant = 14                    \|
      Time       Field           Chn|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F\|
      ----------|---------------|---|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------\|
      09:21:46.0 1331+30500002_0   1|0.156 -112.6   0.128   -5.5 0.156 -178.4   0.169 -146.2   0.160 -177.4   0.148  -89.1 0.173 -117.0   0.145  141.5
      10:05:27.9 1445+09900002_0   1|0.243 -110.6   0.199   -5.7 0.251 -175.4   0.272 -146.9   0.249 -175.0   0.238  -89.5 0.268 -113.5   0.228  142.5
      10:09:05.3         N5921_2   1|0.054   47.1   0.056  105.5 0.042  -84.9   0.043  -18.9   0.058   72.4   0.055  155.6 0.040  -35.0   0.044 -153.6
   
      SpwID = 0, Date = 1995/04/13,  CalTable = NGC5921.ms.bcal (B Jones), MS name = /users/jcrossle/NRAO/casa/NGC5921.ms
         
      -------------------------------------------------------------------------------------------------------------------------------------------------------
                                    \| Ant = 1 \| Ant = 2                     \| Ant = 5 \| Ant = 10                    \|
      Time       Field           Chn|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F\|
      ----------|---------------|---|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------\|
      09:21:46.0 1331+30500002_0  22|0.319    4.6   0.323   -6.8 0.311  109.6   0.315 -109.0   0.286  -26.8   0.324 -106.8 0.303 -146.6   0.303    4.3
      09:21:46.0 1331+30500002_0  23|0.318    4.4   0.323   -6.8 0.309  109.7   0.315 -108.8   0.285  -26.8   0.325 -106.5 0.304 -146.2   0.304    4.6
      09:21:46.0 1331+30500002_0  24|0.318    4.2   0.323   -6.6 0.309  109.8   0.316 -108.6   0.285  -26.8   0.324 -106.6 0.302 -146.1   0.304    5.0
      09:21:46.0 1331+30500002_0  25|0.319    4.3   0.323   -6.6 0.308  109.5   0.315 -108.4   0.285  -26.7   0.323 -106.7 0.301 -145.9   0.303    5.1
      10:05:27.9 1445+09900002_0  22|0.502    7.0   0.508   -7.9 0.483  112.2   0.499 -108.5   0.451  -24.2   0.515 -106.2 0.481 -144.1   0.489    4.6
      10:05:27.9 1445+09900002_0  23|0.498    7.2   0.509   -8.2 0.489  112.6   0.502 -108.8   0.455  -23.9   0.513 -106.2 0.477 -144.0   0.480    5.0
      10:05:27.9 1445+09900002_0  24|0.496    6.3   0.506   -7.1 0.487  111.9   0.502 -108.3   0.450  -23.8   0.517 -106.1 0.473 -144.6   0.478    4.0
      10:05:27.9 1445+09900002_0  25|0.489    6.3   0.512   -8.2 0.483  113.0   0.498 -108.7   0.456  -24.3   0.507 -105.5 0.470 -144.4   0.476    4.3
      10:09:05.3         N5921_2  22|0.089   53.9   0.084   38.8 0.135  -84.0   0.148   54.9   0.100   94.2   0.112    4.4 0.112   90.6   0.115 -124.0
      10:09:05.3         N5921_2  23|0.068   50.4   0.073   31.5 0.117  -80.7   0.150   50.5   0.103   90.3   0.120    2.6 0.104  103.6   0.104 -121.5
      10:09:05.3         N5921_2  24|0.068   51.4   0.080   45.1 0.125  -89.0   0.146   47.3   0.106   99.9   0.122    8.8 0.102   95.9   0.099 -121.4
      10:09:05.3         N5921_2  25|0.060   45.8   0.060   42.5 0.124  -85.4   0.146   47.8   0.110   93.4   0.125    7.2 0.088  100.9   0.096 -115.9
   
                                    \| Ant = 11 \| Ant = 12                    \| Ant = 13 \| Ant = 14                    \|
      Time       Field           Chn|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F|  Amp    Phs F   Amp    Phs F\|
      ----------|---------------|---|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------\|
      09:21:46.0 1331+30500002_0  22|0.302  -99.8   0.301  -10.5 0.341  169.8   0.350 -137.6   0.306 -167.6   0.308  -84.8 0.319 -103.6   0.316  143.7
      09:21:46.0 1331+30500002_0  23|0.301  -99.9   0.302  -10.6 0.341  169.7   0.349 -138.0   0.306 -167.4   0.307  -84.5 0.318 -103.6   0.316  143.8
      09:21:46.0 1331+30500002_0  24|0.300 -100.0   0.301  -10.9 0.342  169.6   0.348 -138.4   0.305 -167.4   0.306  -84.3 0.319 -103.4   0.317  143.4
      09:21:46.0 1331+30500002_0  25|0.301 -100.1   0.300  -11.0 0.339  169.9   0.347 -138.5   0.305 -167.4   0.306  -84.0 0.317 -103.2   0.315  143.5
      10:05:27.9 1445+09900002_0  22|0.478  -97.3   0.482   -9.7 0.535  171.3   0.544 -138.1   0.480 -165.1   0.487  -86.0 0.502 -100.2   0.503  144.6
      10:05:27.9 1445+09900002_0  23|0.481  -97.4   0.479  -10.4 0.531  171.4   0.549 -138.9   0.483 -165.3   0.489  -84.3 0.498  -99.7   0.501  144.7
      10:05:27.9 1445+09900002_0  24|0.482  -97.6   0.484  -10.1 0.532  172.7   0.544 -139.3   0.489 -165.3   0.476  -84.6 0.498 -100.3   0.502  144.6
      10:05:27.9 1445+09900002_0  25|0.479  -98.4   0.484  -10.1 0.534  172.4   0.553 -139.0   0.481 -165.4   0.479  -84.3 0.498 -100.3   0.497  145.0
      10:09:05.3         N5921_2  22|0.127   44.8   0.142  128.9 0.090  -94.4   0.090  -48.5   0.112   41.3   0.103  109.0 0.075    7.2   0.095 -120.1
      10:09:05.3         N5921_2  23|0.135   43.1   0.132  126.0 0.087  -89.3   0.103  -38.2   0.112   39.3   0.100  117.8 0.076   -3.4   0.098 -113.5
      10:09:05.3         N5921_2  24|0.135   49.4   0.137  136.1 0.092  -95.9   0.084  -42.7   0.104   49.9   0.120  117.6 0.087    2.9   0.097 -121.2
      10:09:05.3         N5921_2  25|0.144   49.8   0.119  130.0 0.086  -96.5   0.074  -42.8   0.109   41.5   0.124  120.8 0.087    0.4   0.104 -117.3
      Listed 120 antenna solutions.
   

.. _Development:

Development
   No additional development details

