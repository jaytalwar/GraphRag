# Account Management

## Overview
Account Management allows you to create, organize, and maintain all accounts in your Chart of Accounts. Accounts can be grouped hierarchically (Groups and Ledgers) and are used to track financial activity, balances, and reporting structure.

## Features
- View a hierarchical Chart of Accounts with expandable/collapsible groups
- Add new accounts (ledgers) or groups
- Edit or delete existing accounts (with permissions)
- See account types (Group, Ledger) and their balances (opening/closing)
- Filter and search accounts
- Access quick actions: Add Group, Add Ledger, Edit, Delete

## Configurations
- Define account types: Group (for organizing) and Ledger (for transactions)
- Set opening balances (Dr/Cr) and opening dates
- Assign parent groups for hierarchical structure
- Mark accounts as Bank/Cash or for Reconciliation
- Set categories, maturity dates, and notes for each account

## Use Cases
- Creating a new ledger under a specific group (e.g., adding a new bank account under Assets)
- Editing an account to update its balance, type, or details
- Deleting obsolete accounts (if allowed)
- Organizing accounts for better reporting and compliance

## Examples
**Adding a New Account Ledger:**
1. Click **Add Ledger** in the Chart of Accounts view.
2. Fill in the form:
   - Ledger name
   - Parent group (e.g., Assets)
   - Ledger code
   - Opening Balance (Dr/Cr)
   - Opening Date
   - (Optional) Mark as Bank/Cash account
   - (Optional) Enable Reconciliation
   - Category, Maturity Date, Notes
3. Click **Submit** to create the ledger.

**Viewing and Editing Accounts:**
- Expand/collapse groups to navigate the hierarchy.
- Use **Edit** or **Delete** links next to each account for quick actions.
- Review opening and closing balances for each account.

## Additional Notes
- Only users with the appropriate permissions can add, edit, or delete accounts.
- Opening balances must be set correctly for accurate financial reporting.
- The system will alert you if there is a difference in opening balances.

## FAQ
**Q: What is the difference between a Group and a Ledger?**
A: Groups are used to organize accounts hierarchically and do not hold transactions. Ledgers are transactional accounts where entries are posted.

**Q: Can I mark an account for reconciliation?**
A: Yes, when adding or editing a ledger, you can enable the Reconciliation option to allow it to be reconciled from the Reports > Reconciliation section.

**Q: What happens if opening balances do not match?**
A: The system will display a warning if there is a difference in opening balances, which should be resolved for accurate reporting. 

![accounting Accounts](/img/accounting_accounts.png)