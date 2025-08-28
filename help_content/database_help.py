# help_content/database_help.py

def get_database_content():
    """Database-specific help content for all supported database types"""
    return {
        "Database": {
            "title": "Database Platform Selection",
            "description": """
<b>Choose Your Database Platform</b>

Select the appropriate database type to create optimized connections with platform-specific configurations.

<b>Enterprise Databases:</b>
• <b>Oracle:</b> Enterprise-grade relational database
• <b>SQL Server:</b> Microsoft's flagship database platform
• <b>PostgreSQL:</b> Advanced open-source relational database

<b>Cloud Platforms:</b>
• <b>Snowflake:</b> Cloud data warehouse platform
• <b>Google BigQuery:</b> Serverless data warehouse
• <b>Amazon RedShift:</b> AWS cloud data warehouse
• <b>Azure Synapse:</b> Microsoft's analytics platform

<b>Modern Platforms:</b>
• <b>Databricks:</b> Unified analytics platform
• <b>StarRocks:</b> High-performance analytical database
• <b>MySQL:</b> Popular open-source database

<b>Platform-Specific Features:</b>
Each database type has customized:
• Connection parameter validation
• Performance optimization settings
• Security configuration options
• Data type mapping for test cases

<b>Selection Guide:</b>
• <b>On-Premise:</b> Oracle, SQL Server, PostgreSQL, MySQL
• <b>Cloud-Native:</b> BigQuery, RedShift, Synapse
• <b>Analytics:</b> Snowflake, Databricks, StarRocks
• <b>Hybrid:</b> PostgreSQL, SQL Server (cloud versions available)

Click on your specific database type to see detailed connection setup instructions and requirements.
            """
        },

# -----------------------------------    Oracle Connection     --------------------------------

        "Oracle": {
            "title": "Oracle Database Connection",
            "description": """
<b>Oracle Database Connection - Help Guide</b><br><br>

This module enables seamless and secure integration with <b>Oracle Databases</b> for 
<b>data validation, reporting, and analysis</b> within the INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> on the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>Oracle</b> from the list of available databases.<br><br>

<b>Required Fields (UI Reference):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field Name</th>
<th style="padding:8px; border:1px solid #334155;">Description</th>
<th style="padding:8px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Unique name for this connection. Duplicate names are not allowed.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">Oracle account username for authentication.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">Account password (hidden, with option to show).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Host</td><td style="padding:6px; border:1px solid #334155;">Hostname or IP address of the Oracle DB server (e.g., db.example.com).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">Database server port (default: 1521).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">Database name or SID of the Oracle instance.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">Schema name to access Oracle tables.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Service Name</td><td style="padding:6px; border:1px solid #334155;">Oracle Service Name (used for RAC or multi-tenant setups).</td><td style="padding:6px; border:1px solid #334155;">No</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
1. <b>Enter Connection Name:</b> Example → Finance_Oracle_Prod_2025.<br>
2. <b>Fill Credentials:</b> Enter Username, Password, Host, Port, Database, Schema, Service Name (if applicable).<br>
3. <b>Test Connection:</b> Click <b>Test</b> to verify. If it fails, check inputs or contact DBA.<br>
4. <b>Save:</b> Once successful, click <b>Save</b> to register the connection.<br><br>

<b>Best Practices:</b><br>
• Always use descriptive, unique connection names.<br>
• Do not reuse connection names across environments.<br>
• Use individual credentials for accountability.<br>
• Keep passwords secure and update them regularly.<br><br>

<b>Troubleshooting Tips:</b><br>
• <b>Duplicate Name:</b> Change the connection name.<br>
• <b>Auth Errors:</b> Verify credentials and privileges.<br>
• <b>Network Issues:</b> Confirm host/port with IT.<br>
• <b>Schema/Service Name Issues:</b> Ensure they are valid in RAC/multi-tenant setups.<br><br>

<b>Example:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field</th>
<th style="padding:8px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Oracle_Prod_FIN2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">finance_user</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Host</td><td style="padding:6px; border:1px solid #334155;">oracle-db.company.com</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">1521</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">FINANCE</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">FIN_DATA</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Service Name</td><td style="padding:6px; border:1px solid #334155;">prod_fin_srv</td></tr>
</table><br>

<b>Advanced Tips:</b><br>
• Use TNS strings or VPN if required (consult DBA).<br>
• For multiple schemas, create separate connections.<br><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks passwords and enforces unique names for secure Oracle configurations.<br><br>

<i>Use this help section to set up, test, and manage Oracle connections efficiently and securely.</i>
            """
        },


# ----------------------------------        SQL Server        ------------------------------

        "SQL Server": {
            "title": "SQL Server Database Connection",
            "description": """
<b>SQL Server Database Connection - Help Guide </b><br><br>

<b>Overview</b><br>
The SQL Server Database Connection module enables seamless and secure integration with 
<b>Microsoft SQL Server</b> databases for data validation, reporting, and analytics within the 
INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> on the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>SQL Server</b> from the list of available databases.<br><br>

<b>Required Fields:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field Name</th><th>Description</th><th>Required</th></tr>
<tr><td>Connection Name</td><td>A unique name for this SQL Server connection. Each new connection must have a distinct name; duplicates are not allowed.</td><td>Yes</td></tr>
<tr><td>Username</td><td>SQL Server account username for authentication.</td><td>Yes</td></tr>
<tr><td>Password</td><td>Account password. Click “Show Password” to view as you type.</td><td>Yes</td></tr>
<tr><td>Server</td><td>Hostname, IP address, or named instance of the SQL Server (e.g., sql.company.com).</td><td>Yes</td></tr>
<tr><td>Database</td><td>Name of the target SQL Server database.</td><td>Yes</td></tr>
<tr><td>Schema</td><td>Database schema to access tables within your SQL Server database.</td><td>Yes</td></tr>
<tr><td>Port</td><td>SQL Server port (default: 1433).</td><td>Yes</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
1. <b>Enter a Unique Connection Name</b><br>
&nbsp;&nbsp;• Every connection requires a distinct name (e.g., Finance_SQL_Prod_2025 or HR_SQL_Dev).<br>
&nbsp;&nbsp;• If a name already exists, you will be prompted to enter a different, unique name.<br><br>

2. <b>Fill Out Credentials</b><br>
&nbsp;&nbsp;• Provide Username, Password, Server, Database, Schema, and Port.<br><br>

3. <b>Test the Connection</b><br>
&nbsp;&nbsp;• Click <b>Test</b> to verify connectivity and credentials.<br>
&nbsp;&nbsp;• If testing fails, review your inputs or consult your database administrator.<br><br>

4. <b>Save the Connection</b><br>
&nbsp;&nbsp;• Once the test is successful, click <b>Save</b> to register your connection.<br><br>

<b>Best Practices:</b><br>
• Always use descriptive and unique connection names for each entry.<br>
• Do not reuse connection names between different environments or databases.<br>
• Use individual user credentials to ensure accountability and easy troubleshooting.<br>
• Never share passwords or credentials; keep them secure.<br>
• Regularly update passwords and review permissions as organizational policies evolve.<br><br>

<b>Troubleshooting Tips:</b><br>
• <b>Duplicate Connection Name:</b> Edit the connection name to ensure uniqueness.<br>
• <b>Authentication Errors:</b> Verify username, password, and ensure the account has sufficient privileges.<br>
• <b>Network Errors:</b> Confirm server and port details with your IT or database administrator.<br>
• <b>Schema Issues:</b> Ensure schema exists and the user has access rights.<br><br>

<b>Example:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field</th><th>Example Value</th></tr>
<tr><td>Connection Name</td><td>SQL_HR_Production2025</td></tr>
<tr><td>Username</td><td>hr_user</td></tr>
<tr><td>Password</td><td>****</td></tr>
<tr><td>Server</td><td>sqlserver01.company.com</td></tr>
<tr><td>Database</td><td>HR</td></tr>
<tr><td>Schema</td><td>dbo</td></tr>
<tr><td>Port</td><td>1433</td></tr>
</table><br>

<b>Advanced Tips:</b><br>
• For advanced configurations, such as Windows Authentication, named instances, SSL/TLS, or high-availability setups (AlwaysOn), consult your DBA or official SQL Server documentation.<br>
• If multiple schemas need to be accessed, set up separate connections or request necessary privileges.<br><br>

<b>Security Reminder:</b><br>
The INFOFISCUS Data Validation Tool masks your password on entry and enforces unique connection naming for every new database configuration, following enterprise security best practices.<br><br>

<i>Utilize this help section to successfully set up, test, and manage SQL Server database connections efficiently and securely.</i>
            """
        },


# ----------------------------------          MySQL           ----------------------------- 


        "MySQL": {
            "title": "MySQL Database Connection",
            "description": """
<b>MySQL Database Connection - Help Guide</b><br><br>

<b>Overview</b><br>
The MySQL Database Connection module allows secure integration with 
<b>MySQL databases</b> for data validation, reporting, and analytics using the 
INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> on the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>MySQL</b> from the list of available databases.<br><br>

<b>Required Fields:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field Name</th><th>Description</th><th>Required</th></tr>
<tr><td>Connection Name</td><td>A unique name for this MySQL connection. Each new connection must have a distinct name; duplicates are not allowed.</td><td>Yes</td></tr>
<tr><td>Username</td><td>MySQL database account username for authentication.</td><td>Yes</td></tr>
<tr><td>Password</td><td>Account password. Click “Show Password” to view as you type.</td><td>Yes</td></tr>
<tr><td>Host</td><td>Hostname or IP address of the MySQL server (e.g., mysql.example.com).</td><td>Yes</td></tr>
<tr><td>Port</td><td>MySQL server port (default: 3306).</td><td>Yes</td></tr>
<tr><td>Database</td><td>Name of the target MySQL database.</td><td>Yes</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
1. <b>Enter a Unique Connection Name</b><br>
&nbsp;&nbsp;• Every connection requires a distinct name (e.g., Sales_MySQL_Prod_2025 or Dev_MySQL_Test).<br>
&nbsp;&nbsp;• If a name already exists, you will be prompted to enter a different, unique name.<br><br>

2. <b>Fill Out Credentials</b><br>
&nbsp;&nbsp;• Provide Username, Password, Host, Port, and Database.<br><br>

3. <b>Test the Connection</b><br>
&nbsp;&nbsp;• Click <b>Test</b> to verify connectivity and credentials.<br>
&nbsp;&nbsp;• If testing fails, review your inputs or consult your database administrator.<br><br>

4. <b>Save the Connection</b><br>
&nbsp;&nbsp;• Once the test is successful, click <b>Save</b> to register your connection.<br><br>

<b>Best Practices:</b><br>
• Always use descriptive and unique connection names for each entry.<br>
• Do not reuse connection names between different environments or databases.<br>
• Use individual user credentials to ensure accountability.<br>
• Never share passwords or credentials; keep them secure.<br>
• Regularly update passwords and review permissions as organizational policies evolve.<br><br>

<b>Troubleshooting Tips:</b><br>
• <b>Duplicate Connection Name:</b> Edit the connection name to ensure uniqueness.<br>
• <b>Authentication Errors:</b> Verify username, password, and ensure the account has sufficient privileges.<br>
• <b>Network Errors:</b> Confirm host and port details with your IT or database administrator.<br>
• <b>Database Access Issues:</b> Ensure the specified database exists and the user has access rights.<br><br>

<b>Example:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field</th><th>Example Value</th></tr>
<tr><td>Connection Name</td><td>Sales_MySQL_Prod2025</td></tr>
<tr><td>Username</td><td>sales_user</td></tr>
<tr><td>Password</td><td>****</td></tr>
<tr><td>Host</td><td>mysql-db.company.com</td></tr>
<tr><td>Port</td><td>3306</td></tr>
<tr><td>Database</td><td>SALES</td></tr>
</table><br>

<b>Advanced Tips:</b><br>
• For advanced configurations such as SSL setup, custom ports, or specific storage engines, consult your DBA or official MySQL documentation.<br>
• If connections to multiple databases or with different privileges are needed, set up separate connections with unique names.<br><br>

<b>Security Reminder:</b><br>
The INFOFISCUS Data Validation Tool masks your password on entry and enforces unique connection naming for every new database configuration, following enterprise security best practices.<br><br>

<i>Utilize this help section to successfully set up, test, and manage MySQL database connections efficiently and securely.</i>
            """
        },


# ----------------------------------        PostgreSQL         ---------------------------------

        "PostgreSQL": {
            "title": "PostgreSQL Database Connection",
            "description": """
<b>PostgreSQL Database Connection - Help Guide</b><br><br>

<b>Overview</b><br>
The PostgreSQL Database Connection module allows secure integration with 
<b>PostgreSQL databases</b> for data validation, reporting, and analytics in the 
INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> on the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>PostgreSQL</b> from the list of available databases.<br><br>

<b>Required Fields:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field Name</th><th>Description</th><th>Required</th></tr>
<tr><td>Connection Name</td><td>A unique name for this PostgreSQL connection. Each new connection must have a distinct name; duplicates are not allowed.</td><td>Yes</td></tr>
<tr><td>Username</td><td>PostgreSQL database account username for authentication.</td><td>Yes</td></tr>
<tr><td>Password</td><td>Account password. Click “Show Password” to view as you type.</td><td>Yes</td></tr>
<tr><td>Host</td><td>Hostname or IP address of the PostgreSQL server (e.g., postgres.example.com).</td><td>Yes</td></tr>
<tr><td>Port</td><td>PostgreSQL server port (default: 5432).</td><td>Yes</td></tr>
<tr><td>Database</td><td>Name of the target PostgreSQL database.</td><td>Yes</td></tr>
<tr><td>Schema</td><td>Database schema to access tables within your PostgreSQL database.</td><td>Yes</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
1. <b>Enter a Unique Connection Name</b><br>
&nbsp;&nbsp;• Every connection requires a distinct name (e.g., Analytics_PG_Prod_2025 or Dev_PG_Test).<br>
&nbsp;&nbsp;• If a name already exists, you will be prompted to enter a different, unique name.<br><br>

2. <b>Fill Out Credentials</b><br>
&nbsp;&nbsp;• Provide Username, Password, Host, Port, Database, and Schema.<br><br>

3. <b>Test the Connection</b><br>
&nbsp;&nbsp;• Click <b>Test</b> to verify connectivity and credentials.<br>
&nbsp;&nbsp;• If testing fails, review your inputs or consult your database administrator.<br><br>

4. <b>Save the Connection</b><br>
&nbsp;&nbsp;• Once the test is successful, click <b>Save</b> to register your connection.<br><br>

<b>Best Practices:</b><br>
• Always use descriptive and unique connection names for each entry.<br>
• Do not reuse connection names between different environments or databases.<br>
• Use individual user credentials for accountability.<br>
• Never share passwords or credentials; keep them secure.<br>
• Regularly update passwords and review permissions as organizational policies evolve.<br><br>

<b>Troubleshooting Tips:</b><br>
• <b>Duplicate Connection Name:</b> Edit the connection name to ensure uniqueness.<br>
• <b>Authentication Errors:</b> Verify username, password, and ensure the account has sufficient privileges.<br>
• <b>Network Errors:</b> Confirm host and port details with your IT or database administrator.<br>
• <b>Database or Schema Issues:</b> Ensure the specified database and schema exist, and the user has access rights.<br><br>

<b>Example:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field</th><th>Example Value</th></tr>
<tr><td>Connection Name</td><td>Analytics_PG_Prod2025</td></tr>
<tr><td>Username</td><td>analytics_user</td></tr>
<tr><td>Password</td><td>****</td></tr>
<tr><td>Host</td><td>postgres-db.company.com</td></tr>
<tr><td>Port</td><td>5432</td></tr>
<tr><td>Database</td><td>ANALYTICS</td></tr>
<tr><td>Schema</td><td>public</td></tr>
</table><br>

<b>Advanced Tips:</b><br>
• For configurations involving custom ports, SSL, or advanced security (LDAP, Kerberos), consult your DBA or official PostgreSQL documentation.<br>
• To access multiple schemas or roles, set up separate connections, each with a unique name.<br><br>

<b>Security Reminder:</b><br>
The INFOFISCUS Data Validation Tool masks your password on entry and enforces unique connection naming for every new database configuration in accordance with enterprise security best practices.<br><br>

<i>Utilize this help section to efficiently and securely set up, test, and manage PostgreSQL database connections.</i>
            """
        },


# ----------------------------------         Snowflake        -----------------------------------

        "Snowflake": {
            "title": "Snowflake Data Warehouse Connection",
            "description": """
<b>Snowflake Database Connection - Help Guide</b><br><br>

<b>Overview</b><br>
The Snowflake Database Connection module enables secure integration with 
<b>Snowflake’s cloud data platform</b> for large-scale data validation, analytics, 
and reporting within the INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> on the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>Snowflake</b> from the list of available databases.<br><br>

<b>Required Fields:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field Name</th><th>Description</th><th>Required</th></tr>
<tr><td>Connection Name</td><td>A unique name for this Snowflake connection. Each new connection must have a distinct name; duplicates are not allowed.</td><td>Yes</td></tr>
<tr><td>Username</td><td>Snowflake account username for authentication.</td><td>Yes</td></tr>
<tr><td>Password</td><td>Account password. Click “Show Password” to view as you type.</td><td>Yes</td></tr>
<tr><td>Account ID</td><td>The unique Snowflake account identifier (e.g., ab12345.us-east-1).</td><td>Yes</td></tr>
<tr><td>Warehouse</td><td>Name of the compute warehouse to use for query execution.</td><td>Yes</td></tr>
<tr><td>Database</td><td>Target Snowflake database name.</td><td>Yes</td></tr>
<tr><td>Schema</td><td>Database schema to access tables within Snowflake.</td><td>Yes</td></tr>
<tr><td>Role</td><td>Role to use for permissions and access control.</td><td>No</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
1. <b>Enter a Unique Connection Name</b><br>
&nbsp;&nbsp;• Every connection requires a distinct name (e.g., Analytics_Snowflake_Prod_2025 or Sales_SF_Dev).<br>
&nbsp;&nbsp;• If a name already exists, you will be prompted to enter a different, unique name.<br><br>

2. <b>Fill Out Credentials</b><br>
&nbsp;&nbsp;• Provide Username, Password, Account ID, Warehouse, Database, Schema, and Role (if required).<br><br>

3. <b>Test the Connection</b><br>
&nbsp;&nbsp;• Click <b>Test</b> to verify connectivity and credentials.<br>
&nbsp;&nbsp;• If testing fails, review your inputs or consult your Snowflake administrator.<br><br>

4. <b>Save the Connection</b><br>
&nbsp;&nbsp;• Once the test is successful, click <b>Save</b> to register your connection.<br><br>

<b>Best Practices:</b><br>
• Always use descriptive and unique connection names for each entry.<br>
• Do not reuse connection names between different environments (production, development, QA).<br>
• Choose a warehouse appropriate to your workload and data volume.<br>
• Use individual roles to ensure proper access control and auditing.<br>
• Never share passwords or credentials; keep them secure.<br>
• Regularly update passwords and review permissions as organizational policies evolve.<br><br>

<b>Troubleshooting Tips:</b><br>
• <b>Duplicate Connection Name:</b> Edit the connection name to ensure uniqueness.<br>
• <b>Authentication Errors:</b> Verify username/password, account ID, and ensure the user has the required role and privileges.<br>
• <b>Warehouse or Database Issues:</b> Ensure the specified warehouse and database exist and your user has access rights.<br>
• <b>Network Errors:</b> Ensure access to Snowflake over the Internet (required for cloud connectivity); check with IT if issues persist.<br><br>

<b>Example:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field</th><th>Example Value</th></tr>
<tr><td>Connection Name</td><td>Analytics_Snowflake_Prod2025</td></tr>
<tr><td>Username</td><td>analytics_user</td></tr>
<tr><td>Password</td><td>****</td></tr>
<tr><td>Account ID</td><td>ab12345.us-east-1</td></tr>
<tr><td>Warehouse</td><td>ANALYTICS_WH</td></tr>
<tr><td>Database</td><td>SALES_DB</td></tr>
<tr><td>Schema</td><td>PUBLIC</td></tr>
<tr><td>Role</td><td>ANALYST</td></tr>
</table><br>

<b>Advanced Tips:</b><br>
• For advanced authentication (key pair, MFA, SSO), refer to Snowflake’s official documentation or consult your admin.<br>
• Optimize warehouse size and scaling for performance and cost efficiency.<br>
• Use the appropriate role for least-privilege access and audit compliance.<br>
• Explore features like Time Travel (query previous data states), Secure Views, and Zero-Copy Cloning for advanced analytics and compliance.<br><br>

<b>Security Reminder:</b><br>
The INFOFISCUS Data Validation Tool masks your password on entry and enforces unique connection naming for every new database configuration, following enterprise security best practices.<br>
Warehouse and role selection help control cost and security.<br><br>

<i>Utilize this help section to efficiently and securely set up, test, and manage Snowflake database connections for scalable cloud analytics.</i>
            """
        },



# ---------------------------    Starrocks  ---------------------------- 


        "StarRocks": {
            "title": "StarRocks Database Connection",
            "description": """
<b>Connect to StarRocks Analytical Database</b>

Configure connections to StarRocks for high-performance analytical data validation.

<b>StarRocks Connection Parameters:</b>
• <b>Host:</b> StarRocks Frontend (FE) server address
• <b>Port:</b> Usually 9030 (default query port)
• <b>Database:</b> Target database name
• <b>Username:</b> StarRocks user account
• <b>Password:</b> User authentication password

<b>Connection String Format:</b>
<code>starrocks://username:password@hostname:port/database</code>

<b>StarRocks Features:</b>
• <b>Vectorized Execution:</b> High-performance query processing
• <b>Columnar Storage:</b> Optimized for analytical workloads
• <b>Real-time Analytics:</b> Sub-second query response times
• <b>Auto Materialization:</b> Intelligent materialized view management

<b>Performance Capabilities:</b>
• <b>MPP Architecture:</b> Massively parallel processing
• <b>Intelligent Indexing:</b> Automatic index optimization
• <b>Cost-Based Optimizer:</b> Advanced query optimization
• <b>Stream Processing:</b> Real-time data ingestion and validation

<b>Data Types Support:</b>
• Complex data types (JSON, Array, Map)
• Time series data optimization
• Geospatial data validation
• Large object handling

<b>Validation Features:</b>
StarRocks excels at large-scale analytical validation with features optimized for big data scenarios, real-time streaming validation, and complex analytical queries.
            """
        },


# ----------------------------------    Google BigQuery  -----------------------



        "Google BigQuery": {
            "title": "Google BigQuery Connection",
            "description": """
<b>Connect to Google BigQuery</b>

Set up connections to Google Cloud's serverless data warehouse for scalable data validation.

<b>BigQuery Connection Requirements:</b>
• <b>Project ID:</b> Google Cloud project identifier
• <b>Dataset:</b> Target dataset name (optional)
• <b>Authentication:</b> Service account or OAuth credentials
• <b>Location:</b> Data location/region (optional)

<b>Authentication Methods:</b>
• <b>Service Account:</b> JSON key file authentication
• <b>OAuth 2.0:</b> User credentials with browser authentication
• <b>Application Default:</b> Google Cloud SDK default credentials

<b>BigQuery Features:</b>
• <b>Serverless Architecture:</b> No infrastructure management required
• <b>Automatic Scaling:</b> Handles massive datasets automatically
• <b>Standard SQL:</b> ANSI SQL support with extensions
• <b>Streaming Inserts:</b> Real-time data ingestion capabilities

<b>Performance Advantages:</b>
• <b>Columnar Storage:</b> Optimized for analytical queries
• <b>Automatic Partitioning:</b> Time and range-based partitioning
• <b>Clustered Tables:</b> Improved query performance
• <b>Materialized Views:</b> Pre-computed query results

<b>Security & Compliance:</b>
• IAM-based access control
• Column-level and row-level security
• Data encryption at rest and in transit
• Audit logging and monitoring

<b>Advanced Capabilities:</b>
BigQuery enables validation of petabyte-scale datasets with machine learning integration, geospatial analysis, and real-time streaming data validation.
            """
        },




# ---------------------------------------   Amazon Redshift   ---------------------------

        "Amazon Redshift": {
            "title": "Amazon Redshift Connection",
            "description": """
<b>Amazon Redshift Database Connection - Help Guide</b><br><br>

<b>Overview</b><br>
The Amazon Redshift connection module enables secure integration with 
<b>AWS’s cloud data warehouse</b> for high-performance analytics, reporting, 
and data validation in the INFOFISCUS Data Validation Tool.<br><br>
Connections can be:<br>
• <b>Standard (without TARGET):</b> Direct Redshift connection.<br>
• <b>With TARGET:</b> Includes Amazon S3 credentials for import/export and external data operations.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> on the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>Amazon Redshift</b> from the list.<br><br>

<b>Required Fields:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th colspan="3">Standard Redshift Connection (Without TARGET)</th></tr>
<tr><th>Field Name</th><th>Description</th><th>Required</th></tr>
<tr><td>Connection Name</td><td>Unique connection name (duplicates not allowed).</td><td>Yes</td></tr>
<tr><td>Username</td><td>Redshift cluster user for authentication.</td><td>Yes</td></tr>
<tr><td>Password</td><td>User account password (masked in tool).</td><td>Yes</td></tr>
<tr><td>Host</td><td>Redshift cluster endpoint (e.g., redshift-cluster.company.com).</td><td>Yes</td></tr>
<tr><td>Port</td><td>Redshift port (default: 5439).</td><td>Yes</td></tr>
<tr><td>Database</td><td>Target Redshift database name.</td><td>Yes</td></tr>
<tr><td>Schema</td><td>Schema to access tables within Redshift.</td><td>Yes</td></tr>
</table><br>

<table border="1" cellpadding="4" cellspacing="0">
<tr><th colspan="3">Redshift Connection With TARGET (S3 Integration)</th></tr>
<tr><th>Field Name</th><th>Description</th><th>Required</th></tr>
<tr><td>Bucket Name</td><td>S3 bucket for reads/writes (UNLOAD, COPY, data import/export).</td><td>Yes (if target)</td></tr>
<tr><td>Region Name</td><td>AWS region of S3 bucket (e.g., us-east-1).</td><td>Yes (if target)</td></tr>
<tr><td>Folder Path</td><td>S3 folder for files (e.g., exports/2025/).</td><td>Yes (if target)</td></tr>
<tr><td>Access Key Id</td><td>AWS IAM access key with S3 permissions.</td><td>Yes (if target)</td></tr>
<tr><td>Secret Access Key</td><td>Secret key corresponding to the access key ID.</td><td>Yes (if target)</td></tr>
<tr><td>Endpoint Url</td><td>Custom endpoint (for VPC/private S3).</td><td>No</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
<b>Without TARGET:</b><br>
1. Enter a unique <b>Connection Name</b>.<br>
2. Fill Username, Password, Host, Port, Database, Schema.<br>
3. Click <b>Test</b> to validate.<br>
4. If successful, click <b>Save</b>.<br><br>

<b>With TARGET:</b><br>
1. Enable the <b>TARGET</b> option.<br>
2. Provide S3 details (Bucket, Region, Folder, Keys, Endpoint if needed).<br>
3. Click <b>Test</b> – validates both Redshift and S3 credentials.<br>
4. Click <b>Save</b> to register.<br><br>

<b>Why and When to Use TARGET:</b><br>
<b>What are Target Credentials?</b><br>
Target credentials provide access to S3 for reading/writing data. 
They are required for:<br>
• Exporting query results to S3 (<code>UNLOAD</code>)<br>
• Importing large files from S3 into Redshift (<code>COPY</code>)<br>
• Using Redshift Spectrum for external S3-based tables<br><br>

<b>When to Enable TARGET:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Scenario</th><th>Enable TARGET?</th><th>Reason</th></tr>
<tr><td>Run data checks on Redshift tables only</td><td>No</td><td>All data remains inside Redshift.</td></tr>
<tr><td>Export query results to S3</td><td>Yes</td><td>S3 access required to store results.</td></tr>
<tr><td>Import datasets (CSV/Parquet) from S3</td><td>Yes</td><td>Redshift needs credentials to read S3 files.</td></tr>
<tr><td>Use Redshift Spectrum external tables</td><td>Yes</td><td>Data resides on S3.</td></tr>
</table><br>

<b>Example Configurations:</b><br>
<b>Without TARGET:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field</th><th>Example Value</th></tr>
<tr><td>Connection Name</td><td>Prod_RS_Sales_2025</td></tr>
<tr><td>Username</td><td>sales_admin</td></tr>
<tr><td>Password</td><td>****</td></tr>
<tr><td>Host</td><td>rs-cluster.company.com</td></tr>
<tr><td>Port</td><td>5439</td></tr>
<tr><td>Database</td><td>SALES_DB</td></tr>
<tr><td>Schema</td><td>public</td></tr>
</table><br>

<b>With TARGET:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field</th><th>Example Value</th></tr>
<tr><td>Connection Name</td><td>Prod_RS_Export_Target2025</td></tr>
<tr><td>Username</td><td>export_user</td></tr>
<tr><td>Password</td><td>****</td></tr>
<tr><td>Host</td><td>rs-cluster.company.com</td></tr>
<tr><td>Port</td><td>5439</td></tr>
<tr><td>Database</td><td>EXPORTS_DB</td></tr>
<tr><td>Schema</td><td>export_schema</td></tr>
<tr><td>Bucket Name</td><td>rs-data-exports</td></tr>
<tr><td>Region Name</td><td>us-east-1</td></tr>
<tr><td>Folder Path</td><td>exports/yearly/2025</td></tr>
<tr><td>Access Key Id</td><td>AKIAxxxxxxxxxxxxxxx</td></tr>
<tr><td>Secret Access Key</td><td>wJalrxUtnFEMI/.../EXAMPLEKEY</td></tr>
<tr><td>Endpoint Url</td><td>https://s3.us-east-1.amazonaws.com (optional)</td></tr>
</table><br>

<b>Best Practices:</b><br>
• Always use descriptive, unique names for each connection.<br>
• Store AWS keys securely, rotate them regularly.<br>
• Grant S3 access only to needed buckets/folders (least privilege).<br>
• Use IAM roles instead of static keys when possible.<br><br>

<b>Troubleshooting Tips:</b><br>
• <b>Duplicate Connection Name:</b> Edit the name to ensure uniqueness.<br>
• <b>Credential Issues:</b> Verify Redshift + S3 credentials and privileges.<br>
• <b>Network Errors:</b> Check firewall and endpoint access.<br>
• <b>S3 Permission Errors:</b> Ensure correct bucket/folder access rights.<br><br>

<b>Security Reminder:</b><br>
The INFOFISCUS Data Validation Tool masks Redshift and AWS credentials. 
Unique connection naming is enforced for safety. Keys are never stored in plain text. 
Follow enterprise security guidelines, use IAM roles when possible, and rotate credentials regularly.<br><br>

<i>Use this guide to confidently configure both direct Redshift connections 
and advanced S3-integrated workflows at enterprise scale.</i>
            """
        },



# ----------------------------------------    Azure Synapse  --------------------------------

        "Azure Synapse": {
            "title": "Azure Synapse Analytics Connection",
            "description": """
<b>Azure Synapse Analytics Database Connection - Help Guide</b><br><br>

<b>Overview</b><br>
The Azure Synapse Analytics connection module allows seamless, secure integration 
with <b>Microsoft’s cloud analytics platform</b> for enterprise-scale data validation, 
analytics, and reporting in the INFOFISCUS Data Validation Tool.<br><br>
Connections can be configured as:<br>
• <b>Standard (without TARGET):</b> Direct Synapse connection.<br>
• <b>With TARGET:</b> Extended with Azure Blob Storage credentials for data export/import.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> in the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>Azure Synapse</b>.<br><br>

<b>Required Fields:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th colspan="3">Standard Synapse Connection (Without TARGET)</th></tr>
<tr><th>Field Name</th><th>Description</th><th>Required</th></tr>
<tr><td>Connection Name</td><td>Unique identifier for this connection. Duplicates not allowed.</td><td>Yes</td></tr>
<tr><td>Username</td><td>Synapse database user for authentication.</td><td>Yes</td></tr>
<tr><td>Password</td><td>Account password (masked in tool).</td><td>Yes</td></tr>
<tr><td>Server</td><td>Synapse workspace SQL endpoint address.</td><td>Yes</td></tr>
<tr><td>Database</td><td>Target database name in Synapse.</td><td>Yes</td></tr>
<tr><td>Schema</td><td>Database schema to use within Synapse.</td><td>Yes</td></tr>
</table><br>

<table border="1" cellpadding="4" cellspacing="0">
<tr><th colspan="3">Synapse Connection With TARGET (Blob Storage Integration)</th></tr>
<tr><th>Field Name</th><th>Description</th><th>Required</th></tr>
<tr><td>Bucket Name</td><td>Azure Blob container name for exports/imports.</td><td>Yes (if target)</td></tr>
<tr><td>Folder Path</td><td>Path inside the container for your files (e.g., exports/2025/).</td><td>Yes (if target)</td></tr>
<tr><td>Account Key</td><td>Storage account key for Blob access.</td><td>Yes (if target)</td></tr>
<tr><td>Account Url</td><td>Blob Storage endpoint (e.g., https://account.blob.core.windows.net).</td><td>Yes (if target)</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
<b>Without TARGET:</b><br>
1. Enter a unique <b>Connection Name</b> (e.g., Prod_Synapse_Analytics2025).<br>
2. Fill Username, Password, Server, Database, Schema.<br>
3. Click <b>Test</b> to validate.<br>
4. Click <b>Save</b> if successful.<br><br>

<b>With TARGET:</b><br>
1. Enable the <b>TARGET</b> option.<br>
2. Provide Blob Storage details (Bucket, Folder Path, Account Key, Account URL).<br>
3. Click <b>Test</b> – validates Synapse + Blob credentials.<br>
4. Click <b>Save</b> to register.<br><br>

<b>Why and When to Use TARGET:</b><br>
<b>What are Target Credentials?</b><br>
Target credentials allow Synapse to exchange data with Azure Blob containers.<br>
They are required for:<br>
• Exporting query results to Blob (UNLOAD/EXPORT)<br>
• Importing files (CSV/Parquet) from Blob into Synapse<br>
• Using ETL or pipelines that read/write Blob files<br><br>

<b>When to Enable TARGET:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Scenario</th><th>Enable TARGET?</th><th>Reason</th></tr>
<tr><td>Query Synapse tables only</td><td>No</td><td>All work happens inside Synapse.</td></tr>
<tr><td>Export results to Blob</td><td>Yes</td><td>Blob credentials required for export.</td></tr>
<tr><td>Import datasets from Blob</td><td>Yes</td><td>Needed to load files into Synapse.</td></tr>
<tr><td>Integrate ETL pipelines with Blob</td><td>Yes</td><td>Blob access is mandatory.</td></tr>
</table><br>

<b>Example Configurations:</b><br>
<b>Without TARGET:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field</th><th>Example Value</th></tr>
<tr><td>Connection Name</td><td>Prod_Synapse_Analytics2025</td></tr>
<tr><td>Username</td><td>synapse_user</td></tr>
<tr><td>Password</td><td>****</td></tr>
<tr><td>Server</td><td>synapse-workspace.sql.net</td></tr>
<tr><td>Database</td><td>SALES_DB</td></tr>
<tr><td>Schema</td><td>dbo</td></tr>
</table><br>

<b>With TARGET:</b><br>
<table border="1" cellpadding="4" cellspacing="0">
<tr><th>Field</th><th>Example Value</th></tr>
<tr><td>Connection Name</td><td>Prod_Synapse_Export_Target2025</td></tr>
<tr><td>Username</td><td>export_user</td></tr>
<tr><td>Password</td><td>****</td></tr>
<tr><td>Server</td><td>synapse-workspace.sql.net</td></tr>
<tr><td>Database</td><td>EXPORTS_DB</td></tr>
<tr><td>Schema</td><td>export_schema</td></tr>
<tr><td>Bucket Name</td><td>synapse-data-exports</td></tr>
<tr><td>Folder Path</td><td>exports/annual/2025</td></tr>
<tr><td>Account Key</td><td>q5vLgEXAMPLEKEY==</td></tr>
<tr><td>Account Url</td><td>https://myaccount.blob.core.windows.net</td></tr>
</table><br>

<b>Best Practices:</b><br>
• Use descriptive, unique names for each connection.<br>
• Keep Account Keys safe; rotate them often.<br>
• Apply least-privilege access for Blob Storage.<br>
• Use different containers/folders for each project.<br>
• Only enable TARGET when Blob integration is required.<br><br>

<b>Troubleshooting Tips:</b><br>
• <b>Duplicate Name:</b> Change the connection name.<br>
• <b>Credential Errors:</b> Check Synapse + Blob credentials.<br>
• <b>Network/Server Errors:</b> Verify server endpoint.<br>
• <b>Blob Access Errors:</b> Ensure container + folder exist.<br><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks Synapse and Blob credentials. 
Unique names are enforced. 
Always protect keys, apply least-privilege, and rotate credentials regularly.<br><br>

<i>Use this guide to confidently configure Synapse connections with or without 
Azure Blob integration for secure, scalable data validation workflows.</i>
            """
        },


# ---------------------------------------     Databricks     ------------------------------------



        "Databricks": {
            "title": "Databricks Platform Connection",
            "description": """
<b>Connect to Databricks Unified Analytics Platform</b>

Configure connections to Databricks for advanced data validation and analytics.

<b>Databricks Connection Parameters:</b>
• <b>Server Hostname:</b> Databricks workspace URL
• <b>HTTP Path:</b> Cluster or SQL warehouse HTTP path
• <b>Access Token:</b> Personal access token for authentication
• <b>Port:</b> Usually 443 (HTTPS)

<b>Connection String Format:</b>
<code>databricks://token:access_token@hostname:port/database</code>

<b>Authentication Methods:</b>
• <b>Personal Access Token:</b> User-generated token authentication
• <b>OAuth 2.0:</b> Standard OAuth authentication flow
• <b>Azure AD:</b> Azure Active Directory integration (Azure Databricks)
• <b>AWS IAM:</b> Identity and Access Management (AWS Databricks)

<b>Databricks Features:</b>
• <b>Apache Spark:</b> Distributed computing framework
• <b>Delta Lake:</b> ACID transactions and data versioning
• <b>MLflow:</b> Machine learning lifecycle management
• <b>Collaborative Notebooks:</b> Interactive data analysis environment

<b>Performance Capabilities:</b>
• <b>Auto Scaling:</b> Dynamic cluster scaling based on workload
• <b>Optimized Spark:</b> Performance-tuned Apache Spark runtime
• <b>Delta Engine:</b> High-performance query engine
• <b>Photon:</b> Vectorized query engine for SQL workloads

<b>Data Validation Features:</b>
• <b>Schema Evolution:</b> Automatic schema handling and validation
• <b>Time Travel:</b> Historical data validation with versioning
• <b>Data Quality Checks:</b> Built-in data quality monitoring
• <b>Streaming Validation:</b> Real-time data validation capabilities

<b>Advanced Analytics:</b>
Databricks enables sophisticated validation workflows with machine learning integration, real-time streaming validation, and advanced statistical analysis capabilities.
            """
        },


# -----------------------------------      Edit Databases   ---------------------


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
• <b>Analytics Platforms:</b> Warehouse settings, compute configurations

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
            """
        }
    }