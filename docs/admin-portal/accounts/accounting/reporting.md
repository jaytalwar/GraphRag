# Reporting

## Overview
Reporting in the Accounting module allows users to generate, view, and export a wide variety of financial reports. These reports support financial analysis, auditing, compliance, and business decision-making.

## Features
- Access a comprehensive Reports menu with multiple report types
- Generate reports such as Financial Position, Income Statement, Trial Balance, Ledger Statements, and more
- Apply advanced filters (date range, account, category, etc.)
- Export reports in multiple formats (CSV, XLS, PDF)
- Print reports directly from the UI

## Available Report Types
- **Financial Position:** View the statement of financial position (balance sheet) as of a specific date, showing assets, liabilities, and equity.
- **Income Statement:** Review income and expenses over a period to determine net profit or loss.
- **Notes of Account:** Access detailed notes and breakdowns supporting the main financial statements.
- **Comprehensive Trial Balance:** See a complete listing of all accounts and their balances for a period.
- **Trial Balance:** View a summary of debits and credits for all accounts.
- **Month Trial Balance:** Generate trial balances for specific months.
- **Category Report:** Analyze financial data by custom categories.
- **Ledger Statement:** View detailed transactions and balances for a specific ledger account.
- **Ledger Entries:** List all entries posted to ledgers, with details and export options.
- **Ledger Report:** Summarize ledger activity and balances.
- **Cash Flow:** Track cash inflows and outflows over a period.
- **Owner's Equity:** Review changes in owner's equity accounts.
- **Reconcile Statement:** Generate statements for reconciliation purposes.
- **Reconciliation:** Match and verify transactions between internal and external records.
- **Corporate Tax Note:** Access tax-related notes and calculations for compliance.

## Configurations
- Set up report templates and default filters
- Assign permissions for report access and export
- Configure export formats and print settings

## Use Cases
- Generating a Financial Position report for end-of-period review
- Exporting a Trial Balance for audit or compliance
- Reviewing a Ledger Statement for a specific account
- Reconciling internal records with external statements
- Printing or exporting reports for board meetings or regulatory filings

## Examples
**Generating a Financial Position Report:**
1. Navigate to **Reports > Financial position**.
2. Set the date and any relevant filters.
3. Click **Submit** to view the report.
4. Use **Download CSV**, **Download XLS**, or **Print** to export or print the report.

**Viewing a Ledger Statement:**
1. Go to **Reports > Ledger Statement**.
2. Select the ledger account and date range.
3. Submit to view detailed transactions and balances.

## Additional Notes
- Only users with the appropriate permissions can generate or export reports.
- Some reports may display warnings if there are discrepancies (e.g., opening balance differences).
- Filters and export options help tailor reports to your needs.

## FAQ
**Q: What types of reports can I generate?**
A: The system supports Financial Position, Income Statement, Trial Balance, Ledger Statements, Cash Flow, Reconciliation, and more. See the list above for details.

**Q: Are reports exportable?**
A: Yes, all reports can be exported in CSV, XLS, or PDF formats, or printed directly from the UI.

**Q: Can I filter reports by date or account?**
A: Yes, most reports allow you to set date ranges, select accounts, or apply other filters before generating results.

## Related Files/Components
- Frontend: `report/accounting/`, `accounting.component.ts`, `accounting.component.html`
- Backend: `AccountingManager.cs`, reporting services

---
[Back to Accounting Overview](./README.md) 