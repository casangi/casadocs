

# MS Metadata List/Change 

Using vishead

 

The **vishead** task is provided to access keyword information in the MeasurementSet. The default inputs are:

```
# vishead :: List, get, and put metadata in a MeasurementSet
vis = '' # Name of input visibility file
mode = 'list' # options: list, summary, get, put
listitems = [] # items to list ([] for all)
```

The *mode = 'summary'* option just gives the same output as **listobs**.

For *mode = 'list'* the default options are: *'telescope', 'observer', 'project', 'field', 'freq_group_name', 'spw_name', 'schedule', 'schedule_type', 'release_date'.* To obtain other options, put *mode = 'list'* and *listitems = \[\]*; see [vishead task pages](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_vishead) for a description of these additional options.

```
CASA <29>: vishead('ngc5921.demo.ms',mode='list',listitems=[])
  Out[29]:
{'cal_grp': (array([-1, -1, -1], dtype=int32), {}),
 'field': (array(['1331+30500002_0', '1445+09900002_0', 'N5921_2'],
      dtype='|S16'),
           {}),
 'fld_code': (array(['C', 'A', ''],
      dtype='|S2'), {}),
 'freq_group_name': (array(['none'],
      dtype='|S5'), {}),
 'log': ({'r1': False}, {}),
 'observer': (array(['TEST'],
      dtype='|S5'), {}),
 'project': (array([''],
      dtype='|S1'), {}),
 'ptcs': ({'r1': array([[[-2.74392758]],

       [[ 0.53248521]]]),
           'r2': array([[[-2.42044692]],

       [[ 0.17412604]]]),
           'r3': array([[[-2.26020138]],

       [[ 0.08843002]]])},
          {'MEASINFO': {'Ref': 'J2000', 'type': 'direction'},
           'QuantumUnits': array(['rad', 'rad'],
      dtype='|S4')}),
 'release_date': (array([  4.30444800e+09]),
                  {'MEASINFO': {'Ref': 'TAI', 'type': 'epoch'},
                   'QuantumUnits': array(['s'],
      dtype='|S2')}),
 'schedule': ({'r1': False}, {}),
 'schedule_type': (array([''],
      dtype='|S1'), {}),
 'source_name': (array(['1331+30500002_0', '1445+09900002_0', 'N5921_2'],
      dtype='|S16'),
                 {}),
 'spw_name': (array(['none'],
      dtype='|S5'), {}),
 'telescope': (array(['VLA'],
      dtype='|S4'), {})}
```

You can use *mode='get'* to retrieve the values of specific keywords, and likewise *mode='put'* to change them. The inputs are:

```
mode           =      'get'    #  options: list, summary, get, put
hdkey          =       ''      #  keyword to get/put
hdindex        =       ''      #  keyword index to get/put, counting from zero. ==>all
```

and

```
#  vishead :: List, summary, get, and put metadata in a MeasurementSet
mode           =      'put'    #  options: list, summary, get, put
hdkey          =         ''    #  keyword to get/put
hdindex        =         ''    #  keyword index to get/put, counting from zero. ==>all
hdvalue        =         ''    #  value of hdkey
```

For example, a common operation is to change the Telescope name (e.g. if it is unrecognized), e.g.

```
CASA <36>: vishead('ngc5921.demo.ms',mode='get',hdkey='telescope')
  Out[36]:
  (array(['VLA'],
      dtype='|S4'), {})

CASA <37>: vishead('ngc5921.demo.ms',mode='put',hdkey='telescope',hdvalue='JVLA')

CASA <38>: vishead('ngc5921.demo.ms',mode='get',hdkey='telescope')
  Out[38]:
  (array(['JVLA'],
      dtype='|S5'), {})
```

 

