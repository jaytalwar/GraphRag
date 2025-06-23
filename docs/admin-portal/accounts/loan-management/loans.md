# Loan Management: Loans

## Overview
The **Loans** section in the Admin Portal provides a comprehensive view and management interface for all loans within your organization. This feature allows you to view, search, filter, and export loan data, supporting efficient loan tracking and administration.

---

## Accessing Loans
- Navigate to **Accounts > Loans** in the sidebar menu.
- The Loans page displays three tabs: **Active**, **New**, and **Closed**.
- By default, the **Active** loans tab is shown.

---

## Loan List Table
The main table displays a paginated list of loans with the following columns:

| Column              | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Account Number      | Unique identifier for the loan account. Clickable for details.              |
| Member Name         | Name of the member or client holding the loan.                              |
| Product             | Type of loan product (e.g., Home Loan, Education Loan, etc.).               |
| Loan Officer        | Name of the officer managing the loan.                                      |
| Status              | Current status (e.g., Disbursed, New, Overdue).                             |
| Provisioning Status | Loan provisioning state (e.g., Disbursed, New, Overdue).                    |
| Tenure              | Duration of the loan (e.g., 6 Months, 2 Years).                             |
| Created Date        | Date when the loan was created.                                             |
| Loan Amount (UGX)   | Principal amount of the loan.                                               |
| Balance (UGX)       | Outstanding balance, with breakdown (Principal, Interest, Charges, Balance).|
| Overdue Days        | Number of days the loan is overdue.                                         |

---

## Search and Filter
You can refine the loan list using the following filters:
- **Search Here**: Enter keywords to search by account number, member name, etc.
- **Overdue Loan Category**: Filter by overdue status/category.
- **Loan Officer**: Filter loans by the responsible loan officer.

**Actions:**
- Click **Search** to apply filters.
- Click **Clear** to reset all filters.

---

## Downloading Loan Data
- Click the **Download** button to export the current loan list to Excel format.
- The export respects the current filters and pagination.

---

## Viewing Loan Balances
- Click the eye icon in the **Balance** column to reveal a detailed breakdown:
  - Principal
  - Interest
  - Charges
  - Total Balance

---

## Pagination
- Use the pagination controls at the bottom to navigate through multiple pages of loan records.
- You can also adjust the number of records displayed per page.

---

## Viewing Loan Details
Click on any Account Number in the loan list to open the detailed view for that loan. The loan details page provides comprehensive information and actions for the selected loan, organized into the following sections:

### Tabs
- **Details**: Overview and all key information about the loan.
- **Transactions**: List of all transactions related to the loan.
- **Schedule**: Repayment schedule and due dates.
- **Charges**: All charges applied to the loan.
- **Repayments**: Repayment history and status.
- **Documents**: Uploaded documents related to the loan.
- **History**: Audit trail and status changes.

### Actions
- **Edit**: Modify loan details (if permitted).
- **Loan Top-Up**: Add additional funds to the loan.
- **Delinquent**: Mark the loan as delinquent.
- **Close Loan**: Close the loan account.
- **Reset**: Reset changes or status.
- **Download**: Export loan details.
- **Repay**: Make a repayment on the loan.

### Loan Details Section
| Field                        | Description                                                      |
|------------------------------|------------------------------------------------------------------|
| Account Number               | Unique loan account identifier.                                   |
| Product                      | Type of loan product.                                            |
| Status                       | Current loan status (e.g., Disbursed).                           |
| Loan Amount (UGX)            | Principal amount of the loan.                                    |
| Nominal Interest Rate        | Interest rate applied to the loan.                               |
| Tenure                       | Duration of the loan (e.g., 5 Weeks).                            |
| Loan Officer                 | Officer managing the loan.                                       |
| Loan Type                    | Category/type of the loan (e.g., Emergency Loans).               |
| Economic Sector              | Main economic sector for the loan.                               |
| Economic Sub Sector          | Sub-sector details.                                              |
| Purpose                      | Purpose of the loan.                                             |
| Debt Capacity                | Debt capacity information.                                       |
| Description                  | Additional description or notes.                                 |
| Provisioning Status          | Current provisioning status.                                      |
| Interest On Grace Period     | Whether interest is charged during grace period.                 |

#### Balance Table
| Type        | Principal (UGX) | Interest (UGX) | Charges (UGX) | Total (UGX) |
|-------------|-----------------|---------------|---------------|-------------|
| Opening     | 30,000.00       | 600.00        | 5,732.00      | 36,332.00   |
| Paid        | 7,500.00        | 150.00        | 5,132.00      | 12,782.00   |
| Outstanding | 22,500.00       | 450.00        | 600.00        | 23,550.00   |

### Member Information
- **Member Name** and **ID**
- **Status** (e.g., Active)
- **Branch**
- **Loan Applications**
- **Total Loans**
- **Outstanding Loans**
- **Badstanding Loans**

### Disbursement Details
- **Member Type**
- **Destination Account** (e.g., mobile number or bank account)

### Insurance
| Provider Name     | Insurance Fee | Fee Collection   | Status | Action |
|-------------------|---------------|------------------|--------|--------|
| Sanlam Insurance  | UGX 2,000.00  | On Disbursement  | Paid   |        |

### Guarantor
| Account Number | Type   | Product           | Block Amount (UGX) |
|----------------|--------|-------------------|--------------------|
| 917420043902   | Saving | Mandatory Saving  | DR 30,000.00       |

### Collateral
| Asset Name | Type     | Current Valuation (UGX) | Block Amount (UGX) | Comment | Documents                | Actions |
|------------|----------|------------------------|--------------------|---------|--------------------------|---------|
| home       | personal | 1,000,000,000.00       | DR 300,000.00      | test    | ExpenseReport-2025-05-01 |         |

---

Return to the [Loans List](#loan-list-table) to view or manage other loans.

---

## Related Features
- [Loan Applications](../loan-management/loan-application-details.md)

---

## Notes
- Only users with appropriate permissions can view or manage loans.
- The UI and available actions may vary based on user roles and organization settings.
