---
sidebar_position: 2
---
# Saving Management

The Saving Management feature enables tellers to process saving-related transactions within the system.

## Overview

The saving management interface provides functionality to:
- Record saving transactions
- View transaction history
- Manage saving accounts
- Generate reports
- Process transactions
- Handle approvals

## Features

### Saving Recording
- **Saving Type**: Select from predefined categories
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
The system supports these saving transaction types:
- **Deposit (DPO)**:
  - Updates account balance
  - Creates credit entry
  - Maintains deposit history
  - Updates member saving

- **Withdrawal (WDL)**:
  - Validates balance
  - Updates account
  - Maintains history
  - Updates member saving

- **Transfer (TRF)**:
  - Validates accounts
  - Updates balances
  - Maintains audit trail
  - Updates both accounts

- **Bulk Deposit**:
  - Processes multiple deposits
  - Updates account balances
  - Maintains bulk history
  - Handles group transactions

- **Error Correction**:
  - Corrects transaction errors
  - Supports deposit corrections
  - Handles withdrawal corrections
  - Maintains correction history

### Transaction Modes
Available transaction modes:
- Cash
- Bank
- Transfer
- MNO

### Transaction Processing
1. **Transaction Creation**:
   - Assigns saving account
   - Generates transaction number
   - Records date/time
   - Sets entry type
   - Validates balance
   - Checks eligibility
   - For bulk deposits:
     - Validates group transactions
     - Checks minimum balance
     - Updates multiple accounts
   - For error corrections:
     - Validates original transaction
     - Checks correction type
     - Maintains audit trail

2. **Entry Processing**:
   - Creates account entries
   - Updates balances
   - Maintains ledger codes
   - Updates saving count
   - Validates transfers
   - For bulk deposits:
     - Processes multiple entries
     - Updates member savings
     - Maintains group records
   - For error corrections:
     - Reverses original entry
     - Creates correction entry
     - Updates saving counts

3. **Approval Workflow**:
   - Validates permissions
   - Checks authorization
   - Maintains audit trail
   - Validates teller balance
   - For bulk deposits:
     - Validates group authorization
     - Checks bulk limits
   - For error corrections:
     - Requires special approval
     - Validates correction reason

### Validation Rules
1. **Balance Validation**:
   - Checks available balance
   - Enforces minimum balance
   - Prevents negative balance
   - Validates withdrawal limits

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
   - Validates account type
   - Ensures proper linkage

## Usage Guide

### Recording a Saving Transaction
1. **Access Interface**:
   - Navigate to Saving Management
   - Click "New Saving Transaction"

2. **Select Type**:
   - Choose transaction type
   - System sets entry type

3. **Enter Details**:
   - Amount
   - Description
   - Date
   - Transaction mode

4. **Account Information**:
   - System assigns:
     - Saving account
     - Transaction number
     - Tenant ID
     - Account code
   - For transfers:
     - Source account
     - Destination account
     - Saving type

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

## Best Practices
- Provide clear descriptions
- Attach supporting documents
- Review entries regularly
- Maintain proper categorization
- Keep reference numbers
- Verify details before submission
- Follow approval workflow
- Regular reconciliation
- Special attention to transfers and withdrawals
- Monitor minimum balance requirements
- Track transaction limits

## Screenshot References

![Saving Management Interface](../../../../static/img/teller_saving.png)

## Related Documentation
- [Transaction Management Overview](../README.md)
- [Teller Operations](../README.md) 