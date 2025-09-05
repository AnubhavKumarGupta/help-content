# help_content/connection_help.py

def get_connection_content():
    """Connection management help content - focused only on connection operations"""
    return {

# ----------------------------------------         Connection          ---------------------------------  

"Connection": {
    "title": "Connection",
    "description": """
<b>Connection – Help Guide</b><br><br>

<b>Purpose:</b><br>
The Connection section is your central hub for managing all data source integrations within <b>INFOFISCUS CDWTA</b>. 
It provides an overview of every database and platform connection currently configured, allowing users to view, 
manage, and select the correct linkage for <b>validation, analysis, or ETL workflows</b>.<br><br>

<b>Key Points:</b>
<ul>
  <li>Lists all active connections, each with database platform-specific input fields.</li>
  <li>Enables quick access to connection details and health/status.</li>
  <li>Facilitates edits and deletion to keep integrations secure and up-to-date.</li>
  <li>Supports audit, compliance, and operational transparency by centralizing management of all data access points.</li>
</ul>
"""
}
,

# -----------------------------------------      Create Connection          ---------------------------

"Create Connection": {
    "title": "Create Connection",
    "description": """
<b>Create Connection – Help Guide</b><br><br>

<b>Purpose:</b><br>
The Create Connection section guides users through the process of securely establishing a new integration 
between <b>INFOFISCUS CDWTA</b> and an external database or data platform. It ensures that users provide all required 
parameters and credentials, supporting both connectivity and compliance with organizational policies.<br><br>

<b>Key Points:</b>
<ul>
  <li>Prompts for platform, hostname, authentication, and any special parameters.</li>
  <li>Step-by-step workflow ensures no essential configuration is missed.</li>
  <li>Allows designation of connection names for easy identification.</li>
  <li>Enables secure onboarding of new data sources without affecting existing workflows.</li>
  <li>Foundation for subsequent data validation, scheduling, and analytics tasks.</li>
</ul>
"""
}
,

# ------------------------------------------      Edit Connection            --------------------------  

"Edit Connection": {
    "title": "Edit Database Connection",
    "description": """
<b>Edit Database Connection – Help Guide</b><br><br>

<b>Overview</b><br>
The Edit Database section allows you to update and maintain your existing database connections as your data infrastructure evolves. 
Instead of creating a new connection each time the underlying database changes (such as after new tables are added, schema is updated, 
or credentials are refreshed), you can efficiently update the current connection configuration here—ensuring a seamless workflow and 
avoiding unnecessary duplication.<br><br>

<b>Why Edit Database is Important</b>
<ul>
  <li><b>Avoid Unnecessary Duplication:</b> When changes happen in your source database (new tables/views, schema alterations, etc.), 
      editing your connection ensures the latest structure is reflected without having to create a new connection from scratch.</li>
  <li><b>Preserve Test Case Associations:</b> Existing test cases and validation jobs linked to this connection continue to work – 
      there’s no need to reconfigure or relink them.</li>
  <li><b>Streamlined Maintenance:</b> Editing an existing connection is quicker, reduces potential errors, and helps maintain a clean 
      connection list.</li>
  <li><b>Data Consistency:</b> Keeping the same connection, but refreshing its metadata, ensures consistent access control, naming, and 
      configuration history.</li>
  <li><b>Efficient Change Management:</b> Whether you change connection credentials, update hosts/ports, or refresh schemas, 
      Edit Database keeps transitions smooth and auditable.</li>
</ul><br>

<b>When Should You Use Edit Database?</b>
<ul>
  <li>New tables or views have been added or removed in the database.</li>
  <li>Schema changes such as new columns, changed datatypes, or renamed tables.</li>
  <li>Database user credentials or authentication methods have changed.</li>
  <li>You need to update performance-related parameters (timeout, pooling, etc.).</li>
  <li>Server or database endpoints have migrated or changed (for example, after cloud migration).</li>
  <li>Periodic reconnection to refresh catalog information or re-validate connectivity.</li>
</ul><br>

<b>How It Works</b>
<ol>
  <li>Select the connection you wish to edit from your list of existing connections.</li>
  <li>In Edit Database, the connection details form pre-fills with current values.</li>
  <li>Make the required changes, such as correcting credentials, updating host/port, or simply clicking Test and Save to automatically 
      refresh and reload the metadata (including fetching any new tables or structure changes from the source database).</li>
  <li>The system updates the connection and its metadata, ensuring all linked test cases use the newly updated schema or data without interruption.</li>
  <li>Security is enforced throughout: all password and sensitive field changes are properly secured, and a modification audit trail is recorded.</li>
  <li>Finally, the system validates that all updates are compatible before saving – preventing accidental misconfiguration.</li>
</ol><br>

<b>Benefits</b>
<ul>
  <li>Up-to-date on all schema/structure changes without new setup.</li>
  <li>Efficient troubleshooting and maintenance (no renaming or duplicated connections).</li>
  <li>Centralized auditing and tracking of all configuration changes.</li>
  <li>Fast onboarding of evolving data architecture (especially in dynamic or agile teams).</li>
</ul>
"""
}
,

# -----------------------------            Connection -> Delete Connection          ----------------

"Delete Connection": {
    "title": "Delete Database Connection",
    "description": """
<b>Delete Connection – Help Guide</b><br><br>

<b>Overview</b><br>
The Delete Connection feature enables users (especially admins) to efficiently remove obsolete, duplicate, or invalid database connections from 
the <b>INFOFISCUS CDWTA</b>. Streamlining your connection list improves clarity, reduces clutter, and helps prevent confusion 
or errors during test case management.<br><br>

<b>Why Delete Connections? (Use Cases & Benefits)</b>
<ul>
  <li><b>Maintain a Clean UI:</b> Deleting old or unused connections keeps your connection list easy to navigate—avoiding visual clutter, confusion, 
      and accidental use of incorrect connections.</li>
  <li><b>Remove Invalid or Expired Connections:</b> Connections with expired, rotated, or invalid credentials can be safely deleted to prevent failures 
      in future data validation tasks.</li>
  <li><b>Reduce Duplicates:</b> Eliminates redundant (e.g., similarly named) connections, making it easier to find and select the correct and current 
      integration for your workflows.</li>
  <li><b>Security Best Practice:</b> Removing connections that are no longer needed reduces the surface area for potential security risks.</li>
  <li><b>Audit and Organization:</b> Supports better audit control, as only actively used connections remain visible and manageable.</li>
</ul><br>

<b>How to Delete a Connection – Step-by-Step Instructions</b>
<ol>
  <li><b>Access the Delete Connection Panel:</b><br>
      • Click on Delete Connection in the main sidebar.<br>
      • A list view/table will load, showing all available connections with details like name, database type, user, creation date, and test case count.</li><br>

  <li><b>Admin User Filtering & Search:</b><br>
      • If you’re an admin, you’ll see all connections, including those created by other users.<br>
      • Use the user dropdown at the top to filter connections by a particular user—making it easy to manage connections per user.<br>
      • Optionally, use the dedicated search bar to instantly find a connection by name, user, or database type.</li><br>

  <li><b>Select Connection(s) to Delete:</b><br>
      • In the list, select the radio button next to the connection you wish to delete.<br>
      • Carefully review the details—especially if multiple connections have similar names.</li><br>

  <li><b>Test Case Warning (If Applicable):</b><br>
      • If the selected connection is currently linked to any test cases, a confirmation dialog will appear, summarizing the linked test case names or IDs.<br>
      • The system warns: "X test case(s) are linked to this connection. Deleting it will also delete all associated test cases."<br>
      • Review this carefully: If you delete the connection, all linked test cases will be removed as well.</li><br>

  <li><b>Delete Action:</b><br>
      • Click the Delete button.<br>
      • If a confirmation dialog appears due to linked test cases, choose Yes to proceed (and delete both the connection and linked test cases) or Cancel to abort.<br>
      • For connections with no test cases, deletion happens immediately after confirmation.</li><br>

  <li><b>Post-Deletion Behavior:</b><br>
      • The connection and any associated test cases (if previously warned) will be permanently removed from the system.<br>
      • The connection list/table refreshes, removing the deleted entry.</li>
</ol><br>

<b>Best Practices</b>
<ul>
  <li><b>Confirm selection:</b> Always double-check the connection name and user before deletion—especially when acting as admin on other users’ connections.</li>
  <li><b>Review test case associations:</b> Avoid deleting connections still supporting important validation jobs unless you are certain those test cases are no longer needed.</li>
  <li><b>Routine clean-up:</b> Periodically review and delete outdated connections to maintain a tidy working environment and reduce the risk of using expired integrations.</li>
  <li><b>Document deletions:</b> For environments where audit trails matter, make note of deletion actions for compliance.</li>
</ul><br>

<b>Security Note:</b><br>
Only users with appropriate permissions (typically admins) can see and act upon all connections. Regular users may only delete their own. 
All deletes are logged for accountability.<br><br>

<i>Use the Delete Connection feature to keep your INFOFISCUS CDWTA workspace organized, secure, and optimized for efficient, error-free data validation operations.</i>
"""
}

        
}