# Ultra Short Summary
The EVLA Correlator Backend System is a real-time astronomical data processing pipeline that receives correlator data, performs processing, and delivers formatted results to the End-to-End System.

- Receive real-time lag data from the Correlator and assemble it into time series.
- Perform Fourier Transforms and user-selected processing on the time series.
- Deliver formatted spectra and metadata to the End-to-End System.
- Monitor system health and perform automatic recovery from failures.

- Must handle an input data rate of at least 1.6 Gbytes/sec from the Correlator.
- Must deliver an output data rate of at least 25 MBytes/sec to the End-to-End System.
- All processing must be reversible so raw input data can be recovered from the output.

- Not mentioned
- Not mentioned