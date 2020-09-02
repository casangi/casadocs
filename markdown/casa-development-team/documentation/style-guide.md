

# Style Guide 

 

  --------- -------------------------
  Type      Figure
  ID        , or placing it outside the $\$ ...\$$

delimiters to prevent it from rendering in MathJax.  

Equations can have captions as decribed [above](#captions-for-tables--figures--equations-etc-).

### Preventing LaTex/MathJax When it is not Wanted

Where more than one dollar sign is used in a block of text, MathJax may be triggered unintentionally.  To prevent this, a special HTML tag may be used.  Follow these steps:

1.  To edit HTML, change the drop-down menu below the editor window to \"text/x-web-textile\". 
2.  Find the dollar sign that is being interpreted as the beginning of the MathJax code. 
3.  Put that dollar sign into an HTML span block with class equal to \"tex2jax_ignore\":
    ```
    `<``span` `class``=``"tex2jax_ignore"``>$</``span``>`
    ```

Note that the span block can include more than just the dollar sign, and everything inside the span block will be excluded from MathJax interpretation.


# **CASA Formatting**

CASA tasks and tool (methods) are in bold font, parameters of task or tools in italics. For example. \"In **gaincal** set *caltable=\'table.cal\'* to define the output name of the calibration table.\" Similarly, use italics when referring to table columns, like *CORRECTED_DATA*. 

Known task names will be automatically rendered by Plone, creating links to the task/tool description. This is based on a table of known tasks. If a task is not recognized, please submit a JIRA ticket to Bjorn to have it added to the list of known tasks. We maintain a list of tasks that are auto-linked and ones that are not. For instance, the task **find** is not linked (as it appears a lot in regular text).

Shell commands will be formatted with \"Courier New\" and in italics, e.g. \"*ls -rt*\".

Python code will be written in \"Courier New\" (regular font/no italics) \"listobs(vis=\'test.ms\')\".

<div class="alert alert-warning">
**NOTICE:** With the change in layout for CASA 5.5, auto-linking does no longer work. Please do continue to mark each task or tool in boldface when mentioned on a page.
</div>

 Other writing conventions:

-   If you want to place an emphasis on a text, italics are acceptable. Other options could be underline text to distinguish from parameters. And don\'t forget that there are boxes as explained in the next paragraph. 
-   Names of books, organizations, space-based telescopes should be italicized.
-   Use "Formats" → "Block" →  "Blockquote" for long quotes or indented paragraphs.
-   Strikethroughs may be used to indicate the omission of text, while still leaving the omitted text available to view.

 

# CASA Naming Convention

if possible use the following spelling conventions throughout the document:

MeasurementSetMulti-MSSub-MSMSMMS

 

 

# **Tags and Paths**

## General Tags and Alert Boxes {#general-tags-and-alert-boxes 

We have a number of different pre-defined boxes. 

1\) For CASA inputs, please use the approriate \"CASA input box\" from the \"en.Insert template\" button (looks like a shelf): 

```
This box is intended for CASA Inputs. Insert your text here.
```

interface listings will also go into a CASA input box. The CASA input and output boxes shall be formatted in fixed width font. To do so, mark the text and select \"Font Family-\>Courier New\". For clarification, The text could start with \'\#In CASA\": 

```
#In CASA
CASA<1>: inp listobs
--------> inp(listobs)
#listobs :: List the summary of a data set in the logger or in a file
vis                 =         ''        #Name of input visibility file (MS)
selectdata          =       True        #Data selection parameters
     field          =         ''        #Field names or field index numbers:
                                        #''==>all, field='0~2,3C286'
     spw            =         ''        #spectral-window/frequency/channel
     antenna        =         ''        #antenna/baselines: ''==>all, antenna
                                        #='3,VA04'
     timerange      =         ''        #time range:
                                        #''==>all,timerange='09:14:0~09:54:0'
     correlation    =         ''        #Select data based on correlation
     scan           =         ''        #scan numbers: ''==>all
     intent         =         ''        #Select data based on observation intent:
                                        #''==>all
     feed           =         ''        #multi-feed numbers: Not yet implemented
     array          =         ''        #(sub)array numbers: ''==>all
     uvrange        =         ''        #uv range: ''==>all; uvrange
                                        #='0~100klambda', default units=meters
     observation    =         ''        #Select data based on observation ID:
                                        #''==>all

verbose             =       True
listfile            =         ''        #Name of disk file to write output: ''==>to
                                        #terminal
listunfl            =      False        #List unflagged row counts? If true, it can
                                        #have significant negative performance
                                        #impact.
cachesize           =         50        #EXPERIMENTAL. Maximum size in megabytes of
                                        #cache in which data structures can be
                                        #held.
```

 

2\) For CASA ouput, we have a different template \"CASA output box\" 

```python
CASA <3>: go
--------> go()
Executing:  listobs()

2017-01-04 20:23:45    WARN    listobs::utils::verify    Argument vis failed to verify.
2017-01-04 20:23:45    SEVERE    listobs```:    An error occurred running task listobs.

 

3\) Alert Boxes. Alerts are quite frequent in the cookbook. To transfer those and in general to point out important issues, please use the \"Alert Box\" option in the \"en.Insert template\" tool, add \"**Alert:**\" in bold: 

<div class="alert alert-warning">
**Alert:** This box is intended for alerts. Insert your text here.
</div>

 

4\) Information Boxes: They can be used if additional material is being pointed out that is not critical. Could be references to futher reading, references to the toolbok etc. Add \"**Info:**\" in bold when appropriate:

<div class="alert alert-info">
**Info:** This box is intended for information. Insert your text here.
</div>

5\) Terminal/shell commands: 

Use the \"Terminal\" template. It will create a grey box. Use again Courier New font. You can add \"\#In Terminal\" if it helps distinguishing shell from CASA commands. 

 

```
#In Terminal 

cd /lustre/datadisk

#start casa 

casa
```

 

6\) Some highlighting can also be obtained with the \"Format\"-\>\"Formats\"-\>\"Block\"-\>\"Pre\" setting. Note, however, that some formatting may be lost.

> p.callout - Inserts a grey highlight box. 

 

  

# Paths

When creating paths between functions and pages on plonedocs, use Relative Paths rather than UIDs. This will alow paths to remain intact when versions of plonedocs are rolled over.   

 

# Anchors

If the anchor is to a section of the current page, then mark the relevant text, and open the link menu. Go to the anchor tab and select the section from the drop-down menu. An anchor can also be set anywhere with the \"Anchor\" template (\"Insert-\>Insert Template-\>\"Anchor\". It will work just as figure and table captions, but not display any text. Once the \"Anchor\"  template is set and given a unique id, save the file and click on the link symbol at that location. The pop-up will reveal a unique link that can be used at the referring text. To avoid confusion, we again recommend an identifier naming scheme like \"pagename-an-identifier\' (where \"an\" stands for \"anchor\").

 

# Links/URLS 

URLs shall be hidden in most cases and linked in the text appropriately. There are exceptions where the URL can be spelled out entirely (e.g. my.nrao.edu). Feel free to use the most appropriate way. 


# Footnotes 

Footnotes are not automatically numbered, so please take care about the numbering. First, insert a footnote marker template \"Insert-\>Insert Template-\>Link to Footnote\". Insert a footnotemarker that is unique for the given page.^[\[a\]](#fna)^  

Then create the footnote itself. Insert a \"Footnote\" template (\"Insert-\>Insert Template-\>Footnote\") and a box will be created where the relevant footnotemarker can be specified as well as the footnote text. The footnote will automatically appear at the bottom of the document in a \"Footnote(s)\" section, in alphabetical order, independent of the location of this box.

 

 


# Citations/Bibliography

Similar to footnotes, there are two templates for bibliography references. We recommend astronomy stle reference formats: 

CASAdocs will apply regular astronomy citation style. 

e.g. 

for two-author papers:

Pan & Doe (1999) [\[1\]](#Bibliography)

three-author papers:

Pan, Doe, & Kern (2000) [\[2\]](#Bibliography)

more than three authors: 

Pan et al. (2001) [\[3\]](#Bibliography)

If there are more than one paper per year with the same authors, they shall be appended with letters in the year, e.g. 2000a, 2000b, 2000c.

In parentheses the citations look like: 

(Pan & Doe 1999) [\[1\]](#Bibliography)

more than one citation: 

(Pan & Doe 1999; Pan et al. 2001) [\[1\]](#Bibliography)  [\[3\]](#Bibliography)

 

After each citation, insert a \"Link to Citation\" template. Edit the template to the appropriate index number of the citation (remove the hashtag), as seen above. This will create an index that links to that number in the bibliography. After that, insert a \"Citation\" template. This template contains a Citation Number and Citation Text entry.  Match the Citation Number with the index number you listed in the \"Link to Citation\" template. In the Citation Text area, write the author(s) and year and create a hyperlink to ADS, arxiv, or elsewhere to the actual paper, if possible. (Look at this page in Edit mode if you need an explicit example). Using citation templates will automatically create a Bibiogrpy at the end the page, sorted by the citation id/number. 

# Bibliography

1. Pan\ &\ Doe\ 1999,\ ApJ,\ 123,\ 666\ (
2. Pan,\ Doe,\ &\ Kern\ 2000,\ A&A,\ 99,\ L1\ (
3. Pan\ et\ al.,\ 2001,\ in\ \"Happy\ Edits\ in\ CASAplone\",\ eds.\ E.\ Hobble,\ Kluver,\ Dodrecht,\ p23\ (
^

Footnote(s)

<div>

^a.\ This\ is\ a\ footnote\ text.\ [↩](#refa "Jump back to footnote a in the text.")^

</div>

