---
sidebar_position: 5
---
# Expense Management

The Expense Management feature allows tellers to record and manage various types of expenses within the system. This documentation provides an overview of the expense management functionality and its usage.

## Overview

The expense management interface provides a user-friendly way to:
- Record new expenses
- View expense history
- Manage expense categories
- Track expense details
- Generate expense reports
- Process expense transactions
- Manage expense approvals

## Features

### Expense Recording
- **Expense Type**: Select from predefined expense categories
- **Amount**: Enter the expense amount
- **Description**: Add detailed description of the expense
- **Date**: Record the date of the expense
- **Reference Number**: Optional reference number for tracking
- **Account Code**: System-generated expense account code
- **Transaction Mode**: Select appropriate transaction mode
- **Receipt Number**: Optional receipt number for documentation
- **Transaction Number**: System-generated unique identifier
- **Tenant ID**: Associated organization identifier

### Expense Categories
Common expense categories include:
- Office Supplies
- Travel Expenses
- Utilities
- Maintenance
- Other Operating Expenses

### Transaction Processing
The system handles expense transactions through the following process:
1. **Transaction Creation**:
   - System automatically assigns the default expense account for the Sacco
   - Generates unique transaction number
   - Records transaction date and time
   - Associates with the appropriate tenant

2. **Entry Processing**:
   - Creates debit entry in the expense account
   - Creates corresponding credit entries
   - Maintains proper ledger codes
   - Tracks account balances

3. **Approval Workflow**:
   - Requires appropriate approval permissions
   - Validates account balances
   - Ensures proper authorization
   - Maintains audit trail

## Usage Guide

### Recording a New Expense
1. Navigate to the Expense Management section
2. Click on "New Expense" button
3. Fill in the required details:
   - Select expense type
   - Enter amount
   - Add description
   - Select date
   - (Optional) Add reference number
   - (Optional) Add receipt number
4. Click "Save" to record the expense

### Viewing Expense History
1. Access the expense list view
2. Use filters to search for specific expenses
3. View detailed information for each expense entry including:
   - Account summary
   - Transaction details
   - Balance information
   - Approval status
4. Export expense reports if needed

### Account Summary View
The expense account summary displays:
- Account Name
- Account Number
- General Ledger Code
- Current Balance
- Transaction History
- Approval Status

### Transaction Management
- **Processing**: System automatically processes expense transactions
- **Validation**: Checks for sufficient funds and proper authorization
- **Reconciliation**: Supports transaction reconciliation
- **Deletion**: Allows deletion of transactions with proper permissions
- **Audit Trail**: Maintains complete transaction history

## Best Practices
- Always provide clear descriptions for expenses
- Attach supporting documents when available
- Review expenses regularly
- Maintain proper categorization
- Keep reference numbers for audit purposes
- Ensure accurate account code assignment
- Verify transaction details before submission
- Follow proper approval workflow
- Maintain proper documentation
- Regular reconciliation of expense accounts

## Screenshot Reference

![Expense Management Interface](../../../../static/img/teller_expense.png)

## Related Documentation
- [Transaction Management Overview](../README.md)
- [Teller Operations](../README.md)
