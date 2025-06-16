# Credit Associations (Saccos)

This section provides a comprehensive guide to the **Credit Associations** (commonly known as Saccos) feature in the Superadmin Portal. It covers the creation process, main features, and links to detailed documentation for each tab available within a Sacco's profile.

---

## Overview
Credit Associations (Saccos) are financial cooperatives managed within the Wakandi CAMS platform. Superadmins can create, configure, and manage these entities, each with its own set of features and configurations.

## How Credit Associations Are Created

### Creation Flow
1. **Initiation**: Superadmin clicks the `Create` button on the Credit Associations list page.
2. **Input Details**: Required information such as name, address, registration number, license, admin email, and module type (Saccos, Merrygoround, Microfinance) is provided.
3. **Backend Processing**:
   - The system checks for existing associations with the same name.
   - A new tenant is created for the association.
   - Credit Union (Sacco) details are saved in the database.
   - A unique Credit Union ID is generated.
   - The association is registered in the CRM and accounting systems.
   - Default configurations and accounts are set up (e.g., Wakandi account, liability, and expense accounts).
   - The admin user is assigned and notified.

### Statuses & Stages
- **Status**: Indicates if the Sacco is Active, Pending, or Deactivated.
- **Stage**: Represents the onboarding or operational stage (e.g., Demo, Live).

---

## Main Features
- **List & Search**: View all Credit Associations, search by name or ID.
- **Profile Management**: Access detailed information and configuration for each Sacco.
- **Tabs**: Each Sacco profile contains multiple tabs:
  - Credit Union Details
  - Client Details
  - Features
  - Configurations
  - Jobs
  - Online Payments
  - Fees and Invoice
  - Service Provider

Each tab is documented in a separate file for clarity. See the links below for detailed guides.

---

## Documentation Structure
- [Credit Union Details](./CreditUnionDetails.md)
- [Client Details](./ClientDetails.md)
- [Features](./Features.md)
- [Configurations](./Configurations.md)
- [Jobs](./Jobs.md)
- [Online Payments](./OnlinePayments.md)
- [Fees and Invoice](./FeesAndInvoice.md)
- [Service Provider](./ServiceProvider.md)

---

For further technical details, refer to the backend source files and business logic in the `cams-api` project. 