buildmytasks
=============

How to create your own CASA tasks using the ``buildmytasks`` executable included alongside the casashell environment

.. warning:: This prescription for writing and incorporating tasks in CASA is for the power-user. This procedure may
   also change in future releases.

.. rubric:: The Basics

It is possible to write your own task and have it appear in CASA. For example, if you want to create a task named
**yourtask**, then must create two files, yourtask.xml and a task_yourtask.py. The *.*xml file is use to describe
the interface to the task and the task_yourtask.py does the actual work. The argument names must be the same in both
the yourtask.xml and task_yourtask.py file. The yourtask.xml file is used to generate all the interface files so
**yourtask** will appear in the CASA system. It is easiest to start from one of the existing tasks when constructing
these. You would make the name of the function in the yourtask.py be **yourtask** in this example.

We have provided the **buildmytasks** command in order to assemble your Python and XML into a loadable Python file.
The steps you need to execute (again for an example task
named "yourtask"):

1.  Create python code for task as task_yourtask.py
2.  Create XML for task as yourtask.xml
3.  Execute **buildmytasks**
4.  Import your new task into CASA

We will work through these steps now with the assumption that you already have your XML file and task implementation.
If you need to create these from scratch, the documentation below will provide help.

The first thing that you need to do is add the **bin** directory for CASA to your path: ::

   #Setup your environment for Linux
   -bash$ cd  casa-6.2.0-94/bin
   -bash$ PATH=`pwd`:$PATH

If your XML file is from CASA 5, then it needs to be updated for CASA 6: ::

   #Upgrading the XML in <your-development-path>
   -bash$ cd <your-development-path>
   -bash$ buildmytasks --upgrade yourtask.xml
   upgrading yourtask.xml
   -bash$ 

This step only needs to be done once. The old version is stored in **yourtask.xml.bak**. The update is done with an XML
processor which modifies the XML without changing the content. However, if you had large sections of comments you should
copy these from **yourtask.xml.bak** back into the updated **yourtask.xml** since these comments are not retained in the
conversion.

In CASA 6, **buildmytasks** generates tasks that are designed to be inside of a Python package. You should decide what you
want your package to be called, create it, and copy your XML file into it: ::

   #Create a package
   -bash$ mkdir -p yourpkg/private
   -bash$ cp yourtask.xml yourpkg
   -bash$ cp task_yourtask.py yourpkg/private
   -bash$ cd yourpkg

Now **buildmytask** can be used to create **yourtask** along with the code needed to support **inp**/**go**/etc: ::

   #Generate task
   -bash$ buildmytasks --module yourpkg yourtask.xml 
   generating task for yourtask.xml
   generating 'go task' for yourtask.xml
   -bash$

This adds **yourtask** to the **yourpkg** package, but you still have to export **yourtask** to allow it to be
accessible by users: ::

   #Export task
   -bash$ echo '__name__ = "yourpkg"' > __init__.py
   -bash$ echo '__all__ = [ "yourtask" ]' >> __init__.py
   -bash$ echo 'from .yourtask import yourtask' >> __init__.py

At this point, you should find a **yourtask.py** in the current directory and a **gotasks** subdirectory with
the **inp**/**go** implementation inside it. The commands we just executed created a minimal initialization file
for **yourpkg**, and we can now test our new task: ::

   #Test new task
   -bash$ cd ..
   -bash$ ls -p yourpkg
   gotasks/  yourtask.py  yourtask.xml  __init__.py  private/
   -bash$ casa
   CASA <1>: sys.path.insert(0,'.')
   CASA <2>: from yourpkg.gotasks.yourtask import yourtask
   CASA <3>: inp(yourtask)

This should display the help and inputs for **yourtask** inside CASA. Now you can set the parameters with **inp**,
reset the defaults with **default**, save and restore parameters with **tput** and **tget** and run the task with **go**.
The location of **yourpkg** must be in your **PYTHONPATH**; the first **CASA <1>** command added the current directory
to the path used for imports.

If you have other tasks, you can put their XML files in **yourpkg**. Generate the bindings with **buildmytasks**, and then
edit **__init__.py** to export any that you want the user to have available. 

.. rubric:: The XML file

The key to getting your task into CASA is constructing a task interface description XML file.

Some XML basics, an xml element begins with *\<element\>* and ends with *\</element\>*. If an XML element contains no
other XML element you may specify it via *\<element/\>*. An XML element may have zero or more attributes which are specified
by *attribute=\"attribute value\"*. You must put the attribute value in quotes,
i.e. *\<element myattribute=\"attribute value\"\>*.

All task xml files must start with this header information. ::


   <?xml version="1.0" encoding="UTF-8"?>
   <?xml-stylesheet type="text/xsl" ?>
   <casaxml xmlns="http://casa.nrao.edu/schema/psetTypes.html"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://casa.nrao.edu/schema/casa.xsd
   file:///opt/casa/code/xmlcasa/xml/casa.xsd">

and the file must have the end tag ::

   </casaxml>

Inside a *\<task\>* tags you will need to specify the following elements: ::

   <task>
     Attributes
         type required, allowed value is "function"
         name required
     Subelements
       shortdescription
         required
       description
         required
       input
         optional
       output
         optional
       returns
         optional
       constraints
        optional
   <shortdescription>
      - required by <task>; A short one-line description describing your task
     Attributes
        None
     Subelements
        None
   <description>
      - required] by <task>, Also used by <param>; A longer description describing your task with multiple lines
     Attributes
        None
     Subelements
        None
   <input>
      - optional element used by <task>; An input block specifies which parameters are used for input
     Attributes
        None
     Subelements
        <param> - optional
   <output> - optional
      An output element that contains a list of parameters that are "returned" by the task.
     Attributes
        None
     Subelements
        <param> - optional
   <returns> - optional
      Value returned by the task
     Attributes
        type
          optional; as specified in <param>
     Subelements
        <description> - optional
   <constraints> - optional
      A constraints element that lets you constrain params based on the values of other params.
     Attributes
        None
     Subelements
   <when> - required.
   <param> - optional
        The input and output elements consist of param elements.
     Attributes
        type
        - required; allowed values are record, variant, string int, double, bool, intArray, doubleArray, boolArray, stringArray
     name
        - required;
     subparam
        - optional; allowed values True, False, Yes or No.
     kind
        - optional;
     mustexist
        - optional; allowed values True, False, Yes or No.
        All param elements require name and type attributes.
     Subelements
   <description> - required;
   <value> - optional;
   <allowed> - optional;
   <value> - optional
        Value returned by the task
     Attributes
        type
        - required; as specified in <param> attributes.
     Subelements
        <value>
        - optional
   <allowed>
        - optional; Block of allowed values
     Attributes
        enum
        - required; maybe enum or range. If specified as enum only specific values are allowed If specified as range then the value tags may have min and max attributes.
     Subelements
        <value>
        - optional
   <when> - optional
        When blocks allow value specific handling for parameters
     Attributes
        param
        - required; Specifies special handling for a <param>
     Subelements
        <equals>
        - optional
   <notequals> - optional
   <equals> - optional
        Reset parameters if equal to the specified value
     Attributes
        value
        - required; the value of the parameter
     Subelements
        <default>
        - required
   <notequals> - optional
       Reset specified parameters if not equal to the specified value
     Attributes
        value
        - required; The value of the parameter
     Subelements
   <default> - optional
   <default> - optional
        Resets default values for specified parameters
     Attributes
        param
        - required; Name of the <param> to be reset.
     Subelements
        <value>
        - required, the revised value of the <param>.
        <example> - optional
        An example block, typically in python
     Attributes
       lang optional; specifies the language of the example, defaults to python.
     Subelements
       None


.. rubric:: The task yourtask.py file

You must write the python code that does the actual work. The ``task_*.py`` file function call sequence must be the
same as specified in the XML file. We may relax the requirement that the function call sequence exactly match the
sequence in the XML file in a future release.

