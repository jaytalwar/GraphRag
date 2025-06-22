---
sidebar_position: 4
---

# Online Transaction Reconciliation

## Overview
The **Online Transaction Reconciliation** module is designed to ensure consistency between financial transactions from third-party payment providers (e.g., MPKE, M-PESA) and internal system records. By enabling upload, comparison, and reconciliation of transaction statements, this feature helps maintain financial integrity, identify discrepancies, and facilitate streamlined financial reporting.

It is a critical part of financial operations for SACCOs, cooperatives, and digital financial platforms integrating with external payment processors.

---

## Key Features

### File Upload & Filtering
- **Provider Selection**: Mandatory dropdown to choose a payment provider.
- **Date Range Filter**: Define `From` and `To` dates to scope the reconciliation window.
- **File Upload Validation**: Supports `.xlsx` format, validating headers and data on upload.
- **Submit Button**: Filters data and loads associated uploaded records.
   

###  Transaction Table View
- Displays metadata of uploaded reconciliation files:
  - File Name
  - Statement Dates
  - Provider Name
  - Account Identifier
  - Reconciliation Status (e.g., `874/2212` matched)
  - Uploaded Date
  - Uploaded By (email ID of uploader)
- Supports pagination and dynamic row limits.
    
    Upload & Status View
         ![Online Transaction Reconciliation UI](../../../static/img/online_transactions_reconciliation.png)

###  Download Reconciliation Report
- **Download Statement** button triggers a dialog:
  - Choose between:
    - `Reconciled` transactions
    - `Non-Reconciled` transactions
  - Export formats: `CSV` or `XLSX`
- Only the **latest reconciliation** result is exported.

      Download Options Dialog View
            ![Download Confirmation Dialog](../../../static/img/onlineReconcile.png)

---

## Configuration Details

| Parameter         | Description                                                    |
|------------------|----------------------------------------------------------------|
| File Format       | `.xlsx` only                                                   |
| Required Fields   | Provider Name, From Date, To Date                              |
| Upload Validation | Ensures header structure, date range alignment, duplicate file checks |
| Download Filters  | Reconciled or Non-Reconciled options, export type selection    |
| Pagination        | Configurable per page count (e.g., 10, 20, 50)                 |

---

##  Use Cases

###   Reconciliation for MPKE
A finance officer downloads the daily transaction report from MPKE, uploads it via this module, and matches it against internal payments to detect missing or failed transactions.

###  Monthly Audit Trail
As part of monthly financial audits, reconciliation files for each provider are downloaded and stored. Discrepancies are tagged and addressed through back-office dispute resolution.

###  Failed Reconciliation Investigation
A report shows `0/12` matched transactions for a file. This is flagged, and the user downloads the "Non-Reconciled" report to forward to the provider for clarification or correction.

---

## Workflow Summary

1. **Select Provider and Date Range**
2. **Upload the Excel Transaction File**
3. **System Automatically Parses and Validates**
4. **View Uploaded Records and Match Status**
5. **Download Reconciled/Non-Reconciled Reports for Review**

---

## Best Practices

-  **Standard Naming**: Maintain structured filenames (e.g., `MPKE_Mar2025.xlsx`) for traceability.
-  **Timely Upload**: Upload provider files daily or weekly to avoid bulk errors.
- **Cross Verification**: Always compare file transaction totals with actual system balances.
-  **Audit Logging**: Keep download records and email logs for traceability.


---

## Error Handling

| Error Scenario                 | System Response                                         |
|-------------------------------|---------------------------------------------------------|
| Unsupported file format       | Displays file format validation error                  |
| Empty or incorrect header     | Rejects upload with descriptive message                |
| Duplicate file for same range | Flags and prevents duplicate data ingestion            |
| Reconciliation mismatch       | Flags transactions as "Non-Reconciled" for action      |

---

## Screenshot Reference




---

## FAQ

**Q: What does the status `874/2212` represent?**  
A: It indicates 874 transactions matched with system records out of 2,212 total entries in the uploaded file.

**Q: Can I upload multiple files for the same provider and date range?**  
A: Only the latest file is used for reconciliation in that date range.

**Q: What happens if the upload fails validation?**  
A: A clear message is shown detailing the error (format, missing columns, or invalid data).

**Q: Can we retrieve older reconciliation records?**  
A:  **No**, only the **latest reconciliation file** is considered. Historical uploads are not stored or accessible after a new file is uploaded.

---


