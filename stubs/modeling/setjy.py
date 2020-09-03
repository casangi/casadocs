#
# stub function definition file for docstring parsing
#

def setjy(vis='', field='', spw='', selectdata=False, timerange='', scan='', intent='', observation='', scalebychan=True, standard='Perley-Butler 2017', model='', modimage='', listmodels=False, fluxdensity=-1, spix=0.0, reffreq='1GHz', polindex=[''], polangle=[''], rotmeas=0.0, fluxdict='', useephemdir=False, interpolation='nearest', usescratch=False, ismms=False):
    r"""
Fills the model column with the visibilities of a calibrator

Parameters
   - **vis** (string='') - Name of input visibility file
   - **field** (string='') - Select field using field id(s) or field name(s)
   - **spw** (string='') - Select spectral window/channels
   - **selectdata** (bool=False) - Other data selection parameters

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** (string='') - Select observing intent
      - **observation** ({string, int}='') - Select by observation ID(s)

      .. raw:: html

         </details>
   - **scalebychan** (bool=True) - Scale the flux density on a per channel basis or else on a per spw basis
   - **standard** (string='Perley-Butler 2017') - Flux density standard

      .. raw:: html

         <details><summary><i> standard = Perley-Butler 2017 </i></summary>

      - **model** (string='') - File location for field model
      - **listmodels** (bool=False) - List the available models for VLA calibrators or Tb models for Solar System objects
      - **interpolation** (string='nearest') - Method to be used to interpolate in time

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> standard = Perley-Butler 2013 </i></summary>

      - **model** (string='') - File location for field model
      - **listmodels** (bool=False) - List the available models for VLA calibrators or Tb models for Solar System objects
      - **interpolation** (string='nearest') - Method to be used to interpolate in time

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> standard = Perley-Butler 2010 </i></summary>

      - **model** (string='') - File location for field model
      - **listmodels** (bool=False) - List the available models for VLA calibrators or Tb models for Solar System objects

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> standard = Butler-JPL-Horizons 2012 </i></summary>

      - **listmodels** (bool=False) - List the available models for VLA calibrators or Tb models for Solar System objects
      - **useephemdir** (bool=False) - Use directions in the ephemeris table

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> standard = manual </i></summary>

      - **fluxdensity** ({int, intArray, doubleArray}=-1) - Specified flux density in Jy [I,Q,U,V]; (-1 will lookup values)
      - **spix** ({double, doubleArray}=0.0) - Spectral index (including higher terms) of I fluxdensity
      - **reffreq** (string='1GHz') - Reference frequency for spix
      - **polindex** (doubleArray=['']) - Coefficients of an expansion of frequency-dependent linear polarization fraction expression
      - **polangle** (doubleArray=['']) - Coefficients of an expansion of frequency-dependent polarization angle expression (in radians)
      - **rotmeas** (double=0.0) - Rotation measure (in rad/m^2)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> standard = fluxscale </i></summary>

      - **fluxdict** (record='') - Output dictionary from fluxscale

      .. raw:: html

         </details>
   - **usescratch** (bool=False) - Will create if necessary and use the MODEL_DATA 




    """
    pass
