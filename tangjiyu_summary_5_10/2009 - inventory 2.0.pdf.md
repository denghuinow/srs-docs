# Inventory Management Software Requirements Specification

## 1. Introduction

### 1.1 Purpose
Define requirements of the Inventory Management System proposed by Construction Junction (CJ) staff.

### 1.2 Scope
Creation of a categorized Inventory Management System providing functionality identified by Construction Junction team. Requirements are prioritized by business and technical sponsors.

### 1.3 Audience
Intended for Construction Junction team, individual developers, and system architect.

## 2. Overview

### 2.1 Actors
- Administrator: Perform any Inventory Management functions
- Director: Same as Manager plus view/create/modify/delete Inventory Management users
- Manager: Same as Receiving Associate plus change item properties
- Receiving Associate: Receives donated items, initial entry into system, provides donation receipts
- Customer Service Representative: Constituent/member database management, item returns processing, create drop-off acquisitions
- Pickup Associate: Picks up donated items, brings for processing
- Decon Associate: Executes deconstruction/strip out job, brings items for processing
- Sales Associate: Processes purchases by customers
- Donor: Individual/organization donating items, receives tax deduction
- Buyer: Customer purchasing items
- Primary Contact: Individual who is primary contact for donation
- Vendor: Individual/organization selling items to be added to inventory
- Consigner: Individual donating items under consignment

## 3. Detailed Functional Requirements

### 3.1 View Inventory
Provide categorized view of entire inventory to Construction Junction staff. Navigation from department level through categories and sub-categories to individual items.

### 3.2 Manage Departments
Allow inventory administrators to customize inventory structure by defining departments.

Key requirements:
- Add/Edit/Delete departments
- Department Name, POS Department Code, Unique Tag are mandatory
- Department Name and Unique Tag must be unique
- POS Department Code max 3 characters
- Unique Tag max 18 characters
- Cannot delete department if it contains categories/items

### 3.3 Manage Categories
Allow inventory administrators to customize inventory structure by defining categories.

Key requirements:
- Add/Edit/Delete categories (Unique Item and Stock Item types)
- Move categories between departments/categories
- Category Name and Unique Tag are mandatory and must be unique
- Unique Tag max 18 characters
- When Stock Item Category is created/updated, corresponding item is added/updated in QuickBooks POS

### 3.4 Manage Attributes and Details
Allow inventory administrators to customize attributes and details available for each inventory item.

Key requirements:
- Attributes defined per department (Material, Finish, Color, Features)
- Details defined per department/category
- Attribute/Detail Name must be unique
- Support for Number, Text, Selection detail types

### 3.5 Add Item to Inventory
Items added through donation processes or routine inventory maintenance.

Key requirements:
- Items can be added at any level in categorized inventory
- Only unique and stock items tracked by system
- Integration with QuickBooks POS for item creation/quantity updates
- Mandatory fields vary by item type:
  - Unique items: Quantity, Condition, Price, Description (for generic categories)
  - Stock items: None (all fields pre-set)
  - Under $5 items: Description
- System makes pricing recommendations

### 3.6 Manage Inventory Items
Allow various management actions on existing inventory items (modify, delete, split, view details/history).

Key requirements:
- Only available for Unique and Stock items
- Modify item properties (except system-generated item number)
- Adjust item quantity with reason specification
- Split item into multiple items
- View item history including: item added, price set/changed, item sold, quantity adjusted, item split

### 3.7 Suggest Item Price
Assist in pricing new inventory items by making suggestions based on similar items.

Key requirements:
- Only applicable to Unique items
- Based on historical data for items of same department, category, condition
- Configuration parameters: time period (6 months, 12 months, all), include/exclude item attributes
- Display historical original/sale price information (lowest, mean, highest)

### 3.8 View Acquisitions
View all past and current acquisitions (Drop-Off, Pickup, Decon donations).

Key requirements:
- Display acquisition information: Number, Type, Donor Name, Primary Contact, Start/End Date, Status
- Filter by Type, Donor/Primary Contact Name, Acquisition Number, Phone Number, Status
- Sort by any column (default: descending order of End Date)
- Integration with CRM system for acquisition creation

### 3.9 Receive Acquisition
Process donor items at receiving dock and generate donation receipt.

Key requirements:
- Donor arrives with valid acquisition number or new acquisition created
- Enter information about donated items
- Generate/print donation receipt with: date, item list, Construction Junction representative info, tax deduction info
- Print item tags for unique and stock items
- Support for items set aside for further processing
- Integration with CRM for acquisition updates

### 3.10 Sell Item
Process item purchase by Construction Junction customer.

Key requirements:
- Integration with QuickBooks POS
- Update inventory to reflect sale (sale price, quantity on hand)
- Sale price doesn't override original item price
- Quantity decremented by quantity sold

### 3.11 Reports
Generate reports on inventory, inventory type, donor contact information, and linking inventory to donors.

Examples:
- Current status of inventory (item counts, value, volume by department/category/donor)
- Inventory changes (new items, sales, deletions, price adjustments)
- Acquisitions (partially received, processed, processing time)

## 4. High-Level Functional Requirements

### 4.1 Medium Priority

#### 4.1.1 Website Integration
- Integrate with Construction Junction website for online inventory viewing/searching
- Support hierarchical inventory view and keyword/parameter search
- Integration with Salesforce for "Contact Us" and "Online Donation Form"
- Implement Salesforce.com Ideas for recycling options

#### 4.1.2 E-Blast Flagging
- Flag items for inclusion in e-Blast during/after inventory addition
- Add photographs for e-Blast/marketing material
- View list of flagged items not yet included in e-Blast
- Preview e-Blast with selected items
- Integration with Vertical Response/Exact Target
- "Great and Gone" section for sold items

#### 4.1.3 E-Commerce Integration
- Online purchases and auctions with automatic inventory updates
- Support inventory available only through e-Commerce
- "Add to Cart" and checkout functionality
- Items flagged as available for online purchase only

#### 4.1.4 Membership Program
- Membership card linked to donor/customer contact in CRM and QuickBooks POS
- Rewards program: "Reuse Reward" based on donated items
- Track customer/donor activity
- Print member cards with unique ID in numeric and barcode format

#### 4.1.5 Customer Wish List
- Notify customers when items in wish list categories become available
- Multiple notification forms (email, text, voice, social media)
- View/remove entries from wish list online
- Include categories of items sold in past 15 days

#### 4.1.6 Pickup/Decon Logistics
- Scheduling and tracking Pickup/Decon jobs with map views
- Filter by location, date range, donation type
- Automatic reminder/thank you emails

#### 4.1.7 Inventory Aging/Automatic Price Discount
- Automatically decrease price of items remaining in inventory
- "Subject to Aging Discount" flag
- 10% discount per month in inventory
- Correct discount applied in QuickBooks POS and website

#### 4.1.8 On-site Storage
- Track items purchased but left on-site for up to 7 days
- Automatic emails for pick-up dates
- Return overdue items to sales floor with store credit

#### 4.1.9 Overstock Pricing
- Set thresholds for items/categories indicating over/under stock
- Adjust prices for overstock conditions
- Reports for currently overstock departments/categories

### 4.2 Low Priority

#### 4.2.1 Mobile Handheld Units
- Scan items on store floor and update inventory
- Handheld units for Pickup/Decon crews on worksites

#### 4.2.2 Inventory Item Story/History
- Add history/back story for items with unique origins
- Generate/print signage with item history/details

#### 4.2.3 Calculate Shipping Weight
- Calculate donation size/truck capacity
- Store item weight information and generate reports

#### 4.2.4 Donor Ranking/Feedback
- Enter information on donors (location, ease of working)
- Generate donor statistics/reports

## 5. Supplementary Requirements

### 5.1 Usability
- Operate via touch screen interfaces
- Minimize keyboard/mouse use during acquisitions
- Complete acquisitions with few clicks/page switches

### 5.2 Availability
- Internal users: Available during normal operating hours for donation/sales processing, beyond hours for inventory management
- External users: Available beyond normal hours for website use

### 5.3 Reliability
No specific reliability requirements.

### 5.4 Security
- Require user login for access
- Grant/deny access based on user profile/role
- Record changes with "created user/time", "modified user/time" fields
- Record sensitive operations (deleting items, changing prices)

### 5.5 Performance
- Consistently low response times to avoid impacting staff tasks

### 5.6 Interfaces

#### 5.6.1 User Interface
- Web browser-based interface for all functionality
- Touch screen optimized with extra spacing between rows
- Required fields marked with asterisk
- Validation errors reported and displayed

#### 5.6.2 Hardware Interfaces
- Touch screen monitors
- Bar code readers
- Zebra printers
- Standard color laser printers
- Mobile devices

#### 5.6.3 Software Interfaces
- QuickBooks POS: Synchronize constituent data, inventory updates, sales integration
- Salesforce CRM: Store contact/donor/acquisition information
- Vertical Response: Email marketing functionality
- Construction Junction website: Inventory viewing, wish lists, online purchases
- CTI Telephony Integration
- MS Outlook integration
- Google Apps

### 5.7 Client Platform
Use cross-browser standards, avoid browser-specific features.

### 5.8 Data Migration
- Migrate constituent/sales history from QuickBooks POS to Salesforce
- No inventory data to migrate

### 5.9 Disaster Recovery, Backups, and Business Continuity Plan
- Develop/document procedures for backups, recovery timeframe, fallback procedures

### 5.10 Maintainability
- Written using industry best practices
- Built with Construction Junction approved products/technologies
- Supportable by planned staffing levels

### 5.11 Portability
No applicable portability requirements.

### 5.12 Legal, Copyright and Other Notices
Display copyright notice: © 2009 - <current year> Construction Junction

### 5.13 Licensing
Utilize open source and commercial products, not considered derivative works.

### 5.14 Applicable Standards
No applicable standards.
