# Credit Union Details Tab

✨ **Overview**

**Purpose:**  
The Credit Union Details tab provides Super Admins with a centralized interface to view, manage, and update all essential information related to a specific Credit Association (Sacco) within the Wakandi platform. This feature is introduced to streamline administrative oversight, ensure data accuracy, and facilitate compliance through document management and KYC verification.

**Scope:**  
This feature is accessible to Super Admins within the Superadmin Portal and covers the display, editing, and management of Credit Union (Sacco) profiles, including administrative contacts and document uploads.

---

🧩 **Feature Details**

- Comprehensive display of Sacco profile information (name, registration, license, tax number, etc.)
- Administrative and key account manager contact details
- KYC status and document management (upload, update, and view compliance documents)
- Action buttons for editing, deactivating, and running migration jobs
- Document upload section for compliance and operational files

 ![Credit Union Details tab showing profile information, actions, and document management in the Superadmin Portal.](../../../static/img/Superadmin_CreditUnionDetails.png)
---

📐 **Functional Description**

The Credit Union Details tab is divided into several sections:

1. **Profile Information:**  
   Displays all key identifiers and operational details of the selected Sacco, such as name, registration number, license number, address, tax number, KYC status, and more.
    
    Key Information Displayed :
    
   - **Credit Union Name & Short Name**: The official and abbreviated names of the Sacco, used for identification and display purposes.
   - **Description**: A brief summary or description of the Sacco.
   - **Registration Number**: The official registration number assigned to the Sacco by regulatory authorities.
   - **Module Type**: Indicates the operational type of the Sacco (e.g., Saccos, Microfinance).
   - **Stage**: The current operational stage of the Sacco (e.g., Demo, Live).
   - **Address**: The registered or physical address of the Sacco.
   - **License Number**: The regulatory license number for the Sacco.
   - **Mode**: The operational mode (e.g., STANDARD, LITE) indicating the feature set or edition.
   - **Wakandi ID**: A unique system-generated identifier for the Sacco within the Wakandi platform.
   - **Apex**: The linked apex organization, if any.
   - **Tax Number**: The tax identification number for the Sacco.
   - **KYC Status**: The Know Your Customer (KYC) verification status (e.g., Verified, Pending).
   - **Deletion Date**: The scheduled deletion date, if applicable.
    


2. **Admin & Key Account Manager:**  
   Shows the email addresses of the main administrator and the key account manager responsible for the Sacco.

3. **Actions:**  
   - **Edit:** Opens a form to update Sacco details.
   - **Deactivate:** Temporarily disables the Sacco's access and operations.
   - **Run Migration Job:** Initiates a data migration or synchronization process.

4. **Document Management:**  
   - **Upload Documents:** Allows uploading of required compliance and operational documents (e.g., registration certificate, tax certificate, ID, cheque, logo).
   - **Document List:** Displays uploaded documents with their name, type, upload date, and available actions (e.g., update).
   - **Update Documents:** Button to add or replace existing documents.

  
---

🔄 **Workflow / User Journey**

1. **Viewing Details:**  
   Super Admin selects a Sacco from the Credit Associations list and is presented with the Credit Union Details tab, showing all profile and administrative information.

2. **Editing Information:**  
   By clicking the **Edit** button, the Super Admin can update any of the Sacco's details via a comprehensive form.

   ![Update Credit Union Details](../../../static/img/EditCreditUnionDetails.png)

3. **Managing Status:**  
   The **Deactivate** button allows the Super Admin to temporarily restrict the Sacco's access if needed.

4. **Document Upload:**  
   - Super Admin clicks **Update Documents** to open the document upload modal.
   - Required documents (registration certificate, tax certificate, ID, cheque, logo) are uploaded as per the specified formats and constraints.
   - Uploaded documents are listed with their details for easy management.

    ![Credit Union Details tab showing Document Management.](../../../static/img/UploadDocument.png)


5. **KYC Verification:**  
   The KYC status is displayed and updated based on the uploaded documents and verification process.

---

⚠️ **Validation / Constraints / Configurations**

- Only one file can be uploaded for each required document type (e.g., one registration certificate, one tax certificate, etc.).
- Supported file formats for logo: jpeg, png, pdf.
- National ID uploads can include both sides for authorized signatories.
- All required fields must be completed before submission.
- Deactivation restricts all user access and operations for the Sacco until reactivated.

---

✅ **Acceptance Criteria**

- All Sacco profile fields are displayed accurately and are editable by Super Admins.
- Admin and Key Account Manager email addresses are visible and updatable.
- Action buttons (Edit, Deactivate, Run Migration Job) function as intended.
- Document upload modal enforces file type and quantity constraints.
- Uploaded documents are listed with correct metadata and can be updated.
- KYC status reflects the current verification state based on document uploads.
- Deactivation and reactivation of Saccos work as expected, restricting and restoring access accordingly.

---





