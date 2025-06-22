---
sidebar_position: 5
---

# All Transactions

## Overview

The **All Transactions** module provides a centralized dashboard for tracking every financial transaction processed through the system. It supports granular filtering, detailed auditability, and clear categorization—empowering finance, audit, and operations teams to investigate and report transactions efficiently.

---

## Key Features

### Filter & Search Options

Admins can filter transactions by:

- **Date Range** (`Start Date` to `End Date`)
- **Transaction Status**
- **Transaction Source**
- **Search Criteria**:
  - Transaction Number
  - Product Name
  - Account Number
  - Member Name
  - User

#### Transaction Status Filters Include:

| Status             | Description                                |
|--------------------|--------------------------------------------|
| Initiated          | Transaction was initiated                  |
| Created            | Transaction is recorded but not posted     |
| Submitted          | Transaction submitted for approval         |
| PendingApproval    | Awaiting approval (Maker Checker Transaction)                      |
| Approved           | Approved but not posted                    |
| Posted             | Successfully recorded                      |
| Processed          | Transaction in processing state               |
| Rejected           | Declined during processing or approval     |
| Resubmitted        | Reattempted after rejection                |
| Reversed           | Reversed due to error or correction        |
| Deleted            | Soft-deleted or invalidated transaction    |
| Failed             | Processing error occurred                  |
| Error              | Unexpected system or validation issue (hover on alert to view error)     |

#### Source Filters Include:

| Source Type | Description                               |
|-------------|-------------------------------------------|
| All         | No filter; shows all transactions         |
| Teller      | Initiated by a teller at a branch         |
| Import      | Bulk-uploaded via import file             |
| Online      | Submitted via digital or self-service     |
| Job         | Triggered by scheduled job                |
| System      | System-generated (e.g.,Interest Accrued , ApplicationCharge)      |

---

## Transaction Table Columns

| Column Name        | Description                             |
|--------------------|-----------------------------------------|
| Date               | Transaction timestamp                   |
| Transaction Number | Unique ID for each transaction          |
| Amount (INR)       | Debit or credit value                   |
| Status             | Indicates the current stage of the transaction process    |
| Product Name       | Related financial product (e.g., loan)  |
| Account            | Account involved in the transaction     |
| Member             | Member linked to the transaction        |
| User               | Initiating staff user                   |
| Source             | Source type (e.g:Online, Teller, System, Job ,Import)      |
| Actions            | Edit or review transaction(When there issue in acccouting )              |

   All Transactions View:
      ![All Transactions Interface](../../../static/img/all_transactions.png)

---

## Usage Guide

### Step-by-Step: Access & Filter Transactions

1. Go to **All Transactions** from the sidebar
2. Apply filters for:
   - Source
   - Status
   - Date range
   - User or Member
3. Click on a transaction to view details
4. Use the **Actions** column to make corrections or view full logs

---

## Best Practices

###  Monitoring & Auditing
- Review `Rejected`, `Failed`, or `Reversed` transactions daily
- Cross-check transaction amounts against source accounts
- Maintain logs for high-value and backdated entries

### Error Handling
- Use “Error” and “Resubmitted” filters to diagnose process issues
- Always capture rejection reason when reversing


---
