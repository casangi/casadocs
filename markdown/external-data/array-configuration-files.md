

# Array configuration files 

Array configuration files for various telescopes can be used in the CASA simulator

Array configuration files for various telescopes are distributed with each CASA release. These configuration files can be used to define the telescope for simulator tools and tasks. Currently, configuration files for the following telescopes are available in CASA:

-   ALMA / 12m Array
-   ALMA / 7m ACA
-   VLA
-   VLBA
-   Next-Generation VLA (reference design)
-   ATCA
-   MeerKat
-   PdBI (pre-NOEMA)
-   WSRT
-   SMA
-   Carma

The full list of antenna configurations can be found in the [CASA Guides on Simulations](https://casaguides.nrao.edu/index.php?title=Antenna_Configurations_Models_in_CASA_Cycle6).

One can also locate the directory with the configurations in the CASA distribution and then list the configuration files, using the following commands in CASA:

    CASA <>: print os.getenv('CASAPATH').split(' ')[0] + '/data/alma/simmos/'
    /home/casa/packages/RHEL7/release/casa-release-5.4.0-68/data/alma/simmos/

    CASA <>: ls /home/casa/packages/RHEL6/release/casa-release-5.4.0-68/data/alma/simmos/

<div>

If a configuration file is not distributed with CASA but retrieved elsewhere, then the configuration file can be called by explicitly writing the full path to the location of the configuration file in the antennalist paramter of the simulator tasks.

</div>

<div class="alert alert-info">
[**NOTE**: the most recent ALMA configuration files may not always be available in the most recent CASA version. ALMA configuration files for all cycles are available for download [here](https://almascience.nrao.edu/tools/casa-simulator). For the Next-Generation VLA reference design, the latest information can be found [here](https://ngvla.nrao.edu/page/tools).]{
</div>

 

 

There are currently no items in this folder.

