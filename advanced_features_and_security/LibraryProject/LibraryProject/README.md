# Django Permissions Setup

## Custom Permissions
- `can_view`: Can view articles
- `can_create`: Can create articles
- `can_edit`: Can edit articles
- `can_delete`: Can delete articles

## Groups and Assigned Permissions
- **Viewers**: can_view
- **Editors**: can_create, can_edit
- **Admins**: can_view, can_create, can_edit, can_delete

## How to Assign Users to Groups
1. Go to Django Admin (`/admin`).
2. Navigate to "Users" and select a user.
3. Scroll down to "Groups" and assign the user to a group.

## Enforcing Permissions
Permissions are enforced using:
- `@permission_required('app_name.can_edit', raise_exception=True)`

## Testing
1. Create test users and assign them to groups.
2. Log in as each user and check if they can access their permitted actions.
