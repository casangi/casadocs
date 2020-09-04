#
# stub function definition file for docstring parsing
#

def plotants(vis, figfile='', antindex=False, logpos=False, exclude='', checkbaselines=False, title='', showgui=True):
    r"""
Plot the antenna distribution in the local reference frame:

Parameters
   - **vis** (string) - Name of input visibility file (MS) [1]_
   - **figfile** (string='') - Save the plotted figure to this file [2]_
   - **antindex** (bool=False) - Label antennas with name and antenna ID [3]_
   - **logpos** (bool=False) - Whether to plot logarithmic positions [4]_
   - **exclude** (string='') - Antenna name/id selection to exclude from plot [5]_
   - **checkbaselines** (bool=False) - Whether to check baselines in the main table. [6]_
   - **title** (string='') - Title for the plot [7]_
   - **showgui** (bool=True) - Show plot on gui. [8]_


Description
   .. rubric:: Summary
      

   This task is a simple plotting interface to produce plots of the
   antenna positions at the time that the data were taken. The
   antenna positions are taken from the ANTENNA sub-table of a
   MeasurementSet and are given in the local reference frame. The
   antennas are plotted Y vs. X in meters, where Y is toward local
   north and X is toward local east. The name of each antenna, and
   its ID when requested, is shown next to its respective location.

   .. rubric:: Interactive display
      

   The antennas will be plotted in a plotter window as shown below.
   Tool buttons allow you to interactively pan, zoom, stretch,
   compress, or save the plot, as well as return to the original plot
   view (home) or navigate between previous plot views (forward and
   back).

   .. rubric:: Task parameters
      

   When using **plotants**, you must specify the MeasurementSet to
   plot (*vis* parameter). The plot can be exported by specifying
   *figfile='plot_name.extension'*. Supported format extensions for
   the *figfile* depend on which python modules are installed on your
   system, but may include: emf, eps, pdf, png, ps, raw, rgba, svg,
   and svgz. Formats currently available in a downloaded CASA package
   include all but emf (enhanced metafile).

   Other parameter options allow the user to include the antenna ID
   with the name (*antindex=True*), to plot logarithmic positions
   (*logpos=True*), to exclude an antenna selection (e.g.
   *exclude="5~7"* to exclude antenna IDs 5, 6, and 7), to plot only
   those antennas which appear in the MAIN table
   (*checkbaselines=True*), and to set the title to a specified
   string.

   By default, the plotants GUI will be shown. When it is not
   needed, as in scripting mode to produce a *figfile*, set the
   *showgui* parameter to False. The default setting *showgui=True*
   will be overridden by the casa flags *--nogui, --pipeline,* and
   *--agg*, which suppress GUI tools.

   For more information and sample plots, see the Chapter Pages on
   `"Plotting Antenna
   Positions" <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/plotting-antenna-positions>`__.

   |image1|

   +---------+-----------------------------------------------------------+
   | Type    | Figure 1                                                  |
   +---------+-----------------------------------------------------------+
   | ID      | examination-fig-plotants                                  |
   +---------+-----------------------------------------------------------+
   | Caption | The **plotants** GUI for a VLA dataset, with              |
   |         | *antindex=True*. Tool buttons allow the user to           |
   |         | manipulate and export the plot.                           |
   +---------+-----------------------------------------------------------+

.. |image1| image:: docs/tasks/_apimedia/f05dc15d6cf9628b4e2f819d7e5530c7f27d3bd2.png
:class: image-inline




Details
   Explanation of each parameter

.. [1] 
   **vis** (string)
      | Name of input visibility file (MS)
.. [2] 
   **figfile** (string='')
      | Save the plotted figure to this file
.. [3] 
   **antindex** (bool=False)
      | Label antennas with name and antenna ID
.. [4] 
   **logpos** (bool=False)
      | Whether to plot logarithmic positions
.. [5] 
   **exclude** (string='')
      | Antenna name/id selection to exclude from plot
.. [6] 
   **checkbaselines** (bool=False)
      | Whether to check baselines in the main table.
.. [7] 
   **title** (string='')
      | Title for the plot
.. [8] 
   **showgui** (bool=True)
      | Show plot on gui.

    """
    pass
