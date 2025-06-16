---
sidebar_position: 6
---


#  SSO Users

## Overview
The SSO Users List is a component of the CAMS Super Admin Portal that provides administrators with the ability to view and manage all  users in the system. It includes functionality to monitor user  and unlock accounts that have been locked due to security measures or failed login attempts.

## Features

### User Listing
The system provides a comprehensive paginated view of all SSO users, allowing administrators to efficiently navigate through the user details. Administrators can utilize the powerful search functionality to quickly find specific users using keywords(Name,email,Phone Number), while the detailed user information display includes important status indicators such as account lock status.

### User Management
Administrators have the capability to unlock user accounts that have been locked due to security measures or failed login attempts. The system provides real-time monitoring of user account statuses and blocked users, with immediate status updates reflecting any changes made to user accounts.

### Security
The system implements a robust permission-based access control system integrated with the Wakandi SSO service. All actions are performed through secure API endpoints, and an audit trail is maintained for all unlock actions to ensure accountability and security compliance.

## Configuration

### Required Permissions
To access and manage SSO users, administrators need specific permissions:
- The `Client_Read` permission is required for viewing and accessing user information
- The `Client_Edit` permission is necessary for performing unlock operations on user accounts

## User Workflow

### 1. Accessing SSO Users List
1. Log into the Super Admin Portal using valid credentials
2. Navigate to the SSO Users section from the main menu
3. View the paginated list of all SSO users in the system

### 2. Finding Specific Users
1. Use the search bar at the top of the user list
2. Enter search keywords (Name, Email, or Phone Number)
3. The list will automatically filter to show matching results

### 3. Managing Locked Accounts
1. Identify locked accounts through the status indicator
2. Use the unlock button if authorized
3. Confirm the unlock action

### 4. Monitoring User Status
1. Check status indicators for all users wheater user is lock or unlock
###
###

![SSO Users](../../../static/img/ssousers.png)

## Additional Notes
The SSO Users system is deeply integrated with the Wakandi SSO service for secure user authentication. The unlocking of user accounts requires proper authorization levels, and the system performs thorough account status checks for various types of locks, including those triggered by multiple login attempts and password reset requests.



## FAQ
**Q: Who can unlock user accounts?**

A: Users with `Client_Edit` permission or Support role can unlock accounts.

**Q: Can users unlock their own accounts?**

A: No, users cannot unlock their own accounts. This requires administrator intervention.

**Q: How long do accounts stay locked?**

A: Lock duration depends on the security policy and type of lock (login attempts, password reset, etc.).

**Q: What information is needed to unlock an account?**

A: Administrator needs the user's ID and proper permissions to unlock an account.


