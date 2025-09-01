# help_content/account_help.py

def get_account_content():
    """Account management help content - focused only on user account operations"""
    return {

# -----------------------------        Change Password      --------------------------------------
        "Change Password": {
            "title": "Change Password",
            "description": """
<b>Change Password - Help Guide</b><br><br>

This section guides you through the process to securely change your password.<br><br>

<b>Form Fields & Options:</b><br>
• <b>User Name:</b> Displayed and cannot be changed; it’s automatically set to the logged-in user.<br>
• <b>Old Password:</b> Enter your current password to verify your identity.<br>
• <b>New Password:</b> Must be at least 6 characters and include at least one letter, one number, and one special character.<br>
• <b>Confirm New Password:</b> Re-enter the new password to ensure accuracy.<br>
• <b>Show Password:</b> Checkbox to toggle visibility of your new password entries.<br>
• <b>Next:</b> Click to validate your current password, then follow prompts to set your new password.<br><br>

<b>Important Notes:</b><br>
• If validation fails, you will be notified.<br>
• Please ensure your new password meets all requirements before saving.<br>
• Passwords should never be shared with others.<br><br>

<i>Following these steps ensures your account remains secure.</i>
            """
        },



# ---------------------------------------     Logout      ------------------------------------------------
 
        "Logout": {
            "title": "Logout",
            "description": """
<b>Secure Session Logout</b><br><br>

Safely terminate your current session and protect your account from unauthorized access.<br><br>

<b>Logout Process:</b><br>
• <b>Session Termination:</b> All active sessions are closed.<br>
• <b>Cache Clearing:</b> Temporary data and tokens removed.<br>
• <b>Security Logging:</b> Logout time and location recorded.<br>
• <b>Redirect:</b> Automatically redirected to login page.<br><br>

<b>Security Benefits:</b><br>
• Prevent unauthorized access on shared computers.<br>
• Session security by invalidating authentication tokens.<br>
• Audit trail for compliance and monitoring.<br>
• Resource cleanup for efficiency.<br><br>

<b>Auto-Logout Features:</b><br>
• Inactivity timeout – automatic logout after idle period.<br>
• Session expiration – maximum session duration limits.<br>
• Multiple login detection – limit concurrent sessions.<br>
• Scheduled maintenance – forced logout during updates.<br><br>

<b>Best Practices:</b><br>
• Always logout when finished working.<br>
• Especially important on shared or public computers.<br>
• Don’t rely solely on closing the browser.<br>
• Use logout when switching between accounts.<br><br>

<b>Session Management:</b><br>
• View active sessions.<br>
• Track devices currently logged in.<br>
• Perform remote logout on other devices.<br>
• Review login history for unusual activity.<br><br>

<i>Logging out properly ensures maximum protection of your account and data.</i>
            """
        }
    }
