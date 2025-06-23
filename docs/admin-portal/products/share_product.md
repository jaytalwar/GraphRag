# Share Product

## Overview
The Share Product feature allows administrators to create and manage different types of share products in the system. Share products represent different categories of shares that members can purchase, with specific configurations for value per share, accounting settings, and usage rules.

## Features

### 1. Share Product Management
- Create new share products
- View list of existing share products
- Edit share product details
- Delete share products (if not in use)

### 2. Share Product Configuration
Each share product can be configured with the following parameters:

#### Basic Details
- Name: Unique identifier for the share product
- Per Share Value: The monetary value assigned to each share unit
- Account Code: Associated general ledger account code
- Account Name: Name of the associated account

#### Usage Settings
- Allowed as Guarantor: Whether shares can be used as loan guarantees
- Allowed as Collateral: Whether shares can be used as loan collateral

### 3. Share Account Management
- View all share accounts
- Search share accounts by:
  - Member name
  - Member ID
  - Account number
  - Product name
  - Account status
- Filter by specific share product

## User Interface

### Share Product List
The share product list view displays:
- Product name
- Account number
- General ledger code
- Action buttons for edit operations

### Create/Edit Share Product
The create/edit form includes:
1. Details section
   - Product name
   - Per share value
   - Account configuration
2. Accounting section
   - Account code
   - Account name
3. History section
   - Audit log of changes

## Access Control
The feature is protected by the following permissions:
- `Settings_Product_Read`: Required to view share products
- `Settings_Product_Edit`: Required to create/edit share products
- `Settings_Product_Delete`: Required to delete share products
- `ShareAccount_Read`: Required to view share accounts
- `ShareAccount_Edit`: Required to modify share accounts
- `ShareAccount_Delete`: Required to delete share accounts

## Integration Points

### Member Management
- Share products can be configured as mandatory for new members
- Share accounts are automatically created for new members if configured in membership policy

### Loan Management
- Share products can be used as:
  - Loan guarantees
  - Loan collateral
  - Multiplier for loan eligibility

### Accounting
- Each share product is linked to a general ledger account
- Share transactions are recorded in the accounting system

## Data Import
Share products can be imported through the data import feature:
- Product type must be specified as "Share"
- Product name must match an existing share product
- Per share value must be configured

## Best Practices
1. Configure unique and descriptive names for share products
2. Set appropriate per share values based on organizational requirements
3. Configure accounting settings before allowing share purchases
4. Review audit logs regularly for tracking changes
5. Ensure proper access control settings for different user roles

![Share Product Interface](../../../static/img/share_product.png)
