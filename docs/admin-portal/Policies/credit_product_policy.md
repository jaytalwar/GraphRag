# Credit Product Policy

## Overview
The Credit Product Policy module allows financial institutions to define and manage various loan products with their specific terms, conditions, and operational parameters. This documentation covers all aspects of creating and managing credit product policies in the system.

## Features

### 1. Basic Details
- **Product Name**: Define the name of the credit product
- **Description**: Detailed description of the credit product
- **Active Status**: Toggle to activate/deactivate the credit product
- **External Details**: Optional external reference information

### 2. Terms Configuration
#### Key Components:
- **Loan Amount Range**: 
  - Minimum and maximum loan amount limits
  - Currency specification
  - Impact: Controls the borrowing limits for customers

- **Interest Rate Settings**:
  - Base interest rate configuration
  - Interest calculation method (Reducing Balance/Flat Rate)
  - Fixed/Variable interest rate options
  - Impact: Determines the cost of borrowing for customers

- **Tenure Settings**:
  - Minimum and maximum loan tenure
  - Grace period configuration
  - Impact: Defines the loan repayment timeframe and initial grace period

### 3. Settings
#### Advanced Configuration Options:
- **Loan Disbursement Rules**:
  - Single/Multiple disbursement options
  - Disbursement schedule configuration
  - Impact: Controls how loan amounts are released to borrowers

- **Holiday Treatment**:
  - Holiday exclusion settings for arrears
  - Business day adjustments
  - Impact: Manages payment schedules around holidays

- **Default Notifications**:
  - Pre-due date notification days
  - Post-due date notification days
  - Impact: Ensures timely communication with borrowers

### 4. Repayment Configuration
#### Repayment Rules:
- **Payment Strategy**:
  - Principal and interest payment rules
  - Advance payment handling
  - Impact: Determines how payments are allocated

- **Auto Debit Settings**:
  - Automatic repayment configuration
  - Account linking requirements
  - Impact: Facilitates automated payment collection

### 5. Interest Calculation
#### Interest Parameters:
- **Calculation Method**:
  - Daily/Monthly computation options
  - Interest accrual rules
  - Impact: Affects the total interest charged to borrowers

- **Special Conditions**:
  - Interest capitalization rules
  - Penalty interest configuration
  - Impact: Handles exceptional cases and penalties

### 6. Quick Loan Features
- **Instant Approval Parameters**:
  - Eligibility criteria
  - Documentation requirements
  - Impact: Enables faster loan processing

### 7. Loan Charges
#### Fee Structure:
Loan charges are additional fees that can be configured to apply at various stages of the loan lifecycle. These charges help institutions manage operational costs, risks, and compliance requirements. Below are the types of loan charges available:

- **Payment Upon Delayed Repayment**:
  - Applied when a borrower delays repayment beyond the scheduled due date.
  - Use: Acts as a penalty or late fee to encourage timely payments and compensate for risk.
  - Impact: Increases total repayment amount for late payers.

- **Payment Upon Processing And Disbursement**:
  - Charged at the time of loan processing and when the loan amount is disbursed to the borrower.
  - Use: Covers administrative and processing costs.
  - Impact: Deducted upfront or from the disbursed amount.

- **Payment Upon Application**:
  - Applied when a loan application is submitted, regardless of approval.
  - Use: Screens serious applicants and covers initial review costs.
  - Impact: Non-refundable, even if the loan is not approved.

- **Payment Upon Loan Repayment**:
  - (May be disabled or not applicable in some configurations)
  - Would be charged when the borrower makes a repayment.
  - Use: Could be used for service fees on each repayment transaction.

- **Payment Distributed With All Loan Installment**:
  - The charge is distributed and collected with every loan installment payment.
  - Use: Spreads the fee over the loan tenure, reducing upfront burden.
  - Impact: Increases each installment amount slightly.

- **Payment With First Loan Installment**:
  - The charge is collected together with the first installment payment.
  - Use: Ensures early recovery of fees while not burdening the disbursement amount.
  - Impact: First installment is higher than subsequent ones.

##### Additional Configuration Options:
- **Charge Fee Type**: Defines whether the fee is a fixed amount, a percentage, or based on other criteria.
- **Charge Criteria**: Specifies the conditions under which the charge is applied (e.g., mandatory, optional, conditional).
- **Charge Frequency**: Determines if the charge is one-time or recurring.
- **Component**: Links the charge to a specific part of the loan (principal, interest, etc.).

##### Impact:
- Loan charges directly affect the total cost of borrowing for the customer.
- Proper configuration ensures transparency, regulatory compliance, and cost recovery for the institution.

### 8. Guarantors and Collateral
#### Security Requirements:
- **Guarantor Rules**:
  - Minimum guarantor requirements
  - Guarantor eligibility criteria
  - Impact: Defines loan security parameters

- **Collateral Settings**:
  - Acceptable collateral types
  - Collateral valuation rules
  - Impact: Manages risk through security requirements

### 9. Accounting Configuration
#### Financial Settings:
- **Account Mapping**:
  - Principal account configuration
  - Interest account mapping
  - Suspense account settings
  - Impact: Ensures proper financial recording and tracking

## Policy Approval Workflow
1. **Creation**: Initial policy setup by authorized personnel
2. **Review**: Multi-level review process
3. **Approval**: Final authorization by designated approvers
4. **Implementation**: Activation and deployment of the policy

## Best Practices
1. Regular review and update of policy parameters
2. Maintain clear documentation of policy changes
3. Ensure compliance with regulatory requirements
4. Regular validation of calculation methods
5. Monitor policy effectiveness through reporting

## Impact on System
- Defines the framework for loan product creation
- Controls risk management parameters
- Ensures regulatory compliance
- Standardizes loan processing
- Enables automated decision-making
- Facilitates consistent loan servicing

## Related Components
- Loan Application Processing
- Customer Onboarding
- Risk Assessment
- Payment Processing
- Accounting Integration
- Reporting and Analytics
