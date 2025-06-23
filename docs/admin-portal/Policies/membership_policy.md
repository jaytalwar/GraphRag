# Membership Policy

## Overview
The Membership Policy module allows administrators to configure and manage membership rules and settings for the organization. This documentation covers all aspects of creating and managing membership policies, including their impacts on various system functionalities.

## Features

### Basic Details
- **Name**: Unique identifier for the membership policy
  - Must be unique for each member type
  - Used for policy identification across the system
- **Member Type**: Selection of member classification
  - Determines available features and restrictions
  - Affects credit product eligibility
- **Description**: Detailed description of the policy and its purpose
  - Helps administrators understand policy scope and application

### Next of Kin Configuration
- **Minimum Number of Next Of Kin**: Set the minimum required next of kin entries
  - Enforced during member registration and loan applications
  - System validates this requirement during profile updates
- **Maximum Number of Next Of Kin**: Set the maximum allowed next of kin entries
  - System enforces this limit across all member operations
  - Validated during bulk next of kin updates

Next of Kin Details Include:
- Full Name
- Gender
- Phone Number
- Email ID
- Date of Birth
- Relationship Type
- Tax Number
- ID Number
- Percentage Share

### Minor Members Management
- **Allow Minors**: Toggle to enable/disable minor member registrations
  - When enabled, additional fields become available:
    - Minimum Minor Age
    - Maximum Minor Age
    - Minimum Number of Guardians Required
- **Credit Product Enabled**: Controls whether minors can access credit products
- Special considerations and restrictions apply for minor accounts
- Guardian/parent details are mandatory when enabled

### Member Dormancy Rules
- **Dormant Days**: Define the number of days after which an account becomes dormant
  - System automatically checks and updates member status based on:
    - Last loan repayment
    - Last deposit transaction
    - Last withdrawal transaction
- **Allow Withdraw**: Enable/disable withdrawals for dormant accounts
  - When disabled, system blocks all withdrawal attempts
  - Affects both manual and automated withdrawals
- **Auto Active Upon Deposit**: Automatically activate dormant accounts upon receiving deposits
  - System automatically reactivates the account on any deposit
  - Updates member status from 'Dormant' to 'Active'

### Fee Structure
- **Fee Type**: Select the type of fee to be applied
- **Charges Type**: Define how the fee will be charged
- **Amount**: Set the fee amount in INR
- **Auto Debit**: Enable automatic fee deduction
  - System automatically processes fee deductions when enabled
  - Integrated with the accounting module for automated entries
- **Apply To Migrated Members**: Option to apply fees to migrated member accounts
  - Controls fee application for imported/migrated members
  - Affects bulk member imports

### Member Activation Settings
- **Verification Required**: Mandate verification process for new members
  - When enabled:
    - Members remain in 'Pending' status until verified
    - KYC verification may be required
    - Registration charges apply after verification
- **Deactivate Or Exit Allow**: Configure member exit or deactivation permissions
  - Controls member's ability to voluntarily exit
  - Affects account closure processes

### Mandatory Requirements
- **Mandatory Shares**: Require members to hold a minimum number of shares
  - System enforces minimum share requirements
  - Affects member status and privileges
- **Mandatory Savings**: Enforce minimum savings requirements for members
  - Integrated with savings account module
  - May affect loan eligibility

### Group Membership Settings
- **Group Type**: Define the classification of groups
  - Determines available features and restrictions for the group
  - Options include:
    - Active Member Group
    - Inactive Member Group

- **Minimum Number of Members**: Set minimum group size
  - System enforces this limit during group creation
  - Validates against this number during member removal
  - Affects group status if membership falls below minimum

- **Maximum Number of Members**: Set maximum group size
  - Hard limit enforced during member addition
  - Applies to both manual and bulk member imports
  - System validates against this limit in all member operations

- **Minimum Number of Signatories**: Required number of authorized signatories
  - Critical for group transaction approvals
  - Roles typically include:
    - Chairman
    - Secretary
    - Treasurer
  - System enforces minimum signatories for:
    - Loan applications
    - Withdrawal requests
    - Policy changes

- **Minimum Share Required**: Minimum share holding for groups
  - Mandatory share requirement for group formation
  - May affect:
    - Group activation status
    - Loan eligibility
    - Transaction permissions

- **Allow Member in Multiple Groups**: Toggle multi-group membership
  - When enabled:
    - Members can join multiple groups simultaneously
    - System tracks memberships across groups
    - Affects loan and transaction calculations
  - When disabled:
    - Members are restricted to single group membership
    - System prevents duplicate group assignments
    - Validates during member addition

#### Group Member Types and Roles
1. **Chairman**
   - Primary group representative
   - Required for group formation
   - Special transaction approval rights
   - Access to group management features

2. **Secretary**
   - Documentation and record-keeping
   - Required for certain group operations
   - Secondary approval authority

3. **Treasurer**
   - Financial oversight
   - Transaction monitoring
   - Required for financial operations

4. **Regular Members**
   - Standard group participation
   - Limited to member-level operations
   - Subject to group policy restrictions

#### System Integrations and Impacts

1. **Member Management**
   - Automated validation of group size limits
   - Role-based access control
   - Member status tracking across groups
   - KYC verification requirements

2. **Transaction Processing**
   - Multi-signatory validation
   - Role-based approval workflows
   - Group transaction limits
   - Special handling for group deposits/withdrawals

3. **Document Management**
   - Group-specific document requirements
   - Role-based document access
   - Mandatory document validations for:
    - Group formation
    - Member addition
    - Policy changes

4. **Loan Processing**
   - Group loan eligibility checks
   - Member contribution tracking
   - Collective liability management
   - Role-based loan approval workflow

5. **Reporting and Compliance**
   - Group membership reports
   - Activity tracking by member type
   - Regulatory compliance monitoring
   - Group status notifications

#### Implementation Notes
- Group creation requires minimum member count
- System automatically validates member limits
- Role assignments are permanent until explicitly changed
- Group status affects member operations
- Cross-validation with other policy settings
- Automated notifications for:
  - Member additions/removals
  - Role changes
  - Status updates
  - Policy violations

## System Integrations

The membership policy affects various system components:

1. **Account Management**
   - Account creation rules
   - Transaction permissions
   - Dormancy handling

2. **Loan Processing**
   - Eligibility criteria
   - Next of kin requirements
   - Group loan configurations

3. **Transaction Processing**
   - Withdrawal permissions
   - Deposit handling
   - Fee applications

4. **Member Status Workflow**
   - Activation conditions
   - Dormancy transitions
   - Verification requirements

## Usage Instructions

1. Navigate to the Policies section in the admin portal
2. Select "Membership Policy" from the policy types
3. Fill in all required fields in each section
4. Use the information icons (?) for detailed field descriptions
5. Click "Submit" to save the policy configuration

## Important Notes
- All mandatory fields must be completed before submission
- Policy changes may affect existing members based on selected options
- Review all settings carefully before saving
- Some settings may require additional approvals based on organization rules
- Changes to dormancy rules will trigger system-wide member status updates
- Fee structure changes may affect automated accounting entries

## Related Features
- Saccos Policy
- Credit Product Policy
- Holidays Configuration
- KYC Verification System
- Account Management System
- Transaction Processing System
