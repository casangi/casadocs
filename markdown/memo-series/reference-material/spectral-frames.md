

# Spectral Frames 

Spectral Frames supported in CASA

# Spectral Frames

CASA supported spectral frames:

  Frame            Description                                                                                                                                                                                                                                       Definition  
  ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  REST             rest frequency                                                                                                                                                                                                                                    Lab frame or source frame; cannot be converted to any other frame
  LSRK             LSR as a kinematic (radio) definition  (J2000) based on average velocity of stars in the Solar neighborhood                                                                                                                                       20km/s in direction of RA, Dec - \[270,+30\] deg (B1900.0) (Gordon 1975 [\[1\]](#Bibliography) )
  LSRD             Local Standard of Rest (J2000), dynamical, IAU definition. Solar peculiar velocity in the reference frame of a circular orbit about the Galactic Center, based on average velocity of stars in the Solar neighborhood and solar peculiar motion   U$\odot$=9kms/s, V$\odot$=12km/s,W$\odot$=7km/s. Or 16.552945km/s  towards l,b = 53.13, +25.02 deg (Delhaye 1965 [\[2\]](#Bibliography))
  BARY             Solar System Baryceneter (J2000)                                                                                                                                                                                                                   
  GEO              Geocentric, referenced to the Earth\'s center                                                                                                                                                                                                      
  TOPO             Topocentric                                                                                                                                                                                                                                       Local observatory frame, fixed in observing frequency, no doppler tracking
  GALACTO          Galactocentric (J2000), referenced to dynamical center of the Galaxy                                                                                                                                                                              220 km/s in the direction l,b = 270, +0 deg.  (Kerr and Lynden-Bell 1986  [\[3\]](#Bibliography))
  LGROUP           Mean motion of Local Group Galaxies with respect to its bary center                                                                                                                                                                               308km/s towards l,b = 105,-7
  CMB              Cosmic Microwave Background, COBE measurements of dipole anisotropy                                                                                                                                                                               369.5km/s towards l,b = 264.4,48.4. (Kogut et al. 1993 [\[4\]](#Bibliography))
  Undefined                                                                                                                                                                                                                                                           

 

 

 

 

#  Doppler Types 

CASA supported Doppler types (velocity conventions) where $f_v$ is the observed frequency and $f_0$ is the rest frame frequency of a given lineand positive velocity V is increasing away from the observer:

  Name           Description
  -------------- -----------------------------------------------------------------------------------------------------------------------------------
  RADIO          $$V = c \frac{(f_0 - f_v)}{f_0}$$
  Z              $$V=cz$$  $$z = \frac{(f_0 - f_v)}{f_v}$$
  RATIO          $$V=c(\frac{f_v}{f_o})$$
  BETA           $$V=c\frac{(1-(\frac{f_v}{f_0})^2)}{(1+(\frac{f_v}{f_0})^2)}$$
  GAMMA          $$ V=c\frac{(1 + (\frac{f_v}{f_0})^2)}{2\frac{f_v}{f_0}}$$
  OPTICAL        $$V= c\frac{(f_0 - f_v)}{f_v}$$
  TRUE           $$V=c\frac{(1-(\frac{f_v}{f_0})^2)}{(1+(\frac{f_v}{f_0})^2)}$$
  RELATIVISTIC   $$V=c\frac{(1-(\frac{f_v}{f_0})^2)}{(1+(\frac{f_v}{f_0})^2)}$$

 

# Bibliography

1. Gordon\ 1975:\ \"**Methods\ of\ Experimental\ Physics:\ Volume\ 12:**\ Astrophysics,\ Part\ C:\ Radio\ Observations\",\ ed.\ M.L.Meeks,\ Academic\ Press\ 1976\ 
2. Delhaye\ 1965\ (
3. Kerr\ F.\ J.\ &\ Lynden-Bell\ D.\ 1986\ MNRAS,\ 221,\ 1023\ (
4. Kogut\ A.\ et\ al.\ 1993\ (
^

