# Assets Management

The Assets tab provides comprehensive management of client-owned assets, including property, vehicles, and other valuable items.

## Overview

The Assets management module allows administrators to track and manage client assets, which can be used for collateral or as part of the client's financial profile. The system supports both physical and non-physical assets with document attachments.

## Asset Management Interface

### Asset List View
The main assets page displays a table with the following columns:
- Asset Type
- Asset Value
- Location
- Actions (View, Edit, Delete)

### Adding a New Asset

To add a new client asset:

1. Navigate to the client's Assets tab
2. Click the "Create" button
3. Fill in the required information:
   - **Type** (*required*): Select from predefined asset types
   - **Value** (*required*): Enter the monetary value of the asset
   - **Location** (*required for physical assets*): Specify where the asset is located
   - **Comments/Notes**: Add any additional information about the asset
   - **Documents**: Upload supporting documentation (supported formats: images, PDFs)

### Editing an Asset

To edit an existing asset:

1. Locate the asset in the assets list
2. Click the edit icon (pencil) in the Actions column
3. Modify the desired fields:
   - Asset Type
   - Asset Value
   - Location
   - Comments
   - Supporting Documents

### Asset Details View

The asset details view shows:
- Asset Type
- Asset Value (in default currency)
- Location (if applicable)
- Comments/Notes
- Attached Documents

### Document Management

For each asset, you can:
- Upload supporting documents during creation
- View attached documents
- Update documents during edit
- Download attached documents

## Asset Types

The system supports various asset types categorized as:

### Physical Assets
- Residential Property
- Commercial Property
- Vehicles
- Equipment
- Machinery

### Non-Physical Assets
- Investments
- Financial Instruments
- Intellectual Property
- Other Assets

## Validation Rules

1. **Asset Type**
   - Required field
   - Must be selected from predefined types

2. **Asset Value**
   - Required field
   - Must be a valid numeric value
   - Supports decimal values based on system configuration

3. **Location**
   - Required for physical assets
   - Optional for non-physical assets
   - Alphanumeric with dash characters allowed

4. **Comments**
   - Optional field
   - Maximum length: 264 characters

5. **Documents**
   - Optional
   - Supported file types: Images, PDFs
   - Multiple documents can be attached

## Permissions

Asset management operations are controlled by the following permissions:
- `Client_Read`: Required for viewing assets
- `Client_Edit`: Required for creating, updating, and deleting assets

## Related Features

- [Financial Information](./financial-information.md) - For asset value tracking
- [Documents](./documents.md) - For asset documentation 