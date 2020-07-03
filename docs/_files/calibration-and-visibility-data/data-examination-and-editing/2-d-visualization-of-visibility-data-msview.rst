.. container::
   :name: viewlet-above-content-title

2-D Plot/Flag: viewer/msview
============================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   2-dimensional visualization and editing of visibilities with the
   viewer/msview GUI.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

       

      .. rubric:: Viewing MeasurementSets
         :name: viewing-measurementsets

      --------------

      .. figure:: ../../../../docs/cookbook/casa_cookbook095.png
         :alt: TypeFigure 
         IDLoading measurement set
         CaptionLoading a MeasurementSet: The Load Data - Viewer panel
         as it appears if you select an MS. The only option available is
         to load this as a Raster Image. In this example, clicking on
         the Raster Image button would bring up the displays shown in
         `Data Display Options <#FigDataDisplayOptions>`__.

         TypeFigure 
         IDLoading measurement set
         CaptionLoading a MeasurementSet: The Load Data - Viewer panel
         as it appears if you select an MS. The only option available is
         to load this as a Raster Image. In this example, clicking on
         the Raster Image button would bring up the displays shown in
         `Data Display Options <#FigDataDisplayOptions>`__.

      --------------

      .. container:: center

         Visibility data can also be displayed and flagged directly from
         the viewer or the more tailored task msview. A difference is
         that\ msview\ allows the user to select data before it is
         loaded into the GUI and displayed. A screenshot is shown
         in\ \ `Data Selection in msview. <#FigMSView>`__\ \   
         Selection parameters are\ field, spectral window, time range,
         uv range, antenna, corr, scan, array, and ms selection
         expression\ in the usual CASA selection syntax (see\ \ `Data
         Selection <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__\ \ ).

          

         .. container:: center

            .. figure:: ../../../../docs/cookbook/casa_cookbook100.png
               :alt: 
               ¶ TypeFigure
               IDmsview
               CaptionData Selection in **msview**.

               ¶ TypeFigure
               IDmsview
               CaptionData Selection in **msview**.

          

          

          

         For MeasurementSet files the only option for display is
         ’Raster’ (similar to AIPS taskTVFLG). An example of MS display
         is shown in\ `Data Display
         Options <#FigDataDisplayOptions>`__\ ; loading of an MS is
         shown in\ `Loading a MeasurementSet <#FigLoadMS>`__\ .

         .. container:: info-box

            Warning: Only one MS should be registered at a time on a
            Display Panel.Only one MS can be shown in any case. You do
            not have to close other images/MSs, but you should at least
            ’unregister’ them from the Display Panel used for viewing
            the MS. If you wish to see other images or MSs at the same
            time, create multiple Display Panel windows.

          

         .. rubric:: Data Display Options Panel for MeasurementSets
            :name: data-display-options-panel-for-measurementsets

          

         TheData Display Optionspanel provides adjustments for MSs
         similar to those for images, and also includes flagging
         options. As with images, this window appears when you choose
         theData:Adjustmenu or use the wrench icon from theMain Toolbar.
         It is also shown by default when an MS is loaded. The right
         panel of\ `Data Display
         Options <#FigDataDisplayOptions>`__\ shows aData Optionswindow.
         It has a tab for each open MS, containing a set of categories.
         The options within each category can be either ’rolled up’ or
         expanded by clicking the category label.

         For a MeasurementSet, the categories are:

         -  Advanced
         -  MS and Visibility Selection
         -  Display Axes
         -  Flagging Options
         -  Basic Settings
         -  Axis Drawing and Labels
         -  Color Wedge

          

         .. rubric:: MS Options — Basic Settings
            :name: ms-options-basic-settings

         TheBasic Settingsroll-up is expanded by default. It contains
         entries similar to those for a raster image,\ `Data Display
         Options - Basic
         Settings <#viewerDataDisplayOptionsBasic>`__\ ). Together with
         the brightness/contrast and colormap adjustment icons on
         theMouse Toolbarof the Display Panel, they are especially
         important for adjusting the color display of your MS.

         The available Basic options are:

         -  Data minimum/maximum

            This has the same usage as for raster images. Lowering the
            data maximum will help brighten weaker data values.

         -  Scaling power cycles

            This has exactly the same usage as for raster images
            (see\ `Data Display Options - Basic
            Settings <#viewerDataDisplayOptionsBasic>`__\ ). Again,
            lowering this value often helps make weaker data visible. If
            you want to view several fields with very different
            amplitudes simultaneously, this is typically one of the best
            adjustments to make early, together with theColormap
            fiddlingmouse tool, which is on the middle mouse button by
            default.

         -  Colormap

            GreyscaleorHot Metalcolormaps are generally good choices for
            MS data.

          

         .. rubric:: MS Options— MS and Visibility Selections
            :name: ms-options-ms-and-visibility-selections

          

         -  Visibility Type
         -  Visibility Component
         -  Moving Average Size

         This roll-up provides choice boxes for Visibility Type
         (Observed, Corrected, Model, Residual) and Component
         (Amplitude, Phase, Real, or Imaginary).

         --------------

         .. figure:: ../../../../docs/cookbook/casa_cookbook096.png
            :alt: TypeFigure
            IDvis selection
            Caption MeasurementSet Visibility Selections: The MS for
            NGC4826 BIMA observations has been loaded into the viewer.
            We see the first of the spw in the Display Panel, and have
            opened up MS and Visibility Selections in the Data Display
            Options panel. The display panel raster is not full of
            visibilities because spw 0 is continuum and was only
            observed for the first few scans. This is a case where the
            different spectral windows have different numbers of
            channels also.

            TypeFigure
            IDvis selection
            Caption MeasurementSet Visibility Selections: The MS for
            NGC4826 BIMA observations has been loaded into the viewer.
            We see the first of the spw in the Display Panel, and have
            opened up MS and Visibility Selections in the Data Display
            Options panel. The display panel raster is not full of
            visibilities because spw 0 is continuum and was only
            observed for the first few scans. This is a case where the
            different spectral windows have different numbers of
            channels also.

         --------------

         Changes to Visibility Type or Component (changing from Phase to
         Amplitude, for example) require the data to be retrieved again
         from the disk into memory, which can be a lengthy process. When
         a large MS is first selected for viewing, the user must trigger
         this retrieval manually by pressing theApplybutton (located
         below all the options), after selecting the data to be viewed
         (seeField IDsandSpectral Windows, below).

         Tip:Changing visibility type between ’Observed’ and ’Corrected’
         can also be used to assure that data and flags are reloaded
         from disk. You should do this if you’re using another flagging
         tool such as autoflag simultaneously, so that the viewer sees
         the other tool’s new edits and doesn’t overwrite them with
         obsolete flags. TheApplybutton alone won’t reload unless
         something within the viewer itself requires it; in the future,
         a button will be provided to reload flags from the disk
         unconditionally.

         You can also choose to view the difference from a running mean
         or the local RMS deviation of either Phase or Amplitude. There
         is a slider for choosing the nominal number of time slots in
         the ’local neighborhood’ for these displays.

         .. container:: info-box

            (Note:Insufficient Datais shown in the tracking area during
            these displays when there is no other unflagged data in the
            local neighborhood to compare to the point in question. The
            moving time windows will not extend across changes in either
            field ID or scan number boundaries, so you may see this
            message if your scan numbers change with every time stamp.
            An option will be added later to ignore scan boundaries).

         -  Field IDs
         -  Spectral Windows

         You can retrieve and edit a selected portion of the MS data by
         entering the desired Spectral Window and Field ID numbers into
         these boxes.

         .. container:: info-box

            Important:Especially with large MSs, often the first thing
            you’ll want to do is to selectspectral windowswhich all have
            thesame number of channelsand thesame polarization setup. It
            also makes sense to edit only a few fields at a time. Doing
            this will also greatly reduce data retrieval times and
            memory requirements.

         You can separate the ID numbers with spaces or commas; you do
         not need to enter enclosing brackets. Changes to either entry
         box will cause the selected MS data to be reloaded from disk.

         If you select, say, spectral windows 7, 8, 23, and 24, the
         animator, slice position sliders, and axis labeling will show
         these as 0, 1, 2, and 3 (the ’slice positions’ or ’pixel
         coordinates’ of the chosen spectral windows). Looking at the
         position tracking display is the best way to avoid confusion in
         such cases. It will show something like:Sp Win 23 (s 2)when you
         are viewing spectral window 23 (plane 2 of the selected
         spectral windows).

         Changes to MS selections will not be allowed until you have
         saved (or discarded) any previous edits you have made
         (seeFlagging Options -- Save Edits, below). A warning is
         printed on the console (not the logger).

         Initially, all fields and spectral windows are selected. To
         revert to this ’unselected’ state, choose ’Original’ under the
         wrench icons next to the entry boxes.

         See\ `MeasurementSet Visibility
         Selections <#FigMSVisibilitySelection>`__\ for an example
         showing the use of theMS and Visibility Selectionscontrols when
         viewing an MS.

          

         .. rubric:: MS Options — Display Axes
            :name: ms-options-display-axes

         This roll-up is very similar to that for images: it allows the
         user to choose which axes (from Time, Baseline, Polarization,
         Channel, and Spectral Window) are on the display and the
         animator. There are also sliders here for choosing positions on
         the remaining axes. (It’s useful to note that the
         dataisactually stored internally in memory as an array with
         these five axes).

         --------------

         .. figure:: ../../../../docs/cookbook/casa_cookbook097.png
            :alt: TypeFigure
            IDDisplay axis
            Caption\ **MeasurementSet Display Axes:** The MS for NGC4826
            from `MeasurementSet Visibility
            Selections <#FigMSVisibilitySelection>`__, now with the
            Display Axes open in the Data Display Options panel. By
            default, channels are on the Animation Axis and thus in the
            tapedeck, while spectral window and polarization are on the
            Display Axes sliders.For MSs, changing the choice of axis on
            one control will automatically swap axes, maintaining
            different axes on each control. Changing axes or
            slider/animator positions does not normally require pressing
            Apply— the new slice is shown immediately. However, the
            display may be partially or completely grey in areas if the
            required data is not currently in memory, either because no
            data has been loaded yet, or because not all the selected
            data will fit into the allowed memory. Press theApplybutton
            in this case to load the data (see\ `MS Options - Apply
            Button <#viewerApplyButton>`__\ and Max. Visibility Memory
            at the end of\ `MS Options -
            Advanced <#viewerMSOptionsAdvanced>`__\ ).

            TypeFigure
            IDDisplay axis
            Caption\ **MeasurementSet Display Axes:** The MS for NGC4826
            from `MeasurementSet Visibility
            Selections <#FigMSVisibilitySelection>`__, now with the
            Display Axes open in the Data Display Options panel. By
            default, channels are on the Animation Axis and thus in the
            tapedeck, while spectral window and polarization are on the
            Display Axes sliders.For MSs, changing the choice of axis on
            one control will automatically swap axes, maintaining
            different axes on each control. Changing axes or
            slider/animator positions does not normally require pressing
            Apply— the new slice is shown immediately. However, the
            display may be partially or completely grey in areas if the
            required data is not currently in memory, either because no
            data has been loaded yet, or because not all the selected
            data will fit into the allowed memory. Press theApplybutton
            in this case to load the data (see\ `MS Options - Apply
            Button <#viewerApplyButton>`__\ and Max. Visibility Memory
            at the end of\ `MS Options -
            Advanced <#viewerMSOptionsAdvanced>`__\ ).

         --------------

         .. figure:: ../../../../docs/cookbook/casa_cookbook098.png
            :alt: TypeFigure 
            IDchanging axis
            CaptionChanging the Axis of a MeasurementSet: The MS for
            NGC4826, continuing from `MeasurementSet Display
            Axes <#FigMSDisplayAxes>`__. We have now put spectral window
            on the Animation Axis and used the tapedeck to step to spw
            2, where we see the data from the rest of the scans. Now
            channels is on a Display Axes slider, which has been dragged
            to show Channel 33.

            TypeFigure 
            IDchanging axis
            CaptionChanging the Axis of a MeasurementSet: The MS for
            NGC4826, continuing from `MeasurementSet Display
            Axes <#FigMSDisplayAxes>`__. We have now put spectral window
            on the Animation Axis and used the tapedeck to step to spw
            2, where we see the data from the rest of the scans. Now
            channels is on a Display Axes slider, which has been dragged
            to show Channel 33.

         --------------

         Within theDisplay Axesrollup you may also select whether to
         order the baseline axis by antenna1-antenna2 (the default) or
         by (unprojected) baseline length.

         See\ `MeasurementSet Display
         Axes <#FigMSDisplayAxes>`__\ –\ `Changing the Axis of a
         MeasurementSet <#FigMSChangedAxis>`__\ showing the use of
         theDisplay Axescontrols to change the axes on the animation and
         sliders.

          

         .. rubric:: MS Options — Flagging Options
            :name: ms-options-flagging-options

         These options allow you to edit (flag or unflag) MS data. The
         Point Tool and Rectangle RegionMouse Tools( see\ `Viewer Region
         Positioning <#viewerRegionPositioning>`__\ ) are used on the
         display to select the area to edit. When using the Rectangle
         Region tool, double-click inside the selected rectangle to
         confirm the edit.

         The options below determine how edits will be applied.

         -  Show Flagged Regions...

            You have the option to display flagged regions in the
            background color (as inTVFLG) or to highlight them with
            color. In the former case, flagged regions look just like
            regions of no data. With the (default) color option, flags
            are shown in shades of blue: darker blue for flags already
            saved to disk, lighter blue for new flags not yet saved;
            regions with no data will be shown in black.

         -  Flag or Unflag

            This setting determines whether selected regions will be
            flagged or unflagged. This doesnotaffect previous edits; it
            only determines the effect which later edits will have. Both
            flagging and unflagging edits can be accumulated and then
            saved in one pass through the MS.

         -  Flag/Unflag All...

            These flagging extent checkboxes allow you to extend your
            edit over any of the five data axes. For example, to
            flagallthe data in a given time range, you would check all
            the axesexceptTime, and then select the desired time range
            with theRectangle Regionmouse tool. Such edits will extend
            along the corresponding axes over the entire selected MS
            (whether loaded into memory or not) and optionally over
            unselected portions of the MS as well (Use Entire MS,
            below). Use care in selecting edit extents to assure that
            you’re editing all the data you wish to edit.

         -  Flag/Unflag Entire Antenna?

            This control can be used to extend subsequent edits to all
            baselines which include the desired antenna[s]. For example,
            if you set this item to ’Yes’ and then click the point tool
            on a visibility position with baseline 3-19, the edit would
            extend over baselines 0-3, 1-3, 2-3, 3-3, 3-4, ...
            3-nAntennas-1. Note that the second antenna of the selection
            (19) is irrelevant here – you can click anywhere within the
            ’Antenna 3 block’, i.e., where thefirstantenna number is 3,
            to select all baselines which include antenna 3.

            This item controls the edit extent only along the baseline
            axis. If you wish to flagallthe data for a given antenna,
            you must still check the boxes to flag all Times, Channels,
            Polarizations and Spectral Windows. There would be no point,
            however, in activatingboththis item and the ’Flag All
            Baselines’ checkbox. You can flag an antenna in a limited
            range of times, etc., by using the appropriate checkboxes
            and selecting a rectangular region of visibilities with the
            mouse.

            .. container:: info-box

               Note:You do not need to include the entire ’antenna
               block’ in your rectangle (and you may stray into the next
               antenna if you try). Anywhere within the block will work.
               To flag higher-numbered antennas, it often helps to zoom
               in.

         -  Undo Last Edit

         -  Undo All Edits

            The ’Undo’ buttons do the expected thing: completely undo
            the effect of the last edit (or all unsaved edits). Please
            note, however, that only unsaved edits can be undone here;
            there is no ability to revert to the flagging state at the
            start of the session once flags have been saved to disk
            (unless you have previously saved a ’flag version’. The flag
            version tool is not available through the viewer directly).

         -  Use Entire MS When Saving Edits?

            "Yes" means that saving the edits will flag/unflag over the
            entire MS,includingfields (and possibly spectral windows)
            which are not currently selected for viewing. Specifically,
            data within time range(s) you swept out with the mouse (even
            for unselected fields) will be edited.

            In addition, if "Flag/Unflag All..." boxes were checked,
            such edits will extend throughout the MS. Note that only
            unselectedtimes(fields) can be editedwithoutchecking extent
            boxes for the edits as well. Unselected spectral windows,
            e.g., willnotbe edited unless the edit also has "Flag/Unflag
            All Spectral Windows" checked.

             

            .. container:: info-box

               Warning: Beware of checking “All Spectral Windows” unless
               you have also checked "All Channels" or turned “Entire
               MS” off; channel edits appropriate to the selected
               spectral windows may not be appropriate to unselected
               ones. Set "Use Entire MS" to “No” if your edits need to
               apply only to the portion of the MS you have selected for
               viewing.Edits can often be saved significantly faster
               this way as well.
               Also note that checkboxes apply to individual edits, and
               must be checked before making the edit with the mouse.
               “Use Entire MS”, on the other hand, applies to all the
               edits saved at one time, and must be set as desired
               before pressing "Save Edits".

         -  Save Edits

            MS editing works like a text editor in that you see all of
            your edits immediately, but nothing is committed to disk
            until you press “Save Edits”. Feel free to experiment with
            all the other controls; nothing but ’Save Edits’ will alter
            your MS on disk. As mentioned previously, however, there is
            no way to undo your edits once they are saved, except by
            manually entering the reverse edits (or restoring a
            previously-saved ’flag version’).

            Also,you must save(or discard)your edits before changing the
            MS selections. If edits are pending, the selection change
            will not be allowed, and a warning will appear on the
            console.

            If you close the MS in the viewer,unsaved edits are simply
            discarded, without prior warning. It’s important, therefore,
            to remember to save them yourself. You can distinguish
            unsaved flags (when using the ’Flags In Color’ option),
            because they are in a lighter shade of blue.

            The program must make a pass through the MS on disk to save
            the edits. This can take a little time; progress is shown in
            the console window.

          

         .. rubric:: MS Options— Advanced
            :name: ms-options-advanced

         These settings can help optimize your memory usage, especially
         for large MSs. A rule of thumb is that they can be increased
         until response becomes sluggish, when they should be backed
         down again.

         You can run the unix ’top’ program and hit ’M’ in it (to sort
         by memory usage) in order to examine the effects of these
         settings. Look at the amount of RSS (main memory) and SWAP used
         by the X server and ’casaviewer’ processes. If that sounds
         familiar and easy, then fiddling with these settings is for
         you. Otherwise, the default settings should provide reasonable
         performance in most cases.

         -  Cache size

            The value of this option specifies the maximum number of
            different views of the data to save so that they can be
            redrawn quickly. If you run an animation or scroll around
            zoomed data, you will notice that the data displays
            noticeably faster the second time through because of this
            feature. Often, setting this value to the number of
            animation frames is ideal Note, however, that on multi-panel
            displays, each panel counts as one cached image.

            Large images naturally take more room than small ones. The
            memory used for these images will show up in the X server
            process. If you need more Visibility Memory (below) for a
            really large ms, it is usually better to forgo caching a
            large number of views.

         -  Max. Visibility Memory

            This option specifies how many megabytes of memory may be
            used to store visibility data from the MeasurementSet
            internally.Even if you do not adjust this entry, it is
            useful to look at it to see how many megabytes are required
            to store your entire (selected) MS in memory. If the slider
            setting is above this, the whole selected MS will fit into
            the memory buffer. Otherwise, some data planes will be
            ’grayed out’ (see\ `MS Options - Apply
            Button <#viewerApplyButton>`__\ ), and the selected data
            will have to be viewed one buffer at a time, which is
            somewhat less convenient. In most cases, this means you
            shouldselect fewer fields or spectral windows– see\ `MS
            Options - MS and Visibility
            Selections <#viewerMSVisibilitySelection>`__\ . The
            ’casaviewer’ process contains this buffer memory (it
            contains the entire viewer, but the memory buffer can take
            most of the space).

          

         .. rubric:: MS Options — Apply Button
            :name: ms-options-apply-button

         When viewing large MSs the display may be partially or
         completely grey in areas where the required data is not
         currently in memory, either because no data has been loaded
         yet, or because not all the selected data will fit into the
         allowed memory (seeMax. Visibility Memoryabove). When the
         cursor is over such an area, the following message shows in the
         position tracking area:

         .. code:: verbatim

               press 'Apply' on Adjust panel to load data

         Pressing theApplybutton (which lies below all the options) will
         reload the memory buffer so that it includes the slice you are
         trying to view.

         The messageNo Datahas a different meaning; in that case, there
         simplyisno data in the selected MS at the indicated position.

         For large MeasurementSets, loading visibility data into memory
         is the most time-consuming step. Progress feedback is provided
         in the console window. Again, careful selection of the data to
         be viewed can greatly speed up retrieval.

          

       

.. container:: section
   :name: viewlet-below-content-body
