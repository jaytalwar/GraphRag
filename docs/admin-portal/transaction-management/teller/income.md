---
sidebar_position: 4
---
# Income Management

The Income Management feature allows tellers to record and manage various types of income within the system. This documentation provides an overview of the income management functionality and its usage.

## Overview

The income management interface provides a user-friendly way to:
- Record new income transactions
- View income history
- Manage income categories
- Track income details
- Generate income reports
- Process income transactions
- Manage income approvals

## Features

### Income Recording
- **Income Type**: Select from predefined income categories
- **Amount**: Enter the income amount
- **Description**: Add detailed description of the income
- **Date**: Record the date of the income
- **Reference Number**: Optional reference number for tracking
- **Account Code**: System-generated income account code
- **Transaction Mode**: Select appropriate transaction mode
- **Receipt Number**: Optional receipt number for documentation
- **Transaction Number**: System-generated unique identifier
- **Tenant ID**: Associated organization identifier
- **Entry Type**: System automatically sets to Receipt for Other Income and Application Charges

### Transaction Types
The system supports the following income transaction types:
- **Fee & Penalties**: For recording fees and penalties
- **Other Income**: For miscellaneous income entries
- **Reverse Fee & Penalties**: For reversing fee and penalty entries

### Transaction Modes
Income transactions can be processed through various modes:
- **Cash**: Physical cash transactions
- **Bank**: Bank transfer transactions
- **Transfer**: Internal account transfers
- **MNO**: Mobile Network Operator transactions

### Income Categories
Common income categories include:
- Membership Fees
- Service Charges
- Interest Income
- Other Operating Income
- Investment Income
- Application Charges
- Other Income

### Transaction Processing
The system handles income transactions through the following process:
1. **Transaction Creation**:
   - System automatically assigns the default income account for the Sacco
   - Generates unique transaction number
   - Records transaction date and time
   - Associates with the appropriate tenant
   - Sets appropriate entry type (Receipt for Other Income)

2. **Entry Processing**:
   - Creates credit entry in the income account
   - Creates corresponding debit entries
   - Maintains proper ledger codes
   - Tracks account balances
   - Handles special cases like Application Charges

3. **Approval Workflow**:
   - Requires appropriate approval permissions
   - Validates transaction details
   - Ensures proper authorization
   - Maintains audit trail

### Impact Areas
Income transactions affect several areas of the system:

1. **Account Balances**:
   - Updates the income account balance
   - Affects the corresponding debit account balance
   - Maintains proper credit/debit relationships

2. **Ledger Entries**:
   - Creates entries in the general ledger
   - Updates ledger codes for proper accounting
   - Maintains audit trail of all transactions

3. **Financial Reports**:
   - Impacts income statements
   - Affects balance sheet calculations
   - Influences financial performance metrics

4. **Reconciliation**:
   - Requires regular reconciliation with bank statements
   - Maintains transaction history for audit purposes
   - Supports financial reporting accuracy

5. **System Integration**:
   - Impacts fee and penalty processing

6. **Compliance**:
   - Maintains proper documentation
   - Supports audit requirements
   - Ensures regulatory compliance

## Usage Guide

### Recording a New Income
1. **Access the Income Management Interface**:
   - Navigate to the Income Management section
   - Click on "New Income" button to open the transaction form

2. **Select Transaction Type**:
   - Choose from available income types:
     - Fee & Penalties
     - Other Income
     - Reverse Fee & Penalties
   - The system will automatically set the appropriate entry type based on selection

3. **Enter Transaction Details**:
   - **Amount**: Enter the income amount
   - **Description**: Provide a clear description of the income source
   - **Date**: Select the transaction date
   - **Transaction Mode**: Choose from:
     - Cash
     - Bank
     - Transfer
     - MNO (Mobile Network Operator)

4. **Account Information**:
   - The system automatically assigns:
     - Default income account for the Sacco
     - Unique transaction number
     - Appropriate tenant ID
     - Account code
   - For debit entries, specify:
     - Account ID
     - Ledger code (if applicable)

5. **Optional Information**:
   - Reference Number: For tracking purposes
   - Receipt Number: For documentation
   - Supporting documents: Attach if available

6. **Review and Submit**:
   - Verify all entered details
   - Check account balances
   - Ensure proper authorization
   - Click "Save" to record the income

7. **Post-Submission**:
   - System automatically:
     - Creates credit entry in the income account
     - Creates corresponding debit entries
     - Updates account balances
     - Maintains audit trail
   - Transaction enters approval workflow
   - Status can be tracked in the income history

### Viewing Income History
1. Access the income list view
2. Use filters to search for specific income entries
3. View detailed information for each income entry including:
   - Account summary
   - Transaction details
   - Balance information
   - Approval status
4. Export income reports if needed

### Account Summary View
The income account summary displays:
- Account Name
- Account Number
- General Ledger Code
- Current Balance
- Transaction History
- Approval Status

### Transaction Management
- **Processing**: System automatically processes income transactions
- **Validation**: Checks for proper authorization and documentation
- **Reconciliation**: Supports transaction reconciliation
- **Deletion**: Allows deletion of transactions with proper permissions
- **Audit Trail**: Maintains complete transaction history
- **Special Handling**: 
  - Application Charges are processed as Receipt entries
  - Other Income transactions are automatically set as Receipt type
  - Supports multiple payment modes

## Best Practices
- Always provide clear descriptions for income entries
- Attach supporting documents when available
- Review income entries regularly
- Maintain proper categorization
- Keep reference numbers for audit purposes
- Ensure accurate account code assignment
- Verify transaction details before submission
- Follow proper approval workflow
- Maintain proper documentation
- Regular reconciliation of income accounts
- Special attention to Application Charges and Other Income entries

## Screenshot References

![Income Management Interface - View 1](../../../../static/img/Teller-income-1.png)

![Income Management Interface - View 2](../../../../static/img/Teller-income-2.png)

## Related Documentation
- [Transaction Management Overview](../README.md)
- [Teller Operations](../README.md)
