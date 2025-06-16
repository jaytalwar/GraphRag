# General Ledger Management

The General Ledger Management feature enables tellers to process various types of general ledger entries and corporate tax payments within the system.

## Overview

The general ledger interface provides functionality to:
- Process general ledger entries
- Handle corporate tax payments
- Manage journal entries
- Process transfers between accounts
- Generate ledger reports
- Maintain audit trails

## Features

### General Ledger Recording
- **Transaction Type**: Select from predefined categories
- **Amount**: Enter transaction amount
- **Description**: Add transaction details
- **Date**: Record transaction date
- **Reference Number**: Optional tracking number
- **Account Code**: System-generated code
- **Transaction Mode**: Select payment mode
- **Receipt Number**: Optional documentation number
- **Transaction Number**: System-generated identifier
- **Entry Type**: System-set based on transaction (DR/CR)
- **Ledger Code**: Account classification code
- **Ledger Name**: Account classification name

### Transaction Types
The system supports these general ledger transaction types:
- **General Ledger Entry**:
  - Processes journal entries with debit and credit entries
  - Updates account balances based on entry type
  - Maintains transaction history with ledger codes
  - Handles multiple accounts in a single transaction
  - Validates entry limits and account combinations
  - Supports both debit (DR) and credit (CR) entries
  - Maintains ledger codes and names for each entry
  - Processes complex transaction lists with multiple entries
  - Updates account balances based on entry type
  - Maintains transaction references and dates
  - Records user IDs and tenant information
  - Handles bulk entries for multiple accounts

- **Corporate Tax Payment**:
  - Processes tax payments with proper accounting entries
  - Updates tax accounts with debit and credit entries
  - Maintains tax history with proper documentation
  - Handles tax calculations and validations
  - Validates tax limits and account combinations
  - Calculates total PnL for tax purposes
  - Tracks net income and expenses for tax reporting
  - Maintains tax records with proper documentation
  - Processes tax entries with proper accounting
  - Updates tax balances based on entry type
  - Calculates tax amounts and updates status

### Transaction Processing
1. **Transaction Creation**:
   - Assigns accounts and generates transaction numbers
   - Records date/time and sets entry types
   - Validates balances and checks eligibility
   - For general ledger entries:
     - Validates account combinations and entry limits
     - Updates multiple accounts with proper entries
     - Processes complex transaction lists
     - Maintains ledger codes and names
     - Handles bulk entries for multiple accounts
     - Processes expense/income accounts
     - Updates account balances based on entry type
     - Maintains transaction references
   - For corporate tax:
     - Validates tax accounts and limits
     - Updates tax records with proper entries
     - Calculates tax amounts and processes payments

2. **Entry Processing**:
   - Creates account entries with proper types
   - Updates balances based on entry type
   - Maintains ledger codes and names
   - Updates account status and validates transfers
   - For general ledger entries:
     - Processes multiple entries with proper types
     - Updates account balances based on entry type
     - Maintains transaction records with references
     - Handles debit/credit entries properly
     - Updates ledger information
     - Processes bulk entries for multiple accounts
     - Updates account transactions
     - Maintains user references and dates
   - For corporate tax:
     - Processes tax entries with proper types
     - Updates tax balances based on entry type
     - Maintains tax records with documentation
     - Calculates tax amounts and updates status

3. **Approval Workflow**:
   - Validates permissions and authorization
   - Maintains audit trail and validates teller balance
   - For general ledger entries:
     - Validates account authorization and entry limits
     - Requires special approval for certain entries
     - Verifies ledger codes and account types
     - Validates bulk entries and user permissions
   - For corporate tax:
     - Validates tax authorization and limits
     - Requires tax approval for payments
     - Verifies tax calculations and documentation

### Validation Rules
1. **Balance Validation**:
   - Checks account balances before transactions
   - Validates transaction amounts and limits
   - Prevents overdrafts and invalid entries
   - For corporate tax:
     - Validates tax balances and calculations
     - Verifies tax eligibility and PnL

2. **Transfer Validation**:
   - Validates source/destination accounts
   - Checks transfer limits and account status
   - Ensures sufficient balance for transfers
   - For corporate tax:
     - Validates tax accounts and transfers
     - Verifies tax status and allocation

3. **Teller Validation**:
   - Checks teller balance and reserve ledger
   - Verifies authorization and documentation
   - For corporate tax:
     - Validates tax documentation and records
     - Verifies tax authorization and compliance

4. **Account Validation**:
   - Verifies account status and eligibility
   - Checks account type and proper linkage
   - For corporate tax:
     - Verifies tax account status and type
     - Validates tax account linkage and compliance

## Usage Guide

### Processing a General Ledger Transaction
1. **Access Interface**:
   - Navigate to General Ledger Management
   - Click appropriate transaction type
   - Select between General Ledger Entry or Corporate Tax Payment

2. **Select Type**:
   - Choose transaction type:
     - General Ledger Entry
     - Corporate Tax Payment
   - System sets entry type (DR/CR)
   - For corporate tax:
     - System calculates tax amount
     - Displays tax details

3. **Enter Details**:
   - Amount and description
   - Date and transaction mode
   - For general ledger entries:
     - Account details and entry terms
     - Ledger codes and bulk entry details
     - Account types and user references
   - For corporate tax:
     - Tax details and payment terms
     - Tax calculations and documentation

4. **Account Information**:
   - System assigns:
     - Account numbers and transaction numbers
     - Tenant ID and account codes
     - Ledger codes and user IDs
     - Transaction dates and references
   - For general ledger entries:
     - Source and destination accounts
     - Account types and ledger information
     - Bulk entry accounts and references
   - For corporate tax:
     - Tax accounts and payment accounts
     - Tax types and calculations

5. **Optional Information**:
   - Reference numbers and receipt numbers
   - Supporting documents and tax references
   - Tax documents and records

6. **Review and Submit**:
   - Verify details and check balances
   - Ensure authorization and save transaction
   - For corporate tax:
     - Verify tax details and balances
     - Ensure tax authorization and calculations

### Viewing History
1. Access list view with filters
2. View details:
   - Account summary and transaction details
   - Balance information and approval status
   - For corporate tax:
     - Tax summary and payment details
     - Tax balances and calculations
3. Export reports as needed

### Account Summary
Displays:
- Account details and current balances
- Transaction history and approval status
- Transaction summary and outstanding amounts
- For corporate tax:
  - Tax details and balances
  - Payment history and tax status
  - Tax calculations and documentation

## Best Practices
- Provide clear descriptions and documentation
- Attach supporting documents and references
- Review entries regularly and maintain categorization
- Keep reference numbers and verify details
- Follow approval workflow and reconcile regularly
- Monitor transaction limits and validate combinations
- Handle errors promptly and maintain records
- For corporate tax:
  - Maintain tax records and verify details
  - Track tax history and monitor limits
  - Ensure tax compliance and verify calculations

## Screenshot References

![General Ledger Management Interface](../../../../static/img/teller_generalledger_entries.png)
![Corporate Tax Payment Interface](../../../../static/img/teller_genledger_coorportatetax.png)

## Related Documentation
- [Transaction Management Overview](../README.md)
- [Teller Operations](../README.md)
