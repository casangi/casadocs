Methods
=======

.. container:: documentDescription description

   task applycal parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-methods

          

         .. container:: param

            constructor **sakura**

            .. container:: collcontent

               .. container:: methoddesc

                  This is used to construct an {\tt sakura} tool.

               .. container:: methodsection

                  Parameters : None

               .. container:: methodsection

                  Example

               .. container:: methodexam

                  Manual tool construction is done this way: ssd =
                  casac.sakura()

         .. container:: param

            function **initialize_sakura**

            .. container:: collcontent

               .. container:: methoddesc

                  This function returns True/False based on an result of
                  initialize

               .. container:: methodsection

                  Parameters

               .. container:: parameters2

                  level : undefined = WARN

               .. container:: methodparmtable

                  Log level.

Allowed Value(s)

WARN ERROR INFO DEBUG

.. container:: methodsection

   Example

.. container:: methodexam

   ssd.initialize_sakura("WARN")

.. container:: param

   function **cleanup_sakura**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns True/False based on an result of finalize

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         ssd.cleanup_sakura()

.. container:: section
   :name: viewlet-below-content-body
