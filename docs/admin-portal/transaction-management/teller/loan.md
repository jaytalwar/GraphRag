---
sidebar_position: 1
---
# Loan Management

The Loan Management feature enables tellers to process loan-related transactions within the system.

## Overview

The loan management interface provides functionality to:
- Process loan disbursements
- Handle loan repayments
- Manage application charges
- Process bulk repayments
- Handle error corrections
- Generate reports
- Manage approvals

## Features

### Loan Recording
- **Loan Type**: Select from predefined categories
- **Amount**: Enter transaction amount
- **Description**: Add transaction details
- **Date**: Record transaction date
- **Reference Number**: Optional tracking number
- **Account Code**: System-generated code
- **Transaction Mode**: Select payment mode
- **Receipt Number**: Optional documentation number
- **Transaction Number**: System-generated identifier
- **Tenant ID**: Organization identifier
- **Entry Type**: System-set based on transaction

### Transaction Types
The system supports these loan transaction types:
- **Loan Disbursement (DIS)**:
  - Validates loan approval
  - Creates debit entry
  - Updates loan balance
  - Maintains disbursement history
  - Updates member loan status

- **Loan Repayment (REP)**:
  - Validates loan balance
  - Creates credit entry
  - Updates repayment history
  - Updates member loan status
  - Handles partial/full payments

- **Application Charge (APP)**:
  - Validates loan application
  - Creates charge entry
  - Updates application status
  - Maintains charge history
  - Updates member records

- **Bulk Repayment**:
  - Processes multiple repayments
  - Updates loan balances
  - Maintains bulk history
  - Handles group transactions
  - Validates repayment schedules

- **Error Correction**:
  - Corrects transaction errors
  - Supports disbursement corrections
  - Handles repayment corrections
  - Maintains correction history
  - Validates correction amounts

### Transaction Modes
Available transaction modes:
- Cash
- Bank
- Transfer
- MNO

### Transaction Processing
1. **Transaction Creation**:
   - Assigns loan account
   - Generates transaction number
   - Records date/time
   - Sets entry type
   - Validates balance
   - Checks eligibility
   - For bulk repayments:
     - Validates group transactions
     - Checks repayment schedules
     - Updates multiple accounts
   - For error corrections:
     - Validates original transaction
     - Checks correction type
     - Maintains audit trail

2. **Entry Processing**:
   - Creates account entries
   - Updates balances
   - Maintains ledger codes
   - Updates loan status
   - Validates transfers
   - For bulk repayments:
     - Processes multiple entries
     - Updates member loans
     - Maintains group records
   - For error corrections:
     - Reverses original entry
     - Creates correction entry
     - Updates loan counts

3. **Approval Workflow**:
   - Validates permissions
   - Checks authorization
   - Maintains audit trail
   - Validates teller balance
   - For bulk repayments:
     - Validates group authorization
     - Checks bulk limits
   - For error corrections:
     - Requires special approval
     - Validates correction reason

### Validation Rules
1. **Balance Validation**:
   - Checks loan balance
   - Validates repayment amount
   - Prevents overpayment
   - Validates disbursement limits

2. **Transfer Validation**:
   - Validates source/destination
   - Checks transfer limits
   - Verifies account status
   - Ensures sufficient balance

3. **Teller Validation**:
   - Checks teller balance
   - Validates reserve ledger
   - Verifies authorization
   - Ensures proper documentation

4. **Account Validation**:
   - Verifies account status
   - Checks member eligibility
   - Validates loan type
   - Ensures proper linkage

## Usage Guide

### Processing a Loan Transaction
1. **Access Interface**:
   - Navigate to Loan Management
   - Click appropriate transaction type

2. **Select Type**:
   - Choose transaction type:
     - Disbursement
     - Repayment
     - Application Charge
     - Bulk Repayment
     - Error Correction
   - System sets entry type

3. **Enter Details**:
   - Amount
   - Description
   - Date
   - Transaction mode
   - For disbursements:
     - Loan account details
     - Disbursement terms
   - For repayments:
     - Repayment schedule
     - Payment breakdown

4. **Account Information**:
   - System assigns:
     - Loan account
     - Transaction number
     - Tenant ID
     - Account code
   - For transfers:
     - Source account
     - Destination account
     - Loan type

5. **Optional Information**:
   - Reference number
   - Receipt number
   - Supporting documents

6. **Review and Submit**:
   - Verify details
   - Check balances
   - Ensure authorization
   - Save transaction

### Viewing History
1. Access list view
2. Use filters
3. View details:
   - Account summary
   - Transaction details
   - Balance information
   - Approval status
4. Export reports

### Account Summary
Displays:
- Account details
- Current balance
- Transaction history
- Approval status
- Repayment schedule
- Outstanding amount

## Best Practices
- Provide clear descriptions
- Attach supporting documents
- Review entries regularly
- Maintain proper categorization
- Keep reference numbers
- Verify details before submission
- Follow approval workflow
- Regular reconciliation
- Special attention to disbursements and repayments
- Monitor repayment schedules
- Track transaction limits
- Validate application charges
- Handle error corrections promptly

## Screenshot References

![Loan Management Interface](../../../../static/img/teller-loan.png)

## Related Documentation
- [Transaction Management Overview](../README.md)
- [Teller Operations](../README.md)
