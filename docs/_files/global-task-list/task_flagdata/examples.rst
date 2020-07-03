.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task flagdata examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: info-box

         **NOTE**: The vector mode of the **flagdata** task (pre-dating
         CASA 3.4) can be achieved with this task by using it with
         *mode='list'* and the commands given in a list in *inpfile=[
         ]*.

      .. rubric:: Examples of flagging a MeasurementSet
         :name: examples-of-flagging-a-measurementset

      Flag using the 'list' *mode* and flag commands

      .. container:: casa-input-box

         flagdata('my.ms', inpmode='list', inpfile=["mode='clip'
         clipzeros=True","mode='shadow'])

      Manually flag scans 1~3 and save the parameters to the FLAG_CMD
      sub-table.

      .. container:: casa-input-box

         flagdata('my.ms', scan='1~3, mode='manual', savepars=True)

      Save the parameters to a file that is open in append mode.

      .. container:: casa-input-box

         flagdata('my.ms', scan='1~3, mode='manual', savepars=True,
         outfile='flags.txt')

      Flag all the commands given in the Python list of strings.

      .. container:: casa-input-box

         | cmd = ["scan='1~3' mode='manual'",
         |                "spw='9' mode='tfcrop' correlation='ABS_RR,LL'
           ntime=51.0",
         |                "mode='extend' extendpols=True"]
         |     
         | flagdata('my.ms', mode='list', inpfile=cmd)

      Flag all the commands given in the file called 'flags.txt'.   

      .. container:: casa-input-box

         | cat flags.txt
         |         scan='1~3' mode='manual'
         |         spw='9' mode='tfcrop' correlation='ABS_RR,LL'
           ntime=51.0
         |         mode='extend' extendpols=True
         |     
         | flagdata('my.ms', mode='list', inpfile='flags.txt')

      Display the data and flags per-chunk and do not write flags to the
      MS.

      .. container:: casa-input-box

         flagdata('my.ms', mode='list', inpfile='flags.txt',
         action='calculate', display='data')

      Flag all the antennas except *antenna=5*.

      .. container:: casa-input-box

         flagdata(vis='my.ms', antenna='!5', mode='manual)

      Clip the NaN in the data. An empty *clipminmax* will flag only
      NaN.

      .. container:: casa-input-box

         flagdata('my.ms', mode='clip')

      Clip only the water vapor radiometer data.

      .. container:: casa-input-box

         flagdata('my.ms',mode='clip',clipminmax=[0,50],
         correlation='ABS_WVR')

      Clip only zero-value data.

      .. container:: casa-input-box

         flagdata('my.ms',mode='clip',clipzeros=True)

      Flag only auto-correlations of non-radiometer data using the
      *autocorr* parameter.

      .. container:: casa-input-box

         flagdata('my.ms', autocorr=True)

      Flag only auto-correlations using the *antenna* selection.

      .. container:: casa-input-box

         flagdata('my.ms', mode='manual', antenna='*&amp;&amp;&amp;')

      Flag based on selected reasons from a file.

      .. container:: casa-input-box

         | This box is intended for CASA Inputs. Insert your text here.>
           cat flags.txt
         | scan='1~3' mode='manual' reason='MYREASON'
         | spw='9' mode='clip' clipzeros=True reason='CLIPZEROS'
         | mode='manual' scan='4' reason='MYREASON'

          

         flagdata('my.ms', mode='list', inpfile='flags.txt',
         reason='MYREASON').

      The same result of 10a can be achieved using the task **flagcmd**.

      .. container:: casa-input-box

         flagcmd('my.ms', inpmode='file', inpfile='flags.txt',
         action='apply', reason='MYREASON')

      Automatic flagging using 'rflag', using auto-thresholds, and
      specifying a threshold scale-factor to use for flagging.

      .. container:: casa-input-box

         flagdata('my.ms', mode='rflag', spw='9', timedevscale=4.0,
         action='apply')

      Save the interface parameters to the FLAG_CMD sub-table of the MS.
      Add a *reason* to the flag command. This *cmdreason* will be added
      to the REASON column of the FLAG_CMD sub-table. Apply flags in
      **flagcmd**.

      .. container:: casa-input-box

         | flagdata('my.ms', mode='clip', channelavg=False,
           clipminmax=[30., 60.], spw='0:0~10',
         |                   correlation='ABS_XX,XY', action='',
           savepars=True, cmdreason='CLIPXX_XY')
         | #Select based on the reason.
         | flagcmd('my.ms', action='apply', reason='CLIPXX_XY')

      Flag antennas that are shadowed by antennas not present in the MS.

      .. container:: casa-input-box

         | > Create a text file with information about the antennas.
         | > cat ant.txt
         |           name=VLA01
         |           diameter=25.0
         |           position=[-1601144.96146691, -5041998.01971858,
           3554864.76811967]
         |           name=VLA02
         |           diameter=25.0
         |           position=[-1601105.7664601889, -5042022.3917835914,
           3554847.245159178]
         |           name=VLA09
         |           diameter=25.0
         |           position=[-1601197.2182404203, -5041974.3604805721,
           3554875.1995636248]
         |           name=VLA10
         |           diameter=25.0
         |          
           position=[-1601227.3367843349,-5041975.7011900628,3554859.1642644769]  
            
         |            
         | flagdata('my.vis', mode='shadow', tolerance=10.0,
           addantenna='ant.txt')
         | The antenna information can also be given as a Python
           dictionary. To create the
         | dictionary using the flaghelper functions, do the following
           inside casapy:
         | > import flaghelper as fh
         | > antdic = fh.readAntennaList(antfile)
         | flagdata('my.vis', mode='shadow', tolerance=10.0,
           addantenna=antdic)

      Apply the online flags that come from **importasdm**.

      .. container:: casa-input-box

         | > In importasdm, save the online flags to a file.
         | importasdm('myasdm', 'asdm.ms', process_flags=True,
           savecmds=True, outfile='online_flags.txt')
         | > You can edit the online_flags.txt to add other flagging
           commands or apply it directly.
         | flagdata('asdm.ms', mode='list', inpfile='online_flags.txt')
         | > The same result can be achieved using the task flagcmd.
         | flagcmd('asdm.ms', inpmode='file',
           inpfile='online_flags.txt', action='apply')

      Clip mode pre-averaging data across channels and across time.

      .. container:: casa-input-box

         | flagdata(vis='Four_ants_3C286.ms', flagbackup=False,
           mode='clip', datacolumn='DATA',
         |         timeavg=True, timebin='2s', channelavg=True,
           chanbin=2)

       Reduce the fraction of channels that are required to be flagged,
      and print information for every integration that is flagged. 

      .. container:: casa-input-box

         flagdata(vis, ..., mode='antint', spw='9',
         antint_ref_antenna='ea01', minchanfrac=0.3, verbose=True)

      .. rubric::  
         :name: section

      .. rubric:: Examples of flagging a calibration table
         :name: examples-of-flagging-a-calibration-table

      Clip zero data from a bandpass calibration table.

      .. container:: casa-input-box

         flagdata('cal-X54.B1', mode='clip', clipzeros=True,
         datacolumn='CPARAM')

      Clip data from a cal table with SNR <4.0.

      .. container:: casa-input-box

         flagdata('cal-X54.B1', mode='clip', clipminmax=[0.0,4.0],
         clipoutside=False, datacolumn='SNR')

      Clip the g values of a switched power caltable created using the
      gencal task. The g values are usually < 1.0.

      .. container:: casa-input-box

         flagdata('cal.12A.syspower', mode='clip', clipminmax=[0.1,0.3],
         correlation='Sol1,Sol3', datacolumn='FPARAM')

      Now, clip the Tsys values of the same table from above. The Tsys
      solutions have values between 10 -- 100s.

      .. container:: casa-input-box

         flagdata('cal.12A.syspower', mode='clip',
         clipminmax=[10.0,95.0],correlation='Sol2,Sol4',
         datacolumn='FPARAM')

.. container:: section
   :name: viewlet-below-content-body
