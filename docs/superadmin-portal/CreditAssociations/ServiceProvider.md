# Service Provider Tab

### ✨ Overview

**Purpose:**  
The Service Provider tab enables superadmins to view, manage, and configure external service providers (such as insurance companies) linked to a specific Credit Association (Sacco or MFI). This feature is introduced to streamline the integration and management of third-party services, ensuring that Credit Associations can easily enable or disable services like loan insurance for their members.

**Scope:**  
This documentation covers the Service Provider tab's interface and functionality, focusing on the integration with insurance providers (e.g., Sanlam Insurance), and the enable/disable workflow for these services.

---

### 🧩 Feature Details

- Displays a list of all external service providers associated with the selected Credit Association.
- Shows provider details: name, type (e.g., insurance), and a brief description.
- Indicates the current status of each service (Active/Inactive).
- Provides action buttons to enable or disable a service.
- Includes a direct link to visit the provider's service page.

---

### 📐 Functional Description

- When a superadmin navigates to the Service Provider tab for a Credit Association, they see all available service providers (e.g., Sanlam Insurance).
- Each provider card displays:
  - Provider logo and name
  - Service description
  - Status badge (Active/Inactive)
  - Action button (Enable/Disable)
  - "Visit" link for more information
- The status and available actions depend on the current integration state:
  - If the service is active, the button allows disabling it.
  - If the service is inactive, the button allows enabling it.

---

### 🔄 Workflow / User Journey

1. **Access:**  
   Superadmin selects a Credit Association and navigates to the Service Provider tab.
2. **View Providers:**  
   The tab lists all linked service providers with their current status.
3. **Enable/Disable Service:**  
   - To activate a service (e.g., insurance), click the "Enable" button.
   - To deactivate, click the "Disable" button.

   ![Service Provider - Enable](../../../static/img/ServiceProvider.png)
   
   ![Service Provider - Active](../../../static/img/ServiceProvider_Active.png)
4. **Visit Provider:**  
   For more details, click the "Visit" link to access the provider's external page.
5. **Status Update:**  
   The UI updates to reflect the new status (Active/Inactive) after each action.

---

### ⚠️ Validation / Constraints / Configurations

- Only superadmins have access to enable or disable service providers.
- The enable/disable action may be restricted based on the Credit Association's status (e.g., only available for "Active" associations).
- Some services may require additional configuration or approval before activation.
- The "Visit" link should direct to a valid, secure provider page.

---

### ✅ Acceptance Criteria

- The Service Provider tab must display all available providers for the selected Credit Association.
- Each provider card must show the correct status and available action (Enable/Disable).
- Clicking "Enable" or "Disable" must update the service status and reflect changes in the UI.
- The "Visit" link must be functional and direct to the correct provider page.
- Only authorized users (superadmins) can perform enable/disable actions.
- The tab must handle and display error messages for failed actions (e.g., network issues, permission errors). 