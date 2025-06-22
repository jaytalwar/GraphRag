# Saving Product

## Overview
Saving Products in CAMS are customizable financial products that allow credit unions to define and offer various types of savings accounts to their members. These products can be tailored with specific rules, interest rates, charges, and account settings to meet the needs of different member groups.

---

## Functional Use in CAMS
- **Purpose:** Create and manage savings account offerings for members, such as regular savings or current accounts.
- **Integration:** Saving products are used when opening member accounts and are linked to transactions and reporting within CAMS.

---

## How to Create a Saving Product
To create a new Saving Product, follow these steps:

### 1. Details
- **Name:** Enter the name of the saving product (required).
- **Description:** Optionally, provide a brief description.
- **Type:** Select the type of saving product from the dropdown. The available types are:
  - **Savings:** Standard savings accounts for regular deposits and withdrawals.
  - **Current:** Accounts designed for frequent transactions, typically used by businesses or organizations.
  - **Deposits:** General deposit accounts for holding funds.
  - **Fixed Deposits:** Accounts where money is deposited for a fixed period and earns a higher interest rate, with limited or no withdrawals during the term.
  - **Recurring Deposits:** Accounts where a fixed amount is deposited regularly (e.g., monthly) for a set period, earning interest.
  Choose the type that best matches the product you want to create.

### 2. Terms
- **Minimum Balance:** Set the minimum balance required to keep the account active.
- **Minimum Transaction Amount:** Set the smallest amount allowed for transactions.
- **Maximum Transaction Amount:** Set the largest amount allowed for transactions.
- **Interest Rate:** Specify the interest rate for the product.
- **Interest Rate Period:** Choose how often the interest is applied (e.g., daily, monthly, yearly).
- **Interest Calculation Type:** Choose how interest is calculated (e.g., daily balance, monthly balance).
- **Interest Compounding Period:** Choose how often interest is compounded.
- **Interest Posting Period:** Choose how often interest is credited to the account.
- **Recurring Saving:** Enable if the product is for recurring savings, and set the amount and period.

### 3. Product Settings
- **Allowed Multiple Accounts:** Allow members to have more than one account of this product type if needed.
- **Allowed as Guarantor/Collateral:** Specify if this product can be used as a guarantor or collateral for loans.
- **Mandatory:** Mark if the product is mandatory for members.
- **Default Autodebit:** Enable this option if you want this saving product to be used as the default account for automatic debits (such as loan repayments or scheduled payments). When enabled, transactions that require automatic deductions will prioritize this account.
- **Permission:** Use the dropdown to select which user roles or groups are allowed to access or open this saving product. This helps control which members or staff can use or manage the product, based on their assigned permissions.

### 4. Saving Product Charges
- **Add Charges on Transfer:** Enable if charges should be applied during transfers.
- **Add Charges:** For each charge, specify:
  - **Transaction Type:** The type of transaction the charge applies to (e.g., deposit, withdrawal).
  - **Charge Name:** Select the charge to apply.
  - **Occurrence:** When the charge is applied (e.g., per transaction, monthly).
  - **Charge Fee Type:** Choose if the charge is a fixed amount or a percentage.
  - **Component Type:** The part of the transaction the charge applies to.

### 5. Accounting
- **Account Name:** Enter the name of the account for this product.
- **General Ledger Code:** Enter the code for the product's main account.
- **Interest Payout Account Name:** (Optional) Enter the account for interest payouts.
- **Interest Payout General Ledger Code:** (Optional) Enter the code for interest payouts.

### 6. History
- View the change history for the product (if any changes have been made).

---

## Example Workflow
1. Go to Products > Saving Product > Create Saving Product.
2. Fill in the product details, terms, and settings as described above.
3. Add any charges that should apply to the product.
4. Enter the required accounting information.
5. Click **Save** to create the product. It will now be available for use when opening new member accounts.

---

## Notes
- Only users with the right permissions can create or modify saving products.
- All changes are tracked and visible in the product's history.
- Saving products are essential for managing member accounts, transactions, and reports in CAMS.
