# Member Import

The Member Import functionality allows administrators to bulk import member data into CAMS. This document outlines the process, requirements, and validation rules for importing members.

## Overview

The member import supports importing:
1. Individual Members
2. Groups
3. Group Members

## Import Template Fields

### General Fields

| Field Name | Description | Validation Rules |
|------------|-------------|------------------|
| Ref Id | Unique identifier of the member in the existing system | Conditionally Mandatory (either RefID, PhoneNo, Email Address or UserId) and must be unique |
| User Id | Unique identifier auto generated and assigned to a member in CAMS | Conditionally Mandatory (either RefID, PhoneNo, Email Address or UserId) and must be unique. UserId should be kept blank in case of new import |
| First Name | Member's first name | Mandatory, text only |
| Middle Name | Member's middle name | Optional, text only |
| Surname | Member's last name | Optional, text only |
| MobileNo | Member's mobile number | Conditionally Mandatory (either RefID, PhoneNo, Email Address or UserId) and must be unique. Should not include country code |
| Email Address | Member's email address | Conditionally Mandatory (either RefID, PhoneNo, Email Address or UserId) and must be unique. Valid email format |
| Branch Name | Branch of the IFG the member belongs to | Optional, text only |
| Region | Regional address of the member | Optional, text only |
| District | District address of the member | Optional, text only |
| Ward | Specific area or locality of the member | Optional, text only |
| House Number | House number of the member's residence | Optional, text only |
| AddressLine1 | Primary address line for the member | Optional, text only |
| AddressLine2 | Secondary address line for the member | Optional, text only |
| AddressLine3 | Tertiary address line for the member | Optional, text only |
| Zip | ZIP or postal code of the member's address | Optional, numeric |
| Country | Country of the member's address | Optional, text only |
| DOB | Member's date of birth | Optional, valid date (MM-DD-YYYY), no future dates |
| JoiningDate | Date when the member joined the IFG | Optional, valid date (MM-DD-YYYY), no future dates |
| Gender | Member's gender | Optional, text only |
| MaritalStatus | Member's marital status | Optional, text only. Must be one of: Single, Married, Divorced, Separated, Widowed |
| Member Joining Fee | Membership joining fee applicable to the member | Optional, numeric. MemberRegistrationFee fee must be configured in CAMS |
| Membership Policy Name | Name of the membership policy assigned to the member | Mandatory, must match CAMS configuration |
| Member Type | Type of membership | Mandatory, text only. Must be one of: Individual, Group, GroupMember |
| Group Name | Name of the group the member belongs to | Optional, text only |
| Group Member Type | Role or type of the member within the group | Optional, text only. Must be one of: Member, Chairman, Treasurer, Secretary |
| Relationship Manager Name | Name of the Client Manager assigned to the member | Optional, text only. The Admin with this name must exist in the system with Role "ClientManager" |
| NationalIdNumber | National ID number of the member | Optional, alphanumeric only |
| TaxNumber | Tax identification number of the member | Optional, text only |
| FatherName | Name of the member's father | Optional, text only |
| SpouseName | Name of the member's spouse | Optional, text only |
| OccupationType | Member's occupation type | Optional, text only |
| PayRollNumber | Payroll number for the member | Optional, text only |
| IncomeType | Source of income for the member | Optional, text only. Must be one of: Employment, Business |
| CompanyName | Name of the company associated with the member | Optional, text only |
| CompanyAddress | Address of the company associated with the member | Optional, text only |
| IsMigrated | Indicates whether the member is an existing IFG member or newly onboarded | Optional, Boolean (True/False). Default is treated as False |

### Nominee Fields

#### Nominee 1
| Field Name | Description | Validation Rules |
|------------|-------------|------------------|
| Nominee1Name | Name of the first nominee | Optional, text only |
| Nominee1DOB | Date of birth of the first nominee | Optional, valid date (MM-DD-YYYY) |
| Nominee1TaxNumber | Tax identification number of the first nominee | Optional, text only |
| Nominee1IDNumber | National ID number of the first nominee | Optional, text only |
| Nominee1Relation | Relationship of the first nominee with the member | Optional, text only. Must be one of: Brother, Sister, Husband, Mother, Son, Daughter, Wife, Others, Father |
| Nominee1Percentage | Percentage of benefits allocated to the first nominee | Optional, numeric. Total percentage across all nominees must equal 100 |
| Nominee1PhoneNumber | Phone number of the first nominee | Optional, numeric |

#### Nominee 2
| Field Name | Description | Validation Rules |
|------------|-------------|------------------|
| Nominee2Name | Name of the second nominee | Optional, text only |
| Nominee2DOB | Date of birth of the second nominee | Optional, valid date (MM-DD-YYYY) |
| Nominee2TaxNumber | Tax identification number of the second nominee | Optional, text only (not in use currently) |
| Nominee2IDNumber | National ID number of the second nominee | Optional, text only (not in use currently) |
| Nominee2Relation | Relationship of the second nominee with the member | Optional, text only. Must be one of: Brother, Sister, Husband, Mother, Son, Daughter, Wife, Others, Father |
| Nominee2Percentage | Percentage of benefits allocated to the second nominee | Optional, numeric. Total percentage across all nominees must equal 100 |
| Nominee2PhoneNumber | Phone number of the second nominee | Optional, numeric |

## Validation Rules Summary

### Mandatory Fields

1. **For Individual Member Import:**
   - Either one value is mandatory from Ref ID, MobileNo, and Email Address
   - First Name
   - Membership Policy Name
   - Member Type

2. **For Group Import:**
   - Ref ID
   - First Name
   - Membership Policy Name
   - Member Type

3. **For Group Member Import:**
   - Ref ID
   - First Name
   - Membership Policy Name
   - Member Type
   - Group Name
   - Group Member Type

### Field Format Requirements

1. **Date Fields:**
   - Use MM-DD-YYYY format
   - Ensure no future dates for DOB, JoiningDate, and nominee DOBs

2. **Numeric Fields:**
   - Use numeric-only values for MobileNo, ZIP, Member Joining Fee, and nominee percentages

3. **Field Dependencies:**
   - Nominee percentages must total 100 if multiple nominees are provided
   - For Member Joining Fee, Accounts Setup is required with name "MemberRegistrationFee" as Fee type under Settings → Account Setup → Fee & Penalties

## Impact of "IsMigrated" on Membership Charges

1. **If "IsMigrated" is True (Existing IFG Member):**
   - Only charges in the Membership Policy that have "Apply To Migrated Members" checked will be applied

2. **If "IsMigrated" is False (New Member):**
   - All charges from the Membership Policy will be applied, regardless of whether the "Apply To Migrated Members" checkbox is checked

## Import Process

1. **File Upload**
   - Supported formats: Excel files (.xlsx, .xls)
   - Maximum file size: 5MB
   - File must not have multiple extensions

2. **Data Validation**
   - System validates the uploaded file format and structure
   - Checks for required columns and data integrity
   - Validates member types and their specific requirements

3. **Data Processing**
   - Valid records are processed and imported into the system
   - Failed records are marked with specific error messages
   - Import status can be tracked in the import history

## Error Handling

- Each error is reported with the specific row number and error description
- Common errors include:
  - Missing required fields
  - Invalid member types
  - Duplicate member references
  - Invalid dates
  - Missing policy configurations

## Best Practices

1. **Before Import**
   - Verify all required fields are present
   - Ensure data follows the specified format
   - Validate member references
   - Check policy configurations

2. **During Import**
   - Monitor the import progress
   - Review any validation errors
   - Keep the source file for reference

3. **After Import**
   - Verify imported members in the system
   - Check member relationships and group associations
   - Update any failed entries manually if needed

## Reference Images
![Member Import Process](/img/member_import.png)
