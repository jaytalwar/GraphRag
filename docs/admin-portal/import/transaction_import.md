# Transaction Import

The Transaction Import functionality allows administrators to bulk import financial transactions into CAMS. This document outlines the process, requirements, and validation rules for importing transactions.

## Overview

The transaction import supports importing various types of transactions:
1. Loan Repayments
2. Deposits
3. Withdrawals
4. Fee and Penalties
5. Member Charges

## Import Template Fields

### General Fields

| Field Name | Description | Validation Rules |
|------------|-------------|------------------|
| Ref Id | Unique identifier of the transaction in the existing system | Conditionally Mandatory (either RefId, User Id or Account Number) |
| User Id | CAMS User ID of the member associated with the transaction | Conditionally Mandatory (either RefId, User Id or Account Number) |
| Account Number | Account number where the transaction should be posted | Optional, must exist in CAMS |
| Product Type | Type of account associated with the transaction | Mandatory. Must be one of: Saving, Share, Loan, MemberCharge |
| Product Name | Name of the account product | Mandatory, must match CAMS configuration |
| Transaction Date | Date of the transaction | Mandatory, valid date (MM-DD-YYYY) |
| Amount | Amount involved in the transaction | Mandatory, numeric |
| Type | Type of transaction | Mandatory, must be one of: Repayment, Deposit, Withdraw, FeeAndPenalties |
| Operation Type | Transaction operation type | Mandatory, "DataImport" text only |
| Transaction Mode | Mode of transaction | Optional, text only (e.g., Cash or Online) |
| Transaction Reference Number | Unique identifier for the transaction | Optional, text only (not currently in use) |
| Receipt Number | Receipt number for the transaction | Optional, text only (not currently in use) |
| Cheque Number | Cheque number for the transaction | Optional, text only (not currently in use) |
| Comment | Additional comments about the transaction | Optional, text only (not currently in use) |

### Loan Repayment Fields

| Field Name | Description | Validation Rules |
|------------|-------------|------------------|
| Principal | Principal portion of a loan transaction | Optional, numeric. Adjusted toward the Principal |
| Interest | Interest portion of a loan transaction | Optional, numeric. Adjusted toward the Interest |
| Charges | Charges portion of a loan transaction | Optional, numeric. Adjusted toward the Charges |
| Charge Name | Name of the charge associated with the transaction | Optional, text only |

## Field Applicability

1. **General Fields**
   - Applicable to all transaction types
   - Includes Ref Id, User Id, Account Number, Product Type, Product Name, Transaction Date, and Amount
   - Either one of Ref Id, User Id, or Account Number is required

2. **Loan Repayment Fields**
   - Specific to loan repayment transactions
   - Fields like Principal, Interest, Charges, and Charge Name break down the Amount into components
   - Should be specified only when break up is known, otherwise system breaks the Amount automatically

3. **Optional Fields**
   - Transaction Mode, Transaction Reference Number, Receipt Number, and Comment
   - Provide additional context or tracking
   - Currently not in use for some fields

## Validation Rules Summary

### Mandatory Fields

1. **For All Transactions:**
   - Product Type
   - Product Name
   - Transaction Date
   - Amount
   - Operation Type
   - Either one of Ref Id, User Id, or Account Number

### Field Format Requirements

1. **Date Fields:**
   - Use MM-DD-YYYY format
   - Ensure no future dates

2. **Numeric Fields:**
   - Use valid numeric values for:
     - Amount
     - Principal
     - Interest
     - Charges

3. **Product Matching:**
   - Product Name must match CAMS configuration
   - Product Type must be valid

## Import Process

1. **File Upload**
   - Supported formats: Excel files (.xlsx, .xls)
   - Maximum file size: 5MB
   - File must not have multiple extensions

2. **Data Validation**
   - System validates the uploaded file format and structure
   - Checks for required columns and data integrity
   - Validates transaction types and their specific requirements

3. **Data Processing**
   - Valid records are processed and imported into the system
   - Failed records are marked with specific error messages
   - Import status can be tracked in the import history

## Error Handling

- Each error is reported with the specific row number and error description
- Common errors include:
  - Missing required fields
  - Invalid transaction types
  - Invalid account references
  - Invalid dates
  - Invalid amounts
  - Missing product configurations

## Best Practices

1. **Before Import**
   - Verify all required fields are present
   - Ensure data follows the specified format
   - Validate account references
   - Check product configurations

2. **During Import**
   - Monitor the import progress
   - Review any validation errors
   - Keep the source file for reference

3. **After Import**
   - Verify imported transactions in the system
   - Check account balances and transaction history
   - Update any failed entries manually if needed

## Reference Images
![Transaction Import Process 1](/img/transaction_import1.png)
![Transaction Import Process 2](/img/transaction_import2.png)
