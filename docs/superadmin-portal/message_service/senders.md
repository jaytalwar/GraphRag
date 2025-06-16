# Senders

## Overview
The Senders feature allows administrators to define and manage sender identities for outgoing messages (SMS or Email) on behalf of a company. This ensures proper branding, compliance, and message traceability.

---

## Sender Management Workflow

### Viewing Senders
- The Senders page displays a table listing all sender identities associated with the selected company.
- The table includes the following columns:
  - **Sender**: The sender name/identifier.
  - **Company**: The company the sender is associated with.
  - **Provider**: The service provider (e.g., Airtel, AWS, Africastalking).
  - **Type**: The type of service (SMS or Email).
  - **Actions**: Options to edit or remove the sender.

### Creating a Sender
1. Navigate to the **Companies** section and select the desired company.
2. Click the **Create Sender** button.
3. In the **Create Sender** dialog:
   - **Company**: Pre-filled with the selected company (not editable).
   - **Select Service Type**: Choose either **SMS** or **Email**.
   - **Sender Name**: Enter the sender's name/identifier (required for SMS only).
   - **Select Provider**: Choose the appropriate provider from the dropdown (required).
4. Click **Create** to save the sender. A success notification will appear upon successful creation.

> **Note:** The fields and requirements may vary slightly depending on the selected service type (e.g., Email senders may not require a sender name).

### Editing or Removing a Sender
- Use the actions menu (three dots) in the sender list to edit or remove an existing sender.
- Update the details as needed and save changes.

---

## Key Features
- Create, edit, and remove sender identities
- Associate senders with a specific company
- Specify provider and sender type (SMS/Email)
- View all senders in a searchable, filterable table

---

## Additional Notes
- Only authorized users can manage senders.
- Sender identities help recipients recognize the source of messages and ensure compliance with regulations.
- A success message is displayed after creating a sender: `Sender created successfully`.

---

## FAQ
**Q: What types of senders can I create?**
A: SMS and Email senders are supported.

**Q: Can a sender be associated with multiple companies?**
A: Senders are typically linked to a single company during creation.

---

## Related Links
- [Companies](./companies.md)
- [Logs](./logs.md)
- [Message Templates](./messages.md) 

![messages logs](../../../static/img/Sender.png)