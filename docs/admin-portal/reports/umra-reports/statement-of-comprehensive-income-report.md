# Statement Of Comprehensive Income Report

## Overview
The Statement Of Comprehensive Income Report summarizes the income and expenses of the SACCO for a selected quarter and year, providing insight into financial performance as required by UMRA regulations.

## Features
- Select quarter and year for the report
- View financial income and expense data
- Download report as PDF or Excel
- Save and view previously generated reports

## How It Works
- The user selects the desired quarter and year.
- The system fetches the relevant data from the backend using the `apiMspreportPost` endpoint.
- The report displays columns for current year quarter, last year corresponding quarter, and previous quarter.
- Users can download the report in their preferred format.

## UI Components
- **Form Controls:** Quarter, Year, SACCO Name
- **Table:** Displays income and expense data
- **Buttons:** Download (PDF/Excel), Save Report, View Saved Reports

## Example Usage
1. Navigate to **UMRA Report > Statement Of Comprehensive Income Report**.
2. Select the quarter and year.
3. Click **Download** to export the report.

--- 