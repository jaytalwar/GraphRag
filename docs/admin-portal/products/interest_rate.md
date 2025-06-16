# Interest Rate

## Overview
The Interest Rate feature allows administrators to configure and manage interest rates for various financial products in the system. It supports both fixed and variable interest rate types with flexible configuration options.

## Features

### Interest Rate Types
1. **Fixed Interest Rate**
   - Single interest rate value that remains constant throughout the tenure
   - Applicable for products requiring stable interest rates
   - Easy to understand and calculate

2. **Variable Interest Rate**
   - Interest rates that vary based on multiple factors:
     - Duration ranges
     - Amount ranges
     - Period type (Daily/Monthly/Yearly)
   - More flexible and market-responsive
   - Supports complex interest rate structures

### Configuration Options

#### Basic Information
- **Name**: Unique identifier for the interest rate configuration
- **Description**: Optional details about the interest rate
- **Active Status**: Enable/disable the interest rate configuration
- **Validity Period**:
  - Start Date
  - End Date

#### Frequency Settings
- **Frequency Type**: Select from available frequency types
- **Frequency Value**: Number of times the interest rate applies

#### Fixed Interest Rate Configuration
- **Rate of Interest**: Single percentage value (up to 8 decimal places)
- Validation: Must be a valid percentage above 0

#### Variable Interest Rate Configuration
1. **Duration Type**: Select from:
   - Daily
   - Weekly
   - Monthly
   - Yearly

2. **Duration Ranges**:
   - Minimum Duration
   - Maximum Duration
   - Rate of Interest for each range

3. **Amount Ranges**:
   - Minimum Amount
   - Maximum Amount
   - Associated interest rates

### Interest Rate Calculation Methods

1. **Flat Rate**
   - Simple interest calculation
   - Formula: Principal × Rate × Time
   - Suitable for short-term loans

2. **Compounded Rate**
   - Compound interest calculation
   - Formula: Principal × (1 + Rate)^Time - Principal
   - Suitable for long-term investments

## Usage

### Creating Interest Rate
1. Navigate to Settings > Products > Interest Rate
2. Click "Create Interest Rate"
3. Fill in the required information:
   - Select interest rate type (Fixed/Variable)
   - Configure basic details
   - Set up frequency
   - Enter rate values
4. Save the configuration

### Editing Interest Rate
1. Access the interest rate list
2. Select the interest rate to modify
3. Update the required fields
4. Save changes

### Viewing Interest Rates
- List view shows:
  - Name
  - Start Date
  - End Date
  - Type
  - Actions (Edit/Delete)

## Best Practices
1. Always set appropriate validity periods
2. Use descriptive names for easy identification
3. Review and update variable rates periodically
4. Test calculations before applying to live products
5. Document any special conditions or exceptions

## Related Features
- Loan Products
- Savings Products
- Interest Payout
- Loan Amortization

![Interest Rate Configuration](../../../static/img/interestrate.png)
