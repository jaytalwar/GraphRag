# Configurations Tab 

## ✨ Overview

**Purpose:**  
The Configurations tab empowers superadmins to tailor system-level and operational settings for each Credit Association (Sacco). This feature ensures that each Sacco can align its communication and approval workflows with its unique operational, compliance, and security requirements.

**Scope:**  
This tab is accessible to superadmins managing Credit Associations. It covers configuration of communication channels (Email/SMS) for notifications and the setup of maker-checker (dual control) approval flows for sensitive operations.

---

## 🧩 Feature Details

The Configurations tab is divided into two main sections:
- **Communication Permissions:** Manage how notifications (invites and transactions) are sent to members and administrators via Email and/or SMS.
- **Maker Checker Permissions:** Define which critical operations require a dual-approval workflow, enhancing security and compliance.

---

## 📐 Functional Description

**Communication Permissions:**  
- **Invite Email:** Sends email invitations to new members/users when added to the Sacco.
- **Transaction Email:** Sends email notifications for financial transactions (deposits, withdrawals, loan disbursements).
- **Invite SMS:** Sends SMS invitations to new members/users.
- **Transaction SMS:** Sends SMS notifications for financial transactions.

**Maker Checker Permissions:**  
Enables approval workflows for the following operations:
- Request Loan Interest WaiveOff
- Back Dated Transaction Approval Request
- Request Member Bank
- Request Member MNO
- Request Teller Disbursed
- Request Teller Repayment
- Request Member Detail
- Request Teller Deposit
- Request Teller Ledger Entry
- Request Teller Withdraw

When enabled, these actions require a second user (checker) to approve the request initiated by the first user (maker).

![Configurations tab showing Communication and Maker Checker options in the Superadmin Portal.](../../../static/img/Configuration.png)

---

## 🔄 Workflow / User Journey

1. **Access:**  
   Superadmin navigates to the Configurations tab for a specific Credit Association.
2. **Configure Communication:**  
   - Select/deselect notification channels (Email/SMS) for invites and transactions.
3. **Set Maker Checker:**  
   - Choose which operations require dual approval by checking the relevant boxes.
4. **Save Changes:**  
   - Click the **Save** button to apply the new configuration.
5. **Effect:**  
   - Selected communication channels are used for notifications.
   - Enabled maker-checker operations require approval before completion.

---

## ⚠️ Validation / Constraints / Configurations

- Only superadmins can access and modify these settings.
- At least one communication channel (Email or SMS) should be enabled for critical notifications to ensure members are informed.
- Maker-checker can be enabled for any combination of supported operations, but enabling too many may slow down operational workflows.
- Changes take effect immediately after saving.
- Disabling all communication channels may result in members not receiving important updates.

---

## ✅ Acceptance Criteria

- Superadmin can view and modify communication and maker-checker settings for any Credit Association.
- Changes to settings are saved and reflected immediately in the system.
- Notifications are sent only via the enabled channels.
- Maker-checker approval is enforced for all selected operations.
- The UI clearly indicates the current state (enabled/disabled) of each option.
- The system prevents saving if all communication channels are disabled (optional, based on business rules).
- Audit logs capture all configuration changes for compliance.

---

