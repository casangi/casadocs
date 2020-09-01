

# MeasurementSet v2 

Definition of the MeasurementSet v2

[Introduction](#autotoc-item-autotoc-0){#autotoc-item-autotoc-0 .autotoc-level-2 .active}[MS v2.0 Layout](#autotoc-item-autotoc-1){#autotoc-item-autotoc-1 .autotoc-level-2}[MAIN table: Data, Coordinates and Flags](#autotoc-item-autotoc-2){#autotoc-item-autotoc-2 .autotoc-level-2}[ANTENNA: Antenna Characteristics](#autotoc-item-autotoc-3){#autotoc-item-autotoc-3 .autotoc-level-2}[DATA_DESCRIPTION: Data Description Table](#autotoc-item-autotoc-4){#autotoc-item-autotoc-4 .autotoc-level-2}[DOPPLER: Doppler Tracking Information](#autotoc-item-autotoc-5){#autotoc-item-autotoc-5 .autotoc-level-2}[FEED: Feed Characteristics](#autotoc-item-autotoc-6){#autotoc-item-autotoc-6 .autotoc-level-2}[FIELD: Field Positions for Each Source](#autotoc-item-autotoc-7){#autotoc-item-autotoc-7 .autotoc-level-2}[FLAG_CMD: Flag Commands](#autotoc-item-autotoc-8){#autotoc-item-autotoc-8 .autotoc-level-2}[FREQ_OFFSET: Frequency Offset Information](#autotoc-item-autotoc-9){#autotoc-item-autotoc-9 .autotoc-level-2}[HISTORY: History Information](#autotoc-item-autotoc-10){#autotoc-item-autotoc-10 .autotoc-level-2}[OBSERVATION: Observation Information](#autotoc-item-autotoc-11){#autotoc-item-autotoc-11 .autotoc-level-2}[POINTING: Antenna Pointing Information](#autotoc-item-autotoc-12){#autotoc-item-autotoc-12 .autotoc-level-2}[POLARIZATION: Polarization Setup Information](#autotoc-item-autotoc-13){#autotoc-item-autotoc-13 .autotoc-level-2}[PROCESSOR: Processor Information](#autotoc-item-autotoc-14){#autotoc-item-autotoc-14 .autotoc-level-2}[SOURCE: Source Information](#autotoc-item-autotoc-15){#autotoc-item-autotoc-15 .autotoc-level-2}[SPECTRAL_WINDOW: Spectral Window Description](#autotoc-item-autotoc-16){#autotoc-item-autotoc-16 .autotoc-level-2}[STATE: State Information](#autotoc-item-autotoc-17){#autotoc-item-autotoc-17 .autotoc-level-2}[SYSCAL: System Calibration](#autotoc-item-autotoc-18){#autotoc-item-autotoc-18 .autotoc-level-2}[WEATHER: Weather Station Information](#autotoc-item-autotoc-19){#autotoc-item-autotoc-19 .autotoc-level-2}

## Introduction

The MeasurementSet version 2 [\[1\]](#Bibliography) , is a database designed to hold radioastronomical data to be calibrated following the MeasurementEquation approach by Hamaker, Bregman, and Sault (1996).

Since its publication, the MeasurementSet (MS) design has been implemented by several software development groups, among them the CASA team and, e.g., the European VLBI Network team. CASA has also adopted the MeasurementEquation as its fundamental calibration scheme and has thus embraced the MS as its native way to store radio observations. With CASA becoming the designated analysis package for ALMA and the VLA, this means that the MS is now the default way of storing ALMA and VLA data during the actual analysis.

The ALMA and VLA raw data format, however, is not the MS but the so-called ALMA Science Data Model (ASDM) for ALMA, and the Science Data Model (SDM) for the VLA. Both of which are closely related and are discussed in a separate section. The ALMA and VLA archives hence do not store data in MS format but in (A)SDM format, and when a CASA user starts to work with this data, the first step has to be the import of the (A)SDM into the CASA MS format.

The MS is effectively a relational database which on the one hand tries to permit the storage of all imaginable radio (interferometric, single-dish) data with corresponding metadata, and on the other hand ventures to be storage-space and data-maintenance efficient by avoiding data redundancy.

The universality is achieved by offering many optional parts in the format which cover most imaginable use cases in radio astronomy. So a simple, few-antenna interferometer observing a simple object with time-independent position at just a single frequency can store its data using a small sub-set of the format while a large interferometer with antennas on time-dependent locations, observing many objects in rapid succession with time-dependent source positions using a complex, time-dependent spectral setup etc., can equally use the MS to store its data albeit using a larger subset of the possibilities of the MS.

The non-redundance of the format is achieved by simply following the standard approach of relational databases which is to put repeating pieces of information into separate database tables, the Subtables, and replacing them in the main body of the data base, the Main table, by references to the Subtables. In the case of the MS this happens in two layers of Subtables with the first layer being referenced by the Main table and the second layer being referenced by the first layer. I.e., there are some Subtables which reference other Subtables.

The Subtable referencing mechanism is defined in the original design. It works either via the *line numbers* of the individual Subtable ,this implies that the reference is a zero-based integer and that the removal of a line in such a Subtable requires reindexing in the referencing table(s), or via explicit references to an index column in the Subtable ,the latter is much less common.

These design principles lead to a format which puts the bulk of the data ,the interferometric visibilities and/or the single-dish total-power measurements with their timestamps, into a Main Table , and most of the metadata in the two layers of Subtables.

In the CASA MS implementation, the individual Tables are all stored in the CASA Table format, i.e. they are actually not single files on disk but directories containing several files, essentially one for each column of the table. So the entire MS is also not a single file (like, e.g., in the FITS IDI format) but a whole directory tree. For transport, the MS typically has to be turned into a single file by using the command \"tar\".

The Main Table contains the radio data initially in a column called *DATA* (interferometric data) or *FLOAT_DATA* (pure single-dish data). One of these two columns always has to be present.

When a calibration is applied to the *DATA* column, a *CORRECTED_DATA* column is created to contain the calibrated data leaving the original data untouched. Furthermore, a *MODEL_DATA* column can be required to store expectation values for the emission of calibration sources.

For large datasets these bulk data columns can require large amounts of disk space and access to them may be slow. To mitigate these problems, the CASA team is working on making the columns \"virtual\" as much as possible, i.e. replacing the *CORRECTED_DATA* and *MODEL_DATA* columns by parameterised versions calculated on-the-fly.

In the case of the virtual *MODEL_DATA* column, this is essentially a model image which is stored with the MS and converted on-the-fly to visibilities.

In the case of the virtual *CORRECTED_DATA* column, this is a so-called \"Cal Library\" which permits to calibrate the data in the *DATA* column on-the-fly and make the results available as if they were stored in a standard table column.

Finally, a major case of data redundance for ALMA and VLA data is of course the fact that the raw data arrive at the user in (A)SDM format but then have to be translated into MS format which creates a completely redundant copy of all raw data without any gain for the user. This problem was addressed by introducing the so-called \"lazy\" import of (A)SDM data. The development is not yet completely finished but is already available for ALMA interferometric data. The idea here is to also make the *DATA* column virtual and perform the translation from the (A)SDM format on-the-fly. This typically shrinks the MS by a factor 30 in data volume. Of course the (A)SDM raw data has to be kept on disk for access. Access speeds to a virtual *DATA* column are essentially the same as to a non-virtual one. They may even be a little faster since the (A)SDM data is better compressed.

## MS v2.0 Layout

CASA uses the MeasurementSet Version 2  (A.J. Kemball and M.H. Wieringa, eds., 2000) as the internal working data format. The MeasurementSet set was orignially defined in AIPS++ Note 191 (Wieringa and Cornwell 1996).  Reproduced below is the table structrue for the MeasurementSet as used by CASA. 

There is a MAIN table containing a number of data columns and keys into various subtables. There is at most one of each subtable. The subtables are stored as keywords of the MS, and all defined sub-tables are tabulated below. Optional sub-tables are shown in italics and in parentheses.

**Subtables**

Table

Contents

Keys

ANTENNA

Antenna characteristics

ANTENNA_ID

DATA_DESCRIPTION

Data description

DATA_DESC_ID

(*DOPPLER*)

Doppler tracking

DOPPLER_ID, SOURCE_ID

FEED

Feed characteristics

FEED_ID, ANTENNA_ID, TIME, SPECTRAL_WINDOW_ID

FIELD

Field position

FIELD_ID

FLAG_CMD

Flag commands

TIME

(*FREQ_OFFSET*)

Frequency offset information

FEED_ID, ANTENNA*n*, FEED_ID, TIME, SPECTRAL_WINDOW_ID

HISTORY

History information

OBSERVATION_ID, TIME

OBSERVATION

Observer, Schedule, etc

OBSERVATION_ID

POINTING

Pointing information

ANTENNA_ID, TIME

POLARIZATION

Polarization setup

POLARIZATION_ID

PROCESSOR

Processor information

PROCESSOR_ID

(*SOURCE*)

Source information

SOURCE_ID, SPECTRAL_WINDOW_ID, TIME

SPECTRAL_WINDOW

Spectral window setups

SPECTRAL_WINDOW_ID

STATE

State information

STATE_ID

(*SYSCAL*)

System calibration characteristics

FEED_ID, ANTENNA_ID, TIME, SPECTRAL_WINDOW_ID

(*WEATHER*)

Weather info for each antenna

ANTENNA_ID, TIME

Note that there are two types of subtables. For the first, simpler type, the key (ID) is the row number in the subtable. Examples are FIELD*,* SPECTRAL_WINDOW*,* OBSERVATION and PROCESSOR. For the second, the key is a collection of parameters, usually including TIME. Examples are FEED*, (SOURCE),* (SYSCAL), and *(WEATHER)*.

Note that all optional columns are indicated in italics and in parentheses.

## MAIN table: Data, Coordinates and Flags

**MAIN table: Data, coordinates and flags**

Name

Format

Units

Measure

Comments

**Columns**

*Keywords*

MS_VERSION 

Float 

 

 

MS format version 

*(SORT_COLUMNS)*

String 

 

 

Sort columns 

*(SORT_ORDER)*

String 

 

 

Sort order 

*Key*

TIME 

Double 

s 

EPOCH 

Integration midpoint 

*(TIME_EXTRA_PREC)*

Double 

s 

 

extraTIME precision 

ANTENNA1 

Int 

 

 

First antenna 

ANTENNA2 

Int 

 

 

Second antenna 

*(ANTENNA3)*

Int 

 

 

Third antenna 

FEED1 

Int 

 

 

Feed on ANTENNA1 

FEED2 

Int 

 

 

Feed on ANTENNA2 

*(FEED3)*

Int 

 

 

Feed on ANTENNA3 

DATA_DESC_ID 

Int 

 

 

Data desc. id.

PROCESSOR_ID 

Int 

 

 

Processor id.

*(PHASE_ID)*

Int 

 

 

Phase id.

FIELD_ID 

Int 

 

 

Field id.

*Non-key attributes*

INTERVAL 

Double 

s 

 

Sampling interval 

EXPOSURE 

Double 

s 

 

The effective integration time 

TIME_CENTROID 

Double 

s 

EPOCH 

Time centroid 

*(PULSAR_BIN)*

Int 

 

 

Pulsar bin number 

*(PULSAR_GATE_ID)*

Int 

 

 

Pulsar gate id. 

SCAN_NUMBER 

Int 

 

 

Scan number 

ARRAY_ID 

Int 

 

 

Subarray number

OBSERVATION_ID 

Int 

 

 

Observation id.

STATE_ID 

Int 

 

 

State id.

*(BASELINE_REF)*

Bool 

 

 

Reference antenna 

UVW 

Double(3) 

m 

UVW 

UVW coordinates 

*(UVW2)*

Double(3) 

m 

UVW 

UVW (baseline 2) 

*Data*

*(DATA)*

Complex(*N*~c~, *N*~f~) 

 

 

Complex visibility matrix (synthesis arrays)

*(FLOAT_DATA)*

Float(*N*~c~, *N*~f~) 

 

 

Float data matrix (single dish) 

*(VIDEO_POINT)*

Complex(*N*~c~) 

 

 

Video point 

*(LAG_DATA)*

Complex(*N*~c~, *N*~l~) 

 

 

Correlation function 

SIGMA 

Float(*N*~c~) 

 

 

Estimated rms noise for single channel 

*(SIGMA_SPECTRUM)*

Float(*N*~c~, *N*~f~^\*^) 

 

 

Estimated rms noise 

WEIGHT 

Float(*N*~c~) 

 

 

Weight for whole data matrix 

*(WEIGHT_SPECTRUM)*

Float(*N*~c~, *N*~f~^\*^) 

 

 

Weight for each channel

*Flag information*

FLAG 

Bool(*N*~c~, *N*~f~^\*^) 

 

 

Cumulative data flags 

FLAG_CATEGORY 

Bool(*N*~c~, *N*~f~^\*^, *N*~cat~) 

 

 

Flag categories 

FLAG_ROW 

Bool 

 

 

The row flag 

**Notes:** 
:   Note that *N*~l~= number of lags, *N*~c~= number of correlators, *N*~f~= number of frequency channels, and *N*~cat~= number of flag categories.
:    

**MS_VERSION**
:   The MeasurementSet format revision number, expressed as ${major}_{revision}$ ${minor}_{revision}$. This version is 2.0. 

**SORT_COLUMNS**
:   Sort indices, in the form ${index}_1$ ${index}_2$ $\cdots$, for the underlying MS. A string containing \"NONE\" reflects no sort order. An example might be *SORT_COLUMNS=\"TIME ANTENNA1 ANTENNA2\"*, to indicate sorting in in time-baseline order.

**SORT_ORDER**
:   Sort order as either \"ASCENDING\" or \"DESCENDING\".

**TIME**
:   Mid-point (not centroid) of data interval.

**TIME_EXTRA_PREC**
:   Extra time precision.

**ANTENNA*n***
:   Antenna number (≥ 0), and a direct index into the *ANTENNA* sub-table *rownr*. For *n* \> 2, triple-product data are implied.

**FEED*n***
:   Feed number ≥0). For *n*\> 2, triple-product data are implied.

**DATA_DESC_ID**
:   Data description identifier (≥0), and a direct index into the *DATA_DESCRIPTION* sub-table *rownr*.

**PROCESSOR_ID**
:   Processor indentifier (≥0), and a direct index into the *PROCESSOR* sub-table *rownr*.

**PHASE_ID**
:   Switching phase identifier (≥0)

**FIELD_ID**
:   Field identifier (≥0).

**INTERVAL**
:   Data sampling interval. This is the nominal data interval and does not include the effects of bad data or partial integration.

**EXPOSURE**
:   Effective data interval, including bad data and partial averaging.

**PULSAR_BIN**
:   Pulsar bin number for the data record. Pulsar data may be measured for a limited number of pulse phase bins. The pulse phase bins are described in the *PULSAR* sub-table and indexed by this bin number.

**PULSAR_GATE_ID**
:   Pulsar gate identifier (≥0), and a direct index into the *PULSAR_GATE* sub-table *rownr*.

**SCAN_NUMBER**
:   Arbitrary scan number to identify data taken in the same logical scan. Not required to be unique.

**ARRAY_ID**
:   Subarray identifier (≥0), which identifies data in separate subarrays.

**OBSERVATION_ID**
:   Observation identifier (≥0), which identifies data from separate observations.

**STATE_ID**
:   State identifier (≥0), which identifies information relating to active reference signals or loads.

**BASELINE_REF**
:   Flag to indicate the original correlator reference antenna for baseline-based correlators (True for *ANTENNA1*; False for *ANTENNA2*).

**UVW**
:   *uvw* coordinates for the baseline from *ANTENNE2* to *ANTENNA1*, i.e. the baseline is equal to the difference POSITION2 - POSITION1. The UVW given are for the *TIME_CENTROID*, and correspond in general to the reference type for the *PHASE_DIR* of the relevant field. I.e. J2000 if the phase reference direction is given in J2000 coordinates. However, any known reference is valid. Note that the choice of baseline direction and UVW definition (*W* towards source direction; *V* in plane through source and system\'s pole; *U* in direction of increasing longitude coordinate) also determines the sign of the phase of the recorded data.

**UVW2**
:   *uvw* coordinates for the baseline from *ANTENNE3* to *ANTENNA1* (triple-product data only), i.e. the baseline is equal to the difference POSITION3 - POSITION1. The UVW given are for the *TIME_CENTROID*, and correspond in general to the reference type for the *PHASE_DIR* of the relevant field. I.e. J2000 if the phase reference direction is given in J2000 coordinates. However, any known reference is valid. Note that the choice of baseline direction and UVW definition (*W* towards source direction; *V* in plane through source and system\'s pole; *U* in direction of increasing longitude coordinate) also determines the sign of the phase of the recorded data.

**DATA, FLOAT_DATA, LAG_DATA**
:   At least one of these columns should be present in a given MeasurementSet. In special cases one or more could be present (e.g., single dish data used in synthesis imaging or a mix of auto and crosscorrelations on a multi-feed single dish). If only correlation functions are stored in the MS, then *N*~f~^\*^ is the maximum number of lags (*N*~l~) specified in the LAG table for this LAG_ID. If both correlation functions and frequency spectra are stored in the same MS, then *N*~f~^\*^ is the number of frequency channels, and the weight information refers to the frequency spectra only. The units for these columns (eg. \'Jy\') specify whether the data are in flux density units or correlation coefficients.

**VIDEO_POINT**
:   The video point for the spectrum, to allow the full reverse transform.

**SIGMA**
:   The estimated rms noise for a single channel, for each correlator.

**SIGMA_SPECTRUM**
:   The estimated rms noise for each channel.

**WEIGHT**
:   The weight for the whole data matrix for each correlator, as assigned by the correlator or processor.

**WEIGHT_SPECTRUM**
:   The weight for each channel in the data matrix, as assigned by the correlator or processor. The weight spectrum should be used in preference to the *WEIGHT*, when available.

**FLAG**
:   An array of Boolean values with the same shape as DATA (see the DATA item above) representing the cumulative flags applying to this data matrix, as specified in *FLAG_CATEGORY*. Data are flagged bad if the FLAG array element is True.

**FLAG_CATEGORY**
:   An array of flag matrices with the same shape as DATA, but indexed by category. The category identifiers are specified by a keyword CATEGORY, containing an array of string identifiers, attached to the FLAG_CATEGORY column and thus shared by all rows in the MeasurementSet. The cumulative effect of these flags is reflected in column FLAG. Data are flagged bad if the FLAG array element is True. See Section 3.1.8 for further details.

**FLAG_ROW**
:   True if the entire row is flagged.

## ANTENNA: Antenna Characteristics

**ANTENNA: Antenna characteristics**

Name

Format

Units

Measure

Comments

**Columns**

*Data*

NAME 

String 

 

 

Antenna name 

STATION 

String 

 

 

Station name 

TYPE 

String 

 

 

Antenna type 

MOUNT 

String 

 

 

Mount type:alt-az, equatorial, X-Y, orbiting, bizarre 

POSITION 

Double(3) 

m 

POSITION 

Antenna X,Y,Z phase reference positions 

OFFSET 

Double(3) 

m 

POSITION 

Axes offset of mount to FEED REFERENCE point 

DISH_DIAMETER 

Double 

m 

 

Diameter of dish

*(ORBIT_ID)*

Int 

 

 

Orbit id. 

*(MEAN_ORBIT)*

Double(6) 

 

 

Mean Keplerian elements

*(PHASED_ARRAY_ID)*

Int 

 

 

Phased array id.

Flag information

FLAG_ROW 

Bool 

 

 

Row flag

**Notes:**
:   This sub-table contains the global antenna properties for each antenna in the MS. It is indexed directly from MAIN via ANTENNA*n*.
:   

**NAME**
:   Antenna name (e.g. \"NRAO_140\")

**STATION**
:   Station name (e.g. \"GREENBANK\")

**TYPE**
:   Antenna type. Reserved keywords include: (\"GROUND-BASED\" - conventional antennas; \"SPACE-BASED\" - orbiting antennas; \"TRACKING-STN\" - tracking stations).

**MOUNT**
:   Mount type of the antenna. Reserved keywords include: (\"EQUATORIAL\" - equatorial mount; \"ALT-AZ\" - azimuth-elevation mount; \"X-Y\" - x-y mount; \"SPACE-HALCA\" - specific orientation model.)

**POSITION**
:   In a right-handed frame, X towards the intersection of the equator and the Greenwich meridian, Z towards the pole. The exact frame should be specified in the MEASURE_REFERENCE keyword (ITRF or WGS84). The reference point is the point on the az or ha axis closest to the el or dec axis.

**OFFSET**
:   Axes offset of mount to feed reference point.

**DISH_DIAMETER**
:   Nominal diameter of dish, as opposed to the effective diameter.

**ORBIT_ID**
:   Orbit identifier. Index used in ORBIT sub-table if ANTENNA_TYPE is \"SPACE_BASED\".

**MEAN_ORBIT**
:   Mean Keplerian orbital elements, using the standard convention (Flatters 1998):
    -   **0:** Semi-major axis of orbit (*a*) in *m*.
    -   **1:** Ellipticity of orbit (*e*).
    -   **2:** Inclination of orbit to the celestial equator (*i*) in *deg*.
    -   **3:** Right ascension of the ascending node (Ω) in *deg*.
    -   **4:** Argument of perigee (ω ) in *deg*.
    -   **5:** Mean anomaly (*M*) in *deg*.

**PHASED_ARRAY_ID**
:   Phased array identifier. Points to a *PHASED_ARRAY* sub-table which points back to multiple entries in the *ANTENNA* sub-table and contains information on how they are combined.

**FLAG_ROW**
:   Boolean flag to indicate the validity of this entry. Set to True for an invalid row. This does not imply any flagging of the data in MAIN, but is necessary as the *ANTENNA* index in MAIN points directly into the *ANTENNA* sub-table. Thus *FLAG_ROW* can be used to delete an antenna entry without re-ordering the ANTENNA indices throughout the MS.

## DATA_DESCRIPTION: Data Description Table

**DATA_DESCRIPTION: Data description table**

Name

Format

Units

Measure

Comments

**Columns**

*Data*

SPECTRAL_WINDOW_ID 

Int 

 

 

Spectral window id.

POLARIZATION_ID 

Int 

 

 

Polarization id.

*(LAG_ID)*

Int 

 

 

Lag fn. id.

*Flags*

FLAG_ROW 

Bool 

 

 

Row flag.

**Notes:**
:   This table define the shape of the associated DATA array in MAIN, and in indexed directly by DATA_DESC_ID.
:    

**SPECTRAL_WINDOW_ID**
:   Spectral window identifier.

**POLARIZATION_ID**
:   Polarization identifier (≥0); direct index into the *POLARIZATION* sub-table.

**LAG_ID**
:   Lag function identifier (≥0), and a direct index into the *LAG* sub-table *rownr*.

**FLAG_ROW**
:   True if the row does not contain valid data; does not imply flagging in MAIN.

## DOPPLER: Doppler Tracking Information

**DOPPLER: Doppler tracking information**

Name

Format

Units

Measure

Comments

**Columns**

*Key*

DOPPLER_ID 

Int 

 

 

Doppler tracking id.

SOURCE_ID 

Int 

 

 

Source id.

*Data*

TRANSITION_ID 

Int 

 

 

Transition id.

VELDEF 

Double 

m/s 

Doppler 

Velocity definition of Doppler shift.

**Notes:**
:   This sub-table contains frame information for different Doppler tracking modes. It is indexed from the SPECTRAL_WINDOW_ID sub-table (with SOURCE_ID as a secondary index) and thus allows the specification of a source-dependent Doppler tracking reference for each SPECTRAL_WINDOW. This model allows multiple possible transitions per source per spectral window, but only one reference at any given time.
:    

**DOPPLER_ID**
:   Doppler identifier, as used in the *SPECTRAL_WINDOW* sub-table.

**SOURCE_ID**
:   Source identifier (as used in the *SOURCE* sub-table).

**TRANSITION_ID**
:   This index selects the appropriate line from the list of transitions stored for each SOURCE_ID in the *SOURCE* table.

**VELDEF**
:   Velocity definition of the Doppler shift, e.g., RADIO or OPTICAL velocity in m/s.

## FEED: Feed Characteristics

**FEED: Feed characteristics**

Name

Format

Units

Measure

Comments

**Columns**

*Key*

ANTENNA_ID 

Int 

 

 

Antenna id

FEED_ID 

Int 

 

 

Feed id

SPECTRAL_WINDOW_ID 

Int 

 

 

Spectral window id.

TIME 

Double 

s 

EPOCH 

Interval midpoint 

INTERVAL 

Double 

s 

 

Time interval

*Data description*

NUM_RECEPTORS 

Int 

 

 

\# receptors on this feed 

*Data*

BEAM_ID 

Int 

 

 

Beam model

BEAM_OFFSET 

Double(2, NUM_RECEPTORS) 

rad 

DIRECTION 

Beam position offset (on sky but in antenna reference frame).

*(FOCUS_LENGTH)*

Double 

m 

 

Focus length 

*(PHASED_FEED_ID)*

Int 

 

 

Phased feed

POLARIZATION_TYPE 

String (NUM_RECEPTORS) 

 

 

Type of polarization to which a given RECEPTOR responds.

POL_RESPONSE 

Complex (NUM_RECEPTORS, NUM_RECEPTORS) 

 

 

Feed polzn. response

POSITION 

Double(3) 

m 

POSITION 

Position of feed relative to feed reference position for this antenna

RECEPTOR_ANGLE 

Double (NUM_RECEPTORS) 

rad 

 

The reference angle for polarization.

**Notes:**
:   A feed is a collecting element on an antenna, such as a single horn, that shares joint physical properties and makes sense to calibrate as a single entity. It is an abstraction of a generic antenna feed and is considered to have one or more RECEPTORs that respond to different polarization states. A FEED may have a time-variable beam and polarization response. Feeds are numbered from 0 on each separate antenna for each SPECTRAL_WINDOW_ID. Consequently, FEED_ID should be non-zero only in the case of feed arrays, i.e. multiple, simultaneous beams on the sky at the same frequency and polarization.
:    

**ANTENNA_ID**
:   Antenna number, as indexed from ANTENNA*n* in MAIN.

**FEED_ID**
:   Feed identifier, as indexed from FEED*n* in MAIN.

**SPECTRAL_WINDOW_ID**
:   Spectral window identifier. A value of -1 indicates the row is valid for all spectral windows.

**TIME**
:   Mid-point of time interval for which the feed parameters in this row are valid. The same Measure reference used for the TIME column in MAIN must be used.

**INTERVAL**
:   Time interval. 

**NUM_RECEPTORS**
:   Number of receptors on this feed. See *POLARIZATION_TYPE* for further information.

**BEAM_ID**
:   Beam identifier. Points to an optional BEAM sub-table defining the primary beam and polarization response for this *FEED*. A value of -1 indicates that no associated beam response is defined.

**BEAM_OFFSET**
:   Beam position offset, as defined on the sky but in the antenna reference frame.

**FOCUS_LENGTH**
:   Focus length. As defined along the optical axis of the antenna.

**PHASED_FEED_ID**
:   Phased feed identifier. Points to a *PHASED_FEED* sub-table which in turn points back to multiple entries in the *FEED* table, and specifies the manner in which they are combined. 

**POLARIZATION_TYPE**
:   Polarization type to which each receptor responds (e.g. \"R\",\"L\",\"X\" or \"Y\"). This is the receptor polarization type as recorded in the final correlated data (e.g. \"RR\"); i.e. as measured after all polarization combiners.

**POL_RESPONSE**
:   Polarization response at the center of the beam for this feed. Expressed in a linearly polarized basis ($ \bf\vec e_x$, $ \bf\vec e_y$) using the IEEE convention.

**POSITION**
:   Offset of feed relative to the feed reference position for this antenna (see ANTENNA sub-table).

**RECEPTOR_ANGLE**
:   Polarization reference angle. Converts into parallactic angle in the sky domain.

## FIELD: Field Positions for Each Source

**FIELD: Field positions for each source**

Name

Format

Units

Measure

Comments

**Columns**

*Key*

*Data*

NAME 

String 

 

 

Name of field 

CODE 

String 

 

 

Special characteristics of field 

TIME 

Double 

s 

EPOCH 

Time origin for the directions and rates

NUM_POLY 

Int 

 

 

Series order 

DELAY_DIR 

Double(2, NUM_POLY+1) 

rad 

DIRECTION 

Direction of delay center. 

PHASE_DIR 

Double(2, NUM_POLY+1) 

rad 

DIRECTION 

Phase center. 

REFERENCE_DIR 

Double(2, NUM_POLY+1) 

rad 

DIRECTION 

Reference center 

SOURCE_ID 

Int 

 

 

Index in Source table

*(EPHEMERIS_ID)*

Int 

 

 

Ephemeris id.

Flags

FLAG_ROW 

Bool 

 

 

Row flag

**Notes:**
:   The *FIELD* table defines a field position on the sky. For interferometers, this is the correlated field position. For single dishes, this is the nominal pointing direction.
:   

**NAME**
:   Field name; user specified.

**CODE**
:   Field code indicating special characteristics of the field; user specified.

**TIME**
:   Time reference for the directions and rates. Required to use the same TIME Measure reference as in MAIN.

**NUM_POLY**
:   Series order for the \*\_DIR columns.

**DELAY_DIR**
:   Direction of delay center; can be expressed as a polynomial in time. Final result converted to the defined Direction Measure type.

**PHASE_DIR**
:   Direction of phase center; can be expressed as a polynomial in time. Final result converted to the defined Direction Measure type.

**REFERENCE_DIR**
:   Reference center; can be expressed as a polynomial in time. Final result converted to the defined Direction Measure type. Used in single-dish to record the associated reference direction if position-switching has already been applied. For interferometric data, this is the original correlated field center, and may equal *DELAY_DIR* or *PHASE_DIR*.

**SOURCE_ID**
:   Points to an entry in the optional *SOURCE* subtable, a value of -1 indicates there is no corresponding source defined.

**EPHEMERIS_ID**
:   Points to an entry in the *EPHEMERIS* sub-table, which defines the ephemeris used to compute the field position. Useful for moving, near-field objects, where the ephemeris may be revised over time.

**FLAG_ROW**
:   True if data in this row are invalid, else False. Does not imply flagging in MAIN.

## FLAG_CMD: Flag Commands

**FLAG_CMD: Flag commands**

Name

Format

Units

Measure

Comments

**Columns**

*Key*

TIME 

Double 

s 

EPOCH 

Mid-point of interval 

INTERVAL 

Double 

s 

 

Time interval 

*Data*

TYPE 

String 

 

 

FLAG or UNFLAG

REASON 

String 

 

 

Flag reason

LEVEL 

Int 

 

 

Flag level

SEVERITY 

Int 

 

 

Severity code

APPLIED 

Bool 

 

 

True if applied in MAIN

COMMAND 

String 

 

 

Flag command

**Notes:**
:   The *FLAG_CMD* sub-table defines global flagging commands which apply to the data in MAIN, as described in Section 3.1.8.
:    

**TIME**
:   Mid-point of the time interval to which this flagging command applies. Required to use the same TIME Measure reference as used in *MAIN*.

**INTERVAL**
:   Time interval.

**TYPE**
:   Type of flag command, representing either a flagging (\"FLAG\") or un-flagging (\"UNFLAG\") operation.

**REASON**
:   Flag reason; user specified.

**LEVEL**
:   Flag level (≥0); reflects different revisions of flags which have the same *REASON*.

**SEVERITY**
:   Severity code for the flag, on a scale of 0-10 in order of increasing severity; user specified.

**APPLIED**
:   True if this flag has been applied to *MAIN*, and update in *FLAG_CATEGORY* and *FLAG*. False if this flag has not been applied to *MAIN*.

**COMMAND**
:   Global flag command, expressed in the standard syntax for data selection, as adopted within the project as a whole.

## FREQ_OFFSET: Frequency Offset Information

**FREQ_OFFSET: Frequency offset information**

Name

Format

Units

Measure

Comments

**Columns**

*Key*

ANTENNA1 

Int 

 

 

Antenna 1.

ANTENNA2 

Int 

 

 

Antenna 2.

FEED_ID 

Int 

 

 

Feed id.

SPECTRAL_WINDOW_ID 

Int 

 

 

Spectral window id.

TIME 

Double 

s 

EPOCH 

Interval midpoint

INTERVAL 

Double 

s 

 

Time interval

*Data*

OFFSET 

Double 

Hz 

 

Frequency offset

**Notes:**
:   The table contains frequency offset information, to be added directly to the defined frequency labeling in the *SPECTRAL_WINDOW* sub-table as a Measure offset. This allows bands with small, time-variable, ad hoc frequency offsets to be labeled as the same *SPECTRAL_WINDOW_ID*, and calibrated together if required.
:    

**ANTENNA*n***
:   Antenna identifier, as indexed from *ANTENNAn* in *MAIN*.

**FEED_ID**
:   Antenna identifier, as indexed from *FEEDn* in *MAIN*.

**SPECTRAL_WINDOW_ID**
:   Spectral window identifier.

**TIME**
:   Mid-point of the time interval for which this offset is valid. Required to use the same TIME Measure reference as used in *MAIN*.

**INTERVAL**
:   Time interval.

**OFFSET**
:   Frequency offset to be added to the frequency axis for this spectral window, as defined in the SPECTRAL_WINDOW sub-table. Required to have the same Frequency Measure reference as CHAN_FREQ in that table.

## HISTORY: History Information

**HISTORY: History information**

Name

Format

Units

Measure

Comments

**Columns**

*Key*

TIME 

Double 

s 

EPOCH 

Time-stamp for message

OBSERVATION_ID 

Int 

 

 

Points to OBSERVATION table

*Data*

MESSAGE 

String 

 

 

Log message

PRIORITY 

String 

 

 

Message priority

ORIGIN 

String 

 

 

Code origin

OBJECT_ID 

String 

 

 

Originating ObjectID 

APPLICATION 

String 

 

 

Application name

CLI_COMMAND 

String(\*) 

 

 

CLI command sequence 

APP_PARAMS 

String(\*) 

 

 

Application paramters

**Notes:**
:   This sub-table contains associated history information for the MS.
:    

**TIME**
:   Time-stamp for the history record. Required to have the same TIME Measure reference as used in *MAIN*.

**OBSERVATION_ID**
:   Observation identifier (see the *OBSERVATION* table)

**MESSAGE**
:   Log message.

**PRIORITY**
:   Message priority, with allowed types: (\"DEBUGGING\", \"WARN\", \"NORMAL\", or \"SEVERE\").

**ORIGIN**
:   Source code origin from which message originated.

**OBJECT_ID**
:   Originating ObjectID, if available, else blank.

**APPLICATION**
:   Application name.

**CLI_COMMAND**
:   CLI command sequence invoking the application.

**APP_PARAMS**
:   Application parameter values, in the adopted project-wide format.

## OBSERVATION: Observation Information

**OBSERVATION: Observation information**

Name

Format

Units

Measure

Comments

**Columns**

*Data*

TELESCOPE_NAME 

String 

 

 

Telescope name

TIME_RANGE 

Double(2) 

s 

EPOCH 

Start, end times

OBSERVER 

String 

 

 

Name of observer(s)

LOG 

String(\*) 

 

 

Observing log 

SCHEDULE_TYPE 

String 

 

 

Schedule type

SCHEDULE 

String(\*) 

 

 

Project schedule

PROJECT 

String 

 

 

Project identification string.

RELEASE_DATE 

Double 

s 

EPOCH 

Target release date

*Flags*

FLAG_ROW 

Bool 

 

 

Row flag. 

**Notes:**
:   This table contains information specifying the observing instrument or epoch. See the discussion in Section 3.3 for details. It is indexed directly from *MAIN* via *OBSERVATION_ID*.
:   

**TELESCOPE_NAME**
:   Telescope name (e.g. \"WSRT\" or \"VLBA\").

**TIME_RANGE**
:   The start and end times of the overall observing period spanned by the actual recorded data in *MAIN*. Required to use the same TIME Measure reference as in *MAIN*.

**OBSERVER**
:   The name(s) of the observer(s).

**LOG**
:   The observing log, as supplied by the telescope or instrument.

**SCHEDULE_TYPE**
:   The schedule type, with current reserved types (\"VLBA-CRD\", \"VEX\", \"WSRT\", \"ATNF\").

**SCHEDULE**
:   Unmodified schedule file, of the type specified, and as used by the instrument.

**PROJECT**
:   Project code (e.g. \"BD46\")

**RELEASE_DATE**
:   Project release date. This is the date on which the data may become public.

**FLAG_ROW**
:   Row flag. True if data in this row is invalid, but does not imply any flagging in *MAIN*.
:   

## POINTING: Antenna Pointing Information

**POINTING: Antenna pointing information**

Name

Format

Units

Measure

Comments

**Columns**

*Key*

ANTENNA_ID 

Int 

 

 

Antenna id.

TIME 

Double 

s 

EPOCH 

Interval midpoint

INTERVAL 

Double 

s 

 

Time interval

*Data*

NAME 

String 

 

 

Pointing position desc.

NUM_POLY 

Int 

 

 

Series order 

TIME_ORIGIN 

Double 

s 

EPOCH 

Origin for the polynomial

DIRECTION 

Double(2, NUM_POLY+1) 

rad 

DIRECTION 

Antenna pointing direction

TARGET 

Double(2, NUM_POLY+1) 

rad 

DIRECTION 

Target direction 

*(POINTING_OFFSET)*

Double(2, NUM_POLY+1) 

rad 

DIRECTION 

A priori pointing correction 

*(SOURCE_OFFSET)*

Double(2, NUM_POLY+1) 

rad 

DIRECTION 

Offset from source

*(ENCODER)*

Double(2) 

rad 

DIRECTION 

Encoder values

*(POINTING_MODEL_ID)*

Int 

 

 

Pointing model id. 

TRACKING 

Bool 

 

 

True if on-position 

*(ON_SOURCE)*

Bool 

 

 

True if on-source

*(OVER_THE_TOP)*

Bool 

 

 

True if over the top

**Notes:**

:   This table contains information concerning the primary pointing direction of each antenna as a function of time. Note that the pointing offsets for inidividual feeds on a given antenna are specified in the *FEED* sub-table with respect to this pointing direction.

     

**ANTENNA_ID**
:   Antenna identifier, as specified by *ANTENNAn* in *MAIN*.

**TIME**
:   Mid-point of the time interval for which the information in this row is valid. Required to use the same TIME Measure reference as in *MAIN*.

**INTERVAL**
:   Time interval.

**NAME**
:   Pointing direction name; user specified.

**NUM_POLY**
:   Series order for the polynomial expressions in *DIRECTION* and *POINTING_OFFSET*.

**TIME_ORIGIN**
:   Time origin for the polynomial expansions.

**DIRECTION**
:   Antenna pointing direction, optionally expressed as polynomial coefficients. The final result is interpreted as a Direction Measure using the specified Measure reference. 

**TARGET**
:   Target pointing direction, optionally expressed as polynomial coefficients. The final result is interpreted as a Direction Measure using the specified Measure reference. This is the true expected position of the source, including all coordinate corrections such as precession, nutation etc.

**POINTING_OFFSET**
:   The a priori pointing corrections applied by the telescope in pointing to the *DIRECTION* position, optionally expressed as polynomial coefficients. The final result is interpreted as a Direction Measure using the specified Measure reference.

**SOURCE_OFFSET**
:   The commanded offset from the source position, if offset pointing is being used.

**ENCODER**
:   The current encoder values on the primary axes of the mount type for the antenna, expressed as a Direction Measure.

**TRACKING**
:   True if tracking the nominal pointing position.

**ON-SOURCE**
:   True if the nominal pointing direction coincides with the source, i.e. offset-pointing is not being used.

**OVER-THE-TOP**
:   True if the antenna was driven to this position \"over the top\" (az-el mount).

 

## POLARIZATION: Polarization Setup Information

**POLARIZATION: Polarization setup information**

Name

Format

Units

Measure

Comments

**Columns**

*Data description columns*

NUM_CORR 

Int 

 

 

\# correlations

*Data*

CORR_TYPE 

Int(NUM_CORR) 

 

 

Polarization of correlation 

CORR_PRODUCT 

Int(2, NUM_CORR) 

 

 

Receptor cross-products 

*Flags*

FLAG_ROW 

Bool 

 

 

Row flag

**Notes:**

:   This table defines the polarization labeling of the *DATA* array in *MAIN*, and is directly indexed from the *DATA_DESCRIPTION* table via *POLARIZATION_ID*.

     

**NUM_CORR**
:   The number of correlation polarization products. For example, for (RR) this value would be 1, for (RR, LL) it would be 2, and for (XX,YY,XY,YX) it would be 4, etc.

**CORR_TYPE**
:   An integer for each correlation product indicating the Stokes type as defined in the Stokes class enumeration.

**CORR_PRODUCT**
:   Pair of integers for each correlation product, specifying the receptors from which the signal originated. The receptor polarization is defined in the *POLARIZATION_TYPE* column in the *FEED* table. An example would be (0,0), (0,1), (1,0), (1,1) to specify all correlations between two receptors.

**FLAG_ROW**
:   Row flag. True is the data in this row are not valid, but does not imply the flagging of any *DATA* in *MAIN*.

 

## PROCESSOR: Processor Information

**PROCESSOR: Processor information**

Name

Format

Units

Measure

Comments

**Columns**

*Data*

TYPE 

String 

 

 

Processor type 

SUB_TYPE 

String 

 

 

Processor sub-type

TYPE_ID 

Int 

 

 

Processor type id.

MODE_ID 

Int 

 

 

Processor mode id.

*(PASS_ID)*

Int 

 

 

Processor pass number

*Flags*

FLAG_ROW 

Bool 

 

 

Row flag

**Notes:**

:   This table holds summary information for the back-end processing device used to generate the basic data in the MAIN table. Such devices include correlators, radiometers, spectrometers, pulsar-timers, amongst others. See Section 4.0.4 for further details.

     

**TYPE**
:   Processor type; reserved keywords include (\"CORRELATOR\" - interferometric correlator; \"SPECTROMETER\" - single-dish correlator; \"RADIOMETER\" - generic detector/integrator; \"PULSAR-TIMER\" - pulsar timing device).

**SUB_TYPE**
:   Processor sub-type, e.g. \"GBT\" or \"JIVE\".

**TYPE_ID**
:   Index used in a specialized sub-table named as *subtype_type*, which contains time-independent processor information applicable to the current data record (e.g. a JIVE_CORRELATOR sub-table). Time-dependent information for each device family is contained in other tables, dependent on the device type.

**MODE_ID**
:   Index used in a specialized sub-table named as *subtype_type_mode*, containing information on the processor mode applicable to the current data record. (e.g. a *GBT_SPECTROMETER_MODE* sub-table).

**PASS_ID**
:   Pass identifier; this is used to distinguish data records produced by multiple passes through the same device, where this is possible (e.g. VLBI correlators). Used as an index into the associated table containing pass information.

**FLAG_ROW**
:   Row flag. True if data in the row is not valid, but does not imply flagging in *MAIN*.

 

## SOURCE: Source Information

**SOURCE: Source information**

Name

Format

Units

Measure

Comments

**Columns**

*Key*

SOURCE_ID 

Int 

 

 

Source id

TIME 

Double 

s 

EPOCH 

Midpoint of time for which this set of parameters is accurate

INTERVAL 

Double 

s 

 

Interval

SPECTRAL_WINDOW_ID 

Int 

 

 

Spectral Window id

*Data description*

NUM_LINES 

Int 

 

 

Number of spectral lines

*Data*

NAME 

String 

 

 

Name of source as given during observations

CALIBRATION_GROUP 

Int 

 

 

\# grouping for calibration purpose

CODE 

String 

 

 

Special characteristics of source, e.g. Bandpass calibrator

DIRECTION 

Double(2) 

rad 

DIRECTION 

Direction (e.g. RA, DEC) 

*(POSITION)*

Double(3) 

m 

POSITION 

Position (e.g. for solar system objects) 

PROPER_MOTION 

Double(2) 

rad/s 

 

Proper motion 

*(TRANSITION)*

String(NUM_LINES) 

 

 

Transition name

*(REST_FREQUENCY)*

Double(NUM_LINES) 

Hz 

FREQUENCY 

Line rest frequency

*(SYSVEL)*

Double(NUM_LINES) 

m/s 

RADIAL VELOCITY 

Systemic velocity at reference 

*(SOURCE_MODEL)*

TableRecord 

 

 

Default csm 

*(PULSAR_ID)*

Int 

 

 

Pulsar id. 

**Notes:**

:   This table contains time-variable source information, optionally associated with a given FIELD_ID.

     

**SOURCE_ID**
:   Source identifier (≥ 0), as specified in the *FIELD* sub-table.

**TIME**
:   Mid-point of the time interval for which the data in this row is valid. Required to use the same TIME Measure reference as in *MAIN*.

**INTERVAL**
:   Time interval.

**SPECTRAL_WINDOW_ID**
:   Spectral window identifier. A -1 indicates that the row is valid for all spectral windows.

**NUM_LINES**
:   Number of spectral line transitions associated with this source and spectral window id. combination.

**NAME**
:   Source name; user specified.

**CALIBRATION_GROUP**
:   Calibration group number to which this source belongs; user specified.

**CODE**
:   Source code, used to describe any special characteristics f the source, such as the nature of a calibrator. Reserved keyword, including (\"BANDPASS CAL\").

**DIRECTION**
:   Source direction at this TIME.

**POSITION**
:   Source position (*x*, *y*, *z*) at this TIME (for near-field objects).

**PROPER_MOTION**
:   Source proper motion at this TIME.

**TRANSITION**
:   Transition names applicable for this spectral window (e.g. \"v=1, J=1-0, SiO\").

**REST_FREQUENCY**
:   Rest frequencies for the transitions.

**SYSVEL**
:   Systemic velocity for each transition.

**SOURCE_MODEL**
:   Reference to an assigned component source model table.

**PULSAR_ID**
:   An index used in the *PULSAR* sub-table to define further pulsar-specific properties if the source is a pulsar.

 

## SPECTRAL_WINDOW: Spectral Window Description

**SPECTRAL_WINDOW: Spectral window description**

Name

Format

Units

Measure

Comments

**Columns**

*Data description columns*

NUM_CHAN 

Int 

 

 

\# spectral channels 

*Data*

NAME 

String 

 

 

Spectral window name

REF_FREQUENCY 

Double 

Hz 

FREQUENCY

The reference frequency.

CHAN_FREQ 

Double(NUM_CHAN) 

Hz 

FREQUENCY

Center frequencies for each channel in the data matrix.

CHAN_WIDTH 

Double(NUM_CHAN) 

Hz 

 

Channel width for each channel in the data matrix.

MEAS_FREQ_REF 

Int 

 

 

FREQUENCY Measure ref.

EFFECTIVE_BW 

Double(NUM_CHAN) 

Hz 

 

The effective noise bandwidth of each spectral channel

RESOLUTION 

Double(NUM_CHAN) 

Hz 

 

The effective spectral resolution of each channel

TOTAL_BANDWIDTH 

Double 

Hz 

 

total bandwidth for this window 

NET_SIDEBAND 

Int 

 

 

Net sideband

*(BBC_NO)*

Int 

 

 

Baseband converter no.

*(BBC_SIDEBAND)*

Int 

 

 

BBC sideband

IF_CONV_CHAIN 

Int 

 

 

The IF conversion chain 

*(RECEIVER_ID)*

Int 

 

 

Receiver id.

FREQ_GROUP 

Int 

 

 

Frequency group

FREQ_GROUP_NAME 

String 

 

 

Freq. group name 

*(DOPPLER_ID)*

Int 

 

 

Doppler id.

*(ASSOC_SPW_ID)*

Int(\*) 

 

 

Associated spw_id.

*(ASSOC_NATURE)*

String(\*) 

 

 

Nature of association

Flags

FLAG_ROW 

Bool 

 

 

 

 

 

 

 

 

**Notes:**

:   This table describes properties for each defined spectral window. A spectral window is both a frequency label for the associated DATA array in MAIN, but also represents a generic frequency conversion chain that shares joint physical properties and makes sense to calibrate as a single entity.

     

**NUM_CHAN**
:   Number of spectral channels.

**NAME**
:   Spectral window name; user specified.

**REF_FREQUENCY**
:   The reference frequency. A frequency representative of this spectral window, usually the sky frequency corresponding to the DC edge of the baseband. Used by the calibration system if a fixed scaling frequency is required or in algorithms to identify the observing band.

**CHAN_FREQ**
:   Center frequencies for each channel in the data matrix. These can be frequency-dependent, to accommodate instruments such as acousto-optical spectrometers. Note that the channel frequencies may be in ascending or descending frequency order.

**CHAN_WIDTH**
:   Nomical channel width of each spectral channel. Although these can be derived from *CHAN_FREQ* by differencing, it is more efficient to keep a separate reference to this information.

**MEAS_FREQ_REF**
:   Frequency Measure reference for *CHAN_FREQ*. This allows a row-based reference for this column in order to optimize the choice of Measure reference when Doppler tracking is used. Modified only by the MS access code.

**EFFECTIVE_BW**
:   The effective noise bandwidth of each spectral channel.

**RESOLUTION**
:   The effective spectral resolution of each channel.

**TOTAL_BANDWIDTH**
:   The total bandwidth for this spectral window.

**NET_SIDEBAND**
:   The net sideband for this spectral window.

**BBC_NO**
:   The baseband converter number, if applicable.

**BBC_SIDEBAND**
:   The baseband converter sideband, is applicable.

**IF_CONV_CHAIN**
:   Identification of the electronic signal path for the case of multiple (simultaneous) IFs. (e.g. VLA: AC=0, BD=1, ATCA: Freq1=0, Freq2=1)

**RECEIVER_ID**
:   Index used to identify the receiver associated with the spectral window. Further state information is planned to be stored in a RECEIVER sub-table.

**FREQ_GROUP**
:   The frequency group to which the spectral window belongs. This is used to associate spectral windows for joint calibration purposes.

**FREQ_GROUP_NAME**
:   The frequency group name; user specified.

**DOPPLER_ID**
:   The Doppler identifier defining frame information for this spectral window.

**ASSOC_SPW_ID**
:   Associated spectral windows, which are related in some fashion (e.g. \"channel-zero\").

**ASSOC_NATURE**
:   Nature of the association for ASSOC_SPW_ID; reserved keywords are (\"CHANNEL-ZERO\" - channel zero; \"EQUAL-FREQUENCY\" - same frequency labels; \"SUBSET\" - narrow-band subset).

**FLAG_ROW**
:   True if the row does not contain valid data.

 

## STATE: State Information

**STATE: State information**

Name

Format

Units

Measure

Comments

**Columns**

*Data*

SIG 

Bool 

 

 

Signal 

REF 

Bool 

 

 

Reference 

CAL 

Double 

K 

 

Noise calibration 

LOAD 

Double 

K 

 

Load temperature

SUB_SCAN 

Int 

 

 

Sub-scan number

OBS_MODE 

String 

 

 

Observing mode

*Flags*

FLAG_ROW 

Bool 

 

 

Row flag

**Notes:**

:   This table defines the state parameters for a particular data record as they refer to external loads, calibration sources or references, and also characterizes the observing mode of the data record, as an aid to defining the scheduling heuristics. It is indexed directly via STATE_ID in *MAIN*.

     

**SIG**
:   True if the source signal is being observed.

**REF**
:   True for a reference phase.

**CAL**
:   Noise calibration temperature (zero if not added).

**LOAD**
:   Load temperature (zero if no load).

**SUB_SCAN**
:   Sub-scan number (≥ 0), relative to the *SCAN_NUMBER* in MAIN. Used to identify observing sequences.

**OBS_MODE**
:   Observing mode; defined by a set of reserved keywords characterizing the current observing mode (e.g. \"OFF-SPECTRUM\"). Used to define the schedule strategy.

**FLAG_ROW**
:   True if the row does not contain valid data. Does not imply flagging in *MAIN*.

 

## SYSCAL: System Calibration

**SYSCAL: System calibration**

Name

Format

Units

Measure

Comments

**Columns**

*Key*

ANTENNA_ID 

Int 

 

 

Antenna id

FEED_ID 

Int 

 

 

Feed id

SPECTRAL_WINDOW_ID 

Int 

 

 

Spectral window id

TIME 

Double 

s 

EPOCH 

Midpoint of time for which this set of parameters is accurate

INTERVAL 

Double 

s 

 

Interval

*Data*

*(PHASE_DIFF)*

Float 

rad 

 

Phase difference between receptor 0 and receptor 1

*(TCAL)*

Float (*N*~r~) 

K 

 

Calibration temp

*(TRX)*

Float (*N*~r~) 

K 

 

Receiver temperature

*(TSKY)*

Float (*N*~r~) 

K 

 

Sky temperature

*(TSYS)*

Float (*N*~r~) 

K 

 

System temp

*(TANT)*

Float (*N*~r~) 

K 

 

Antenna temperature

*(TANT_TSYS)*

Float(*N*~r~) 

 

 

$ {{T_{ant}}\over{T_{sys}}}$

*(TCAL_SPECTRUM)*

Float (*N*~r~, *N*~f~) 

K 

 

Calibration temp

*(TRX_SPECTRUM)*

Float (*N*~r~, *N*~f~) 

K 

 

Receiver temperature

*(TSKY_SPECTRUM)*

Float (*N*~r~, *N*~f~) 

K 

 

Sky temperature spectrum

*(TSYS_SPECTRUM)*

Float (*N*~r~, *N*~f~) 

K 

 

System temp

*(TANT_SPECTRUM)*

Float (*N*~r~, *N*~f~) 

K 

 

Antenna temperature spectrum

*(TANT_TSYS_SPECTRUM)*

Float (*N*~r~,*N*~f~) 

 

 

$ {{T_{ant}}\over{T_{sys}}}$ spectrum

*Flags*

*(PHASE_DIFF_FLAG)*

Bool 

 

 

Flag for PHASE_DIFF

*(TCAL_FLAG)*

Bool 

 

 

Flag for TCAL

*(TRX_FLAG)*

Bool 

 

 

Flag for TRX

*(TSKY_FLAG)*

Bool 

 

 

Flag for TSKY

*(TSYS_FLAG)*

Bool 

 

 

Flag for TSYS

*(TANT_FLAG)*

Bool 

 

 

Flag for TANT

*(TANT_TSYS_FLAG)*

Bool 

 

 

Flag for ${{T_{ant}}\over{T_{sys}}}$

**Notes:**

:   This table contains time-variable calibration measurements for each antenna, as indexed on feed and spectral window. Note that *N*~r~= number of receptors, and *N*~f~= number of frequency channels.

     

**ANTENNA_ID**
:   Antenna identifier, as indexed by *ANTENNAn* in *MAIN*.

**FEED_ID**
:   Feed identifier, as indexed by *FEEDn* in *MAIN*.

**SPECTRAL_WINDOW_ID**
:   Spectral window identifier.

**TIME**
:   Mid-point of the time interval for which the data in this row are valid. Required to use the same TIME Measure reference as that in *MAIN*.

**INTERVAL**
:   Time interval.

**PHASE_DIFF**
:   Phase difference between receptor 0 and receptor 1.

**TCAL**
:   Calibration temperature.

**TRX**
:   Receiver temperature.

**TSKY**
:   Sky temperature.

**TSYS**
:   System temperature.

**TANT**
:   Antenna temperature.

**TANT_TSYS**
:   Antenna temperature over system temperature.

**TCAL_SPECTRUM**
:   Calibration temperature spectrum.

**TRX_SPECTRUM**
:   Receiver temperature spectrum.

**TSKY_SPECTRUM**
:   Sky temperature spectrum.

**TSYS_SPECTRUM**
:   System temperature spectrum.

**TANT_SPECTRUM**
:   Antenna temperature spectrum.

**TANT_TSYS_SPECTRUM**
:   Antenna temperature over system temperature spectrum.

**PHASE_DIFF_FLAG**
:   True if *PHASE_DIFF* flagged.

**TCAL_FLAG**
:   True if *TCAL* flagged.

**TRX_FLAG**
:   True if *TRX* flagged.

**TSKY_FLAG**
:   True if *TSKY* flagged.

**TSYS_FLAG**
:   True if *TSYS* flagged.

**TANT_FLAG**
:   True if *TANT* flagged.

**TANT_TSYS_FLAG**
:   True if *TANT_TSYS* flagged.

 

## WEATHER: Weather Station Information

**WEATHER: weather station information**

Name

Format

Units

Measure

Comments

**Columns**

*Key*

ANTENNA_ID 

Int 

 

 

Antenna number

TIME 

Double 

s 

EPOCH 

Mid-point of interval

INTERVAL 

Double 

s 

 

Interval over which data is relevant

*Data*

*(H2O)*

Float 

*m*^-2^

 

Average column density of water

*(IONOS_ELECTRON)*

Float 

*m*^-2^

 

Average column density of electrons

*(PRESSURE)*

Float 

hPa 

 

Ambient atmospheric pressure

*(REL_HUMIDITY)*

Float 

 

 

Ambient relative humidity

*(TEMPERATURE)*

Float 

K 

 

Ambient air temperature for an antenna

*(DEW_POINT)*

Float 

K 

 

Dew point 

*(WIND_DIRECTION)*

Float 

rad 

 

Average wind direction

*(WIND_SPEED)*

Float 

m/s 

 

Average wind speed 

*Flags*

*(H2O_FLAG)*

Bool 

 

 

Flag for H2O 

*(IONOS_ELECTRON_FLAG)*

Bool 

 

 

Flag for IONOS_ELECTRON 

*(PRESSURE_FLAG)*

Bool 

 

 

Flag for PRESSURE 

*(REL_HUMIDITY_FLAG)*

Bool 

 

 

Flag for REL_HUMIDITY 

*(TEMPERATURE_FLAG)*

Bool 

 

 

Flag for TEMPERATURE 

*(DEW_POINT_FLAG)*

Bool 

 

 

Flag for DEW_POINT 

*(WIND_DIRECTION_FLAG)*

Bool 

 

 

Flag for WIND_DIRECTION 

*(WIND_SPEED_FLAG)*

Bool 

 

 

Flag for WIND_SPEED 

**Notes:**

:   This table contains mean external atmosphere and weather information.

     

**ANTENNA_ID**
:   Antenna identifier, as indexed by *ANTENNAn* from *MAIN*.

**TIME**
:   Mid-point of the time interval over which the data in the row are valid. Required to use the same TIME Measure reference as in *MAIN*.

**INTERVAL**
:   Time interval.

**H2O**
:   Average column density of water.

**IONOS_ELECTRON**
:   Average column density of electrons.

**PRESSURE**
:   Ambient atmospheric pressure.

**REL_HUMIDITY**
:   Ambient relative humidity.

**TEMPERATURE**
:   Ambient air temperature.

**DEW_POINT**
:   Dew point temperature.

**WIND_DIRECTION**
:   Average wind direction.

**WIND_SPEED**
:   Average wind speed.

**H2O_FLAG**
:   Flag for H2O.

**IONOS_ELECTRON_FLAG**
:   Flag for IONOS_ELECTRON.

**PRESSURE_FLAG**
:   Flag for PRESSURE.

**REL_HUMIDITY_FLAG**
:   Flag for REL_HUMIDITY.

**TEMPERATURE_FLAG**
:   Flag for TEMPERATURE.

**DEW_POINT_FLAG**
:   Flag for DEW_POINT.

**WIND_DIRECTION_FLAG**
:   Flag for DEW_POINT.

**WIND_SPEED_FLAG**
:   Flag for DEW_POINT.

 

# Bibliography

1. [Kemball\ &\ Wieringa\ 2000](https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/229.pdf)\ 
^

