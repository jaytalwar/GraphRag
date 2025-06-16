# Statement Of Financial Position Report

## Overview
The Statement Of Financial Position Report provides a summary of the assets, liabilities, and equity of the SACCO for a selected quarter and year. It is designed to comply with UMRA regulatory requirements and supports both PDF and Excel downloads.

## Features
- Select quarter and year for the report
- View assets, liabilities, and equity data
- Download report as PDF or Excel
- Save and view previously generated reports

## How It Works
- The user selects the desired quarter and year.
- The system fetches the relevant data from the backend using the `apiMspreportPost` endpoint.
- The report displays columns for current year quarter, last year corresponding quarter, and previous quarter.
- Users can download the report in their preferred format.

## UI Components
- **Form Controls:** Quarter, Year, SACCO Name
- **Table:** Displays asset and liability data
- **Buttons:** Download (PDF/Excel), Save Report, View Saved Reports

## Example Usage
1. Navigate to **UMRA Report > Statement Of Financial Position Report**.
2. Select the quarter and year.
3. Click **Download** to export the report.

--- 