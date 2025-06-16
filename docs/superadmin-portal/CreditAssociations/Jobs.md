# Jobs Tab



## ✨ Overview

**Purpose:**  
The Jobs Tab enables superadmins to view, manage, and configure background jobs and scheduled tasks associated with a specific Credit Association (Sacco). This feature streamlines the administration of automated processes, ensuring operational efficiency and transparency for critical backend activities.

**Scope:**  
This feature is available to superadmin users within the Superadmin Portal, specifically under the Credit Associations module. It covers the display, selection, and management of various jobs (such as loan accrual, interest payout, reconciliation, and more) that are essential for the smooth functioning of a Sacco.

---

## 🧩 Feature Details
- Presents a categorized list of all available jobs for a selected Credit Association.
- Allows superadmins to enable or disable specific jobs by selecting checkboxes.
- Provides a clear overview of each job's function (e.g., Loan Accrual, Interest Payout, Transaction Reconciliation).
- Includes a "Save" button to persist configuration changes.
- Supports both operational (e.g., batch processing) and maintenance (e.g., reconciliation) jobs.

---

## 📐 Functional Description
- The Jobs Tab is accessible from the Credit Associations section in the Superadmin Portal.
- Jobs are displayed in a two-column layout, each with a checkbox for activation.
- Each job is labeled with a descriptive name (e.g., Jobs.Loan.Accrual, Jobs.TransactionReconcileJob).
- Superadmins can select or deselect jobs as required for the Credit Association.
- The "Save" button at the bottom commits the selected configuration.
- The tab is part of a broader navigation system, allowing switching between other configuration areas (e.g., Client Details, Features, Online Payments).

---

## 🔄 Workflow / User Journey

![Jobs Tab UI](../../../static/img/Jobs.png)
*Figure: The Jobs Tab interface allows superadmins to select and manage background jobs for a Credit Association in a clear, organized manner.*

1. Superadmin logs into the Superadmin Portal.
2. Navigates to Credit Associations and selects a specific Sacco.
3. Clicks on the "Jobs" tab to view all available jobs.
4. Reviews the list and selects/deselects jobs according to operational needs.
5. Clicks the "Save" button to apply changes.
6. The system updates the job configuration for the selected Sacco, enabling or disabling background processes as specified.

---

## ⚠️ Validation / Constraints / Configurations
- Only users with superadmin privileges can access and modify the Jobs Tab.
- At least one job must be selected to ensure essential background processes are not inadvertently disabled (if applicable).
- Some jobs may have dependencies; disabling one job may affect the operation of others (e.g., disabling Loan Accrual may impact Interest Payout).
- Changes are applied only after clicking "Save"; unsaved changes will be lost if the user navigates away.
- The system should validate selections and provide warnings if critical jobs are deselected.

---

## ✅ Acceptance Criteria
- The Jobs Tab is visible and accessible to superadmin users under Credit Associations.
- All relevant jobs for the selected Sacco are listed with clear, descriptive names.
- Superadmins can select or deselect jobs and save their configuration.
- The system persists changes and updates the job schedule accordingly.
- Appropriate validation and warnings are provided for critical job dependencies or missing selections.
- The UI is responsive and user-friendly, with clear feedback on successful or failed operations.

---

## Typical Jobs
- Data migration (e.g., Run Migration Job)
- Synchronization with external systems (CRM, accounting)
- Batch updates or maintenance tasks 