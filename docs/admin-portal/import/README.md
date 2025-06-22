# Import Feature

## Overview

The Import Feature in CAMS enables seamless data migration from external systems into CAMS. This includes importing Members, Accounts (Savings, Loan, Share, FD), and Transactions. Each template has specific fields with validations to ensure accurate and error-free imports.

## Import Process

### Step-by-Step Guide

1. **Choose the Import Option:**
   - Navigate to the Import section in the main menu on the left side of the CAMS application
   - Select the desired import type:
     - Member Import
     - Account Import
     - Transaction Import

2. **Download the Template:**
   - Use the Download Template option to download the required template file for the selected import type
   - Templates are pre-structured to ensure compatibility with CAMS

3. **Prepare the Data:**
   - Populate the downloaded template with the data to be imported
   - Refer to field-level validation rules for guidance
   - Validate data manually to avoid errors during the import

4. **Upload the File:**
   - Use the Upload option on the import page to upload the prepared template file
   - Provide any additional details required:
     - Assigned To: Specifies the user responsible for managing the import
     - Template Type: Required for Account imports
     - Account (DR/CR): Required for Transaction imports to indicate which IFG account is debited or credited

5. **View File Details:**
   - Click the filename in the main view to access the detailed import view
   - The detailed view shows:
     - Data for each record
     - Status of each record (e.g., New, InProgress, Error)

6. **Submit the Import:**
   - If the import status is New, review the details and click Submit to begin the import process
   - The system will process the data and update the status accordingly

7. **Monitor Import Status:**
   The status of the import can change as follows:
   - **New:** File is uploaded but not yet processed
   - **InProgress:** File is being processed; the number of uploaded records shows progress
   - **Pending:** Applicable only on Account import. In case validation failure or constraint check failure, import goes in Pending status
   - **Error:** Some records encountered issues during import
   - **Deleting:** Applicable only on Transaction import, the import gets in this status when the import is opted for Delete
   - **Deleted:** Applicable only on Transaction import, all the Transactions are deleted successfully. No actions are permitted on this import once its deleted
   - **Success:** All records have been imported successfully
   - **Archive:** Applicable only for Transaction Import. If the file is not submitted (i.e., the import is in New status), the import can be archived. Once an import is in Archive status, no actions are permitted

8. **View Error Details (if applicable):**
   - For imports with an Error status:
     - Click the Error status to view specific issues for each record
     - Resolve errors in the source file and re-upload, if necessary
   - For imports with a Pending status (only for account imports):
     - Click on the uploaded file name
     - A new tab "Pending Data" gets visible, with list of all the pending records
     - Click on the Edit/Delete in front of record and correct the data
     - Once all data is rectified, click on submit to Resubmit the file for processing

## Related Documentation

- [Member Import](./member_import.md)
- [Account Import](./account_import.md)
- [Transaction Import](./transaction_import.md) 