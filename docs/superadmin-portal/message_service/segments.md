# Segments

## Overview
The Segments tab allows administrators to group users for targeted communication. Segments simplify sending messages to specific sets of users based on criteria such as branch, role, region, or custom filters (e.g., OTP verification status, phone number, city).

## Features
- Create, edit, and disable segments
- Assign aliases for easy identification
- Filter and search segments
- Enable/disable segments as needed
- Configure segment membership using multiple filters and logical operators (AND/OR)
- View segment creation date and perform actions (edit/delete)

## Configurations
- Set segment name and alias
- Define criteria for segment membership using filters (e.g., OTP Verified, Phone, City)
- Combine multiple filters using AND/OR logical operators
- Enable or disable segment using the toggle switch
- View segment creation date

## Use Cases
- Creating a segment for all tenant user
- Creating a segment for users who have not completed OTP verification
- Creating a segment for users in a specific city or with a specific phone number
- Disabling a segment that is no longer needed
- Updating a segment to reflect organizational changes or new criteria

## Examples
**Creating a New Segment:**
1. Go to the Segments tab under Message Service.
2. Click **Create > Create Segment**.
3. Enter the segment **Name** and **Alias**.
4. (Optional) Add a **Description**.
5. Under **Create Filters**, select filter criteria (e.g., OTP Verified = False, Phone = 897324671, City = Tanzania).
6. Use **AND/OR** to combine multiple filters as needed.
7. Click **Save** to create the segment.
8. Enable the segment using the toggle switch in the segment list.

**Editing or Updating a Segment:**
1. In the Segments list, click the action menu (three dots) next to the segment.
2. Select **Edit**.
3. Update the name, alias, or filter criteria as needed.
4. Click **Save** to apply changes.

**Disabling a Segment:**
1. Find the segment in the list.
2. Toggle **Enable/Disable** as needed.

**Deleting a Filter from a Segment:**
- When editing a segment, click the trash icon next to a filter to remove it.

## Additional Notes
- Segments help ensure messages are relevant and targeted.
- Only enabled segments can be selected when sending messages.
- Users can belong to multiple segments based on filter criteria.
- The segment list displays the name, alias, creation date, and enable/disable status.

## Impact of Segments in the Module
Segments play a crucial role in the Message Service module by enabling targeted communication and efficient user management. Their impact includes:

- **Targeted Messaging:** When composing or sending a message, you can select a segment to send messages only to users who match the segment's criteria. This ensures that communications are relevant and reach the intended audience.

## FAQ
**Q: Can a user belong to multiple segments?**
A: Yes, users can be included in multiple segments.

**Q: How do I update a segment's criteria?**
A: Edit the segment, adjust its filters and details, then save.

**Q: What logical operators can I use when defining filters?**
A: You can use AND/OR to combine multiple filter conditions.

## Related Links
- [Users](./users.md)
- [Send Message Workflow](./send-message.md)
- [Logs](./logs.md)

![segment view](../../../static/img/segment1.png)
![segment create](../../../static/img/Segment2.png)

> **Note:** The actual visibility of users in a segment may depend on system permissions and UI capabilities. Always refer to the latest UI for available options. 