

.. _Description:

Description
   tool sakura description
   
   --CASA Developer--
   
   The **sakura** tool is intended to be an interface to functions
   that sakura library provide. Since, however, sakura functions are
   responsible for low level data processing such as interpolation,
   least-square fitting, etc., they are not exposed to CASA interface
   in general. Instead, they are used inside other tools such as
   **singledishms** and **calibrater**. Exceptions are two
   administrative methods, **initialize_sakura**
   and **cleanup_sakura**. The sakura library must be initialized
   before using any available functions. Also, it must be cleaned up
   finally. As name indicates, **initialize_sakura** and
   **cleanup_sakura** are responsible for those mandatory steps for
   sakura library. However, you don't need to worry about
   initializing and cleaning up sakura library. CASA properly manages
   sakura library using these methods during its startup and exit.
   
   It is not recommended that users interact with **sakura** tool
   explicitly. Manual use of **sakura** tool may cause unexpected
   error. For this reason, **sakura** tool is not available to the
   users by default. Users are able to create **sakura** tool by
   yourself but it is also not recommended.
   

.. _Examples:

Examples
   --CASA Developer--
   
   No example is provided since current version of **sakura** tool is
   not available to users in general.
   

.. _Development:

Development
   --CASA Developer--
   