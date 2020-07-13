Parameters
==========

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file

Example

vis='ngc5921.ms'

.. container:: param

   .. container:: parameters2

      mode : string = summary

   Mode of operation for vishead

Allowed Value(s)

list summary get put

Example

To list the available keywords in a MeasurementSet:
vishead(vis='measurementset.ms',mode='list') To get a field name
(string), hdvalue=vishead(vis = '3C84C.ms', mode = 'get', hdkey =
'field', hdindex = '2'); print(hdvalue[0]) -> the name for field='2' To
get an phase center (number) hdvalue = vishead(vis = '3C84C.ms', mode =
'get', hdkey = 'ptcs', hdindex = '1'); hdvalue[0][0] gives the ra,
hdvalue[0][1] gives the dec in field '1' To change a string, vishead(vis
= '3C84C.ms', mode = 'put', hdkey = 'field', hdindex = '2', hdvalue =
'junk') field='2' is renamed 'junk'

.. container:: param

   .. container:: parameters2

      listitems : stringArray = telescope observer project field
      freq_group_name spw_name schedule schedule_type release_date

   Keyword items to list. This parameter is only relevant in list mode.
   Note that the default list is a subset of the possible keywords. To
   get all the keywords set listitems=[]

Example

listitems = ['field', 'ptcs']; see description for list of keywords

.. container:: param

   .. container:: parameters2

      hdkey : string

   Keyword to get/put

Example

hdkey='telescope'; see description for list of keywords

.. container:: param

   .. container:: parameters2

      hdindex : string

   Index (counting from 0) if keyword is an array (used in get/put mode
   only). The empty string means all elements

Example

hdindex='3'; see description for list of keywords

.. container:: param

   .. container:: parameters2

      hdvalue : undefined

   Value of the keywords to be put in the MS (used in put mode only)

Example

hdvalue=['VLA','BIMA']

.. container:: section
   :name: viewlet-below-content-body
