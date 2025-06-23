# Online Payments Tab




## ✨ Overview

**Purpose:**  
The Online Payments Provider Management feature enables superadmins to view, configure, and manage online payment providers and wallets associated with a specific Credit Association (Sacco). This feature is introduced to streamline the integration and administration of various payment channels, ensuring seamless digital transactions for the Sacco and its members.

**Scope:**  
This feature covers the addition, editing, and management of payment providers (such as mobile money and bank APIs), wallet linking, and the configuration of transaction types and provider-specific credentials. It is accessible from the "Online Payments" tab within the Credit Association's management interface.

## 🧩 Feature Details

- List all payment providers currently linked to the Sacco, showing their status, type (Pooled/Dedicated), and enabled features (collection/disbursement).
- Add new payment providers by specifying provider name, transaction type, wallet details, and integration type.
- Edit existing provider configurations to update credentials or change provider status.
- Enable or disable online payments and two-factor authentication for added security.
- Monitor the status of each provider (Active/Inactive) and manage their operational parameters.

## 📐 Functional Description

- The main interface displays a table of all configured payment providers, including their name, enabled status, type, collection/disbursement capabilities, and an action button for editing.
- The "Add Provider" button opens a modal where superadmins can select a provider, define transaction types (e.g., ALL), choose between Pooled or Dedicated integration, and enter wallet credentials.
- Each provider entry can be edited to update its configuration or credentials as needed.
- The interface supports toggling online payments and enabling two-factor authentication for enhanced security.

## 🔄 Workflow / User Journey

1. Superadmin navigates to the "Credit Associations" section and selects a Sacco.
2. Under the "Online Payments" tab, the admin views all current payment providers and their statuses.
3. To add a new provider, the admin clicks "Add Provider," fills in the required details (provider name, type, wallet), and saves the configuration.
4. To update an existing provider, the admin clicks "Edit" next to the provider, modifies the necessary fields, and saves changes.
5. The admin can enable/disable online payments or activate two-factor authentication as needed.
6. All changes are reflected in real-time, ensuring up-to-date provider management.

![Online Payments Provider Manangement](../../../static/img/Online_Payments.png)

## ⚠️ Validation / Constraints / Configurations

- Provider Name and Wallet fields are mandatory when adding or editing a provider.
- Only valid and supported provider types (Pooled/Dedicated) can be selected.
- Two-factor authentication can only be enabled if online payments are active.
- The system validates wallet credentials before saving provider configurations.
- Only superadmins or users with appropriate permissions can manage providers.

## ✅ Acceptance Criteria

- The Online Payments tab lists all current payment providers with accurate status and configuration details.
- Superadmins can successfully add a new provider, specifying all required fields.
- Editing a provider updates its configuration and credentials as expected.
- Online payments and two-factor authentication toggles work as intended, with appropriate validation.
- Error messages are displayed for missing or invalid input during provider configuration.
- All changes are saved and reflected immediately in the provider list. 
---