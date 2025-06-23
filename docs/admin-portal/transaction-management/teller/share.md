---
sidebar_position: 3
---
# Share Management

The Share Management feature enables tellers to process share-related transactions within the system.

## Overview

The share management interface provides functionality to:
- Record share transactions
- View transaction history
- Manage share accounts
- Generate reports
- Process transactions
- Handle approvals

## Features

### Share Recording
- **Share Type**: Select from predefined categories
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
The system supports these share transaction types:
- **Share Purchase (DPO)**:
  - Updates member share count
  - Creates credit entry
  - Maintains purchase history
  - Updates shareholding

- **Share Transfer (TRF)**:
  - Validates accounts
  - Updates balances
  - Maintains audit trail
  - Updates share counts

- **Share Withdrawal (WDL)**:
  - Validates balance
  - Updates account
  - Maintains history
  - Updates shareholding

- **Share Adjustment**:
  - Requires authorization
  - Maintains history
  - Updates balances
  - Updates counts

- **Bulk Share Deposit**:
  - Processes multiple share purchases
  - Updates member share counts
  - Maintains bulk transaction history
  - Handles group transactions
  - Validates per-share value
  - Updates share balances

- **Error Correction**:
  - Corrects transaction errors
  - Supports deposit corrections
  - Handles withdrawal corrections
  - Maintains correction history
  - Validates correction amounts
  - Updates share balances

### Transaction Modes
Available transaction modes:
- Cash
- Bank
- Transfer
- MNO

### Transaction Processing
1. **Transaction Creation**:
   - Assigns share account
   - Generates transaction number
   - Records date/time
   - Sets entry type
   - Validates balance
   - Checks eligibility
   - For bulk deposits:
     - Validates group transactions
     - Checks per-share value
     - Updates multiple accounts
   - For error corrections:
     - Validates original transaction
     - Checks correction type
     - Maintains audit trail

2. **Entry Processing**:
   - Creates account entries
   - Updates balances
   - Maintains ledger codes
   - Updates share count
   - Validates transfers
   - For bulk deposits:
     - Processes multiple entries
     - Updates member shares
     - Maintains group records
   - For error corrections:
     - Reverses original entry
     - Creates correction entry
     - Updates share counts

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

2. **Transfer Validation**:
   - Validates source/destination
   - Checks transfer limits
   - Verifies account status

3. **Teller Validation**:
   - Checks teller balance
   - Validates reserve ledger
   - Verifies authorization

4. **Account Validation**:
   - Verifies account status
   - Checks member eligibility
   - Validates account type

## Usage Guide

### Recording a Share Transaction
1. **Access Interface**:
   - Navigate to Share Management
   - Click "New Share Transaction"

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
     - Share account
     - Transaction number
     - Tenant ID
     - Account code
   - For transfers:
     - Source account
     - Destination account
     - Share type

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

## Screenshot References

![Share Management Interface](../../../../static/img/teller_share.png)

## Related Documentation
- [Transaction Management Overview](../README.md)
- [Teller Operations](../README.md)
