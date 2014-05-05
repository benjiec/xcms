
XCMS Extensions and Fixes
=========================

Ginkgo Bioworks' version of XCMS. Originally "forked" from version 1.39.2 from
Bioconductor (http://www.bioconductor.org/packages/devel/bioc/html/xcms.html).

Main changes are 

  1. Improved centWave peak detection 

    With this change, XCMS now picks the best scale for a peak using CWT
    coefficient, rather than fixed area integration. Using fixed area
    integration tends to favor narrower peak shape, even though a broader peak
    shape is better. To fine tune a broad peak, XCMS now narrows down the RT
    range of a peak by skipping regions less than 1% of the max intensity,
    rather than skipping regions with 0 intensities.

    See commit 7a12243565

  2. Improved centWave peak integration

    Add Tony Larson's integration improvement, to handle non-uniform scan
    densities. See https://groups.google.com/forum/#!topic/xcms-devel/bdkvPGSWOU0

    See commit 1980288a05

  3. Added targeted peak detection to centWave

    Prior to this change, XCMS does not pickup weak peaks consistently or at
    all. I believe XCMS fails to pickup these peaks for three reasons.

    1) XCMS tries to identify "regions of interest" (ROI) prior to peak
    detection and integration. It may fail to pick up a weak peak with only a
    few spikes spanning several scans as an ROI.

    2) XCMS can only pick up ROIs with contiguous scans. This was mentioned in
    the centWave peak detection paper, and correlates with behavior of the
    code. To handle weak peaks with scan gaps, XCMS extends each ROI laterally
    (in time domain) by a multiple of the specified minimum peak width, prior
    to running peak detection on the ROI. But if the specified minimum peak
    width is small, this lateral extension may not pick up all the scans that
    make up the real peak.

    3) XCMS throws away an ROI if it believes there aren't enough above-noise
    signals in the ROI. XCMS determines the noise level locally, from an
    average of the signals in the ROI. For weak peaks from equipment with low
    real detector noise, real signals can be considered as noise, causing an
    ROI with weak peak to be thrown away before peak detection.

    "targeted centWave" works around all three of these problems. 
    
    A) User defines each target as a triple (mz range, scan range, peak width
    range) and provides a target list to centWave.
    
    B) For each target, "targeted centWave" constructs an ROI that covers the
    mz and scan ranges of the target, and runs CWT peak detection on that ROI,
    using the peak width range of the target. CWT peak detection works over
    large scan ranges and can pick up multiple peaks within the scan range. 
    
    C) For each detected peak, instead of walking down from detected peak
    center to find RT boundaries and integrating between the boundaries,
    "targeted centWave" uses the peak shape with the best CWT coefficient to
    compute RT boundaries, removing regions less than 10% of max intensity at
    each end to remove trailing noise. This last integration techique
    (integrate=3 option to centWave) also works when running centWave in
    untargeted mode.  
    
    D) Finally, in targeted mode, user can set snthresh=1 for peak detection,
    bypassing centWave's noise estimation code. Because user also specifies the
    optimal peak width for the target, only and all peaks matching those
    optimal peak width are returned, regardless of the computed signal to noise
    ratio.

    See commit 8ca593a551


Compile and Use
---------------

To install to ~/R, run ". install_xcms".

Alternatively, you can run "python setup.py install" or include this repository
in your Python project's requirements.txt file.

To use this copy of the XCMS library, run the following in R (lib.loc specifies
where package is installed).

> library(xcms,lib.loc='~/R')

or run R with the following environment variable: R_LIBS_USER=~/R


Acknowledgment
--------------

We at Ginkgo Bioworks are indebted to the XCMS team for creating and improving
XCMS over the years.
