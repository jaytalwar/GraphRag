# Income Details Management

The Income Details tab provides comprehensive management of client income information from both employment and business sources.

## Overview

The Income Details section allows administrators to manage and track client income information from two main sources:
- Employment Income
- Business Income

## Employment Information

### Employment Status
- Radio button selection for employment status (Yes/No)
- When "No" is selected, all employment-related fields are disabled

### Employment Details
- **Company Name** (Required)
  - Must contain only alphabetic characters
  - Length: 2-64 characters
- **Company Address** (Required)
  - Allows alphanumeric characters and dashes
  - Length: 2-64 characters
- **Monthly Income** (Required)
  - Numeric value
  - Supports decimal values based on system configuration
- **Contract Type** (Required)
  - Dropdown selection from predefined contract types
  - Managed through system configuration

## Business Information

### Business Status
- Radio button selection for business status (Yes/No)
- When "No" is selected, all business-related fields are disabled

### Business Details
- **Business Address** (Required)
  - Allows alphanumeric characters and dashes
  - Length: 2-64 characters
- **Business Registration Number** (Required)
  - Numeric characters only
  - Length: 2-50 characters
- **Business License Number** (Required)
  - Numeric characters only
  - Length: 2-50 characters
- **TIN Number** (Required)
  - Numeric characters only
- **Business Turnover** (Required)
  - Numeric value
  - Supports decimal values based on system configuration

## Form Validation

### Employment Validation
- All fields are required when employment status is "Yes"
- Fields are automatically disabled and cleared when status is "No"
- Input validation for:
  - Alphabetic characters in company name
  - Alphanumeric characters in address
  - Numeric values in income fields

### Business Validation
- All fields are required when business status is "Yes"
- Fields are automatically disabled and cleared when status is "No"
- Input validation for:
  - Alphanumeric characters in address
  - Numeric values in registration numbers
  - Numeric values in turnover amount

## Actions

### Add New Income Details
1. Select employment status and fill required employment details
2. Select business status and fill required business details
3. Click Submit to save the information

### Edit Income Details
1. Navigate to the client's Income Details tab
2. Modify the required information
3. Click Update to save changes

### View Income Details
- All saved income information is displayed in a read-only format
- "N.A" is displayed for empty or null values
- Monetary values are formatted with 2 decimal places

## Permissions

- **Client_Read**: Required to view income details
- **Client_Edit**: Required to add or update income details

## Related Features

- [Client Details](./client_details.md)
- [KYC Information](/docs/admin-portal/clients/documents.md)
- [Financial Information](./financial-information.md) 