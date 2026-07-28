**Short Summary**

**Background and objectives**  
ABC Paint is migrating to a new paint numbering scheme in Q3 2004 and needs a web-based application to help customers and distributors transition smoothly. The system must be in place by Q2 2004 to allow time for adjustment and will be used long-term for handling old-scheme paint numbers.

**In scope**  
- Graphical, pointing-device-driven color chooser.  
- Translator for converting old paint numbers to the new scheme.  
- Tool to find the closest colors to a given paint within a target collection.  
- Color search engine for locating paints by name, number, or color value.  
- Session-persistent user color palette for storing recent searches and uploaded images.

**Out of scope**  
- Client display calibration for accurate color representation.  
- Support for legacy monochrome displays.  
- Full "keyboard-only" functionality (pointing device required for some features).  
- Guarantees on internet-based performance and timeliness.  
- The color sample matcher module (specified but low priority/not required).

**Stakeholders and core use cases**  
*Stakeholders:*  
- **ABC Paint customers:** End-users who need to find and transition to new paint numbers.  
- **ABC Paint distributors:** Users who assist customers and need access to conversion tools.  
- **ABC Paint IT department:** Responsible for deploying and managing the application.  
- **Administrative users (Levels 1-3):** Personnel who update, add, or delete paint data and manage user access.  

*User stories:*  
1. As a customer, I want to translate an old paint number to the new scheme so that I can order the correct replacement.  
2. As a distributor, I want to search for paints by name or color value so that I can quickly find products for a customer.  
3. As a customer, I want to select a color visually using a graphical chooser so that I can explore color options intuitively.  
4. As an administrative user, I want to update paint collection information so that the database remains accurate.  
5. As a user, I want my recent color searches saved in a session so that I can easily revisit them.  
6. As an IT manager, I want the application to be themable so that it integrates seamlessly into our existing website.

**Success metrics**  
- Color searches are processed in sub-second time on the server.  
- The application is successfully integrated into the ABC Paint website with a consistent theme.  
- Administrative updates to paint data occur in real-time (processing time varies with data volume).

**Major constraints**  
- The application must be web-based to ensure high accessibility.  
- The client requires a display capable of 16.7 million colors and a pointing device for full functionality.  
- The server requires at least a 1GHz processor and 512MB RAM per 50 concurrent users.  
- Client must use Internet Explorer 4.01, Netscape 6.0, or Mozilla 1.0 or later.  
- User data in the color palette is private but not secure and is removed after 30 days.

**Undecided issues**  
None (all TBD items have been resolved).