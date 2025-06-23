# Risk Classification Of Assets Provisioning Report

## Overview
The Risk Classification Of Assets Provisioning Report provides a detailed analysis of the SACCO's loan portfolio, classifying assets and provisioning requirements for a selected quarter and year, as per UMRA guidelines.

## Features
- Select quarter and year for the report
- View classification, number of accounts, outstanding loan portfolio, required provision percentage, and required provision
- Download report as PDF or Excel
- Save and view previously generated reports

## How It Works
- The user selects the desired quarter and year.
- The system fetches the relevant data from the backend using the `apiMspreportPost` endpoint.
- The report displays asset classification and provisioning details.
- Users can download the report in their preferred format.

## UI Components
- **Form Controls:** Quarter, Year, SACCO Name
- **Table:** Displays classification, number of accounts, outstanding loan portfolio, required provision percentage, and required provision
- **Buttons:** Download (PDF/Excel), Save Report, View Saved Reports

## Example Usage
1. Navigate to **UMRA Report > Risk Classification Of Assets Provisioning Report**.
2. Select the quarter and year.
3. Click **Download** to export the report.

---