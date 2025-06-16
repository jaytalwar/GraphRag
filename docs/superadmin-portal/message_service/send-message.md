# Send Message Workflow

## Overview
The Send Message feature enables administrators to efficiently communicate with users by sending SMS or Email messages. Messages can be sent in bulk to selected recipients or segments, or as a test to preview content before mass delivery. The interface provides options to customize message type, company, template, provider/sender, and recipient segment.

## Message Types
- **Bulk Message:** Send to all users in a selected segment or to individually selected users.
- **Test Message:** Send a preview to a specific email address or phone number before sending to all recipients.
- **SMS or Email:** Choose the delivery channel as per your communication needs.

## UI Field Explanations
- **Type:** Select either 'SMS' or 'Email' as the message channel.
- **Company:** Choose the company/tenant for which the message is being sent.
- **Template:** Pick a predefined message template (e.g., User Invite link).
- **Provider/Sender:**
  - For Email: Select the email provider (if applicable).
  - For SMS: Select the sender ID (e.g., Dev Six-101344).
- **Segment:** Choose the group of users to receive the message (e.g., Active users).
- **Charge Credits:** (SMS only) Enable this to deduct credits for sending SMS messages.

## Sending a Bulk Message
1. Go to **Message Service > Messages** and click **Send Message**.
2. Select the **Type** (SMS or Email).
3. Choose the **Company**.
4. Select the **Template**.
5. For SMS, select the **Sender**; for Email, select the **Provider** (if required).
6. Choose the **Segment** (e.g., Active users).
7. (Optional, SMS only) Check **Charge Credits** to deduct from your SMS balance.
8. Select individual users or all users in the segment from the list below.
9. Click **Send Message** to deliver to all selected recipients.

## Sending a Test Message
1. Fill in all message details as above (Type, Company, Template, etc.).
2. Click **Test Message**.
3. In the popup, enter the recipient's email address (for Email) or phone number (for SMS).
4. Click **Send** to deliver the test message to the specified address/number.
5. Review the test message before sending to all recipients.

## Notes & Best Practices
- Only users with the appropriate permissions can send messages.
- Ensure sufficient SMS credits are available before sending bulk SMS.
- The **Test Message** feature is recommended to verify content and formatting.
- You can select individual users or use the segment dropdown for bulk targeting.
- For each message, only one segment can be selected at a time. Repeat the process for each segment if needed.

## FAQ
**Q: Can I send a message to multiple segments at once?**
A: No, only one segment can be selected per message. Repeat the process for each segment.

**Q: What is the Test Message option for?**
A: It allows you to preview the message by sending it to a specific recipient before mass delivery.

**Q: What does 'Charge Credits' mean?**
A: For SMS, enabling this option will deduct credits from your account for each message sent.

## Related Links
- [Segments](./segments.md)
- [Message Templates](./messages.md)
- [Companies](./companies.md) 

![send sms](../../../static/img/send_sms.png)
![send email](../../../static/img/send_email.png)