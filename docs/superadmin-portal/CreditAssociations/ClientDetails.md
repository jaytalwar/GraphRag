# Client Details Tab 


## ✨ Overview

**Purpose:**  
The Client Details tab provides superadmins and managers with a centralized interface to view, search, filter, and manage all members associated with a Credit Association (Sacco). This feature streamlines member management, enhances support capabilities, and ensures efficient onboarding and communication.

**Scope:**  
This documentation covers the functionalities, workflows, and validation rules of the Client Details tab within the Superadmin Portal for Credit Associations. It is intended for superadmins, support staff, and system managers responsible for member administration.

---

## 🧩 Feature Details

- Paginated table listing all Sacco members.
- Columns: Full Name, Phone Number, Email Address, Status.
- Search and filter options for efficient member lookup.
- Bulk action: Activate all pending members.
- Pagination controls for navigating large member lists.

---

## 📐 Functional Description

- **Member List Table:**  
  Displays all members with their full name, phone number, email address, and current status (e.g., Active, Pending, Exited).
- **Search Bar:**  
  Allows searching for members by name, phone number, or email address.
- **Status Filter:**  
  Dropdown to filter members by their status (All, Blocked, Rejected, Requested, Dormant, Active, Pending).
- **Activate All Members Button:**  
  Enables superadmins to activate all members currently in a pending state with a single click.
- **Pagination Controls:**  
  Located at the bottom of the table, allowing navigation through multiple pages of members.

---

## 🔄 Workflow / User Journey

1. **Accessing the Tab:**  
   The superadmin navigates to the Credit Associations section and selects the desired Sacco.
2. **Viewing Members:**  
   The Client Details tab displays a paginated list of all members, showing key contact and status information.
3. **Searching/Filtering:**  
   The user can search for specific members or filter the list by status to quickly locate individuals or groups.
4. **Bulk Activation:**  
   If there are members in a pending state, the superadmin can activate all of them at once using the "Activate All Members" button.
5. **Pagination:**  
   For Saccos with many members, the user can navigate between pages using the pagination controls.
   ![Client Details tab showing member list, status, and pagination controls in the Superadmin Portal.](../../../static/img/Superadmin_Client%20_Details.png)
*Figure 1: Client Details tab showing member list, status, and pagination controls in the Superadmin Portal.*

---

## ⚠️ Validation / Constraints / Configurations

- Only users with superadmin or appropriate permissions can access and perform actions in this tab.
- The "Activate All Members" button is enabled only if there are members in the pending state.
- Search and filter inputs must be valid (e.g., no special characters in the search bar).
- Pagination ensures performance and usability for large member lists.

---

## ✅ Acceptance Criteria

- The member list displays all relevant columns and is paginated.
- Search and filter functionalities return accurate results based on user input.
- The "Activate All Members" button activates only pending members and is disabled otherwise.
- Pagination controls work as expected, allowing navigation through all member pages.
- Only authorized users can access and perform actions in the Client Details tab.
- The UI reflects real-time status changes (e.g., after activation, members' statuses update to Active).

---




 