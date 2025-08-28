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

        "Edit Connection": {
            "title": "Edit Database Connection",
            "description": """
<b>Modify Existing Database Connections</b>

Update connection parameters while preserving test case associations and historical data.

<b>Editable Parameters:</b>
• <b>Connection Details:</b> Server, port, database name
• <b>Credentials:</b> Username and password updates
• <b>Advanced Settings:</b> Timeouts, encryption, pooling
• <b>Connection Name:</b> Descriptive identifier

<b>Important Considerations:</b>
• <b>Test Case Impact:</b> Existing test cases will use updated connection
• <b>Historical Data:</b> Previous test results remain unchanged
• <b>Validation Required:</b> Connection testing recommended after changes
• <b>Backup Recommended:</b> Export connection settings before major changes

<b>Common Edit Scenarios:</b>
• <b>Password Changes:</b> Update expired or rotated passwords
• <b>Server Migration:</b> Update server addresses after migrations
• <b>Performance Tuning:</b> Adjust timeout and pooling settings
• <b>Security Updates:</b> Enable encryption or change auth methods

<b>Edit Process:</b>
1. Select existing connection from the list
2. Modify required parameters
3. Test updated connection settings
4. Save changes and verify functionality
5. Update any affected test cases if needed

<b>Security During Edits:</b>
• Password changes are immediately encrypted
• Previous passwords are securely overwritten
• All modifications are logged for audit purposes
• Access restricted to authorized users only

<b>Testing After Changes:</b>
• Automatic connection validation available
• Test existing test cases with updated connection
• Performance impact assessment tools
• Rollback capability if issues detected
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

        "Delete Connection": {
            "title": "Delete Database Connection",
            "description": """
<b>Delete Connection - Help Guide</b>

Use this interface to safely delete database connections linked to your client account.

<b>Finding Connections:</b>
• <b>User Filter:</b> Select a user from the dropdown to view their connections
• <b>Search:</b> Quickly find connections by name or attributes
• <b>Connection Table:</b> Displays Client ID, Database Type, User ID, Test Case Count, and Creation Date

<b>Selecting a Connection:</b>
• Choose a connection using the radio button in the table
• This enables deletion and other related actions

<b>Deletion Process:</b>
1. Select the connection you want to delete
2. If test cases are linked, you will be prompted before deletion
3. Confirm deletion to remove all linkages and connection details

<b>Table Features:</b>
• Sort connections using column headers
• Organize and manage records easily

<b>Additional Controls:</b>
• <b>Previous:</b> Navigate to earlier records
• <b>Filter:</b> Apply filters for refined results
• <b>Save:</b> Store filtered or updated views
• <b>Execute:</b> Run related test case workflows

<b>Best Practice:</b>
Regularly review and remove unused connections to maintain system integrity and ensure data accuracy.

<b>Important Warnings:</b>
• Deleted connections cannot be recovered
• All associated test cases will be affected
• Historical test results may lose connection context
• Export connection settings before deletion if needed
            """,
        }
    }