# help_content/admin_help.py

def get_admin_content():
    """Admin panel help content - fully enhanced with detailed points & UI references"""
    return {

# -------------------------------          Admin Panel       --------------------------------

"Admin": {
    "title": "Administration Panel",
    "description": """
<b>Administration Panel – Help Guide</b><br><br>

The <b>Administration Panel</b> is the control hub for managing users, 
security, and system-level settings. From here, you can add/edit users, 
reset their passwords, update logout sessions, and ensure smooth & secure operations.<br><br>

<b>Main Features</b>
<ul>
  <li><b>Create New User:</b> Add new accounts with role-based access.</li>
  <li><b>Edit User:</b> Manage all accounts in a detailed table view.</li>
  <li><b>Update Logout Time:</b> Correct or update incorrect session details.</li>
  <li><b>Password Reset:</b> Reset user passwords securely.</li>
</ul>

<br>

<b>User Roles</b>
<ul>
  <li><b>Super Admin:</b> Unlimited access & configuration rights.</li>
  <li><b>Admin:</b> Manage user accounts and key settings.</li>
</ul>

<br>

<b>Security Features</b>
<ul>
  <li>Strong password enforcement.</li>
  <li>Role-based access permissions.</li>
  <li>Session tracking & logout update.</li>
</ul>

<br>

<i>Use the Administration Panel to keep your system secure and user access well managed.</i>
"""
},


# -----------------------------     Admin - Create New User    --------------------------------

"Create New User": {
    "title": "Create New User Account",
    "description": """
<b>Create New User – Help Guide</b><br><br>
This option allows you to create new user accounts using a dedicated form.<br><br>

<b>Steps</b>
<ol>
  <li>Open the <b>Create New User</b> section.</li>
  <li>Fill required fields:
    <ul>
      <li><b>Client ID:</b> Auto-fetched, cannot be changed.</li>
      <li><b>Username:</b> Must be unique, alphabets only (A-Z).</li>
      <li><b>Password:</b> Must contain 1 letter, 1 number, 1 special character.</li>
      <li><b>First/Last Name:</b> Alphabets only.</li>
      <li><b>Admin Checkbox:</b> Select if this account should have Admin rights.</li>
    </ul>
  </li>
  <li>Click <b>Save</b> button to create the account.</li>
</ol>

<br>

<b>Best Practices</b>
<ul>
  <li>Always set a strong password.</li>
  <li>Avoid generic usernames like "admin" or "test".</li>
  <li>Assign Admin rights only when necessary.</li>
</ul>
"""
}
,

# ----------------------------        Edit Admin Panel        ------------------------------- 

"Edit User": {
    "title": "Edit User Account",
    "description": """
<b>Edit User – Help Guide</b><br><br>
This section lists all users in a <b>tabular format</b> for quick overview & management.<br><br>

<b>System Limits</b>
<ul>
  <li>Max Users: 15</li>
  <li>Max Admins: 7</li>
</ul>

<br>

<b>Steps</b>
<ol>
  <li>Open the <b>Edit User</b> section.</li>
  <li>Review the table with the following columns:
    <ul>
      <li><b>S. No.:</b> Serial number.</li>
      <li><b>Username:</b> User’s login name.</li>
      <li><b>First / Last Name:</b> Full identity.</li>
      <li><b>Admin:</b> Shows if user has Admin rights.</li>
      <li><b>Active:</b> Shows user is Active or not.</li>
      <li><b>Last Login:</b> Last login timestamp.</li>
      <li><b>Last Logout:</b> Last logout timestamp.</li>
      <li><b>MAC Address:</b> Device MAC Address.</li>
    </ul>
  </li>
  <li>Select a user from the list.</li>
  <li>Edit required details (Name, Role, Active status).</li>
  <li>Save changes to update the account.</li>
</ol>

<br>

<b>Available Actions</b>
<ul>
  <li>Change user roles (User/Admin).</li>
  <li>Track login/logout history.</li>
  <li>Sort and filter users for faster search.</li>
  <li>Review MAC Address to detect unauthorized device access.</li>
</ul>

<br>

<b>Use Cases</b>
<ul>
  <li>Promoting a user to Admin role.</li>
  <li>Updating user names or correcting typos.</li>
</ul>

<br>

<b>Best Practices</b>
<ul>
  <li>Limit number of Admins to maintain security.</li>
  <li>Cross-check MAC address if suspicious logins are found.</li>
  <li>Keep track of last login/logout for compliance audits.</li>
</ul>
"""
}

,

# ----------------------------      Admin Update Logout       --------------------------------

"Update Logout Time": {
    "title": "Update Logout Time",
    "description": """
<b>Update Logout Time – Help Guide</b><br><br>
This option is used when a user session did not log out correctly. It helps to fix inaccurate session details.<br><br>

<b>Steps</b>
<ol>
  <li>Open <b>User Name</b> dropdown (shows only logged-in users).</li>
  <li>Select the required user.</li>
  <li>Click <b>Update Logout Time</b> to set current timestamp.</li>
</ol>

<br>

<b>Use Cases</b>
<ul>
  <li>User forgot to log out.</li>
  <li>Unexpected system shutdown.</li>
  <li>Session not recorded properly.</li>
</ul>
"""
}
,

# -----------------------------        Password Reset         --------------------------------

"Password Reset": {
    "title": "Password Reset Management",
    "description": """
<b>Password Reset – Help Guide</b><br><br>
This feature allows secure password reset for users via the reset form in UI.<br><br>

<b>Steps</b>
<ol>
  <li>Choose a user from <b>User Name</b> dropdown.</li>
  <li>Enter new password in <b>New Password</b> field.</li>
  <li>Retype password to confirm.</li>
  <li>Tick <b>Show Password</b> to verify input.</li>
  <li>Click <b>Save</b> to apply changes.</li>
</ol>

<br>

<b>Password Rules</b>
<ul>
  <li>Minimum 6 characters.</li>
  <li>At least one alphabet.</li>
  <li>At least one number.</li>
  <li>At least one special character.</li>
</ul>

<br>

<b>Best Practices</b>
<ul>
  <li>Never reuse old or common passwords.</li>
  <li>Do not share credentials with others.</li>
  <li>Recommend periodic password changes.</li>
  <li>Use password managers if required.</li>
</ul>
"""
}

    
}
