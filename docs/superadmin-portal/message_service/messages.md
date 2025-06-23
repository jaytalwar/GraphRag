# Message Templates

## Overview
The Messages tab is where administrators create, manage, and organize message templates for both SMS and Email communications. Templates ensure consistency and save time for recurring messages.

## Features
- Create, edit, and delete templates
- Enable or disable templates
- Assign templates to specific companies
- Track template versions and costing
- Filter and search templates
- Support for both Email and SMS templates


## Template Creation & Fields
When creating a new message template, you will see a form with the following fields:

- **Select Type**: Choose the type of message (e.g., Account, Request, Transaction, Jobs, Other).
- **Name**: Enter a descriptive name for the template.
- **Template Key**: Provide a unique key to identify the template (used for referencing in workflows).
- **Select Company**: Assign the template to a specific company.

> **Note:** All fields marked with * are mandatory.

## Creating Template Content
After filling in the basic template details, you will be prompted to add the content for your template:

- **Select Language**: Choose the language for the template content.
- **Email Template**:
  - **Subject**: Enter the subject line for email notifications.
  - **Body**: Compose the main content of the email. Use formatting tools (bold, italic, lists, links, etc.) and insert variables (e.g., `{name}`, `{phone}`, `{email}`) for personalization.
- **SMS Template**:
  - **SMS Text**: Enter the content of the SMS message. Variables can also be used here for dynamic content.
  - A character count is displayed to help you stay within SMS limits.

You can add content for multiple languages by selecting a different language and providing the corresponding Email and SMS content.

## Step-by-Step: Creating a New Template
1. Go to the **Messages** tab.
2. Click **Create** > **Create Template**.
3. Fill in the required fields:
   - Select Type
   - Name
   - Template Key
   - Select Company
4. Add the template content:
   - Select Language
   - Enter Email Subject and Body
   - Enter SMS Text
5. Click **Create** to save the template.
6. The template will appear in the list, where you can enable/disable it and manage costing.

## Examples
1. Find the template in the list.
2. Click the template **Name**.
3. Update the template details or content, including email subject/body, and SMS text.
4. Click **Update** to save changes.

## Disabling a Template
1. Find the template in the list.
2. Toggle **Enable/Disable** as needed.

## Additional Notes
- Only enabled templates can be used for sending messages.
- Costing may apply to certain templates (e.g., paid SMS).
- Template version is incremented when you update a template.
- Templates are typically assigned to one company at a time.

## Template Costing and Its Impact
Some message templates are marked as 'Paid' under the Costing column. This means that sending messages using these templates will incur a cost, typically for SMS or other premium communication channels. 

- **Costing Toggle:** Administrators can enable or disable costing for each template. When costing is enabled, any message sent using that template will be billed according to the organization's pricing plan.
- **Impact on Admin Portal:**
  - The costing status is visible in the template list, helping admins track which templates are free and which are paid.
  - Only users with the appropriate permissions can change the costing status.
  - Enabling costing may restrict the use of certain templates to avoid unnecessary expenses, or require additional approval workflows.
- **Best Practices:**
  - Use costing for templates that require premium delivery (e.g., urgent SMS notifications).

## Visual Guidance
- The template creation form includes dropdowns and input fields for all required information.
- The template content section provides a rich text editor for emails and a plain text box for SMS, with variable support.
- The template list view shows all templates with their type, version, key, costing, enable/disable status, and assigned company.

## FAQ
**Q: Can I assign a template to multiple companies?**
A: Templates are typically assigned to one company at a time.

**Q: How do I update a template version?**
A: Edit the template and increment the version number.

## Related Links
- [Logs](./logs.md)
- [Companies](./companies.md)
- [Send Message Workflow](./send-message.md) 

![template](../../../static/img/template.png)
![template create](../../../static/img/create_template%20(1).png)
![template content](../../../static/img/template_content.png)