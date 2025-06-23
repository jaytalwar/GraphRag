# Fees and Invoice Tab 


✨ **Overview**

**Purpose:**  
The "Fees and Invoice" tab is designed to provide superadmins with a comprehensive interface for managing, configuring, and tracking all fees, charges, and invoices associated with a specific Credit Association (Sacco). This feature streamlines financial oversight, ensures transparency, and supports efficient fee management and invoicing processes.

**Scope:**  
This feature is available to superadmin users within the Superadmin Portal and applies to all registered Credit Associations (Saccos). It covers fee configuration, invoice generation, payment tracking, and integration with accounting modules.

---

🧩 **Feature Details**

- **Fee Configuration:** Set up, update, and manage various fee types (e.g., subscription, service, transaction, provider convenience fees).
- **Invoice Management:** Generate, view, and archive invoices; monitor invoice history and payment statuses.
- **Payment Tracking:** Track outstanding balances, paid/unpaid invoices, and apply filters for detailed financial reporting.
- **Version Control:** Maintain and select different fee configuration versions for historical and future applicability.
- **Integration:** Seamless connection with accounting and payment modules for accurate financial reconciliation.

---

📐 **Functional Description**

- **Invoice List:**  
  Displays all generated invoices for the selected Credit Association, including details such as invoice date, ID, name, status (paid/unpaid), duration, amount, discount, and creator information. Invoices can be archived for record-keeping.

- **Fee Configuration:**  
  Allows superadmins to enable/disable fees, set overdraft limits, grace periods, and configure detailed fee structures (subscription, user, service, quick loan, message charges, provider convenience fees). Supports versioning and effective date ranges for each configuration.

- **Invoice Generation:**  
  Superadmins can generate new invoices by specifying the invoice name, selecting a fee configuration version, setting the transaction fee status, and defining the applicable date range. The system calculates and displays all relevant fees, product codes, prices, and transaction counts.

- **Detailed Fee Breakdown:**  
  For each invoice, a breakdown of all applicable fees is shown, including service and provider fees, message charges, and subscription fees, along with transaction counts and total amounts.

---

🔄 **Workflow / User Journey**

1. **Accessing the Tab:**  
   Superadmin navigates to the "Fees and Invoice" tab for a specific Credit Association.

2. **Viewing Invoices:**  
   The invoice list is displayed, showing all historical and current invoices with their statuses and details.

3. **Configuring Fees:**  
   By clicking "Fees Config," the superadmin can view and edit fee structures, set limits, and manage provider-specific fees. Changes can be versioned and scheduled for future applicability.

4. **Generating Invoices:**  
   The superadmin clicks "Generate Invoice," fills in the required details, applies filters (e.g., date range, fee status), and reviews the calculated fees before saving or downloading the invoice.

5. **Archiving Invoices:**  
   Invoices can be archived for organizational or compliance purposes.

   ![Fees and Invoice Main Screen](../../../static/img/FeeAndInvoice_1.png)
   
   <br/>
   
   ![Generate Invoice Screen](../../../static/img/GenerateInvoice.png)

---

⚠️ **Validation / Constraints / Configurations**

- **Required Fields:**  
  Invoice name, configuration version, transaction fee status, and date range are mandatory for invoice generation.
- **Fee Limits:**  
  Min/max transaction amounts and applicable fees must adhere to system-defined constraints (e.g., max amount ≤ 999,999,999,999.99).
- **Version Control:**  
  Only one fee configuration version can be active for a given period; overlapping date ranges are not permitted.
- **Provider Fees:**  
  Provider convenience fees must be configured per provider and transaction type (e.g., collection/disbursement).
- **Data Integrity:**  
  All changes to fee configurations are logged and versioned for auditability.

  ![Fees and Invoice Main Screen](../../../static/img/FeeAndInvoice_2.png)
   
   
  ![Fees and Invoice Main Screen](../../../static/img/FeeAndInvoice_3.png)

---

✅ **Acceptance Criteria**

- Superadmin can view, generate, and archive invoices for any Credit Association.
- Fee configurations can be created, updated, and versioned with effective date ranges.
- The system enforces all validation rules for required fields and fee limits.
- The invoice list accurately reflects all historical and current invoices, with correct statuses and amounts.
- Detailed fee breakdowns are displayed for each invoice, including all configured fee types.
- Integration with accounting and payment modules is functional, ensuring accurate financial reporting.
- All user actions (e.g., fee updates, invoice generation) are logged for audit purposes. 