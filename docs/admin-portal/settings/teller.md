# Teller Management

The Teller module in CAMS provides comprehensive management of bank tellers, their permissions, and operational capabilities. This section allows administrators to create and manage teller accounts, set transaction limits, and configure various operational parameters.

## Overview

Tellers are bank staff members who handle direct customer transactions. In CAMS, a teller is created by first:
1. Creating a user account with appropriate credentials
2. Assigning the teller role to the user
3. Configuring the teller settings and permissions

## Teller Configuration

### Adding a New Teller

To add a new teller:
1. Navigate to Settings > Teller
2. Click the "Add Teller" button
3. Fill in the following required details:
   - Name: Full name of the teller
   - User: Select the user account (must have teller role)
   - Branch: Assign the branch where teller will operate

### Teller Details
The teller configuration includes several key sections:

#### Basic Details
- Name: Teller's full name
- User: Associated user account
- Branch: Operating branch assignment
- Account Number: System-generated unique identifier

#### Permissions
Tellers can be granted specific permissions:
- Post Principal, Interest and Penalties Separately
- Allow Transfer To Other Tellers
- Allow Posting On Behalf Of Other Tellers

#### Accounting Configuration
- General Ledger Code: For transaction posting
- Reserve Ledger Code: For reserve management

#### Transaction Limits
Configure transaction limits for:
- Daily transaction volume
- Single transaction amount
- Cash drawer balance
- Vault access limits

## Teller Operations

### Daily Activities
- Cash drawer management
- Transaction processing
- Balance maintenance
- End-of-day reconciliation

### Transaction Types
Tellers can handle various transactions based on their permissions:
- Cash deposits and withdrawals
- Fund transfers
- Loan payments
- Account services

## Branch-wise Teller Impact

### Branch Operations
- Each branch maintains its own set of tellers
- Tellers are restricted to operations within their assigned branch
- Branch managers can monitor and control teller activities specific to their branch
- Transaction limits and permissions can be set at branch level

### Financial Impact
1. Branch-wise Cash Management
   - Each branch maintains separate cash limits
   - Teller cash drawers contribute to branch cash position
   - Inter-branch transfers require specific permissions
   - Branch-wise reconciliation and reporting

2. Transaction Processing
   - Transactions are tagged to specific branches via teller assignments
   - Affects branch-wise financial statements
   - Impacts branch performance metrics
   - Contributes to branch-specific audit trails

3. Customer Service
   - Branch-specific customer handling
   - Local transaction processing
   - Branch-level service delivery
   - Customer relationship management

### Operational Impact
1. Branch Efficiency
   - Number of tellers affects branch transaction capacity
   - Teller performance impacts branch service levels
   - Queue management and customer wait times
   - Branch resource utilization

2. Risk Management
   - Branch-specific transaction limits
   - Local cash exposure control
   - Branch-level security measures
   - Compliance monitoring per branch

3. Reporting and Analytics
   - Branch-wise transaction volumes
   - Teller performance by branch
   - Cash position per branch
   - Branch-specific audit requirements

### Administrative Control
1. Branch Management
   - Local teller supervision
   - Branch-specific operating hours
   - Local override authorities
   - Branch-level access control

2. Resource Allocation
   - Teller staffing per branch
   - Cash allocation to branches
   - Equipment and resource distribution
   - Training and support requirements

## Security and Compliance

### Access Control
- Unique teller IDs
- Branch-specific access
- Transaction authorization levels
- Audit trail maintenance

### Monitoring
- Transaction logging
- Activity reports
- Balance verification
- Security alerts

## Best Practices

1. Regular password updates
2. Transaction verification
3. Cash drawer reconciliation
4. Proper documentation
5. Security protocol adherence

- Branch-specific guidelines adherence
- Regular branch-wise reconciliation
- Branch-level security protocols
- Inter-branch coordination procedures

## Related Settings
- [User Management](../settings/administrators.md)
- [Roles and Permissions](./roles.md)
- [Branch Settings](../settings/branches.md)
- [Security Settings](./security.md)

## Important Notes
- Always maintain accurate transaction records
- Follow security protocols strictly
- Regular system updates are mandatory
- Comply with banking regulations
- Maintain proper documentation 