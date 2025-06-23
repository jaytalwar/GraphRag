# Account Import

The Account Import functionality allows administrators to bulk import different types of accounts (Loan, Saving, Share, and Fixed Deposit) into the system. This document outlines the process, requirements, and validation rules for importing accounts.

## Overview

The account import supports two main methods:
1. **Migrate Existing Account**
   - Import existing accounts with their current balances and details
   - Supports loan accounts with repayment history

2. **Bulk Create New Account**
   - Create new accounts in bulk
   - Set initial balances and configurations
   - Establish new account relationships

## Import Process

1. **File Upload**
   - Supported formats: Excel files (.xlsx, .xls)
   - Maximum file size: 5MB
   - File must not have multiple extensions

2. **Data Validation**
   - System validates the uploaded file format and structure
   - Checks for required columns and data integrity
   - Validates account types and their specific requirements

3. **Data Processing**
   - Valid records are processed and imported into the system
   - Failed records are marked with specific error messages
   - Import status can be tracked in the import history

## Import Template Fields

### General Fields (Applicable to All Account Types)

| Field Name | Description | Validation Rules |
|------------|-------------|------------------|
| Ref Id | Unique identifier of the account in the existing system | Mandatory |
| User Id | CAMS User ID of the member associated with the account | Conditionally Mandatory (either RefID, User Id, or Email Address) |
| Email Address | Email of the member, used for associating the account | Conditionally Mandatory (either RefID, User Id, or Email Address) |
| Product Type | Type of account (Saving, Share, Loan) | Mandatory, must match predefined types |
| Product Name | Name of the account product (e.g., Savings Plan A) | Mandatory, text only |
| Opening Balance | Initial balance of the account | Mandatory, numeric |

### Loan Account Fields

| Field Name | Description | Validation Rules |
|------------|-------------|------------------|
| Total Principal | Total loan principal amount | Mandatory, numeric |
| Total Interest | Total interest amount calculated on the loan principal | Mandatory, numeric |
| Outstanding Principal | Remaining principal amount on the loan | Mandatory, numeric |
| Outstanding Interest | Remaining interest amount on the loan | Mandatory, numeric |
| Total Charges | Total charges applicable to the loan | Optional, numeric |
| Paid Principal | Amount of principal repaid | Mandatory, numeric |
| Paid Interest | Amount of interest repaid | Mandatory, numeric |
| Paid Charges | Amount of charges repaid | Optional, numeric |
| Outstanding Charges | Amount of outstanding charges | Optional, numeric |
| Charge Name | Charge name attached with Loan Product | Optional, text only (only one charge name allowed) |
| No of Installments | Loan tenure | Mandatory, numeric |
| Disbursement Date | Date when the loan was disbursed | Mandatory, valid date (MM-DD-YYYY) |
| Ending Date | Date when the loan would be closed | Mandatory, valid date (MM-DD-YYYY) |
| Loan Officer Email | Loan Officer Email ID | Optional, valid email ID |
| Allow Lower Interest Amount | Boolean value for interest amount flexibility | Optional, Boolean (True/False, default: False) |
| GracePeriodTenure | Grace period tenure | Optional, numeric |
| HasInterestOnGracePeriod | Boolean for grace period interest | Optional, Boolean (True/False, default: False) |

### Fixed Deposit Account Fields

| Field Name | Description | Validation Rules |
|------------|-------------|------------------|
| Opening Date | Date when the FD was opened | Mandatory, valid date (MM-DD-YYYY) |
| Interest Rate | Interest rate applicable to the FD product | Mandatory, numeric (e.g., 12.5) |
| Tenure | FD tenure | Mandatory, numeric |
| Duration | Duration of the FD | Mandatory, text (Monthly/Yearly) |
| Maturity Configuration | FD handling at maturity | Mandatory, must be one of: WithdrawalMaturity, TransferToSavingAccount, TransferInterestToSavingAccountAndRenew, RenewPrincipalAndInterest |
| Credit Account Saving Product Name | Saving product for FD maturity amount | Mandatory when Maturity Configuration is TransferToSavingAccount or TransferInterestToSavingAndRenew |
| Interest Calculation Method | Method to calculate FD interest | Mandatory, text only (Flat/Compounded) |

## Validation Rules Summary

### Mandatory Fields

1. **All Account Types**
   - Ref Id
   - Product Type
   - Product Name
   - Opening Balance

2. **Loan Accounts**
   - Opening Balance
   - Total Interest
   - Outstanding Principal
   - Total Principal
   - Paid Principal
   - Outstanding Interest
   - Total Interest
   - Paid Interest
   - No Of Installments
   - Disbursement Date
   - Ending Date

3. **Fixed Deposit Accounts**
   - Opening Date
   - Interest Rate
   - Tenure
   - Duration
   - Maturity Configuration
   - Interest Calculation Method

### Field Format Requirements

1. **Date Fields**
   - Use MM-DD-YYYY format
   - All dates must be valid

2. **Numeric Fields**
   - Opening Balance
   - Total Principal
   - Interest Rate
   - Must contain valid numeric values

3. **Configuration Matching**
   - Product Name must match CAMS setup
   - Maturity Configuration must match predefined options
   - Duration must be either Monthly or Yearly
   - Interest Calculation Method must match system options

### Calculative Fields Validation

1. **Opening Balance**
   - Must be equal to Outstanding Principal
   - Must be equal to Total Principal

2. **Outstanding Amounts**
   - Outstanding Principal = Total Principal - Paid Principal
   - Outstanding Interest = Total Interest - Paid Interest

### Special Notes

1. **Loan Accounts**
   - Charge Name: Only one charge name is allowed, must match the loan product configuration
   - Allow Lower Interest Amount: 
     - Default is False
     - Set to True to bypass system interest calculation validation
   - Grace Period:
     - GracePeriodTenure and HasInterestOnGracePeriod are optional
     - Default for HasInterestOnGracePeriod is False

2. **Fixed Deposit Accounts**
   - Credit Account Saving Product Name:
     - Required when Maturity Configuration is TransferToSavingAccount or TransferInterestToSavingAndRenew
     - Must match an existing saving product in the system

## Import Methods

### 1. Migrate Existing Account
- Used for importing existing accounts with their current state
- Supports loan accounts with repayment history
- Preserves account balances and transactions

### 2. Bulk Create New Account
- Used for creating new accounts in bulk
- Sets initial balances and configurations
- Establishes new account relationships
- Does not support loan repayments

## Error Handling

- Each error is reported with the specific row number and error description
- Common errors include:
  - Missing required fields
  - Invalid product types
  - Invalid amounts
  - Duplicate accounts
  - Invalid dates
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
   - Verify imported accounts in the system
   - Check account balances and relationships
   - Update any failed entries manually if needed

## Reference Images
![Account Import Process 1](/img/account_import1.png)
![Account Import Process 2](/img/account_import2.png)
