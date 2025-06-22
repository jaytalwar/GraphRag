# Message Service Users

## Overview
The **Users** tab in the Message Service module displays a comprehensive list of all users eligible to receive messages. Administrators can manage each user's communication preferences for SMS and Email directly from this interface.

## Interface Breakdown
- **Tabs:** The Message Service screen is divided into multiple tabs: **Logs**, **Messages**, **Segments**, and **Users**. Select the **Users** tab to view and manage user-specific messaging settings.
- **Organization Filter:** At the top right, use the dropdown menu to filter users by organization or group. Selecting "ALL" displays users from all organizations, while selecting a specific organization narrows the list accordingly.
- **Refresh Button:** Click the **Refresh** button to reload the user list and ensure you are viewing the most up-to-date information.
- **User Table Columns:**
  - **Name:** The user's display name.
  - **Phone:** The user's registered phone number.
  - **Email:** The user's email address.
  - **Enable SMS:** Toggle to enable or disable SMS notifications for the user.
  - **Enable Email:** Toggle to enable or disable Email notifications for the user.

## Features
- View all users eligible for messaging, filtered by organization if needed
- Enable or disable SMS/Email for each user using toggle switches
- Filter and search users by name, phone, or email using the search bar above the table

## Configurations
- Set SMS and Email enablement per user using the toggles in the table
- Update user contact details as needed (if permissions allow)

## Use Cases
- **Disabling SMS for a User:**
  1. Find the user in the list (use search or filters if needed).
  2. Toggle the SMS switch to disable.
- **Enabling Email for a New User:**
  1. Locate the user and toggle the Email switch to enable.
- **Searching for a User:**
  1. Use the search bar to find a user by name, phone, or email.
- **Filtering by Organization:**
  1. Use the dropdown at the top right to select the relevant organization.

## Additional Notes
- Only users with the appropriate permissions can update user preferences.
- Disabling both SMS and Email will prevent the user from receiving any messages.
- The user list can be refreshed at any time using the Refresh button.

## FAQ
**Q: Can I bulk update user preferences?**
A: Bulk update depends on system capabilities; check with your administrator.

**Q: What happens if both SMS and Email are disabled for a user?**
A: The user will not receive any messages from the system.

**Q: How do I filter users by organization?**
A: Use the dropdown menu at the top right to select the desired organization.

## Related Links
- [Segments](./segments.md)
- [Send Message Workflow](./send-message.md)
- [Logs](./logs.md)

![Message Service Users tab with organization filter and toggles](../../../static/img/Users.png)