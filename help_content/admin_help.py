# help_content/admin_help.py

def get_admin_content():
    """Admin panel help content - fully enhanced with detailed points & UI references"""
    return {

# --------------------------         Admin Panel     -----------------
"Admin": {
            "title": "Administration Panel",
            "description": """
<b>System Administration & User Management</b><br><br>

The <b>Administration Panel</b> is the control hub for managing users, 
security, and system-level settings. From here, you can add/edit users, 
reset their passwords, update logout sessions, and ensure smooth & secure operations.<br><br>

<b>Main Features:</b><br>
• <b>Create New User:</b> Add new accounts with role-based access.<br>
• <b>Edit User:</b> Manage all accounts in a detailed table view.<br>
• <b>Update Logout Time:</b> Correct or update incorrect session details.<br>
• <b>Password Reset:</b> Reset user passwords securely.<br><br>

<b>User Roles:</b><br>
• <b>Super Admin:</b> Unlimited access & configuration rights.<br>
• <b>Admin:</b> Manage user accounts and key settings.<br><br>

<b>Security Features:</b><br>
• Strong password enforcement<br>
• Role-based access permissions<br>
• Session tracking & logout update
"""
        },


# --------------------------      Admin - Create New User   ------------------------

"Create New User": {
            "title": "Create New User Account",
            "description": """
<b>Create New User - Help Guide</b><br><br>
This option allows you to create new user accounts using a dedicated form.<br><br>

<b>Steps:</b><br>
1. Open the <b>Create New User</b> section.<br>
2. Fill required fields:<br>
&nbsp;&nbsp;• <b>Client ID:</b> Auto-fetched, cannot be changed.<br>
&nbsp;&nbsp;• <b>Username:</b> Must be unique, alphabets only (A-Z).<br>
&nbsp;&nbsp;• <b>Password:</b> Must contain 1 letter, 1 number, 1 special character.<br>
&nbsp;&nbsp;• <b>First/Last Name:</b> Alphabets only.<br>
&nbsp;&nbsp;• <b>Admin Checkbox:</b> Select if this account should have Admin rights.<br>
3. Click <b>Save</b> button to create the account.<br><br>

<b>Best Practices:</b><br>
• Always set a strong password.<br>
• Avoid generic usernames like "admin" or "test".<br>
• Assign Admin rights only when necessary.
            """
        },


# ----------------------------        Edit Admin Panel        ---------------------  

"Edit User": {
            "title": "Edit User Account",
            "description": """
<b>Edit User - Help Guide</b><br><br>
This section lists all users in a <b>tabular format</b> for quick overview & management.<br><br>

<b>System Limits:</b><br>
• Max Users: 15<br>
• Max Admins: 7<br><br>

<b>Steps:</b><br>
1. Open the <b>Edit User</b> section.<br>
2. Review the table with the following columns:<br>
&nbsp;&nbsp;• <b>S. No.:</b> Serial number.<br>
&nbsp;&nbsp;• <b>Username:</b> User’s login name.<br>
&nbsp;&nbsp;• <b>First / Last Name:</b> Full identity.<br>
&nbsp;&nbsp;• <b>Admin:</b> Shows if user has Admin rights.<br>
&nbsp;&nbsp;• <b>Active:</b> Shows user is Active or not. <br>
&nbsp;&nbsp;• <b>Last Login:</b> Last login timestamp.<br>
&nbsp;&nbsp;• <b>Last Logout:</b> Last logout timestamp.<br>
&nbsp;&nbsp;• <b>MAC Address:</b> Device MAC Address.<br>
3. Select a user from the list.<br>
4. Edit required details (Name, Role, Active status).<br>
5. Save changes to update the account.<br><br>

<b>Available Actions:</b><br>
• Change user roles (User/Admin).<br>
• Track login/logout history.<br>
• Sort and filter users for faster search.<br>
• Review MAC Address to detect unauthorized device access.<br><br>

<b>Use Cases:</b><br>
• Promoting a user to Admin role.<br>
• Updating user names or correcting typos.<br><br>

<b>Best Practices:</b><br>
• Limit number of Admins to maintain security.<br>
• Cross-check MAC address if suspicious logins are found.<br>
• Keep track of last login/logout for compliance audits.
"""
        },


# ---------------------------------   Admin Update Logout  -------------------------


"Update Logout Time": {
            "title": "Update Logout Time",
            "description": """
<b>Update Logout Time - Help Guide</b><br><br>
This option is used when a user session did not log out correctly. It helps to fix inaccurate session details.<br><br>

<b>Steps:</b><br>
1. Open <b>User Name</b> dropdown (shows only logged-in users).<br>
2. Select the required user.<br>
3. Click <b>Update Logout Time</b> to set current timestamp.<br><br>

<b>Use Cases:</b><br>
• User forgot to log out.<br>
• Unexpected system shutdown.<br>
• Session not recorded properly.
            """
        },


# ------------------------------------------    Password Reset   --------------------------------

"Password Reset": {
            "title": "Password Reset Management",
            "description": """
<b>Password Reset - Help Guide</b><br><br>
This feature allows secure password reset for users via the reset form in UI.<br><br>

<b>Steps:</b><br>
1. Choose a user from <b>User Name</b> dropdown.<br>
2. Enter new password in <b>New Password</b> field.<br>
3. Retype password to confirm.<br>
4. Tick <b>Show Password</b> to verify input.<br>
5. Click <b>Save</b> to apply changes.<br><br>

<b>Password Rules:</b><br>
• Minimum 6 characters.<br>
• At least one alphabet.<br>
• At least one number.<br>
• At least one special character.<br><br>

<b>Best Practices:</b><br>
• Never reuse old or common passwords.<br>
• Do not share credentials with others.<br>
• Recommend periodic password changes.<br>
• Use password managers if required.
            """
        }
    }
