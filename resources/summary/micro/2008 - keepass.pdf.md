**Purpose & Scope**: Securely store and manage user passwords and credentials in an encrypted database, accessible via a single master key.

**Core Functions**:
*   Create, open, and save an encrypted password database.
*   Add, view, edit, and delete credential entries within organized groups.
*   Generate and use passwords, including one-time TANs.

**Key Constraints**:
*   The database is locked by a composite master key (password and/or key file); loss results in permanent, unrecoverable data loss.
*   A copied password remains available in memory for only 10 seconds.
*   Must run on specified 32-bit MS Windows operating systems and WINE.