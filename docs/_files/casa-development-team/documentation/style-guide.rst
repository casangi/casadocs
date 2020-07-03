.. container::
   :name: viewlet-above-content-title

Style Guide
===========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Rules on the layout

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

       

      .. rubric:: **Introduction**
         :name: introduction

      This document describes the appropriate style to be used in adding
      content to the CASA Docs.  Please follow these guidelines when
      writing and editing documentation.

      .. rubric:: CASA Docs Organization
         :name: casa-docs-organization

      The CASA Docs are organized first by CASA release version. You can
      see this by opening the CASA Docs `home
      page <https://casa.nrao.edu/casadocs-devel/>`__.  The latest
      version of the documentation is the "Stable" version. Other
      released versions of CASA, beginning with CASA 5.0 are also
      available here. At the time of a CASA release, a snapshot of the
      stable documentation will be taken and that documentation will be
      frozen on the Plone server.

      Within each release version, the CASA documentation is divided
      into *topics*, which may be selected from the *directory* at the
      left sidebar. Each topic may have one or more *pages*, and each
      page may have zero or more *subpages*.  The only difference
      between a page and subpage is the way the item is formatted in the
      left sidebar directory.  Subpages are indented, whereas pages are
      not.  This allows authors to break long sections into multiple
      pages and indicate to the reader that the content is all related. 
      Aside from directory indentation, pages and subpages are
      identical.

      This style guide provides instructions on how to format different
      elements of each page. The goal is to have a rather uniform
      CASAdocs look and feel.  

      .. rubric:: **Page Design and Layouts**
         :name: page-design-and-layouts

      .. rubric:: **Headers**
         :name: headers

      Content within a page can be divided into sections by using
      headers.  Four headers are available from the
      "Formats->Formats->Headers" pull down menu.  The highest level
      sections should use Header 1, followed by Header 2, 3, and 4.

      .. rubric:: Header 1
         :name: header-1

      .. rubric:: Header 2
         :name: header-2

      .. rubric:: Header 3
         :name: header-3

      .. rubric:: Header 4
         :name: header-4

      All section headers should be left aligned. 

      .. container:: alert-box

         When logged in, the headers appear different than when logged
         out (for example, colors are blue instead of grey). This is a
         result of a major update to the CASA Docs layout in CASA 5.5.
         When following the instructions on this page, the final layout
         will be ok.

       

      .. rubric:: Captions for Tables, Figures, Equations etc.
         :name: captions-for-tables-figures-equations-etc.

      To create a caption that can be referenced from the text, place
      your cursor directly underneath the table. Then select
      "Insert->Insert Template->Caption" and press ok. That will create
      a caption box. In the "Type" field, enter "Table" for Tables,
      "Figure" for figures, etc. and under "ID", create an identifier
      text that is unique. We recommend to use a scheme like
      "pagename-fig/tab/eq/fn-identifier' where the second word is *fig*
      for figures, *tab* for tables, *eq* for equations, and *fn* for
      footnotes. e.g. "styleguide-fig-casalogo" for the caption of the
      CASA logo
      `below <http://casa.nrao.edu/casadocs/stable/documentation/style-guide#figid-styleguidefigcasalogo>`__.
      Under "Caption" enter the caption text. Save the page. In the
      updated page, the caption will show a little link symbol and
      clicking on it reveals a unique URL. This URL can then be used to
      refer to the table in the text. Select as 'external URL' and add
      the string when the link is created in plone.

      See the Table and Figure captions below for examples.

       

      .. rubric:: **Tables **
         :name: tables

      Tables are created through "Table"->"Insert Table". As a first
      step, define the numbers of rows and column on the displayed grid.

      Headers can be used within tables to create heading cells for
      rows, columns, or the entire table.  We use a template for the
      property of all header cells. Place the cursor in a cell, or mark
      the cell or multiple content. Multiple cells can be selected.
      Right-click and go to"Cell Properites"  and switch "Cell Type" to
      "Header Cell".  Although little may change, setting the cell type
      to "Header" will allow the automatic application of table header
      templates that will propagate throughout the document.  

      Table captions are inserted as described
      `above. <#captions-for-tables--figures--equations-etc->`__

       

      ====== ====== ======
      Header Header Header
      ====== ====== ======
      Header         
      Header        stuff
      Header stuff   
      ====== ====== ======

      .. rubric::  
         :name: section

      ======= ======================
      Type    Table
      ID      styleguide-tab-example
      Caption Your caption here.
      ======= ======================

       

      .. rubric:: Images
         :name: images

      Images may be added using the "Insert/Edit Image" button |image1|
      in the editor control bar (the little postcard symbol).  It is
      highly recommended to include multiple images with documentation
      in order to add an illustrative dimension to content. Captions
      should be added as described
      `above <#captions-for-tables--figures--equations-etc->`__.

       

      |image2|

       

      ======= =======================
      Type    Figure
      ID      styleguide-fig-casalogo
      Caption The CASA logo.
      ======= =======================

      .. rubric:: **Sizing**
         :name: sizing

      .. container::

         Images may be uploaded to CASA documentation as a large
         resolution. However, images added with the html text editor
         will not automatically resize. Images can be resized with your
         cursor via an image transformation box that will appear when
         the image is clicked. Pixel dimensions are listed next to the
         image transformation box. We recommend though to use the
         "Preview" Size of 400x400 pixels, a number that can be set from
         the "Insert/edit" pop-up. Other sizes as appropriate, however,
         are also possible. 

      .. container::

         Note that image content is responsive, so once you decide on an
         ideal size for the image relative to the page content, the
         image will resize for smaller screens.

      .. container::

          

      .. rubric:: **Alignment**
         :name: alignment

      .. container::

         Images, Tables, and Captions are all center aligned on a page,
         but content within the cells of a Table should be left
         justified. 

      .. container::

          

      .. rubric:: **Equations/Text and Math Formatting**
         :name: equationstext-and-math-formatting

      .. rubric:: **LaTex/MathJax**
         :name: latexmathjax

      LaTex code can be used to render math and long text documentation.
      This is possible through a local version of MathJax. 

      .. rubric:: **Inserting a formula with MathJax**
         :name: inserting-a-formula-with-mathjax

      Our local version of MathJax uses  $\$ ...\$$ as a delimiter to
      signal an equation.

      ::

         $a^2 + b^2 = c^2$

      (the above was using the "Pre" formatting, which does not render
      latex, but shows text verbatim)

      will lead to 

      $a^2 + b^2 = c^2$. 

      Other characters, such as "&" can occasionally cause formatting
      issues when placed inside a MathJax formula. This can be fixed by
      replacing the "&" with its hexidecimal unicode: \unicode{x26}, or
      placing it outside the $\$ ...\$$

      delimiters to prevent it from rendering in MathJax.  

      Equations can have captions as decribed
      `above <#captions-for-tables--figures--equations-etc->`__.

      .. rubric:: Preventing LaTex/MathJax When it is not Wanted
         :name: preventing-latexmathjax-when-it-is-not-wanted

      Where more than one dollar sign is used in a block of text,
      MathJax may be triggered unintentionally.  To prevent this, a
      special HTML tag may be used.  Follow these steps:

      #. To edit HTML, change the drop-down menu below the editor window
         to "text/x-web-textile". 
      #. Find the dollar sign that is being interpreted as the beginning
         of the MathJax code. 
      #. Put that dollar sign into an HTML span block with class equal
         to "tex2jax_ignore":

         .. container:: terminal-box

            ``<``\ ``span``
            ``class``\ ``=``\ ``"tex2jax_ignore"``\ ``>$</``\ ``span``\ ``>``

      Note that the span block can include more than just the dollar
      sign, and everything inside the span block will be excluded from
      MathJax interpretation.

      .. rubric::  
         :name: section-1

      .. rubric:: **CASA Formatting**
         :name: casa-formatting

      CASA tasks and tool (methods) are in bold font, parameters of task
      or tools in italics. For example. "In **gaincal** set
      *caltable='table.cal'* to define the output name of the
      calibration table." Similarly, use italics when referring to table
      columns, like *CORRECTED_DATA*. 

      Known task names will be automatically rendered by Plone, creating
      links to the task/tool description. This is based on a table of
      known tasks. If a task is not recognized, please submit a JIRA
      ticket to Bjorn to have it added to the list of known tasks. We
      maintain a list of tasks that are auto-linked and ones that are
      not. For instance, the task **find** is not linked (as it appears
      a lot in regular text).

      Shell commands will be formatted with "Courier New" and in
      italics, e.g. "*ls -rt*".

      Python code will be written in "Courier New" (regular font/no
      italics) "listobs(vis='test.ms')".

      .. container:: alert-box

         **NOTICE:** With the change in layout for CASA 5.5,
         auto-linking does no longer work. Please do continue to mark
         each task or tool in boldface when mentioned on a page.

       Other writing conventions:

      -  If you want to place an emphasis on a text, italics are
         acceptable. Other options could be underline text to
         distinguish from parameters. And don't forget that there are
         boxes as explained in the next paragraph. 
      -  Names of books, organizations, space-based telescopes should be
         italicized.
      -  Use “Formats” → “Block” →  “Blockquote” for long quotes or
         indented paragraphs.
      -  Strikethroughs may be used to indicate the omission of text,
         while still leaving the omitted text available to view.

       

      .. rubric:: CASA Naming Convention
         :name: casa-naming-convention

      if possible use the following spelling conventions throughout the
      document:

      | MeasurementSet
      | Multi-MS
      | Sub-MS
      | MS
      | MMS

       

       

      .. rubric:: **Tags and Paths**
         :name: tags-and-paths

      .. rubric:: General Tags and Alert Boxes
         :name: general-tags-and-alert-boxes

      We have a number of different pre-defined boxes. 

      1) For CASA inputs, please use the approriate "CASA input box"
      from the "en.Insert template" button (looks like a shelf): 

      .. container:: casa-input-box

         This box is intended for CASA Inputs. Insert your text here.

      interface listings will also go into a CASA input box. The CASA
      input and output boxes shall be formatted in fixed width font. To
      do so, mark the text and select "Font Family->Courier New". For
      clarification, The text could start with '#In CASA": 

      .. container:: casa-input-box

         #In CASA
         CASA<1>: inp listobs
         --------> inp(listobs)
         #  listobs :: List the summary of a data set in the logger or
         in a file
         vis                 =         ''        #  Name of input
         visibility file (MS)
         selectdata          =       True        #  Data selection
         parameters
              field          =         ''        #  Field names or field
         index numbers:
                                                 #   ''==>all,
         field='0~2,3C286'
              spw            =         ''        # 
         spectral-window/frequency/channel
              antenna        =         ''        #  antenna/baselines:
         ''==>all, antenna
                                                 #   ='3,VA04'
              timerange      =         ''        #  time range:
                                                 #  
         ''==>all,timerange='09:14:0~09:54:0'
              correlation    =         ''        #  Select data based on
         correlation
              scan           =         ''        #  scan numbers:
         ''==>all
              intent         =         ''        #  Select data based on
         observation intent:
                                                 #   ''==>all
              feed           =         ''        #  multi-feed numbers:
         Not yet implemented
              array          =         ''        #  (sub)array numbers:
         ''==>all
              uvrange        =         ''        #  uv range: ''==>all;
         uvrange
                                                 #   ='0~100klambda',
         default units=meters
              observation    =         ''        #  Select data based on
         observation ID:
                                                 #   ''==>all
         verbose             =       True
         listfile            =         ''        #  Name of disk file to
         write output: ''==>to
                                                 #   terminal
         listunfl            =      False        #  List unflagged row
         counts? If true, it can
                                                 #   have significant
         negative performance
                                                 #   impact.
         cachesize           =         50        #  EXPERIMENTAL.
         Maximum size in megabytes of
                                                 #   cache in which data
         structures can be
                                                 #   held.

       

      2) For CASA ouput, we have a different template "CASA output box" 

      .. container:: casa-output-box

         CASA <3>: go
         --------> go()
         Executing:  listobs()
         2017-01-04 20:23:45    WARN    listobs::utils::verify  
          Argument vis failed to verify.
         2017-01-04 20:23:45    SEVERE    listobs::::    An error
         occurred running task listobs.

       

      3) Alert Boxes. Alerts are quite frequent in the cookbook. To
      transfer those and in general to point out important issues,
      please use the "Alert Box" option in the "en.Insert template"
      tool, add "**Alert:**" in bold: 

      .. container:: alert-box

         Alert: This box is intended for alerts. Insert your text here.

       

      4) Information Boxes: They can be used if additional material is
      being pointed out that is not critical. Could be references to
      futher reading, references to the toolbok etc. Add "**Info:**" in
      bold when appropriate:

      .. container:: info-box

         Info: This box is intended for information. Insert your text
         here.

      5) Terminal/shell commands: 

      Use the "Terminal" template. It will create a grey box. Use
      againCourier New font. You can add "#In Terminal" if it helps
      distinguishing shell from CASA commands. 

       

      .. container:: terminal-box

         #In Terminal

         cd /lustre/datadisk

         #start casa 

         casa

       

      6) Some highlighting can also be obtained with
      the "Format"->"Formats"->"Block"->"Pre" setting. Note, however,
      that some formatting may be lost.

         p.callout - Inserts a grey highlight box. 

       

        

      .. rubric:: Paths
         :name: paths

      When creating paths between functions and pages on plonedocs, use
      Relative Paths rather than UIDs. This will alow paths to remain
      intact when versions of plonedocs are rolled over.   

       

      .. rubric:: Anchors
         :name: anchors

      If the anchor is to a section of the current page, then mark the
      relevant text, and open the link menu. Go to the anchor tab and
      select the section from the drop-down menu. An anchor can also be
      set anywhere with the "Anchor" template ("Insert->Insert
      Template->"Anchor". It will work just as figure and table
      captions, but not display any text. Once the "Anchor"  template is
      set and given a unique id, save the file and click on the link
      symbol at that location. The pop-up will reveal a unique link that
      can be used at the referring text. To avoid confusion, we again
      recommend an identifier naming scheme like
      "pagename-an-identifier' (where "an" stands for "anchor").

       

      .. rubric:: Links/URLS 
         :name: linksurls

      URLs shall be hidden in most cases and linked in the text
      appropriately. There are exceptions where the URL can be spelled
      out entirely (e.g. my.nrao.edu). Feel free to use the most
      appropriate way. 

      .. rubric::  
         :name: section-2

      .. rubric:: Footnotes 
         :name: footnotes

      Footnotes are not automatically numbered, so please take care
      about the numbering. First, insert a footnote marker template
      "Insert->Insert Template->Link to Footnote". Insert a
      footnotemarker that is unique for the given page.\ `[a] <#fn>`__  

      Then create the footnote itself. Insert a "Footnote" template
      ("Insert->Insert Template->Footnote") and a box will be created
      where the relevant footnotemarker can be specified as well as the
      footnote text. The footnote will automatically appear at the
      bottom of the document in a "Footnote(s)" section, in alphabetical
      order, independent of the location of this box.

       

      =============== ========================
      Footnote Number a
      Footnote Text   This is a footnote text.
      =============== ========================

       

      .. rubric::  
         :name: section-3

      .. rubric:: Citations/Bibliography
         :name: citationsbibliography

      Similar to footnotes, there are two templates for bibliography
      references. We recommend astronomy stle reference formats: 

      CASAdocs will apply regular astronomy citation style. 

      e.g. 

      for two-author papers:

      Pan & Doe (1999) `[1] <#cit>`__

      three-author papers:

      Pan, Doe, & Kern (2000) `[2] <#cit>`__

      more than three authors: 

      Pan et al. (2001) `[3] <#cit>`__

      If there are more than one paper per year with the same authors,
      they shall be appended with letters in the year, e.g. 2000a,
      2000b, 2000c.

      In parentheses the citations look like: 

      (Pan & Doe 1999) `[1] <#cit>`__

      more than one citation: 

      (Pan & Doe 1999; Pan et al. 2001) `[1] <#cit>`__  `[3] <#cit>`__

       

      After each citation, insert a "Link to Citation" template. Edit
      the template to the appropriate index number of the citation
      (remove the hashtag), as seen above. This will create an index
      that links to that number in the bibliography. After that, insert
      a "Citation" template. This template contains a Citation Number
      and Citation Text entry.  Match the Citation Number with the index
      number you listed in the "Link to Citation" template. In the
      Citation Text area, write the author(s) and year and create a
      hyperlink to ADS, arxiv, or elsewhere to the actual paper, if
      possible. (Look at this page in Edit mode if you need an explicit
      example). Using citation templates will automatically create a
      Bibiogrpy at the end the page, sorted by the citation id/number. 

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pan & Doe 1999, ApJ, 123, 666                     |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2017ApJ...834...39P>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 2                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pan, Doe, & Kern 2000, A&A, 99, L1                |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2016ApJ...817...72P>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 3                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pan et al., 2001, in "Happy Edits in CASAplone",  |
      |                 | eds. E. Hobble, Kluver, Dodrecht, p23             |
      |                 | (`arxiv <https://arxiv.org/abs/1601.07988>`__)    |
      +-----------------+---------------------------------------------------+

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/casa-development-team/documentation/insert-edit-image-button.png/@@images/04bf895f-1fd2-4c2f-856f-9e0f9296162e.png
   :class: image-right
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/casa-development-team/documentation/copy_of_casa-logo.png/@@images/3f140024-f7f0-45fc-b8ca-f1cd99e27f55.png
   :class: image-inline
   :width: 269px
   :height: 399px
