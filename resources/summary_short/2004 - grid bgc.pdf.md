# Short Summary

- **Background and objectives**: Develop a grid-based software infrastructure to support bio-geo-chemical modeling using Daymet and Biome-BGC models, providing a graphical user interface and leveraging grid technologies for secure remote computing.

- **In scope**:
  - User account management with NCAR Gatekeeper integration.
  - Data organization into objects and projects for modeling workflows.
  - Support for Daymet and BiomeBGC modeling runs with input/output handling.
  - Template-based object sharing and collaboration features.
  - Web portal interface for all system functions.

- **Out of scope**:
  - Visualization features (marked as low priority).
  - Resource quotas implementation (lowest priority).
  - Data user functionality (lowest priority user class).
  - Non-NCAR Gatekeeper authentication methods.
  - Custom data validation during merge operations.

- **Roles and core use cases**:
  - As a Scientist, I want to manage input data and run simulations so that I can perform BGC modeling and analysis.
  - As a Portal Administrator, I want to manage user accounts and system operations so that the portal runs smoothly and securely.
  - As a Data User, I want to access simulation output data so that I can use it for research without running models.

- **Success metrics**:
  - Successful execution of Daymet and BiomeBGC modeling runs.
  - User ability to share and reuse objects and templates.
  - Secure and reliable access to remote computational resources.

- **Major constraints**:
  - Must use the Globus toolkit.
  - Must comply with NCAR security policies.
  - Must use NCAR Mass Storage System for all file storage.
  - Must support specified web browsers (IE 6.0, Netscape 7.1, Safari 1.2.1).
  - Requires users to enable cookies.

- **Undecided issues**:
  - Visualization implementation details.
  - Resource quota enforcement.
  - Data publication integration method.
  - MSS access credential handling.
  - Specific system settings for admin control.