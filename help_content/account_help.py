# help_content/account_help.py

def get_account_content():
    """Account management help content - focused only on user account operations"""
    return {

# -------------------------------------     Change Password      --------------------------------------

"Change Password": {
    "title": "Change Password",
    "description": """
<b>Change Password – Help Guide</b><br><br>

This section guides you through the process to securely change your password.<br><br>

<b>Form Fields & Options</b>
<ol>
  <li><b>User Name</b>
        <p>Displayed and cannot be changed; it’s automatically set to the logged-in user.</p>
  </li>
  <li><b>Old Password</b>
        <p>Enter your current password to verify your identity.</p>
  </li>
  <li><b>New Password</b>
        <p>Must be at least 6 characters and include at least one letter, one number, and one special character.</p>
  </li>
  <li><b>Confirm New Password</b>
        <p>Re-enter the new password to ensure accuracy.</p>
  </li>
  <li><b>Show Password</b>
        <p>Checkbox to toggle visibility of your new password entries.</p>
  </li>
  <li><b>Next</b>
        <p>Click to validate your current password, then follow prompts to set your new password.</p>
  </li>
</ol>

<br>

<b>Important Notes</b>
<ul>
  <li>If validation fails, you will be notified.</li>
  <li>Please ensure your new password meets all requirements before saving.</li>
  <li>Passwords should never be shared with others.</li>
</ul>

<br>

<i>Following these steps ensures your account remains secure.</i>
"""
}
,


# -------------------------------------        Logout            ---------------------------------------
 
"Logout": {
    "title": "Logout",
    "description": """
<b>Secure Session Logout – Help Guide</b><br><br>

Safely terminate your current session and protect your account from unauthorized access.<br><br>

<b>Logout Process</b>
<ol>
  <li><b>Session Termination</b>
        <p>All active sessions are closed.</p>
  </li>
  <li><b>Cache Clearing</b>
        <p>Temporary data and tokens removed.</p>
  </li>
  <li><b>Security Logging</b>
        <p>Logout time and location recorded.</p>
  </li>
</ol>

<br>

<b>Security Benefits</b>
<ul>
  <li>Prevent unauthorized access on shared computers.</li>
  <li>Session security by invalidating authentication tokens.</li>
  <li>Audit trail for compliance and monitoring.</li>
  <li>Resource cleanup for efficiency.</li>
</ul>

<br>

<b>Session Management</b>
<ul>
  <li>View active sessions.</li>
  <li>Track devices currently logged in.</li>
  <li>Review login history for unusual activity.</li>
</ul>

<br>

<b>Best Practices</b>
<ul>
  <li>Always logout when finished working.</li>
  <li>Especially important on shared or public computers.</li>
  <li>Use logout when switching between accounts.</li>
</ul>

<br>

<i>Logging out properly ensures maximum protection of your account and data.</i>
"""
}

    
    }
