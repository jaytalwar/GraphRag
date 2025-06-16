# Message Logs

## Overview
The Logs tab provides a comprehensive record of all messages sent through the system, including SMS and Email. It allows administrators to track delivery, status, and other key details for compliance and transparency. Logs are essential for monitoring all outgoing communications, verifying delivery status, troubleshooting failed messages, and maintaining an audit trail for compliance.

## Features
- View all sent messages with detailed status
- Filter and search logs by recipient, date, status, and more
- Clickable templates for message details
- Real-time refresh of logs
- Track delivery, type, recipient, status, template, credits, and company for each message
- **Batch Logs:** View and track the status of messages sent in bulk (batch), including individual delivery results for each recipient in the batch

### Columns & Details
- **Delivery:** Shows delivery status (e.g., delivered, failed, batch count like 13/18)
- **Date:** Timestamp of when the message was sent
- **Type:** Message type (SMS or Email)
- **Recipient:** Email address or phone number of the recipient
- **Sending Status:** Indicates if the message was sent, failed, or is in progress
- **Message Type:** E.g., Transactional, Notification, Service
- **Template:** The template used for the message (clickable for details)
- **Credits:** Number of SMS credits used (if applicable)
- **Company:** The company associated with the message
- **Batch Status:** For bulk messages, shows the count of successful/total deliveries (e.g., 13/18)
- **Batch Log Statuses and General Statuses:**
  - **Success:** Message delivered successfully to the recipient.
  - **Failed:** Message could not be delivered.
  - **InvalidPhoneNumber:** The recipient's phone number is invalid.
  - **Sent:** Message has been sent from the system (may not be delivered yet).
  - **Undelivered:** Message was not delivered to the recipient (reason may vary).
  - **Insufficient SMS Credits:** The company does not have enough SMS credits to send the message.
  - **SMS Disabled for Company:** SMS sending is disabled for the selected company.
  - **Email Disabled for Company:** Email sending is disabled for the selected company.
  - **In Progress:** Message is currently being processed for delivery.
  - **Delivered:** Message was delivered to the recipient (sometimes used instead of "Success").
  - **Bulk/Batch Count:** (e.g., 13/18) Indicates how many messages in a batch were delivered out of the total attempted.

## Configurations
- Set filters for columns (date, type, recipient, status, etc.)
- Customize visible columns if supported

## Use Cases
- Auditing message delivery for compliance
- Troubleshooting failed messages
- Reviewing communication history for a specific user
- Monitoring the success rate of bulk (batch) message campaigns

## Examples
**Filtering Logs by Status:**
1. Go to Logs tab.
2. Use the filter on Sending Status to view only failed messages.

**Viewing Batch Log Details:**
1. Locate a batch message entry (e.g., Delivery column shows 13/18).
2. Click to expand or view details for each recipient's delivery status (Success, Failed, InvalidPhoneNumber, Insufficient SMS Credits, SMS Disabled for Company, etc.).

**How to Use:**
1. Navigate to **Message Service > Logs**
2. Use filters on each column to search for specific messages, recipients, or statuses
3. Click on a template name to view its details
4. Use the **Refresh** button to update the log view

## Additional Notes
- Only users with appropriate permissions can access full logs.
- Batch logs provide transparency for bulk messaging and help identify delivery issues at the recipient level.

## FAQ
**Q: How long are logs retained?**
A: Log retention depends on system policy; check with your administrator.

**Q: Can I export logs?**
A: Export functionality depends on system configuration.

**Q: What does the batch delivery count (e.g., 13/18) mean?**
A: It shows how many recipients in a batch received the message successfully out of the total attempted.

**Q: What do the different batch log statuses mean?**
A: See the list above for all possible statuses and their meanings.

## Related Links
- [Companies](./companies.md)
- [Message Templates](./messages.md)
- [Segments](./segments.md)



> The Logs tab is essential for tracking communication effectiveness and ensuring all messages reach their intended recipients. 

![messages](../../../static/img/logs1.png)
![messages logs](../../../static/img/logs.png)
