---
sidebar_position: 3
---

# Online Transactions

## Overview

The **Online Transactions** module provides a centralized view of all financial transactions occurring across the platform. It enables administrators and operations teams to **monitor, investigate, reconcile, and take action** on transactions in real-time and historically—ensuring accuracy and operational efficiency.

---

## Key Features

###  Transaction Categories

| Category              | Subtypes                                                                 |
|-----------------------|--------------------------------------------------------------------------|
| **Collections (DPO)** | Savings Deposit, Share Deposit (via USSD), Loan Repayment, Loan Charges, Member Charges |
| **Withdrawals (WDL)** | Savings Withdrawals, Loan Disbursements (Normal & Quick Loan)            |
| **Top-ups**           | WBA Top-ups, Collection Wallet Deposits                                  |
| **Prefunds**          | External Credit Disbursements                                            |

---

###  Transaction Statuses

**1. Processing Status**

| Status         | Meaning                                                  |
|----------------|----------------------------------------------------------|
| `INITIATE`     | Transaction has been initiated                           |
| `PENDING`      | Awaiting confirmation from payment gateway               |
| `SUCCESS`      | Successfully processed                                   |
| `FAILED`       | Transaction failed                                       |
| `REJECTED`     | Rejected due to validation or provider failure           |
| `TIMEOUT`      | No response received within expected timeframe           |
| `NEED ATTENTION` | Requires manual review or data correction               |

---

## User Interface Breakdown

###  Filters & Search Options

Admins can filter or search transactions using:

- **Transaction Status**
- **Date Range** (`Start Date` to `End Date`)
- **Search Fields**:
  - Account Number
  - Transaction ID (GUID)
  - Reference ID
  - External ID

 **Pro Tip**: Filter by `NEED ATTENTION` status to quickly identify transactions requiring manual review.

---

###  Transaction Table Columns

| Column Name       | Description                                           |
|-------------------|-------------------------------------------------------|
| **Creation Date** | Date the transaction was initiated                    |
| **Member Name**   | Member involved in the transaction                    |
| **Account Number**| Source or destination account                         |
| **Reference ID**  | Internal transaction reference                        |
| **External ID**   | Identifier from payment provider                      |
| **Payment Provider** | e.g. AIRTEL, COOP, MPKE                            |
| **Type**          | Collection, Disbursement, etc.                        |
| **Status**        | SUCCESS, FAILED, NEED ATTENTION, etc.                |
| **Reconciled**    | Indicates if transaction is reconciled (true/false)   |
| **Amount (INR)**  | Monetary value of the transaction                     |
| **Actions**       | If in `NEED ATTENTION`, shows ✏️ Edit for correction   |

---
### Online Transactions Overview
![Online Transactions](../../../static/img/online_transaction.png)

---

###  Transaction Detail Modal — `NEED ATTENTION`

When a transaction is marked `NEED ATTENTION`, clicking **✏️ Edit** opens the **Transaction Detail Dialog**.

This modal displays:

| Field                  | Description                                      |
|------------------------|--------------------------------------------------|
| **Payment Provider**   | e.g., MPKE, AIRTEL                               |
| **Amount**             | Total transaction value                          |
| **Reference ID & External ID** | Used for reconciliation and traceability  |
| **Error Message**      | Explains failure reason (e.g., missing account)  |
| **Status**             | Always `NEED ATTENTION`                          |
| **Account Correction** | Admin must:                                      |
|                        | - Select Account Type (dropdown)                 |
|                        | - Enter valid Account Number                     |

After correction, choose **Reprocess** to retry or **Cancel** to abort.

### Need Attention Modal
![Need Attention Modal](../../../static/img/needAttention.png)

---

##  Usage Guide

### Step-by-Step Workflow

1. Navigate to **Online Transactions** from the sidebar.
2. Apply filters to locate relevant transactions.
3. For transactions marked `NEED ATTENTION`:
   - Click **✏️ Edit**
   - Review the error message
   - Correct the account or ledger details
   - Click **Reprocess** to retry the transaction

---

##  Best Practices

### Monitoring
- Review all **PENDING** and **FAILED** transactions daily
- Prioritize transactions in `NEED ATTENTION` status
- Cross-verify inconsistencies with payment provider logs

###  Security
- Ensure account numbers are unique and member-specific
- Do not process without validating transaction references
- Maintain clear audit trails for all updates and corrections

###  Documentation
- Maintain a daily log of reconciliations and mismatches
- Capture and archive screenshots for unhandled exceptions
- Escalate unresolved failures to gateway support or engineering

## Frequently Asked Questions (FAQ)

### 1. What does "NEED ATTENTION" status mean?
This status indicates a transaction could not be processed due to incomplete or mismatched data—such as an invalid account number or missing ledger info. Manual review is required via the ✏️ Edit option.

### 2. Can a transaction in `NEED ATTENTION` be reprocessed automatically?
No. Admins must correct the relevant data and click **Reprocess** to manually retry the transaction. This ensures errors aren’t retried without validation.

### 3. What’s the difference between Reference ID and External ID?
- **Reference ID**: Generated internally to track the transaction within your system.
- **External ID**: Issued by the external payment provider (e.g., MPKE, AIRTEL) for reconciliation and traceability.

---

