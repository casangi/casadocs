

.. _Returns:

Returns
   out (dict) - keyword value, when mode='get'. Image metainformation
   when mode='summary'. Supported keywords when mode='list'


.. _Description:

Description
   imhead task: List, get and put image header parameters.
   
   This task allows the user to manipulate metadata associated with a
   CASA image. Both float and complex valued images are fully
   supported.
   
   .. note:: NOTE: For measurement sets, the task vishead should be used.
   
    The supported mode values are:
   
   +---------+-----------------------------------------------------------+
   | Values  |  **Description**                                          |
   +---------+-----------------------------------------------------------+
   | add     | Add a new metadata value to the image.                    |
   +---------+-----------------------------------------------------------+
   | del     | Delete a key or reset its value to a fiducial value if    |
   |         | possible. Ignores *hdvalue* parameter.                    |
   +---------+-----------------------------------------------------------+
   | get     | Return the specified keyword value. Ignores the *hdvalue* |
   |         | parameter.                                                |
   +---------+-----------------------------------------------------------+
   | history | Log image history. Ignores the *hdkey* and *hdvalue*      |
   |         | parameters.                                               |
   +---------+-----------------------------------------------------------+
   | list    | Show supported keywords and their values. Ignores the     |
   |         | *hdkey* and *hdvalue* parameters.                         |
   +---------+-----------------------------------------------------------+
   | put     | Modify the value associated with the keyword using the    |
   |         | specified value.                                          |
   +---------+-----------------------------------------------------------+
   | summary | Log a summary of the image and return a dictionary of     |
   |         | various metadata values. Ignores the *hdkey* and          |
   |         | *hdvalue* parameters.                                     |
   +---------+-----------------------------------------------------------+
   
   See below for details about how these modes act for specific
   keywords.
   
   .. warning:: ALERT: Only limited checking is implemented to ensure modifying
      a specific value will leave the image metadata in a consistent
      state, so, if one is not careful, one could end up with an
      image that has an inconsistent set of metadata and is
      therefore, nonsensical and useless.
   
      That is, PROCEED AT YOUR OWN RISK when using modes add, del, or
      put.
   
   .. rubric:: Notes for *mode='list'*
   
   Supported keywords that can be listed with parameter 'hdkey' when
   using mode='list':
   
   +-------------------+-------------------------------------------------+
   | **Values**        | Description                                     |
   +===================+=================================================+
   | beammajor or bmaj | Major axis of the clean beam.                   |
   +-------------------+-------------------------------------------------+
   | beamminor or bmin | Minor axis of the clean beam.                   |
   +-------------------+-------------------------------------------------+
   | beampa or bpa     | Position angle of the clean beam. **NOTE**: If  |
   |                   | the image contains multiple beams, use          |
   |                   | *mode='summary'* to list them with              |
   |                   | *verbose=True*.                                 |
   +-------------------+-------------------------------------------------+
   | bunit             | Image units (K, Jy/beam, etc).                  |
   +-------------------+-------------------------------------------------+
   | cdelt *n*         | Pixel size, *n* th axis. *n* is one-based.      |
   +-------------------+-------------------------------------------------+
   | crpix *n*         | The pixel designated as the reference location, |
   |                   | *n* th axis *n* is one-based.                   |
   +-------------------+-------------------------------------------------+
   | crval *n*         | World coordinate value of the reference pixel   |
   |                   | for the *n* th axis. *n* is one-based.          |
   +-------------------+-------------------------------------------------+
   | ctype *n*         | Name of *n* th axis. *n* is one-based.          |
   +-------------------+-------------------------------------------------+
   | cunit *n*         | Units of *n* th axis. *n* is one based.         |
   +-------------------+-------------------------------------------------+
   | datamax           | Maximum pixel value.                            |
   +-------------------+-------------------------------------------------+
   | datamin           | Minimum pixel value.                            |
   +-------------------+-------------------------------------------------+
   | date-obs          | Date (epoch) of the observation.                |
   +-------------------+-------------------------------------------------+
   | equinox           | Direction reference frame.                      |
   +-------------------+-------------------------------------------------+
   | imtype            | Image type (e.g. Intensity).                    |
   +-------------------+-------------------------------------------------+
   | minpos            | World coordinate position of minimum pixel      |
   |                   | value.                                          |
   +-------------------+-------------------------------------------------+
   | minpixpos         | Pixel coordinate position of minimum pixel      |
   |                   | value.                                          |
   +-------------------+-------------------------------------------------+
   | maxpos            | World coordinate position of maximum pixel      |
   |                   | value.                                          |
   +-------------------+-------------------------------------------------+
   | maxpixpos         | Pixel coordinate position of maximum pixel      |
   |                   | value.                                          |
   +-------------------+-------------------------------------------------+
   | object            | Source name.                                    |
   +-------------------+-------------------------------------------------+
   | observer          | Observer name.                                  |
   +-------------------+-------------------------------------------------+
   | projection        | Direction coordinate projection (e.g.           |
   |                   | 'SIN','TAN', or 'ZEA').                         |
   +-------------------+-------------------------------------------------+
   | reffreqtype       | Spectral reference frame.                       |
   +-------------------+-------------------------------------------------+
   | restfreq          | Rest Frequency.                                 |
   +-------------------+-------------------------------------------------+
   | shape             | Number of pixels along each axis.               |
   +-------------------+-------------------------------------------------+
   | telescope         | Telescope name.                                 |
   +-------------------+-------------------------------------------------+
   
   .. rubric:: Notes for *mode='add'*
   
   The behavior of *mode='add'* depends on the keyword that the user
   specifies under 'hdkey'. Below is a summary of the per keyword
   behavior of this mode. In general, the return value will be True
   if the operation succeeds, or False if it fails or is not
   supported. If unsuccessful or not supported, a message is normally
   logged which describes the failure. In most cases, you probably
   want to use *mode='put'* rather than *mode='add'*. We continue to
   support *mode='add'* mainly for backward compatibility.
   
   +--------------------------+------------------------------------------+
   | **Values**               | Description                              |
   +==========================+==========================================+
   | beammajor or bmaj        | If image has no beam(s), a single,       |
   |                          | global, circular beam of diameter        |
   |                          | specified in *hdvalue* is added.         |
   |                          | *hdvalue* must be a valid angular        |
   |                          | quantity (string or dictionary) or the   |
   |                          | operation will fail and False will be    |
   |                          | returned. If the image has a beam(s),    |
   |                          | the operation fails and False is         |
   |                          | returned. Examples of acceptable values  |
   |                          | of *hdvalue* are "4arcsec",              |
   |                          | **qa.quantity** ("4arcsec"), {'unit':    |
   |                          | 'arcsec', 'value': 4.0}. If you wish an  |
   |                          | image to have multiple beams, use        |
   |                          | **ia.setrestoringbeam** ().              |
   +--------------------------+------------------------------------------+
   | beamminor or bmin        | Behavior is the same as that for         |
   |                          | beammajor or bmaj.                       |
   +--------------------------+------------------------------------------+
   | beampa or bpa            | Operation has no effect and always       |
   |                          | returns False. If you wish to add a      |
   |                          | beam, use beammajor, bmaj, beamminor, or |
   |                          | bmin.                                    |
   +--------------------------+------------------------------------------+
   | bunit                    | If image has no brightness unit, add the |
   |                          | value specified in *hdvalue* which must  |
   |                          | be a unit supported by CASA. Else do     |
   |                          | nothing and return False.                |
   +--------------------------+------------------------------------------+
   | cdelt\*                  | No effect. Addition of coordinate system |
   |                          | parameters is not supported. Always      |
   |                          | returns False. Use the **cs** tool to    |
   |                          | add coordinates.                         |
   +--------------------------+------------------------------------------+
   | crpix\*                  | No effect. Addition of coordinate system |
   |                          | parameters is not supported. Always      |
   |                          | returns False. Use the **cs** tool to    |
   |                          | add coordinates.                         |
   +--------------------------+------------------------------------------+
   | crval\*                  | No effect. Addition of coordinate system |
   |                          | parameters is not supported. Always      |
   |                          | returns False. Use the **cs** tool to    |
   |                          | add coordinates.                         |
   +--------------------------+------------------------------------------+
   | ctype\*                  | No effect. Addition of coordinate system |
   |                          | parameters is not supported. Always      |
   |                          | returns False. Use the **cs** tool to    |
   |                          | add coordinates.                         |
   +--------------------------+------------------------------------------+
   | cunit\*                  | No effect. Addition of coordinate system |
   |                          | parameters is not supported. Always      |
   |                          | returns False. Use the **cs** tool to    |
   |                          | add coordinates.                         |
   +--------------------------+------------------------------------------+
   | datamax                  | No effect. Addition of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | datamin                  | No effect. Addition of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | date-obs or epoch        | No effect.                               |
   +--------------------------+------------------------------------------+
   | equinox                  | No effect.                               |
   +--------------------------+------------------------------------------+
   | imtype                   | If image type does not exist, add the    |
   |                          | type specified in *hdvalue*. *hdvalue*   |
   |                          | must be one of "Undefined", "Intensity", |
   |                          | "Beam", "Column Density",                |
   |                          | "Depolarization Ratio", "Kinetic         |
   |                          | Temperature", "Magnetic Field", "Optical |
   |                          | Depth", "Rotation Measure", "Rotational  |
   |                          | Temperature", "Spectral                  |
   |                          | Index","Velocity", or "Velocity          |
   |                          | Dispersion".                             |
   +--------------------------+------------------------------------------+
   | masks                    | No effect. Addition of masks is not      |
   |                          | supported. Use **ia.calcmask** ().       |
   +--------------------------+------------------------------------------+
   | maxpos                   | No effect. Addition of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | maxpixpos                | No effect. Addition of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | minpos                   | No effect. Addition of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | minpixpos                | No effect. Addition of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | object                   | If image has no object, add the value    |
   |                          | specified in *hdvalue*. Else do nothing  |
   |                          | and return False.                        |
   +--------------------------+------------------------------------------+
   | observer                 | If image has no observer, add the value  |
   |                          | specified in *hdvalue*. Else do nothing  |
   |                          | and return False.                        |
   +--------------------------+------------------------------------------+
   | projection               | No effect.                               |
   +--------------------------+------------------------------------------+
   | reffreqtype              | No effect.                               |
   +--------------------------+------------------------------------------+
   | restfreq                 | If image has a spectral coordinate and   |
   |                          | no rest frequency, set the rest          |
   |                          | frequency to the value specified in      |
   |                          | *hdvalue*. This value must be a valid    |
   |                          | CASA quantity with frequency units. Else |
   |                          | do nothing and return False. Examples of |
   |                          | valid values are "1GHz",                 |
   |                          | **qa.quantity** ("1GHz"), {'unit':       |
   |                          | 'GHz', 'value': 1.0}.                    |
   +--------------------------+------------------------------------------+
   | shape                    | No effect.                               |
   +--------------------------+------------------------------------------+
   | telescope                | If image has no telescope, add the value |
   |                          | specified in *hdvalue*. Else do nothing  |
   |                          | and return False.                        |
   +--------------------------+------------------------------------------+
   | any user defined keyword | Add the key-value pair if the key does   |
   |                          | not exist. Else do nothing and return    |
   |                          | False.                                   |
   +--------------------------+------------------------------------------+
   
   .. rubric:: Notes for *mode='del'*
   
   The behavior of *mode='del'* depends on the keyword that the user
   specifies under 'hdkey'. Below is a summary of the per keyword
   behavior of this mode. In general, the return value will be True
   if the operation succeeds, or False if it fails or is not
   supported. If unsuccessful or not supported, a warning message is
   normally logged which describes the failure.
   
   +--------------------------+------------------------------------------+
   | **Values**               |  **Description**                         |
   +--------------------------+------------------------------------------+
   | beammajor or bmaj        | Deletes all beams. Returns False if the  |
   |                          | image has no beams.                      |
   +--------------------------+------------------------------------------+
   | beamminor or bmin        | Deletes all beams. Returns False if the  |
   |                          | image has no beams.                      |
   +--------------------------+------------------------------------------+
   | beampa or bpa            | Deletes all beams. Returns False if the  |
   |                          | image has no beams.                      |
   +--------------------------+------------------------------------------+
   | bunit                    | Sets the associated value to the empty   |
   |                          | string.                                  |
   +--------------------------+------------------------------------------+
   | cdelt\*                  | No effect. Deletion of coordinate system |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | crpix\*                  | No effect. Deletion of coordinate system |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | crval\*                  | No effect. Deletion of coordinate system |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | ctype\*                  | No effect. Deletion of coordinate system |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | cunit\*                  | No effect. Deletion of coordinate system |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | datamax                  | No effect. Deletion of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | datamin                  | No effect. Deletion of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | date-obs or epoch        | No effect.                               |
   +--------------------------+------------------------------------------+
   | equinox                  | No effect.                               |
   +--------------------------+------------------------------------------+
   | imtype                   | No effect.                               |
   +--------------------------+------------------------------------------+
   | masks                    | Deletes the single mask specified in     |
   |                          | *hdvalue*, or if *hdvalue=''*, deletes   |
   |                          | all masks.                               |
   +--------------------------+------------------------------------------+
   | maxpos                   | No effect. Deletion of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | maxpixpos                | No effect. Deletion of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | minpos                   | No effect. Deletion of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | minpixpos                | No effect. Deletion of statistical       |
   |                          | parameters is not supported.             |
   +--------------------------+------------------------------------------+
   | object                   | Sets the associated value to an empty    |
   |                          | string.                                  |
   +--------------------------+------------------------------------------+
   | observer                 | Sets the associated value to an empty    |
   |                          | string.                                  |
   +--------------------------+------------------------------------------+
   | projection               | No effect.                               |
   +--------------------------+------------------------------------------+
   | reffreqtype              | No effect.                               |
   +--------------------------+------------------------------------------+
   | restfreq                 | No effect.                               |
   +--------------------------+------------------------------------------+
   | shape                    | No effect.                               |
   +--------------------------+------------------------------------------+
   | telescope                | Sets the associated value to an empty    |
   |                          | string.                                  |
   +--------------------------+------------------------------------------+
   | any user defined keyword | Deletes the key-value pair.              |
   +--------------------------+------------------------------------------+

   
   .. rubric:: Notes for *mode='get'*
   
   The data type of the value returned by **imhead** when
   *mode='get'* depends on the keyword that the user specifies under
   'hdkey'. Below is a list of keywords on the data type that will be
   returned when *mode='get'* for each. A "quantity dictionary" is a
   dictionary with 'value' and 'unit' keys that can be used as input
   to various methods of the **qa** tool.
   
   +-------------------------+-------------------------------------------+
   | **Values**              |  **Description**                          |
   +-------------------------+-------------------------------------------+
   | beammajor or bmaj       | Returns quantity dictionary.              |
   +-------------------------+-------------------------------------------+
   | beamminor or bmin       | Returns quantity dictionary.              |
   +-------------------------+-------------------------------------------+
   | beampa or bpa           | Returns quantity dictionary.              |
   +-------------------------+-------------------------------------------+
   | bunit                   | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | cdelt\*                 | Returns quantity dictionary.              |
   +-------------------------+-------------------------------------------+
   | crpix\*                 | Returns float.                            |
   +-------------------------+-------------------------------------------+
   | crval\*                 | Returns quantity dictionary, unless the   |
   |                         | value for the stokes axis is requested,   |
   |                         | in which case an array of strings is      |
   |                         | returned.                                 |
   +-------------------------+-------------------------------------------+
   | ctype\*                 | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | cunit\*                 | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | datamax                 | Returns image pixel data type.            |
   +-------------------------+-------------------------------------------+
   | datamin                 | Returns image pixel data type.            |
   +-------------------------+-------------------------------------------+
   | date-obs or epoch       | Returns string (in YYYY/MM/DD/hh:mm:ss    |
   |                         | format).                                  |
   +-------------------------+-------------------------------------------+
   | equinox                 | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | imtype                  | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | masks                   | Returns string array.                     |
   +-------------------------+-------------------------------------------+
   | maxpos                  | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | maxpixpos               | Returns integer array.                    |
   +-------------------------+-------------------------------------------+
   | minpos                  | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | minpixpos               | Returns integer array.                    |
   +-------------------------+-------------------------------------------+
   | object                  | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | observer                | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | projection              | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | reffreqtype             | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | restfreq                | Returns quantity dictionary.              |
   +-------------------------+-------------------------------------------+
   | shape                   | Returns integer array.                    |
   +-------------------------+-------------------------------------------+
   | telescope               | Returns string.                           |
   +-------------------------+-------------------------------------------+
   | any user defined keword | Returns string.                           |
   +-------------------------+-------------------------------------------+

   
   .. rubric:: Notes for *mode='put'*
   
   In general, *mode='put'* will modify the specified key to the
   specified value that the user specifies under 'hdkey'. True is
   returned if the metadatum was successfully modified, False
   otherwise. Normally, a diagnostic message is logged if there is a
   failure. Only the parameter specified is modified; e.g., no
   modification of reference direction occurs to implicitly account
   for precession to a new reference frame. The following are the
   exceptional cases for *mode='put'*.
   
   +--------------------------+------------------------------------------+
   | **Values**               |  **Description**                         |
   +--------------------------+------------------------------------------+
   | beammajor or bmaj        | Will always fail if image has multiple   |
   |                          | beams. Use **ia.setrestoringbeam** ()    |
   |                          | in this case. If image has no beam(s), a |
   |                          | single, global, circular beam of         |
   |                          | diameter specified in *hdvalue* is       |
   |                          | added. *hdvalue* must be a valid angular |
   |                          | quantity (string or dictionary) or the   |
   |                          | operation will fail and False will be    |
   |                          | returned. If the image has a single      |
   |                          | beam, the value of the major axis will   |
   |                          | be modified, unless the specified value  |
   |                          | is smaller than the minor axis of the    |
   |                          | existing beam, in which case nothing is  |
   |                          | modified and False is returned. Examples |
   |                          | of acceptable values of *hdvalue* are    |
   |                          | "4arcsec", **qa.quantity** ("4arcsec"),  |
   |                          | {'unit': 'arcsec', 'value': 4.0}.        |
   +--------------------------+------------------------------------------+
   | beamminor or bmin        | Behavior is the same as that for bmaj,   |
   |                          | although of course if the image already  |
   |                          | has a single beam, the specified value   |
   |                          | must be less than the existing major     |
   |                          | axis value, or nothing is modified and   |
   |                          | False is returned.                       |
   +--------------------------+------------------------------------------+
   | beampa or bpa            | If the image does not already have a     |
   |                          | single beam, nothing is modified and     |
   |                          | False is returned. Angular units are     |
   |                          | required.                                |
   +--------------------------+------------------------------------------+
   | bunit                    | Fails if *hdvalue* is not a supported    |
   |                          | CASA unit.                               |
   +--------------------------+------------------------------------------+
   | cdelt *n*                | One-based axis *n* must be less than or  |
   |                          | equal to the number of axes in the       |
   |                          | image. *hdvalue* type must be a number   |
   |                          | (in which case the unit of the           |
   |                          | corresponding axis is assumed) or a      |
   |                          | quantity (string or dictionary). If a    |
   |                          | quantity, the unit must conform to the   |
   |                          | existing axis unit.                      |
   +--------------------------+------------------------------------------+
   | crpix *n*                | One-based axis *n* must be less than or  |
   |                          | equal to the number of axes in the       |
   |                          | image. *hdvalue* type must be a number.  |
   |                          | Will fail if the polarization axis is    |
   |                          | specified.                               |
   +--------------------------+------------------------------------------+
   | crval *n*                | One-based axis *n* must be less than or  |
   |                          | equal to the number of axes in the       |
   |                          | image. If not the polarization/stokes    |
   |                          | axis, *hdvalue* type must be a number    |
   |                          | (in which case the unit of the           |
   |                          | corresponding axis is assumed), a        |
   |                          | quantity (string or dictionary), or a    |
   |                          | valid measurement format (such as a      |
   |                          | sexagesimal direction axis specification |
   |                          | for an axis with angular units). If a    |
   |                          | quantity, the unit must conform to the   |
   |                          | existing axis unit. If the               |
   |                          | stokes/polarization axis, one must       |
   |                          | provide an array of stokes/polarization  |
   |                          | strings (e.g., ["I", "Q", "XX"]) that is |
   |                          | the same length as the stokes axis. If   |
   |                          | the stokes axis is degenerate, one can   |
   |                          | alternatively provide a string           |
   |                          | indicating the stokes value (e.g. "U").  |
   +--------------------------+------------------------------------------+
   | ctype *n*                | One-based axis *n* must be less than or  |
   |                          | equal to the number of axes in the       |
   |                          | image. *hdvalue* type must be a string.  |
   +--------------------------+------------------------------------------+
   | cunit *n*                | One-based axis *n* must be less than or  |
   |                          | equal to the number of axes in the       |
   |                          | image. Specified unit must conform to    |
   |                          | the existing axis unit. Will fail if     |
   |                          | stokes/polarization axis is specified.   |
   +--------------------------+------------------------------------------+
   | datamax                  | This cannot be modified. False is always |
   |                          | returned.                                |
   +--------------------------+------------------------------------------+
   | datamin                  | This cannot be modified. False is always |
   |                          | returned.                                |
   +--------------------------+------------------------------------------+
   | date-obs or epoch        | A valid time specification must be       |
   |                          | given.                                   |
   +--------------------------+------------------------------------------+
   | equinox                  | A valid direction reference frame        |
   |                          | specification string must be given.      |
   +--------------------------+------------------------------------------+
   | imtype                   | A CASA-supported image type string must  |
   |                          | be given or the image type will be set   |
   |                          | to 'Intensity'.                          |
   +--------------------------+------------------------------------------+
   | masks                    | Masks may not be modified. False is      |
   |                          | always returned.                         |
   +--------------------------+------------------------------------------+
   | maxpos                   | This cannot be modified.                 |
   +--------------------------+------------------------------------------+
   | maxpixpos                | This cannot be modified.                 |
   +--------------------------+------------------------------------------+
   | minpos                   | This cannot be modified.                 |
   +--------------------------+------------------------------------------+
   | minpixpos                | This cannot be modified.                 |
   +--------------------------+------------------------------------------+
   | object                   | *hdvalue* must be a string.              |
   +--------------------------+------------------------------------------+
   | projection               | *hdvalue* must be a string representing  |
   |                          | a supported CASA projection              |
   |                          | specification.                           |
   +--------------------------+------------------------------------------+
   | reffreqtype              | *hdvalue* must be a string representing  |
   |                          | a supported CASA velocity reference      |
   |                          | frame specification.                     |
   +--------------------------+------------------------------------------+
   | restfreq                 | *hdvalue* can be a number (in which case |
   |                          | frequency axis units are assumed) or a   |
   |                          | valid quantity string or quantity        |
   |                          | dictionary in which case the unit must   |
   |                          | conform to Hz. Only the active rest      |
   |                          | frequency may be modified. The spectral  |
   |                          | coordinate can hold several rest         |
   |                          | frequencies (e.g., to handle an          |
   |                          | observations where the band covers many  |
   |                          | lines), but only one is active (for      |
   |                          | velocity conversion) at any time. For    |
   |                          | more functionality, please use           |
   |                          | **cs.setrestfrequency** ().              |
   +--------------------------+------------------------------------------+
   | shape                    | This cannot be modified.                 |
   +--------------------------+------------------------------------------+
   | telescope                | *hdvalue* must be a string.              |
   +--------------------------+------------------------------------------+
   | any user defined keyword | *hdvalue* can be practically any         |
   |                          | supported input parameter type.          |
   +--------------------------+------------------------------------------+

   
   .. rubric:: Notes for *mode='summary'*
   
   If *mode='summary'*, various metadata will be listed to the
   logger, and a dictionary containing some metadata will be
   returned. The key/value pairs in the returned dicitonary will be:
   
   +---------------+-----------------------------------------------------+
   | **Values**    |  **Description**                                    |
   +---------------+-----------------------------------------------------+
   | axisnames     | Array of image axes names.                          |
   +---------------+-----------------------------------------------------+
   | axisunits     | Array of image axes units.                          |
   +---------------+-----------------------------------------------------+
   | defaultmask   | name of the default mask. The empty string          |
   |               | indicates the image has no default mask.            |
   +---------------+-----------------------------------------------------+
   | hasmask       | Boolean value indicating if the image has a mask.   |
   +---------------+-----------------------------------------------------+
   | imagetype     | String describing what the image pixels represent.  |
   |               | Possible values are: *'Intensity', 'Beam', 'Column  |
   |               | Density', 'Depolarization Ratio', 'Kinetic          |
   |               | Temperature', 'Magnetic Field', 'Optical Depth',    |
   |               | 'Rotation Measure', 'Rotation Temperature',         |
   |               | 'Spectral Index', 'Velocity', 'Velocity             |
   |               | Dispersion', and 'Undefined'*.                      |
   +---------------+-----------------------------------------------------+
   | incr          | Array of axes increments, in axes units.            |
   +---------------+-----------------------------------------------------+
   | masks         | Array of all mask names associated with the image.  |
   +---------------+-----------------------------------------------------+
   | messages      | Currently unused. Will always be the empty string.  |
   +---------------+-----------------------------------------------------+
   | ndim          | number of dimensions for the image.                 |
   +---------------+-----------------------------------------------------+
   | perplanebeams | Dictionary of per-plane beams. Only present if the  |
   |               | image has per-plane beams.                          |
   +---------------+-----------------------------------------------------+
   | refpix        | Array of numerical values indicating the image axes |
   |               | reference pixels.                                   |
   +---------------+-----------------------------------------------------+
   | refval        | Array of numerical values indicating the reference  |
   |               | values of the axes in axes units.                   |
   +---------------+-----------------------------------------------------+
   | restoringbeam | The image restoring beam, only present if the the   |
   |               | image has a single, global restoring beam.          |
   +---------------+-----------------------------------------------------+
   | shape         | Array of integers indicating the number of pixels   |
   |               | on each image axis.                                 |
   +---------------+-----------------------------------------------------+
   | tileshape     | Image tile shape.                                   |
   +---------------+-----------------------------------------------------+
   | unit          | Image brightness unit.                              |
   +---------------+-----------------------------------------------------+
   
    
   
   .. rubric:: Task-specific Parameters Summary

   *mode*
   
   Mode of operation. See above for details. Modes which involve
   writing parameters will fail on read-only images, such as FITS
   images.
   
   *hdkey*
   
   The associated keyword for modes *"add"*, *"del"*, *"get"*, or
   *"put"*. Only *mode="get"* will succeed for read-only images. See
   above for supported values.
   
   *hdvalue*
   
   Value of keyword used only for modes add or put.
   
   *verbose*
   
   Give a full listing of beams or just a short summary? Only used
   when the image has multiple beams and *mode="summary"*.
   

.. _Examples:

Examples
   mode='get' (image has direction and spectral coordinates)
   
   ::
   
      epoch = imhead(imagename=imagename, mode="get", hdkey="date-obs")
      observer = imhead(imagename=imagename, mode="get", hdkey="observer")
      projection = imhead(imagename=imagename, mode="get", hdkey="projection")
      restfreq = imhead(imagename=imagename, mode="get", hdkey="restfreq")
   
   mode='add'
   
   ::

      if imhead(imagename=imagename, mode="add", hdkey="mykey", hdvalue="myvalue"):
           print "mykey added".
      else:
           print "addition of mykey failed."
   
   mode="del"
   
   ::
   
      if imhead(imagename=imagename, mode="del", hdkey="mykey"):
           print "mykey deleted".
      else:
           print "deletion of mykey failed."
   
   mode="put"
   
   ::
   
      # change the reference RA value
      key = 'crval1'
      imhead(imagename=imagename, mode="put", hdkey=key, hdvalue="3:00:00")

      # or equivalently
      imhead(imagename=imagename, mode="put", hdkey=key, hdvalue="45deg")

      # change the direction reference frame (NOTE, no precession of the existing
      # reference values is done!)
      imhead(imagename=imagename, mode="put", hdkey="equinox", hdvalue="GALACTIC")

      # change the object
      imhead(imagename=imagename, mode="put", hdkey="object",
             hdvalue="Milliways, also known as The Restaurant at the End of the Universe")

   

.. _Development:

Development
   No additional development details

