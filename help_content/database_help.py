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

# ---------------------------------         Oracle       --------------------------------

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
• Use individual credentials for accountability.<br> <br>

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


# ----------------------------------      SQL Server      ------------------------------

"SQL Server": {
    "title": "SQL Server Database Connection",
    "description": """
<b>SQL Server Database Connection - Help Guide</b><br><br>

This module enables seamless and secure integration with <b>Microsoft SQL Server</b> databases for 
<b>data validation, reporting, and analytics</b> within the INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> on the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>SQL Server</b> from the list of available databases.<br><br>

<b>Required Fields (UI Reference):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field Name</th>
<th style="padding:8px; border:1px solid #334155;">Description</th>
<th style="padding:8px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Unique name for this SQL Server connection. Duplicate names are not allowed.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">SQL Server account username for authentication.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">Account password (hidden, with option to show).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Server</td><td style="padding:6px; border:1px solid #334155;">Hostname, IP address, or named instance of SQL Server (e.g., sql.company.com).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">Target SQL Server database name.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">Schema to access SQL Server tables.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">SQL Server port (default: 1433).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
1. <b>Enter Connection Name:</b> Example → Finance_SQL_Prod_2025.<br>
2. <b>Fill Credentials:</b> Enter Username, Password, Server, Database, Schema, Port.<br>
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
• <b>Network Issues:</b> Confirm server/port with IT.<br>
• <b>Schema Issues:</b> Ensure schema exists and you have access.<br><br>

<b>Example:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field</th>
<th style="padding:8px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">SQL_HR_Production2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">hr_user</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Server</td><td style="padding:6px; border:1px solid #334155;">sqlserver01.company.com</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">HR</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">dbo</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">1433</td></tr>
</table><br>

<b>Advanced Tips:</b><br>
• Use Windows Authentication, SSL/TLS, or AlwaysOn setups if required.<br>
• For multiple schemas, create separate connections.<br><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks passwords and enforces unique names for secure SQL Server configurations.<br><br>

<i>Use this help section to set up, test, and manage SQL Server connections efficiently and securely.</i>
    """
},


# ----------------------------------        MySQL         --------------------------------

"MySQL": {
    "title": "MySQL Database Connection",
    "description": """
<b>MySQL Database Connection - Help Guide</b><br><br>

This module allows secure integration with <b>MySQL databases</b> for 
<b>data validation, reporting, and analytics</b> using the INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> on the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>MySQL</b> from the list of available databases.<br><br>

<b>Required Fields (UI Reference):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field Name</th>
<th style="padding:8px; border:1px solid #334155;">Description</th>
<th style="padding:8px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Unique name for this MySQL connection. Duplicate names are not allowed.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">MySQL account username for authentication.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">Account password (hidden, with option to show).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Host</td><td style="padding:6px; border:1px solid #334155;">Hostname or IP address of the MySQL server (e.g., mysql.example.com).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">MySQL server port (default: 3306).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">Target MySQL database name.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
1. <b>Enter Connection Name:</b> Example → Sales_MySQL_Prod_2025.<br>
2. <b>Fill Credentials:</b> Enter Username, Password, Host, Port, Database.<br>
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
• <b>Database Access Issues:</b> Ensure the database exists and you have access.<br><br>

<b>Example:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field</th>
<th style="padding:8px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Sales_MySQL_Prod2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">sales_user</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Host</td><td style="padding:6px; border:1px solid #334155;">mysql-db.company.com</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">3306</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">SALES</td></tr>
</table><br>

<b>Advanced Tips:</b><br>
• Use SSL, custom ports, or storage engines if required.<br>
• For multiple databases or privileges, create separate connections.<br><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks passwords and enforces unique names for secure MySQL configurations.<br><br>

<i>Use this help section to set up, test, and manage MySQL connections efficiently and securely.</i>
    """
},


# ----------------------------------        PostgreSQL    ---------------------------------

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
<table style="width:100%; border-collapse: collapse; margin-top:8px;">
<tr style="background-color:#1e293b; color:#38bdf8;">
  <th style="padding:6px; border:1px solid #334155;">Field Name</th>
  <th style="padding:6px; border:1px solid #334155;">Description</th>
  <th style="padding:6px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">A unique name for this PostgreSQL connection. Each new connection must have a distinct name; duplicates are not allowed.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">PostgreSQL database account username for authentication.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">Account password. Click “Show Password” to view as you type.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Host</td><td style="padding:6px; border:1px solid #334155;">Hostname or IP address of the PostgreSQL server (e.g., postgres.example.com).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">PostgreSQL server port (default: 5432).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">Name of the target PostgreSQL database.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">Database schema to access tables within your PostgreSQL database.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
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
<table style="width:100%; border-collapse: collapse; margin-top:8px;">
<tr style="background-color:#1e293b; color:#38bdf8;">
  <th style="padding:6px; border:1px solid #334155;">Field</th>
  <th style="padding:6px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Analytics_PG_Prod2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">analytics_user</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Host</td><td style="padding:6px; border:1px solid #334155;">postgres-db.company.com</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">5432</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">ANALYTICS</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">public</td></tr>
</table><br>

<b>Advanced Tips:</b><br>
• For configurations involving custom ports, SSL, or advanced security (LDAP, Kerberos), consult your DBA or official PostgreSQL documentation.<br>
• To access multiple schemas or roles, set up separate connections, each with a unique name.<br><br>

<b>Security Reminder:</b><br>
The INFOFISCUS Data Validation Tool masks your password on entry and enforces unique connection naming for every new database configuration in accordance with enterprise security best practices.<br><br>

<i>Utilize this help section to efficiently and securely set up, test, and manage PostgreSQL database connections.</i>
"""
},


# ----------------------------------        Snowflake     -----------------------------------

"Snowflake": {
    "title": "Snowflake Database Connection",
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
<table style="width:100%; border-collapse: collapse; margin-top:10px;">
<tr style="background-color:#1e293b; color:#38bdf8; text-align:left;">
  <th style="padding:6px; border:1px solid #334155;">Field Name</th>
  <th style="padding:6px; border:1px solid #334155;">Description</th>
  <th style="padding:6px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">A unique name for this Snowflake connection. Each new connection must have a distinct name; duplicates are not allowed.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">Snowflake account username for authentication.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">Account password. Click “Show Password” to view as you type.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Account ID</td><td style="padding:6px; border:1px solid #334155;">The unique Snowflake account identifier (e.g., ab12345.us-east-1).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Warehouse</td><td style="padding:6px; border:1px solid #334155;">Name of the compute warehouse to use for query execution.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">Target Snowflake database name.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">Database schema to access tables within Snowflake.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Role</td><td style="padding:6px; border:1px solid #334155;">Role to use for permissions and access control.</td><td style="padding:6px; border:1px solid #334155;">No</td></tr>
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
<table style="width:100%; border-collapse: collapse; margin-top:10px;">
<tr style="background-color:#1e293b; color:#38bdf8; text-align:left;">
  <th style="padding:6px; border:1px solid #334155;">Field</th>
  <th style="padding:6px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Analytics_Snowflake_Prod2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">analytics_user</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Account ID</td><td style="padding:6px; border:1px solid #334155;">ab12345.us-east-1</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Warehouse</td><td style="padding:6px; border:1px solid #334155;">ANALYTICS_WH</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">SALES_DB</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">PUBLIC</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Role</td><td style="padding:6px; border:1px solid #334155;">ANALYST</td></tr>
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


# ----------------------------------        Starrocks     ------------------------------------ 

"StarRocks": {
    "title": "StarRocks Database Connection",
    "description": """
<b>StarRocks Database Connection – Help Guide</b><br><br>

<b>Overview</b><br>
The StarRocks connection module enables fast, secure integration with the StarRocks analytical 
database platform for real-time data validation, reporting, and analytics within the 
<b>INFOFISCUS Data Validation Tool</b>. StarRocks is designed for high-performance analytical workloads 
and interactive query scenarios.<br><br>

<b>How to Navigate</b><br>
• Click <b>Connection</b> on the sidebar.<br>
• Double-click <b>Create Connection</b>.<br>
• Double-click <b>Database</b>.<br>
• Select <b>StarRocks</b> from the list of databases.<br><br>

<b>Required Fields</b><br>
<table border="1" cellspacing="0" cellpadding="5">
<tr><th>Field</th><th>Description</th><th>Required</th></tr>
<tr><td>Connection Name</td><td>Unique, descriptive name for your connection.</td><td>Yes</td></tr>
<tr><td>Username</td><td>StarRocks user account for authentication.</td><td>Yes</td></tr>
<tr><td>Password</td><td>Password associated with the username.</td><td>Yes</td></tr>
<tr><td>Host</td><td>StarRocks Frontend (FE) hostname or IP (e.g., starrocks-fe.example.com). 
Note: distinct from MySQL/PostgreSQL hosts.</td><td>Yes</td></tr>
<tr><td>Port</td><td>Query port used to connect to StarRocks FE. Default is 9030 
(different from MySQL's 3306).</td><td>Yes</td></tr>
<tr><td>Database</td><td>Name of the database to connect to in StarRocks.</td><td>Yes</td></tr>
</table><br>

<b>Step-by-Step Instructions</b><br>
1. Enter a unique <b>Connection Name</b> (e.g., <i>Analytics_StarRocks_Prod</i>).<br>
2. Fill in <b>Username</b> and <b>Password</b>.<br>
3. Provide the correct <b>Host</b> for the StarRocks FE server and specify <b>Port 9030</b>.<br>
4. Specify the <b>Database</b> name.<br>
5. Click <b>Test</b> to verify connectivity and credentials.<br>
6. If successful, click <b>Save</b> to register the connection.<br><br>

<b>Important Notes</b><br>
• The host must point to a StarRocks Frontend (FE) node, not backend or other services.<br>
• The port is typically 9030, do not use MySQL default port 3306 or PostgreSQL's 5432.<br>
• Make sure your network/firewall allows communication over port 9030 to the FE host.<br><br>

<b>Best Practices</b><br>
• Use descriptive, unique connection names per environment or project.<br>
• Keep credentials secure and change passwords regularly.<br>
• Assign minimal required permissions to the user.<br>
• Document all connection details for auditing purposes.<br><br>

<b>Troubleshooting Tips</b><br>
• Confirm the Host and Port values correspond to a reachable FE node.<br>
• Check username and password correctness.<br>
• Verify that the specified Database exists and is accessible to the user.<br>
• Look out for firewall or network restrictions blocking port 9030.<br><br>

<b>Example</b><br>
<table border="1" cellspacing="0" cellpadding="5">
<tr><th>Field</th><th>Example Value</th></tr>
<tr><td>Connection Name</td><td>Analytics_StarRocks_Prod</td></tr>
<tr><td>Username</td><td>starrocks_user</td></tr>
<tr><td>Password</td><td>****</td></tr>
<tr><td>Host</td><td>starrocks-fe.example.com</td></tr>
<tr><td>Port</td><td>9030</td></tr>
<tr><td>Database</td><td>analytics_db</td></tr>
</table><br>

<b>Security Reminder</b><br>
INFOFISCUS masks passwords and enforces unique naming for connections. 
Use secure credential management and restrict user privileges as per best practices.
"""
},


# --------------------------------------    Google BigQuery  -----------------------

"Google BigQuery": {
    "title": "Google BigQuery Database Connection",
    "description": """
<b>Google BigQuery Database Connection – Help Guide</b><br><br>

<b>Overview</b><br>
The Google BigQuery connection module enables secure and scalable access to 
<b>Google’s serverless data warehouse service</b> for enterprise-grade data validation, 
analytics, and reporting in the INFOFISCUS Data Validation Tool.<br>
Connections can be configured as:<br>
• <b>Standard (Without TARGET):</b> Direct BigQuery connection.<br>
• <b>With TARGET:</b> Extended with <b>Google Cloud Storage (GCS)</b> integration 
for staging and file-based workflows.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> in the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>Google BigQuery</b>.<br><br>

<b>Required Fields – Standard Connection (Without TARGET):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field Name</th>
<th style="padding:8px; border:1px solid #334155;">Description</th>
<th style="padding:8px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Unique identifier for this connection. Duplicates not allowed.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">BigQuery Credentials</td><td style="padding:6px; border:1px solid #334155;">Upload Google Service Account JSON key file via Browse.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Google Cloud Project Id</td><td style="padding:6px; border:1px solid #334155;">Your GCP project ID (e.g., my-gcp-project).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Dataset Id</td><td style="padding:6px; border:1px solid #334155;">BigQuery dataset name (e.g., sales_data).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<b>Required Fields – Target Connection (With TARGET Enabled – GCS Integration):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field Name</th>
<th style="padding:8px; border:1px solid #334155;">Description</th>
<th style="padding:8px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Bucket Name</td><td style="padding:6px; border:1px solid #334155;">GCS bucket used for staging/exporting data files.</td><td style="padding:6px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Folder Path</td><td style="padding:6px; border:1px solid #334155;">GCS folder path (e.g., exports/2025/).</td><td style="padding:6px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Service Account Json</td><td style="padding:6px; border:1px solid #334155;">JSON key file with permissions to access GCS.</td><td style="padding:6px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Endpoint Url</td><td style="padding:6px; border:1px solid #334155;">Optional custom/private GCS endpoint URL.</td><td style="padding:6px; border:1px solid #334155;">No</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
1. Enter a unique <b>Connection Name</b> (e.g., Prod_GBQ_Sales_2025).<br>
2. Upload <b>Service Account JSON</b> credentials.<br>
3. Enter <b>Project ID</b> and <b>Dataset ID</b>.<br>
4. (Optional) Enable <b>TARGET</b> if GCS staging is required.<br>
&nbsp;&nbsp;&nbsp;• Provide <b>Bucket Name</b>, <b>Folder Path</b>, <b>Service Account JSON</b>, and <b>Endpoint URL</b> if needed.<br>
5. Click <b>Test</b> to validate credentials (BigQuery + GCS if TARGET enabled).<br>
6. Click <b>Save</b> after successful validation.<br><br>

<b>When to Use TARGET Option:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Scenario</th>
<th style="padding:8px; border:1px solid #334155;">Enable TARGET?</th>
<th style="padding:8px; border:1px solid #334155;">Reason</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Query BigQuery tables only</td><td style="padding:6px; border:1px solid #334155;">No</td><td style="padding:6px; border:1px solid #334155;">All work happens directly in BigQuery.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Export data to GCS</td><td style="padding:6px; border:1px solid #334155;">Yes</td><td style="padding:6px; border:1px solid #334155;">Bucket access required for export.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Import files from GCS into BigQuery</td><td style="padding:6px; border:1px solid #334155;">Yes</td><td style="padding:6px; border:1px solid #334155;">Needed for COPY/External Table operations.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">ETL workflows involving GCS staging</td><td style="padding:6px; border:1px solid #334155;">Yes</td><td style="padding:6px; border:1px solid #334155;">File-based pipelines require GCS access.</td></tr>
</table><br>

<b>Best Practices:</b><br>
• Use clear, descriptive connection names per project/environment.<br>
• Keep JSON keys safe; rotate them regularly.<br>
• Restrict GCS permissions to only required buckets/folders.<br>
• Enable TARGET only when file staging is necessary.<br><br>

<b>Troubleshooting Tips:</b><br>
• <b>Invalid/Expired Key:</b> Ensure service account key has required BigQuery/GCS permissions.<br>
• <b>Project ID/Dataset Errors:</b> Check spelling and ensure they exist.<br>
• <b>Bucket Access Issues:</b> Confirm bucket existence and proper IAM roles.<br>
• <b>Endpoint URL:</b> Use only if custom GCS endpoint is required.<br><br>

<b>Example Configuration – Without TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field</th>
<th style="padding:8px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Prod_GBQ_Sales_2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">BigQuery Credentials</td><td style="padding:6px; border:1px solid #334155;">service-account.json</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Google Cloud Project Id</td><td style="padding:6px; border:1px solid #334155;">sales-gcp-prod</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Dataset Id</td><td style="padding:6px; border:1px solid #334155;">sales_data</td></tr>
</table><br>

<b>Example Configuration – With TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field</th>
<th style="padding:8px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Prod_GBQ_Target_2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">BigQuery Credentials</td><td style="padding:6px; border:1px solid #334155;">service-account.json</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Google Cloud Project Id</td><td style="padding:6px; border:1px solid #334155;">sales-gcp-prod</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Dataset Id</td><td style="padding:6px; border:1px solid #334155;">sales_data</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Bucket Name</td><td style="padding:6px; border:1px solid #334155;">gbq-data-exports</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Folder Path</td><td style="padding:6px; border:1px solid #334155;">exports/yearly/2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Service Account Json</td><td style="padding:6px; border:1px solid #334155;">gcs-service-account.json</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Endpoint Url</td><td style="padding:6px; border:1px solid #334155;">https://storage.googleapis.com</td></tr>
</table><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks all credentials and enforces unique connection names.<br>
Always follow enterprise credential management policies:<br>
• Use least-privilege IAM roles.<br>
• Rotate keys frequently.<br>
• Protect service account JSON files.<br><br>

<i>Use this guide to configure secure and scalable Google BigQuery connections 
with or without Google Cloud Storage integration.</i>
"""
},


# ---------------------------------------   Amazon Redshift   ---------------------------

"Amazon RedShift": {
    "title": "Amazon Redshift Database Connection",
    "description": """
<b>Amazon Redshift Database Connection - Help Guide</b><br><br>

<b>Overview</b><br>
The Amazon Redshift connection module enables secure integration with 
<b>AWS's cloud data warehouse</b> for high-performance analytics, reporting, 
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
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;" colspan="3">Standard Redshift Connection (Without TARGET)</th>
</tr>
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field Name</th>
<th style="padding:8px; border:1px solid #334155;">Description</th>
<th style="padding:8px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Unique connection name (duplicates not allowed).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">Redshift cluster user for authentication.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">User account password (masked in tool).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Host</td><td style="padding:6px; border:1px solid #334155;">Redshift cluster endpoint (e.g., redshift-cluster.company.com).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">Redshift port (default: 5439).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">Target Redshift database name.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">Schema to access tables within Redshift.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;" colspan="3">Redshift Connection With TARGET (S3 Integration)</th>
</tr>
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field Name</th>
<th style="padding:8px; border:1px solid #334155;">Description</th>
<th style="padding:8px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Bucket Name</td><td style="padding:6px; border:1px solid #334155;">S3 bucket for reads/writes (UNLOAD, COPY, data import/export).</td><td style="padding:6px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Region Name</td><td style="padding:6px; border:1px solid #334155;">AWS region of S3 bucket (e.g., us-east-1).</td><td style="padding:6px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Folder Path</td><td style="padding:6px; border:1px solid #334155;">S3 folder for files (e.g., exports/2025/).</td><td style="padding:6px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Access Key Id</td><td style="padding:6px; border:1px solid #334155;">AWS IAM access key with S3 permissions.</td><td style="padding:6px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Secret Access Key</td><td style="padding:6px; border:1px solid #334155;">Secret key corresponding to the access key ID.</td><td style="padding:6px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Endpoint Url</td><td style="padding:6px; border:1px solid #334155;">Custom endpoint (for VPC/private S3).</td><td style="padding:6px; border:1px solid #334155;">No</td></tr>
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
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Scenario</th>
<th style="padding:8px; border:1px solid #334155;">Enable TARGET?</th>
<th style="padding:8px; border:1px solid #334155;">Reason</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Run data checks on Redshift tables only</td><td style="padding:6px; border:1px solid #334155;">No</td><td style="padding:6px; border:1px solid #334155;">All data remains inside Redshift.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Export query results to S3</td><td style="padding:6px; border:1px solid #334155;">Yes</td><td style="padding:6px; border:1px solid #334155;">S3 access required to store results.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Import datasets (CSV/Parquet) from S3</td><td style="padding:6px; border:1px solid #334155;">Yes</td><td style="padding:6px; border:1px solid #334155;">Redshift needs credentials to read S3 files.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Use Redshift Spectrum external tables</td><td style="padding:6px; border:1px solid #334155;">Yes</td><td style="padding:6px; border:1px solid #334155;">Data resides on S3.</td></tr>
</table><br>

<b>Example Configurations:</b><br>
<b>Without TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field</th>
<th style="padding:8px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Prod_RS_Sales_2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">sales_admin</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Host</td><td style="padding:6px; border:1px solid #334155;">rs-cluster.company.com</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">5439</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">SALES_DB</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">public</td></tr>
</table><br>

<b>With TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field</th>
<th style="padding:8px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Prod_RS_Export_Target2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">export_user</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Host</td><td style="padding:6px; border:1px solid #334155;">rs-cluster.company.com</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Port</td><td style="padding:6px; border:1px solid #334155;">5439</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">EXPORTS_DB</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">export_schema</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Bucket Name</td><td style="padding:6px; border:1px solid #334155;">rs-data-exports</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Region Name</td><td style="padding:6px; border:1px solid #334155;">us-east-1</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Folder Path</td><td style="padding:6px; border:1px solid #334155;">exports/yearly/2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Access Key Id</td><td style="padding:6px; border:1px solid #334155;">AKIAxxxxxxxxxxxxxxx</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Secret Access Key</td><td style="padding:6px; border:1px solid #334155;">wJalrxUtnFEMI/.../EXAMPLEKEY</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Endpoint Url</td><td style="padding:6px; border:1px solid #334155;">https://s3.us-east-1.amazonaws.com (optional)</td></tr>
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
<b>Azure Synapse Analytics Connection – Help Guide</b><br><br>

<b>Overview</b><br>
The Azure Synapse Analytics connection module enables secure and seamless integration with 
<b>Microsoft's cloud-scale analytics platform</b> for data validation, transformation, and reporting 
within the INFOFISCUS Data Validation Tool.<br><br>
Connections can be configured in two ways:<br>
• <b>Standard (Without TARGET):</b> Direct Synapse connection.<br>
• <b>With TARGET:</b> Extended with Azure Blob Storage credentials for file-based data exchange.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> in the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>Azure Synapse</b>.<br><br>

<b>Required Fields</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;" colspan="3">Standard Synapse Connection (Without TARGET)</th>
</tr>
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field Name</th>
<th style="padding:8px; border:1px solid #334155;">Description</th>
<th style="padding:8px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Unique identifier for this connection. Duplicates are not allowed.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">Synapse database login for authentication.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">Account password (masked in tool).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Server</td><td style="padding:6px; border:1px solid #334155;">Synapse workspace SQL endpoint address.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">Name of the database in Synapse to connect to.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">Default schema to be used within the database.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;" colspan="3">Synapse Connection With TARGET (Blob Storage Integration)</th>
</tr>
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field Name</th>
<th style="padding:8px; border:1px solid #334155;">Description</th>
<th style="padding:8px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Bucket Name</td><td style="padding:6px; border:1px solid #334155;">Azure Blob container name for import/export operations.</td><td style="padding:6px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Folder Path</td><td style="padding:6px; border:1px solid #334155;">Path within the container (e.g., exports/2025/).</td><td style="padding:6px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Account Key</td><td style="padding:6px; border:1px solid #334155;">Azure Storage account access key.</td><td style="padding:6px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Account URL</td><td style="padding:6px; border:1px solid #334155;">Blob Storage endpoint URL (e.g., https://account.blob.core.windows.net).</td><td style="padding:6px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
</table><br>

<b>Step-by-Step Instructions</b><br>
<b>Without TARGET:</b><br>
1. Enter a unique <b>Connection Name</b>.<br>
2. Fill Username, Password, Server, Database, and Schema.<br>
3. Click <b>Test</b> to validate the connection.<br>
4. If successful, click <b>Save</b>.<br><br>

<b>With TARGET:</b><br>
1. Enable the <b>TARGET</b> option.<br>
2. Provide Blob Storage details (Bucket Name, Folder Path, Account Key, Account URL).<br>
3. Click <b>Test</b> – validates both Synapse and Blob credentials.<br>
4. If successful, click <b>Save</b>.<br><br>

<b>Why and When to Use TARGET</b><br>
Target credentials allow Synapse to read from and write to Azure Blob Storage. They are required when:<br>
• Exporting query results to Blob containers.<br>
• Importing datasets (CSV, Parquet) from Blob into Synapse.<br>
• Integrating ETL pipelines that exchange files with Blob.<br><br>

<b>Enable TARGET only when:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Scenario</th>
<th style="padding:8px; border:1px solid #334155;">Enable TARGET?</th>
<th style="padding:8px; border:1px solid #334155;">Reason</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Query Synapse tables only</td><td style="padding:6px; border:1px solid #334155;">No</td><td style="padding:6px; border:1px solid #334155;">All queries remain within Synapse.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Export query results to Blob</td><td style="padding:6px; border:1px solid #334155;">Yes</td><td style="padding:6px; border:1px solid #334155;">Blob credentials required for export.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Import files from Blob</td><td style="padding:6px; border:1px solid #334155;">Yes</td><td style="padding:6px; border:1px solid #334155;">Needed to load external datasets.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">ETL pipelines with Blob</td><td style="padding:6px; border:1px solid #334155;">Yes</td><td style="padding:6px; border:1px solid #334155;">Blob access is mandatory.</td></tr>
</table><br>

<b>Example Configurations</b><br>
<b>Without TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field</th>
<th style="padding:8px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Prod_Synapse_Analytics2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">synapse_user</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Server</td><td style="padding:6px; border:1px solid #334155;">synapse-workspace.sql.net</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">SALES_DB</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">dbo</td></tr>
</table><br>

<b>With TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field</th>
<th style="padding:8px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Prod_Synapse_Export_Target2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Username</td><td style="padding:6px; border:1px solid #334155;">export_user</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Password</td><td style="padding:6px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Server</td><td style="padding:6px; border:1px solid #334155;">synapse-workspace.sql.net</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database</td><td style="padding:6px; border:1px solid #334155;">EXPORTS_DB</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Schema</td><td style="padding:6px; border:1px solid #334155;">export_schema</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Bucket Name</td><td style="padding:6px; border:1px solid #334155;">synapse-data-exports</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Folder Path</td><td style="padding:6px; border:1px solid #334155;">exports/annual/2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Account Key</td><td style="padding:6px; border:1px solid #334155;">q5vLgEXAMPLEKEY==</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Account URL</td><td style="padding:6px; border:1px solid #334155;">https://myaccount.blob.core.windows.net</td></tr>
</table><br>

<b>Best Practices</b><br>
• Use descriptive, unique names for each connection.<br>
• Rotate Account Keys periodically and keep them secure.<br>
• Apply least-privilege access for Blob containers.<br>
• Maintain separate containers/folders for projects.<br>
• Only enable TARGET when Blob integration is required.<br><br>

<b>Troubleshooting Tips</b><br>
• <b>Duplicate Name:</b> Choose a unique Connection Name.<br>
• <b>Authentication Errors:</b> Verify Synapse credentials.<br>
• <b>Network/Server Issues:</b> Confirm SQL endpoint address.<br>
• <b>Blob Access Failures:</b> Ensure container/folder exist and credentials are correct.<br><br>

<b>Security Reminder</b><br>
INFOFISCUS masks Synapse and Blob credentials. 
Unique connection names are enforced. 
Always protect sensitive keys, use least-privilege principles, and rotate credentials regularly.<br><br>

<i>Use this guide to configure Azure Synapse connections with or without Blob integration 
for secure, enterprise-scale data validation workflows.</i>
"""
},

# ---------------------------------------     Databricks     ------------------------------------

"Databricks": {
            "title": "Databricks Connection",
            "description": """
<b>Databricks Connection - Help Guide</b><br><br>

This module enables seamless and secure integration with <b>Databricks' Unified Data and AI Platform</b> for 
<b>data validation, analytics, and reporting</b> within the INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b><br>
1. Click <b>Connection</b> on the sidebar.<br>
2. Double-click <b>Create Connection</b>.<br>
3. Double-click <b>Database</b>.<br>
4. Select <b>Databricks</b> from the list of available databases.<br><br>

<b>Required Fields (UI Reference):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field Name</th>
<th style="padding:8px; border:1px solid #334155;">Description</th>
<th style="padding:8px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">Unique name for this connection. Duplicate names are not allowed.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Server Hostname</td><td style="padding:6px; border:1px solid #334155;">Databricks workspace hostname (e.g., adb-12345.6.azuredatabricks.net).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Access Token</td><td style="padding:6px; border:1px solid #334155;">Personal access token generated from Databricks (hidden, with option to show).</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">HTTP Path</td><td style="padding:6px; border:1px solid #334155;">Path for the target SQL Warehouse or Cluster from Databricks UI.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Catalog</td><td style="padding:6px; border:1px solid #334155;">Unity Catalog name to organize schemas and databases.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database/Schema</td><td style="padding:6px; border:1px solid #334155;">Schema name under the catalog where target tables exist.</td><td style="padding:6px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
1. <b>Enter Connection Name:</b> Example → DBX_Prod_Analytics2025.<br>
2. <b>Fill Connection Details:</b> Enter Server Hostname, Access Token, HTTP Path, Catalog, Database/Schema.<br>
3. <b>Test Connection:</b> Click <b>Test</b> to verify. If it fails, check inputs or contact Databricks admin.<br>
4. <b>Save:</b> Once successful, click <b>Save</b> to register the connection.<br><br>

<b>Best Practices:</b><br>
• Always use descriptive, unique connection names.<br>
• Do not reuse connection names across environments.<br>
• Store access tokens securely and rotate them regularly.<br>
• Apply least privilege when generating tokens.<br><br>

<b>Troubleshooting Tips:</b><br>
• <b>Duplicate Name:</b> Change the connection name.<br>
• <b>Auth Errors:</b> Verify access token and regenerate if needed.<br>
• <b>Network Issues:</b> Confirm server hostname and HTTP path.<br>
• <b>Catalog/Schema Issues:</b> Ensure they exist and you have proper permissions.<br><br>

<b>Example:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Field</th>
<th style="padding:8px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Connection Name</td><td style="padding:6px; border:1px solid #334155;">DBX_Prod_Analytics2025</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Server Hostname</td><td style="padding:6px; border:1px solid #334155;">adb-12345.6.azuredatabricks.net</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Access Token</td><td style="padding:6px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">HTTP Path</td><td style="padding:6px; border:1px solid #334155;">/sql/1.0/warehouses/abcd1234</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Catalog</td><td style="padding:6px; border:1px solid #334155;">main</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Database/Schema</td><td style="padding:6px; border:1px solid #334155;">analytics</td></tr>
</table><br>

<b>Advanced Tips:</b><br>
• Use Unity Catalog for centralized governance.<br>
• Scale SQL Warehouses dynamically for performance and cost efficiency.<br><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks access tokens and enforces unique names for secure Databricks configurations.<br><br>

<i>Use this help section to set up, test, and manage Databricks connections efficiently and securely.</i>
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