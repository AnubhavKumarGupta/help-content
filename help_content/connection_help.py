# help_content/connection_help.py

def get_connection_content():
    """Connection management help content - focused only on connection operations"""
    return {
        "Connection": {
            "title": "Database Connection Management",
            "description": """
<b>Manage Database Connections for Data Validation</b>

This section provides comprehensive tools for managing database connections across your organization.

<b>Key Features:</b>
• <b>Multi-Database Support:</b> Connect to 10+ database types
• <b>Connection Testing:</b> Verify connectivity before saving
• <b>Secure Storage:</b> Encrypted credential management
• <b>Connection Pooling:</b> Optimized performance for multiple tests

<b>Available Operations:</b>
• <b>Create Connection:</b> Set up new database connections
• <b>Edit Connection:</b> Modify existing connection parameters
• <b>Delete Connection:</b> Remove unused connections
• <b>Test Connection:</b> Validate connection parameters

<b>Supported Database Types:</b>
• Traditional: Oracle, SQL Server, MySQL, PostgreSQL
• Cloud: Snowflake, Google BigQuery, Amazon RedShift
• Modern: StarRocks, Databricks, Azure Synapse

<b>Security Features:</b>
• Password encryption at rest
• Connection string obfuscation
• Role-based access control
• Audit logging for all operations

Select a specific database type from the submenu to see detailed connection instructions and requirements.
            """,
        },

        "Create Connection": {
            "title": "Create New Database Connection",
            "description": """
<b>Set Up New Database Connection</b>

Create secure, reliable connections to your data sources for validation testing.

<b>Setup Process:</b>
1. <b>Select Database Type:</b> Choose from supported database platforms
2. <b>Enter Connection Details:</b> Provide server, port, credentials
3. <b>Test Connection:</b> Verify connectivity before saving
4. <b>Save Configuration:</b> Store encrypted connection details

<b>Required Information:</b>
• <b>Connection Name:</b> Unique identifier for this connection
• <b>Server/Host:</b> Database server address or hostname
• <b>Port:</b> Database service port (auto-filled for common types)
• <b>Database/Schema:</b> Target database or schema name
• <b>Credentials:</b> Username and password (encrypted storage)

<b>Best Practices:</b>
• Use descriptive connection names (e.g., "PROD_HR_Oracle")
• Create separate connections for different environments
• Test connections before creating validation test cases
• Use service accounts with minimal required permissions

<b>Advanced Options:</b>
• Connection timeout settings
• SSL/TLS encryption options
• Connection pooling parameters
• Custom connection string modifications

Choose your database type from the Database submenu to see platform-specific setup instructions.
            """,
        },

# ----------------------            Edit Connection              --------------------------  


"Edit Connection": {
    "title": "Edit Database Connection",
    "description": """
<b>Edit Database Connection – Help Guide</b><br><br>

<b>Overview</b><br>
The Edit Database section allows you to update and maintain your existing database connections as your data infrastructure evolves. 
Instead of creating a new connection each time the underlying database changes (such as after new tables are added, schema is updated, 
or credentials are refreshed), you can efficiently update the current connection configuration here—ensuring a seamless workflow and 
avoiding unnecessary duplication.<br><br>

<b>Why Edit Database is Important</b><br>
• <b>Avoid Unnecessary Duplication:</b> When changes happen in your source database (new tables/views, schema alterations, etc.), 
editing your connection ensures the latest structure is reflected without having to create a new connection from scratch.<br>
• <b>Preserve Test Case Associations:</b> Existing test cases and validation jobs linked to this connection continue to work – 
there’s no need to reconfigure or relink them.<br>
• <b>Streamlined Maintenance:</b> Editing an existing connection is quicker, reduces potential errors, and helps maintain a clean 
connection list.<br>
• <b>Data Consistency:</b> Keeping the same connection, but refreshing its metadata, ensures consistent access control, naming, and 
configuration history.<br>
• <b>Efficient Change Management:</b> Whether you change connection credentials, update hosts/ports, or refresh schemas, 
Edit Database keeps transitions smooth and auditable.<br><br>

<b>When Should You Use Edit Database?</b><br>
• New tables or views have been added or removed in the database.<br>
• Schema changes such as new columns, changed datatypes, or renamed tables.<br>
• Database user credentials or authentication methods have changed.<br>
• You need to update performance-related parameters (timeout, pooling, etc.).<br>
• Server or database endpoints have migrated or changed (for example, after cloud migration).<br>
• Periodic reconnection to refresh catalog information or re-validate connectivity.<br><br>

<b>How It Works</b><br>
1. Select the connection you wish to edit from your list of existing connections.<br>
2. In Edit Database, the connection details form pre-fills with current values.<br>
3. Make the required changes, such as correcting credentials, updating host/port, or simply clicking Test and Save to automatically 
   refresh and reload the metadata (including fetching any new tables or structure changes from the source database).<br>
4. The system updates the connection and its metadata, ensuring all linked test cases use the newly updated schema or data without interruption.<br>
5. Security is enforced throughout: all password and sensitive field changes are properly secured, and a modification audit trail is recorded.<br>
6. Finally, the system validates that all updates are compatible before saving – preventing accidental misconfiguration.<br><br>

<b>Benefits</b><br>
• Up-to-date on all schema/structure changes without new setup.<br>
• Efficient troubleshooting and maintenance (no renaming or duplicated connections).<br>
• Centralized auditing and tracking of all configuration changes.<br>
• Fast onboarding of evolving data architecture (especially in dynamic or agile teams).
    """,
},






        "Edit Database": {
            "title": "Edit Database Connection Parameters",
            "description": """
<b>Modify Database-Specific Connection Settings</b>

Update database connection parameters with platform-specific optimizations.

<b>Database-Specific Parameters:</b>
• <b>Connection String:</b> Platform-specific connection formats
• <b>Driver Settings:</b> Database driver configurations
• <b>Performance Tuning:</b> Query timeout and pooling settings
• <b>Security Options:</b> Encryption and authentication methods

<b>Supported Modifications:</b>
• <b>Server Details:</b> Hostname, port, instance names
• <b>Database Selection:</b> Target databases and schemas
• <b>Authentication:</b> Credential updates and auth method changes
• <b>Advanced Options:</b> SSL settings, connection pooling

<b>Platform-Specific Settings:</b>
• <b>Oracle:</b> TNS names, wallet configurations, RAC settings
• <b>SQL Server:</b> Instance names, authentication modes, encryption
• <b>Cloud Databases:</b> Region settings, service accounts, API keys
• <b>NoSQL:</b> Cluster configurations, replication settings

<b>Validation Process:</b>
1. Modify connection parameters
2. Test connection with new settings
3. Validate against existing test cases
4. Monitor performance impact
5. Document changes for audit trail

<b>Best Practices:</b>
• Test changes in non-production environments first
• Maintain backup of working configurations
• Document all parameter changes
• Monitor performance after modifications
            """,
        },

# ----------------------------            Connection -> Delete Connection          ----------------

"Delete Connection": {
    "title": "Delete Database Connection",
    "description": """
<b>Delete Connection – Help Guide</b><br><br>

<b>Overview</b><br>
The Delete Connection feature enables users (especially admins) to efficiently remove obsolete, duplicate, or invalid database connections from 
the <b>INFOFISCUS Data Validation Tool</b>. Streamlining your connection list improves clarity, reduces clutter, and helps prevent confusion 
or errors during test case management.<br><br>

<b>Why Delete Connections? (Use Cases & Benefits)</b><br>
• <b>Maintain a Clean UI:</b> Deleting old or unused connections keeps your connection list easy to navigate—avoiding visual clutter, confusion, 
and accidental use of incorrect connections.<br>
• <b>Remove Invalid or Expired Connections:</b> Connections with expired, rotated, or invalid credentials can be safely deleted to prevent failures 
in future data validation tasks.<br>
• <b>Reduce Duplicates:</b> Eliminates redundant (e.g., similarly named) connections, making it easier to find and select the correct and current 
integration for your workflows.<br>
• <b>Security Best Practice:</b> Removing connections that are no longer needed reduces the surface area for potential security risks.<br>
• <b>Audit and Organization:</b> Supports better audit control, as only actively used connections remain visible and manageable.<br><br>

<b>How to Delete a Connection – Step-by-Step Instructions</b><br>
1. <b>Access the Delete Connection Panel:</b><br>
   • Click on Delete Connection in the main sidebar.<br>
   • A list view/table will load, showing all available connections with details like name, database type, user, creation date, and test case count.<br><br>

2. <b>Admin User Filtering & Search:</b><br>
   • If you’re an admin, you’ll see all connections, including those created by other users.<br>
   • Use the user dropdown at the top to filter connections by a particular user—making it easy to manage connections per user.<br>
   • Optionally, use the dedicated search bar to instantly find a connection by name, user, or database type.<br><br>

3. <b>Select Connection(s) to Delete:</b><br>
   • In the list, select the radio button next to the connection you wish to delete.<br>
   • Carefully review the details—especially if multiple connections have similar names.<br><br>

4. <b>Test Case Warning (If Applicable):</b><br>
   • If the selected connection is currently linked to any test cases, a confirmation dialog will appear, summarizing the linked test case names or IDs.<br>
   • The system warns: "X test case(s) are linked to this connection. Deleting it will also delete all associated test cases."<br>
   • Review this carefully: If you delete the connection, all linked test cases will be removed as well.<br><br>

5. <b>Delete Action:</b><br>
   • Click the Delete button.<br>
   • If a confirmation dialog appears due to linked test cases, choose Yes to proceed (and delete both the connection and linked test cases) or Cancel to abort.<br>
   • For connections with no test cases, deletion happens immediately after confirmation.<br><br>

6. <b>Post-Deletion Behavior:</b><br>
   • The connection and any associated test cases (if previously warned) will be permanently removed from the system.<br>
   • The connection list/table refreshes, removing the deleted entry.<br><br>

<b>Best Practices</b><br>
• <b>Confirm selection:</b> Always double-check the connection name and user before deletion—especially when acting as admin on other users’ connections.<br>
• <b>Review test case associations:</b> Avoid deleting connections still supporting important validation jobs unless you are certain those test cases are no longer needed.<br>
• <b>Routine clean-up:</b> Periodically review and delete outdated connections to maintain a tidy working environment and reduce the risk of using expired integrations.<br>
• <b>Document deletions:</b> For environments where audit trails matter, make note of deletion actions for compliance.<br><br>

<b>Security Note:</b><br>
Only users with appropriate permissions (typically admins) can see and act upon all connections. Regular users may only delete their own. 
All deletes are logged for accountability.<br><br>

<i>Use the Delete Connection feature to keep your INFOFISCUS workspace organized, secure, and optimized for efficient, error-free data validation operations.</i>
"""
},


        
    }