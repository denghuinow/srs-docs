# Short Summary

- **Background and objectives**: GAMMA-J Web Store is a plug-and-play USB-based e-commerce system designed to help new online store owners quickly set up and manage sales over the internet, with secure and reliable operation.

- **In scope**:
  - Customer account creation and management.
  - Online inventory management with multi-tiered categories.
  - Shopping cart functionality for item storage and checkout.
  - Secure order confirmation and email notifications.
  - Plug-in API for future system enhancements.

- **Out of scope**:
  - Telephonic order integration.
  - Internal tracking number and transportation system.
  - Customer order analysis features.
  - Support for browsers other than IE 6/7 and Netscape 4/5.
  - Responsibility for Yoggie-provided OS and USB hardware functionality.

- **Roles and core use cases**:
  - As a **Customer**, I want to browse products and complete purchases so that I can buy items securely.
  - As a **Sales Personnel**, I want to update product details and inventory so that the store catalog remains accurate.
  - As a **System Administrator**, I want to manage user accounts and install plug-ins so that the system remains secure and extensible.

- **Success metrics**:
  - System availability of 99.99%.
  - Support for 1000 concurrent customer logins.
  - Product search results returned in under 1 second.

- **Major constraints**:
  - Must use SQL-based database.
  - Compatible only with specified browser versions.
  - Runs on Yoggie USB hardware with Slackware Linux and Apache.
  - Uses SSL for security and encrypted data storage.
  - Plug-and-play deployment with no software installation required.

- **Undecided issues**:
  - Transition strategy from telephonic to online orders.
  - Future module for generating tracking numbers.
  - Customer order analysis capability.
  - Not mentioned.
  - Not mentioned.