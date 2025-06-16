---
sidebar_position: 2
---

# Teller Reconciliation

The **Teller Reconciliation** module provides a secure and efficient way for tellers and administrators to review, validate, and export transaction data, track account balances.

---

##  Overview

The Teller Reconciliation system ensures transparency in financial operations by enabling users to:

- Review teller-specific transaction summaries
- Verify debit and credit totals
- Track current account balances
- Generate and export reconciliation reports
- Maintain financial accuracy and accountability

---

##  Features

###  Key Functionalities

- **Real-Time Summary Display**
  - Teller name, account number, user ID
  - Debit and credit totals
  - Current account balance


           ![Teller Transaction Reconciliation summary Interface](../../../static/img/teller_reconcile.png)

- **Search & Filter Options**
  - Filter by teller name, account number, transaction totals, or date range(start and end date)

- **Reconciliation Reports**
  - View detailed ledger entries with transaction date and Id, transaction type, and running balances
  - Export reports in **PDF** and **Excel** formats

         ![Teller Transaction Reconciliation Interface](../../../static/img/tellerReconcile2.png)


- **Role-Based Access Control**
  - Admins can view all teller records
  - Tellers can only view their own reconciliation details
  - Controlled via `Transaction_Read` permission

---

##  Configuration & Setup

### Requirements

- Tellers must be mapped to valid user accounts and account numbers
- Proper permissions (`Transaction_Read`) must be assigned

### Data Sources

- Transaction data is retrieved from the core ledger
- Balances are calculated using historical and current-day transactions
- Ledger records are associated with teller system user IDs

---

##  Use Cases

| Scenario                         | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| Daily EOD Reconciliation         | Tellers verify total credits/debits before closing operations              |
| Internal Audit & Compliance      | Admins export transaction data for auditing and compliance checks          |
| Discrepancy Investigation        | Quickly locate and resolve mismatched transaction or balance entries       |
| Financial Reporting              | Use downloaded Excel reports for internal or external reporting            |

---

##  Example Workflow

### Example: Reconciling Teller Records for a Date Range

1. Go to **Teller Reconcile File** module.
2. Input `Start Date` and `End Date` (e.g., `01-02-2025` to `06-06-2025`).
3. Search by teller name or account number if needed.
4. View:
   - Debit (e.g., ₹13,502,784.32)
   - Credit (e.g., ₹11,970,860.78)
   - Current Balance (e.g., `CR 1,531,923.54`)
5. Click on a teller row to open their **Teller Report**.
6. Review:
   - Transaction ID, Date, Type, Ledger accounts
   - Debit/Credit amounts, Running Balance
7. Use the **Download** menu to export report as PDF or Excel.

---

##  FAQ

### Q1: Can I export reconciliation data for recordkeeping?
Yes, click on **Download** in the Teller Report interface and choose PDF or Excel.

### Q2: Can tellers see other tellers' records?
No. Only Admins with appropriate permission can view all teller data.

### Q3: Why doesn’t total balance match (credit - debit)?
Because balances may include opening or previous day’s closing amounts not shown in the filtered result.

---


