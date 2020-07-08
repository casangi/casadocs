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

               caltable : string

            Name of input calibration table

Example

.. container:: param

   .. container:: parameters2

      xaxis : string

   Value to plot along x axis (time,chan,freq,
   antenna,antenna1,antenna2,scan, amp,phase,real,imag,snr,
   tsys,delay,rate,disp,spgain)

Allowed Value(s)

time chan freq antenna antenna1 antenna2 scan amp phase real imag snr
tsys tec delay rate disp spgain

Example

.. container:: param

   .. container:: parameters2

      yaxis : string

   Value to plot along y axis (amp,phase,real,imag,snr,
   antenna,antenna1,antenna2,scan, tsys,delay,rate,disp,spgain,tec)

Allowed Value(s)

amp phase real imag snr antenna antenna1 antenna2 scan tsys tec delay
rate disp spgain

Example

.. container:: param

   .. container:: parameters2

      poln : string

   Antenna polarization to plot (RL,R,L,XY,X,Y,/)

Allowed Value(s)

RL R L X Y /

Example

.. container:: param

   .. container:: parameters2

      field : string

   field names or index of calibrators: \\'\'==>all

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   antenna/baselines: \\'\'==>all, antenna = \\'3,VA04\'

Example

.. container:: param

   .. container:: parameters2

      spw : string

   spectral window:channels: \\'\'==>all, spw=\'1:5~57\'

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   time range: \\'\'==>all

Example

.. container:: param

   .. container:: parameters2

      subplot : int = 111

   Panel number on display screen (yxn)

Example

.. container:: param

   .. container:: parameters2

      overplot : bool = False

   Overplot solutions on existing display

Example

.. container:: param

   .. container:: parameters2

      clearpanel : string = Auto

   Specify if old plots are cleared or not (ignore)

Allowed Value(s)

Current None Auto All

Example

.. container:: param

   .. container:: parameters2

      iteration : string

   Iterate plots on antenna,time,spw,field

Example

.. container:: param

   .. container:: parameters2

      plotrange : doubleArray =

   plot axes ranges: [xmin,xmax,ymin,ymax]

Example

.. container:: param

   .. container:: parameters2

      showflags : bool = False

   If true, show flagged solutions

Example

.. container:: param

   .. container:: parameters2

      plotsymbol : string = o

   pylab plot symbol

Example

.. container:: param

   .. container:: parameters2

      plotcolor : string = blue

   initial plotting color

Example

.. container:: param

   .. container:: parameters2

      markersize : double = 5.0

   Size of plotted marks

Example

.. container:: param

   .. container:: parameters2

      fontsize : double = 10.0

   Font size for labels

Example

.. container:: param

   .. container:: parameters2

      showgui : bool = True

   Show plot on gui

Example

.. container:: param

   .. container:: parameters2

      figfile : string

   \\'\'= no plot hardcopy, otherwise supply name

Example

.. container:: section
   :name: viewlet-below-content-body
