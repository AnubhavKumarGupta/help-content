# help_content/database_help.py

def get_database_content():
    """Database-specific help content for all supported database types"""
    return {

# -----------------------      Connection -> Create Connection -> Database     -----------------

"Database": {
    "title": "Database Platform Selection",
    "description": """
<b>Choose Your Database Platform – Help Guide</b><br><br>

<b>Overview</b><br>
Select the appropriate database type to create optimized connections with platform-specific configurations in the <b>INFOFISCUS Data Validation Tool</b>.<br><br>

<b>Enterprise Databases:</b>
<ul>
  <li><b>MySQL:</b> Popular open-source database</li>
  <li><b>Oracle:</b> Enterprise-grade relational database</li>
  <li><b>SQL Server:</b> Microsoft’s flagship database platform</li>
  <li><b>PostgreSQL:</b> Advanced open-source relational database</li>
</ul><br>

<b>Cloud Data Warehouse Platforms:</b>
<ul>
  <li><b>Snowflake:</b> Cloud data warehouse platform</li>
  <li><b>Google BigQuery:</b> Serverless data warehouse</li>
  <li><b>Amazon RedShift:</b> AWS cloud data warehouse</li>
  <li><b>Databricks:</b> Unified analytics platform</li>
  <li><b>StarRocks:</b> High-performance analytical database</li>
  <li><b>Azure Synapse:</b> Microsoft’s analytics platform</li>
</ul><br>

<b>Platform-Specific Features:</b>
<ul>
  <li>Connection parameter validation</li>
  <li>Performance optimization settings</li>
  <li>Security configuration options</li>
  <li>Data type mapping for test cases</li>
</ul><br>

<i>Click on your specific database type to see detailed connection setup instructions and requirements.</i>
"""
}
,

# ---------------------------------         Oracle       --------------------------------

"Oracle": {
    "title": "Oracle Database Connection",
    "description": """
<b>Oracle Database Connection - Help Guide</b><br><br>

This module enables seamless and secure integration with <b>Oracle Databases</b> for 
<b>data validation, reporting, and analysis</b> within the INFOFISCUS Data Validation Tool.<br>

<br>

<b>How to Navigate:</b>
<ol>
<li>Click <b>Connection</b> on the sidebar.</li>
<li>Double-click on the name or single-click on dropdown arrow to open <b>Create Connection</b>.</li>
<li>Double-click on the name or single-click on dropdown arrow to see the list of databases (<b>Database</b>).</li>
<li>Select <b>Oracle</b> from the list of available databases.</li>
</ol><br>

<b>Required Fields (UI Reference):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Unique name for this connection. Duplicate names are not allowed.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">Oracle account username for authentication.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">Account password (hidden, with option to show).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">Hostname or IP address of the Oracle DB server (e.g., db.example.com).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">Database server port (default: 1521).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">Database name or SID of the Oracle instance.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">Schema name to access Oracle tables.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Service Name</td><td style="padding:2px 4px; border:1px solid #334155;">Oracle Service Name (used for RAC or multi-tenant setups).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<br>

<b>Step-by-Step Instructions:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Enter Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Example → Finance_Oracle_Prod_2025.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Fill Credentials:</b></td><td style="padding:4px; border: none; vertical-align: top;">Enter Username, Password, Host, Port, Database, Schema, Service Name.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test</b> to verify. If it fails, check inputs or contact DBA.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Save:</b></td><td style="padding:4px; border: none; vertical-align: top;">Once successful, click <b>Save</b> to register the connection.</td></tr>
</table><br>

<br>
<b>Best Practices & Tips:</b>
<ul>
<li>Always use descriptive, unique connection names.</li>
<li>Do not reuse connection names across environments.</li>
<li>Use individual credentials for accountability.</li>
</ul><br>

<b>Troubleshooting Tips:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;">•</td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Duplicate Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Change the connection name.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Auth Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Verify credentials and privileges.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Network Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Confirm host/port with IT.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Schema/Service Name Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Ensure they are valid names.</td></tr>
</table><br>

<b>Example:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Oracle_Prod_FIN2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">finance_user</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">oracle-db.company.com</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">1521</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">FINANCE</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">FIN_DATA</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Service Name</td><td style="padding:2px 4px; border:1px solid #334155;">prod_fin_srv</td></tr>
</table><br>

<br>
<b>Advanced Tips:</b>
<ul>
<li>Use TNS strings or VPN if required (consult DBA).</li>
<li>For multiple schemas, create separate connections.</li>
</ul><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks passwords and enforces unique names for secure Oracle configurations.<br><br>

<i>Use this help section to set up, test, and manage Oracle connections efficiently and securely.</i>
"""
}
,

# ----------------------------------      SQL Server      ------------------------------

"SQL Server": {
    "title": "SQL Server Database Connection",
    "description": """
<b>SQL Server Database Connection - Help Guide</b><br><br>

This module enables seamless and secure integration with <b>Microsoft SQL Server</b> databases for 
<b>data validation, reporting, and analytics</b> within the INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b>
<ol>
<li>Click <b>Connection</b> on the sidebar.</li>
<li>Double-click on the name or single-click on dropdown arrow to open <b>Create Connection</b>.</li>
<li>Double-click on the name or single-click on dropdown arrow to see the list of databases (<b>Database</b>).</li>
<li>Select <b>SQL Server</b> from the list of available databases.</li>
</ol><br>

<b>Required Fields (UI Reference):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Unique name for this SQL Server connection. Duplicate names are not allowed.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">SQL Server account username for authentication.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">Account password (hidden, with option to show).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Server</td><td style="padding:2px 4px; border:1px solid #334155;">Hostname, IP address, or named instance of SQL Server (e.g., sql.company.com).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">Target SQL Server database name.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">Schema to access SQL Server tables.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">SQL Server port (default: 1433).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<br>

<b>Step-by-Step Instructions:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Enter Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Example → Finance_SQL_Prod_2025.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Fill Credentials:</b></td><td style="padding:4px; border: none; vertical-align: top;">Enter Username, Password, Server, Database, Schema, Port.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test</b> to verify. If it fails, check inputs or contact DBA.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Save:</b></td><td style="padding:4px; border: none; vertical-align: top;">Once successful, click <b>Save</b> to register the connection.</td></tr>
</table><br>

<br>
<b>Best Practices & Tips:</b>
<ul>
<li>Always use descriptive, unique connection names.</li>
<li>Do not reuse connection names across environments.</li>
<li>Use individual credentials for accountability.</li>
<li>Keep passwords secure and update them regularly.</li>
</ul><br>

<b>Troubleshooting Tips:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;">•</td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Duplicate Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Change the connection name.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Auth Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Verify credentials and privileges.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Network Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Confirm server/port with IT.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Schema Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Ensure schema exists and you have access.</td></tr>
</table><br>

<b>Example:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">SQL_HR_Production2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">hr_user</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Server</td><td style="padding:2px 4px; border:1px solid #334155;">sqlserver01.company.com</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">HR</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">dbo</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">1433</td></tr>
</table><br>

<br>
<b>Advanced Tips:</b>
<ul>
<li>Use Windows Authentication, SSL/TLS, or AlwaysOn setups if required.</li>
<li>For multiple schemas, create separate connections.</li>
</ul><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks passwords and enforces unique names for secure SQL Server configurations.<br><br>

<i>Use this help section to set up, test, and manage SQL Server connections efficiently and securely.</i>
"""
}
,

# ----------------------------------        MySQL         --------------------------------
"MySQL": {
    "title": "MySQL Database Connection",
    "description": """
<b>MySQL Database Connection - Help Guide</b><br><br>

This module allows secure integration with <b>MySQL databases</b> for 
<b>data validation, reporting, and analytics</b> using the INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b>
<ol>
<li>Click <b>Connection</b> on the sidebar.</li>
<li>Double-click on the name or single-click on dropdown arrow to see open the dropdown <b>Create Connection</b>.</li>
<li>Double-click on the name or single-click on dropdown arrow to see the list of databases (<b>Database</b>).</li>
<li>Select <b>MySQL</b> from the list of available databases.</li>
</ol><br>

<b>Required Fields (UI Reference):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Unique name for this MySQL connection. Duplicate names are not allowed.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">MySQL account username for authentication.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">Account password (hidden, with option to show).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">Hostname or IP address of the MySQL server (e.g., mysql.example.com).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">MySQL server port (default: 3306).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">Target MySQL database name.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<br>

<b>Step-by-Step Instructions:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Enter Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Example → Sales_MySQL_Prod_2025.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Fill Credentials:</b></td><td style="padding:4px; border: none; vertical-align: top;">Enter Username, Password, Host, Port, Database.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test</b> to verify. If it fails, check inputs or contact DBA.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Save:</b></td><td style="padding:4px; border: none; vertical-align: top;">Once successful, click <b>Save</b> to register the connection.</td></tr>
</table><br>

<br>

<b>Best Practices & Tips:</b>
<ul>
<li>Always use descriptive, unique connection names.</li>
<li>Do not reuse connection names across environments.</li>
<li>Use individual credentials for accountability.</li>
<li>Keep passwords secure and update them regularly.</li>
</ul><br>

<b>Troubleshooting Tips:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;">•</td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Duplicate Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Change the connection name.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Auth Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Verify credentials and privileges.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Network Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Confirm host/port with IT.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Database Access Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Ensure the database exists and you have access.</td></tr>
</table><br>

<br>

<b>Example:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Sales_MySQL_Prod2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">sales_user</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">mysql-db.company.com</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">3306</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">SALES</td></tr>
</table><br>

<br>

<b>Advanced Tips:</b>
<ul>
<li>Use SSL, custom ports, or storage engines if required.</li>
<li>For multiple databases or privileges, create separate connections.</li>
</ul><br>

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

This PostgreSQL Database Connection module allows secure integration with 
<b>PostgreSQL databases</b> for data validation, reporting, and analytics in the 
INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b>
<ol>
<li>Click <b>Connection</b> on the sidebar.</li>
<li>Double-click on the name or Single-click on dropdown arrow to see open the dropdown <b>Create Connection</b>.</li>
<li>Double-click on the name or Single-click on dropdown arrow to see the list of databases (<b>Database</b>).</li>
<li>Select <b>PostgreSQL</b> from the list of available databases.</li>
</ol><br>

<b>Required Fields (UI Reference):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">A unique name for this PostgreSQL connection. Each new connection must have a distinct name; duplicates are not allowed.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">PostgreSQL database account username for authentication.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">Account password. Click "Show Password" to view as you type.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">Hostname or IP address of the PostgreSQL server (e.g., postgres.example.com).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">PostgreSQL server port (default: 5432).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">Name of the target PostgreSQL database.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">Database schema to access tables within your PostgreSQL database.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<br>

<b>Step-by-Step Instructions:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 220px;"><b>Enter a Unique Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Every connection requires a distinct name (e.g., Analytics_PG_Prod_2025 or Dev_PG_Test). If a name already exists, you will be prompted to enter a different, unique name.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Fill Out Credentials:</b></td><td style="padding:4px; border: none; vertical-align: top;">Provide Username, Password, Host, Port, Database, and Schema.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test the Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test</b> to verify connectivity and credentials. If testing fails, review your inputs or consult your database administrator.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Save the Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Once the test is successful, click <b>Save</b> to register your connection.</td></tr>
</table><br>

<br>

<b>Best Practices & Tips:</b>
<ul>
<li>Always use descriptive and unique connection names for each entry.</li>
<li>Do not reuse connection names between different environments or databases.</li>
<li>Use individual user credentials for accountability.</li>
<li>Never share passwords or credentials; keep them secure.</li>
<li>Regularly update passwords and review permissions as organizational policies evolve.</li>
</ul><br>

<b>Troubleshooting Tips:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;">•</td><td style="padding:4px; border: none; vertical-align: top; width: 220px;"><b>Duplicate Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Edit the connection name to ensure uniqueness.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Authentication Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Verify username, password, and ensure the account has sufficient privileges.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Network Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Confirm host and port details with your IT or database administrator.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Database or Schema Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Ensure the specified database and schema exist, and the user has access rights.</td></tr>
</table><br>

<b>Example:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Analytics_PG_Prod2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">analytics_user</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border: none; vertical-align: top;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">postgres-db.company.com</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">5432</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">ANALYTICS</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">public</td></tr>
</table><br>

<br>
<b>Advanced Tips:</b>
<ul>
<li>For configurations involving custom ports, SSL, or advanced security (LDAP, Kerberos), consult your DBA or official PostgreSQL documentation.</li>
<li>To access multiple schemas or roles, set up separate connections, each with a unique name.</li>
</ul><br>

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

The Snowflake Database Connection module enables secure integration with 
<b>Snowflake's cloud data platform</b> for large-scale data validation, analytics, 
and reporting within the INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b>
<ol>
<li>Click <b>Connection</b> on the sidebar.</li>
<li>Double-click on the name or Single-click on dropdown arrow to see open the dropdown <b>Create Connection</b>.</li>
<li>Double-click on the name or Single-click on dropdown arrow to see the list of databases (<b>Database</b>).</li>
<li>Select <b>Snowflake</b> from the list of available databases.</li>
</ol><br>

<b>Required Fields (UI Reference):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:1px 3px; border:1px solid #334155;">Field Name</th>
<th style="padding:1px 3px; border:1px solid #334155;">Description</th>
<th style="padding:1px 3px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">A unique name for this Snowflake connection. Each new connection must have a distinct name; duplicates are not allowed.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">Snowflake account username for authentication.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">Account password. Click "Show Password" to view as you type.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Account ID</td><td style="padding:2px 4px; border:1px solid #334155;">The unique Snowflake account identifier (e.g., ab12345.us-east-1).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Warehouse</td><td style="padding:2px 4px; border:1px solid #334155;">Name of the compute warehouse to use for query execution.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">Target Snowflake database name.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">Database schema to access tables within Snowflake.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Role</td><td style="padding:2px 4px; border:1px solid #334155;">Role to use for permissions and access control.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<br>

<b>Step-by-Step Instructions:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 240px;"><b>Enter a Unique Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Every connection requires a distinct name (e.g., Analytics_Snowflake_Prod_2025 or Sales_SF_Dev). If a name already exists, you will be prompted to enter a different, unique name.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Fill Out Credentials:</b></td><td style="padding:4px; border: none; vertical-align: top;">Provide Username, Password, Account ID, Warehouse, Database, Schema, and Role (if required).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test the Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test</b> to verify connectivity and credentials. If testing fails, review your inputs or consult your Snowflake administrator.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Save the Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Once the test is successful, click <b>Save</b> to register your connection.</td></tr>
</table><br>

<br>

<b>Best Practices & Tips:</b>
<ul>
<li>Always use descriptive and unique connection names for each entry.</li>
<li>Do not reuse connection names between different environments (production, development, QA).</li>
<li>Choose a warehouse appropriate to your workload and data volume.</li>
<li>Use individual roles to ensure proper access control and auditing.</li>
<li>Never share passwords or credentials; keep them secure.</li>
<li>Regularly update passwords and review permissions as organizational policies evolve.</li>
</ul><br>

<b>Troubleshooting Tips:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;">•</td><td style="padding:4px; border: none; vertical-align: top; width: 240px;"><b>Duplicate Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Edit the connection name to ensure uniqueness.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Authentication Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Verify username/password, account ID, and ensure the user has the required role and privileges.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Warehouse or Database Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Ensure the specified warehouse and database exist and your user has access rights.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Network Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Ensure access to Snowflake over the Internet (required for cloud connectivity); check with IT if issues persist.</td></tr>
</table><br>

<b>Example:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:1px 3px; border:1px solid #334155;">Field</th>
<th style="padding:1px 3px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Analytics_Snowflake_Prod2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">analytics_user</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Account ID</td><td style="padding:2px 4px; border:1px solid #334155;">ab12345.us-east-1</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Warehouse</td><td style="padding:2px 4px; border:1px solid #334155;">ANALYTICS_WH</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">SALES_DB</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">PUBLIC</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Role</td><td style="padding:2px 4px; border:1px solid #334155;">ANALYST</td></tr>
</table><br>

<br>
<b>Advanced Tips:</b>
<ul>
<li>For advanced authentication (key pair, MFA, SSO), refer to Snowflake's official documentation or consult your admin.</li>
<li>Optimize warehouse size and scaling for performance and cost efficiency.</li>
<li>Use the appropriate role for least-privilege access and audit compliance.</li>
<li>Explore features like Time Travel (query previous data states), Secure Views, and Zero-Copy Cloning for advanced analytics and compliance.</li>
</ul><br>

<b>Security Reminder:</b><br>
The INFOFISCUS Data Validation Tool masks your password on entry and enforces unique connection naming for every new database configuration, following enterprise security best practices.<br>
Warehouse and role selection help control cost and security.<br><br>

<i>Utilize this help section to efficiently and securely set up, test, and manage Snowflake database connections for scalable cloud analytics.</i>
"""
}

,


# ----------------------------------        Starrocks     ------------------------------------ 

"StarRocks": {
    "title": "StarRocks Database Connection",
    "description": """
<b>StarRocks Database Connection – Help Guide</b><br><br>

This StarRocks connection module enables fast, secure integration with the StarRocks analytical 
database platform for real-time data validation, reporting, and analytics within the 
<b>INFOFISCUS Data Validation Tool</b>. StarRocks is designed for high-performance analytical workloads 
and interactive query scenarios.<br><br>

<b>How to Navigate:</b>
<ol>
<li>Click <b>Connection</b> on the sidebar.</li>
<li>Double-click on the name or single-click on dropdown arrow to see <b>Create Connection</b>.</li>
<li>Double-click on the name or single-click on dropdown arrow to see the list of databases (<b>Database</b>).</li>
<li>Select <b>StarRocks</b> from the list of databases.</li>
</ol><br>

<b>Required Fields (UI Reference):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Unique, descriptive name for your connection.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">StarRocks user account for authentication.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">Password associated with the username.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">StarRocks Frontend (FE) hostname or IP (e.g., starrocks-fe.example.com). Distinct from MySQL/PostgreSQL hosts.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">Query port used to connect to StarRocks FE. Default: 9030.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">Name of the database to connect to in StarRocks.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<br>

<b>Step-by-Step Instructions:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Enter Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Example → Analytics_StarRocks_Prod.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Fill Credentials:</b></td><td style="padding:4px; border: none; vertical-align: top;">Enter Username and Password.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Provide Host & Port:</b></td><td style="padding:4px; border: none; vertical-align: top;">Enter correct FE host and Port 9030.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Specify Database:</b></td><td style="padding:4px; border: none; vertical-align: top;">Enter the StarRocks database name.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>5.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test</b> to verify.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>6.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Save:</b></td><td style="padding:4px; border: none; vertical-align: top;">Once successful, click <b>Save</b> to register the connection.</td></tr>
</table><br>

<br>

<b>Important Notes:</b>
<ul>
<li>The StarRocks database must be enabled before connecting/validating.</li>
<li>The host must point to a StarRocks Frontend (FE) node.</li>
<li>The port is typically 9030; do not use MySQL 3306 or PostgreSQL 5432.</li>
<li>Ensure network/firewall allows communication over port 9030 to the FE host.</li>
</ul><br>

<b>Best Practices:</b>
<ul>
<li>Use descriptive, unique connection names per environment or project.</li>
<li>Keep credentials secure and change passwords regularly.</li>
<li>Assign minimal required permissions to the user.</li>
<li>Document all connection details for auditing purposes.</li>
</ul><br>

<b>Troubleshooting Tips:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;">•</td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Host/Port Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Confirm values correspond to a reachable FE node.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Authentication Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Check username and password correctness.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Database Access Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Verify database exists and is accessible.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Network Restrictions:</b></td><td style="padding:4px; border: none; vertical-align: top;">Check firewall or network blocking port 9030.</td></tr>
</table><br>

<br>

<b>Example:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Analytics_StarRocks_Prod</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">starrocks_user</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">starrocks-fe.example.com</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">9030</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">analytics_db</td></tr>
</table><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks passwords and enforces unique naming for connections. Use secure credential management and restrict user privileges as per best practices.<br><br>

<i>Use this help section to set up, test, and manage StarRocks connections efficiently and securely.</i>
"""
}
,


# --------------------------------------    Google BigQuery  -----------------------

"Google BigQuery": {
    "title": "Google BigQuery Database Connection",
    "description": """
<b>Google BigQuery Connection – Help Guide</b><br><br>

This Google BigQuery connection module enables secure and scalable access to 
<b>Google’s serverless data warehouse service</b> for enterprise-grade data validation, 
analytics, and reporting in the <b>INFOFISCUS Data Validation Tool</b>.<br><br>

Connections can be configured as:
<ul>
<li><b>Standard (Without TARGET):</b> Direct BigQuery connection.</li>
<li><b>With TARGET:</b> Extended with <b>Google Cloud Storage (GCS)</b> integration for staging and file-based workflows.</li>
</ul><br>

<b>How to Navigate:</b>
<ol>
<li>Click <b>Connection</b> in the sidebar.</li>
<li>Double-click on the name or single-click on dropdown arrow to open <b>Create Connection</b>.</li>
<li>Double-click on the name or single-click on dropdown arrow to see the list of databases (<b>Database</b>).</li>
<li>Select <b>Google BigQuery</b>.</li>
</ol><br>

<b>Required Fields – Standard Connection (Without TARGET):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Unique identifier for this connection. Duplicates not allowed.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">BigQuery Credentials</td><td style="padding:2px 4px; border:1px solid #334155;">Upload Google Service Account JSON key file via Browse.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Google Cloud Project Id</td><td style="padding:2px 4px; border:1px solid #334155;">Your GCP project ID (e.g., my-gcp-project).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Dataset Id</td><td style="padding:2px 4px; border:1px solid #334155;">BigQuery dataset name (e.g., sales_data).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<b>Required Fields – Target Connection (With TARGET Enabled – GCS Integration):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Bucket Name</td><td style="padding:2px 4px; border:1px solid #334155;">GCS bucket used for staging/exporting data files.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Folder Path</td><td style="padding:2px 4px; border:1px solid #334155;">GCS folder path (e.g., exports/2025/).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Service Account Json</td><td style="padding:2px 4px; border:1px solid #334155;">JSON key file with permissions to access GCS.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if target)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Endpoint Url</td><td style="padding:2px 4px; border:1px solid #334155;">Optional custom/private GCS endpoint URL.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if target)</td></tr>
</table><br>

<b>Step-by-Step Instructions:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Enter Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Example → Prod_GBQ_Sales_2025.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Upload Credentials:</b></td><td style="padding:4px; border: none; vertical-align: top;">Upload Service Account JSON key file via the Browse button.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Provide Project & Dataset:</b></td><td style="padding:4px; border: none; vertical-align: top;">Fill in Project ID and Dataset ID fields (e.g., sales-gcp-prod / sales_data).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Enable TARGET (Optional):</b></td><td style="padding:4px; border: none; vertical-align: top;">If GCS staging is required, provide Bucket Name, Folder Path, Service Account JSON, and Endpoint URL.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>5.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test</b> to validate BigQuery (and GCS if TARGET enabled).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>6.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Save:</b></td><td style="padding:4px; border: none; vertical-align: top;">If the test succeeds, click <b>Save</b> to register the connection.</td></tr>
</table><br>

<b>When to Use TARGET Option:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Scenario</th>
<th style="padding:2px 4px; border:1px solid #334155;">Enable TARGET?</th>
<th style="padding:2px 4px; border:1px solid #334155;">Reason</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Query BigQuery tables only</td><td style="padding:2px 4px; border:1px solid #334155;">No</td><td style="padding:2px 4px; border:1px solid #334155;">All work happens directly in BigQuery.</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Export data to GCS</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td><td style="padding:2px 4px; border:1px solid #334155;">Bucket access required for export operations.</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Import files from GCS into BigQuery</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td><td style="padding:2px 4px; border:1px solid #334155;">Needed for COPY/External Table operations.</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">ETL workflows involving GCS staging</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td><td style="padding:2px 4px; border:1px solid #334155;">File-based pipelines require GCS access.</td></tr>
</table><br>

<b>Best Practices:</b>
<ul>
<li>Use clear, descriptive connection names per project/environment.</li>
<li>Keep JSON keys safe; rotate them regularly.</li>
<li>Restrict GCS permissions to only required buckets/folders.</li>
<li>Enable TARGET only when file staging is necessary.</li>
</ul><br>

<b>Troubleshooting Tips:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;">•</td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Invalid Credentials:</b></td><td style="padding:4px; border: none; vertical-align: top;">Ensure the service account JSON key is valid, not expired, and has BigQuery and GCS permissions (roles/bigquery.user, roles/storage.objectViewer, etc., as required).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Incorrect Project/Dataset:</b></td><td style="padding:4px; border: none; vertical-align: top;">Verify the Project ID and Dataset ID are correctly spelled and that the dataset exists in the specified project.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Bucket Access Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Confirm the GCS bucket/folder exists and the service account has access to the bucket (correct IAM roles and bindings).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Network/Endpoint Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">If using a custom endpoint, ensure the Endpoint URL is correct and reachable from the application network (no firewall blocking).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Permission Denied on Operations:</b></td><td style="padding:4px; border: none; vertical-align: top;">Check that the service account has the specific roles required for the operation (e.g., jobs.create, tables.get, storage.objects.create).</td></tr>
</table><br>

<b>Example Configuration – Without TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Prod_GBQ_Sales_2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">BigQuery Credentials</td><td style="padding:2px 4px; border:1px solid #334155;">service-account.json</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Google Cloud Project Id</td><td style="padding:2px 4px; border:1px solid #334155;">sales-gcp-prod</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Dataset Id</td><td style="padding:2px 4px; border:1px solid #334155;">sales_data</td></tr>
</table><br>

<br>

<b>Example Configuration – With TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Prod_GBQ_Target_2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">BigQuery Credentials</td><td style="padding:2px 4px; border:1px solid #334155;">service-account.json</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Google Cloud Project Id</td><td style="padding:2px 4px; border:1px solid #334155;">sales-gcp-prod</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Dataset Id</td><td style="padding:2px 4px; border:1px solid #334155;">sales_data</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Bucket Name</td><td style="padding:2px 4px; border:1px solid #334155;">gbq-data-exports</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Folder Path</td><td style="padding:2px 4px; border:1px solid #334155;">exports/yearly/2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Service Account Json</td><td style="padding:2px 4px; border:1px solid #334155;">gcs-service-account.json</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Endpoint Url</td><td style="padding:2px 4px; border:1px solid #334155;">https://storage.googleapis.com</td></tr>
</table><br>

<br>

<b>Security Reminder:</b><br>
INFOFISCUS masks all credentials and enforces unique connection names.<br>
Always follow enterprise credential management policies:
<ul>
<li>Use least-privilege IAM roles.</li>
<li>Rotate keys frequently.</li>
<li>Protect service account JSON files.</li>
</ul><br>

<i>Use this guide to configure secure and scalable Google BigQuery connections with or without Google Cloud Storage integration.</i>
"""
}

,


# ---------------------------------------   Amazon Redshift   ---------------------------

"Amazon RedShift": {
    "title": "Amazon Redshift Database Connection",
    "description": """
<b>Amazon Redshift Connection – Help Guide</b><br><br>

This Amazon Redshift connection module enables secure integration with 
<b>AWS's cloud data warehouse</b> for high-performance analytics, reporting, 
and data validation in the INFOFISCUS Data Validation Tool.<br><br>

Connections can be configured in two ways:
<ul>
<li><b>Standard (Without TARGET):</b> Direct Redshift connection.</li>
<li><b>With TARGET:</b> Extended with Amazon S3 credentials for file-based data exchange.</li>
</ul><br>

<b>How to Navigate:</b>
<ol>
<li>Click <b>Connection</b> in the sidebar.</li>
<li>Double-click on the name or Single-click on dropdown arrow to see open the dropdown <b>Create Connection</b>.</li>
<li>Double-click on the name or Single-click on dropdown arrow to see the list of databases <b>Database</b>.</li>
<li>Select <b>Amazon Redshift</b>.</li>
</ol><br>

<b>Required Fields – Standard Redshift Connection (Without TARGET):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Unique connection name(duplicates are not allowed).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">Redshift cluster user for authentication.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">Account password (masked in tool).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">Redshift cluster endpoint address.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">Redshift port (default: 5439).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">Target Redshift database name.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">Schema to access tables within Redshift.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<b>Required Fields – Target Connection (With TARGET Enabled – S3 Integration):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Bucket Name</td><td style="padding:2px 4px; border:1px solid #334155;">S3 bucket name for import/export operations.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Region Name</td><td style="padding:2px 4px; border:1px solid #334155;">AWS region of the bucket (e.g., us-east-1).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Folder Path</td><td style="padding:2px 4px; border:1px solid #334155;">Path within the bucket (e.g., exports/2025/).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Access Key Id</td><td style="padding:2px 4px; border:1px solid #334155;">AWS IAM access key for S3 operations.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Secret Access Key</td><td style="padding:2px 4px; border:1px solid #334155;">Secret key corresponding to access key ID.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Endpoint Url</td><td style="padding:2px 4px; border:1px solid #334155;">Custom endpoint URL (optional, for VPC/private S3).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
</table><br>

<br>

<b>Step-by-Step Instructions:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Enter Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Enter a unique Connection Name (e.g., Prod_RS_Sales_2025).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Fill Redshift Details:</b></td><td style="padding:4px; border: none; vertical-align: top;">Provide Username, Password, Host, Port, Database, and Schema.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Enable TARGET (Optional):</b></td><td style="padding:4px; border: none; vertical-align: top;">If S3 integration is needed, enable TARGET and provide S3 details (Bucket Name, Region Name, Folder Path, Access Key Id, Secret Access Key, Endpoint Url).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test</b> to validate Redshift (and S3 if TARGET enabled).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>5.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Save:</b></td><td style="padding:4px; border: none; vertical-align: top;">If the test succeeds, click <b>Save</b> to register the connection.</td></tr>
</table><br>

<br>

<b>Why and When to Use TARGET:</b><br>
Target credentials allow Redshift to read/write to S3. They are required for:
<ul>
<li>Exporting query results (<code>UNLOAD</code>)</li>
<li>Importing files from S3 (<code>COPY</code>)</li>
<li>Using Redshift Spectrum with external S3 tables</li>
</ul><br>

<b>Enable TARGET only when:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Scenario</th>
<th style="padding:2px 4px; border:1px solid #334155;">Enable TARGET?</th>
<th style="padding:2px 4px; border:1px solid #334155;">Reason</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Run checks on Redshift tables only</td><td style="padding:2px 4px; border:1px solid #334155;">No</td><td style="padding:2px 4px; border:1px solid #334155;">All data stays in Redshift.</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Export query results to S3</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td><td style="padding:2px 4px; border:1px solid #334155;">S3 access required.</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Import datasets from S3</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td><td style="padding:2px 4px; border:1px solid #334155;">Redshift needs credentials to read S3.</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Use Redshift Spectrum external tables</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td><td style="padding:2px 4px; border:1px solid #334155;">Data resides in S3.</td></tr>
</table><br>

<b>Example Configuration – Without TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Prod_RS_Sales_2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">sales_admin</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">rs-cluster.company.com</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">5439</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">SALES_DB</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">public</td></tr>
</table><br>

<b>Example Configuration – With TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Prod_RS_Export_Target2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">export_user</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Host</td><td style="padding:2px 4px; border:1px solid #334155;">rs-cluster.company.com</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Port</td><td style="padding:2px 4px; border:1px solid #334155;">5439</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">EXPORTS_DB</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">export_schema</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Bucket Name</td><td style="padding:2px 4px; border:1px solid #334155;">rs-data-exports</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Region Name</td><td style="padding:2px 4px; border:1px solid #334155;">us-east-1</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Folder Path</td><td style="padding:2px 4px; border:1px solid #334155;">exports/yearly/2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Access Key Id</td><td style="padding:2px 4px; border:1px solid #334155;">AKIAxxxxxxxxxxxxxxx</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Secret Access Key</td><td style="padding:2px 4px; border:1px solid #334155;">wJalrxUtnFEMI/.../EXAMPLEKEY</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Endpoint Url</td><td style="padding:2px 4px; border:1px solid #334155;">https://s3.us-east-1.amazonaws.com (optional)</td></tr>
</table><br>

<br>

<b>Best Practices:</b>
<ul>
<li>Use unique, descriptive connection names.</li>
<li>Store AWS keys securely and rotate regularly.</li>
<li>Grant S3 access only to required buckets/folders.</li>
<li>Use IAM roles instead of static keys where possible.</li>
</ul><br>

<b>Troubleshooting Tips:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;">•</td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Duplicate Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Use a unique connection name.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Credential Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Verify Redshift + S3 credentials.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Network/Endpoint Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Check firewall and endpoint.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>S3 Permission Failures:</b></td><td style="padding:4px; border: none; vertical-align: top;">Confirm bucket/folder access.</td></tr>
</table><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks Redshift and S3 credentials. Unique connection names are enforced. 
Always protect keys, use least-privilege principles, and rotate credentials regularly.<br><br>

<i>Use this guide to configure Amazon Redshift connections with or without S3 integration 
for secure, enterprise-scale data validation workflows.</i>
"""
}
,


# ----------------------------------------    Azure Synapse  --------------------------------

"Azure Synapse": {
    "title": "Azure Synapse Analytics Connection",
    "description": """
<b>Azure Synapse Analytics Connection – Help Guide</b><br><br>

This Azure Synapse Analytics connection module enables secure and seamless integration with 
<b>Microsoft's cloud-scale analytics platform</b> for data validation, transformation, and reporting 
within the INFOFISCUS Data Validation Tool.<br><br>

Connections can be configured in two ways:
<ul>
<li><b>Standard (Without TARGET):</b> Direct Synapse connection.</li>
<li><b>With TARGET:</b> Extended with Azure Blob Storage credentials for file-based data exchange.</li>
</ul><br>

<b>How to Navigate:</b>
<ol>
<li>Click <b>Connection</b> in the sidebar.</li>
<li>Double-click on the name or Single-click on dropdown arrow to see open the dropdown <b>Create Connection</b>.</li>
<li>Double-click on the name or Single-click on dropdown arrow to see the list of databases <b>Database</b>.</li>
<li>Select <b>Azure Synapse</b>.</li>
</ol><br>

<b>Required Fields – Standard Synapse Connection (Without TARGET):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Unique identifier for this connection. Duplicates are not allowed.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">Synapse database login for authentication.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">Account password (masked in tool).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Server</td><td style="padding:2px 4px; border:1px solid #334155;">Synapse workspace SQL endpoint address.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">Name of the database in Synapse to connect to.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">Default schema to be used within the database.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<b>Required Fields – Target Connection (With TARGET Enabled – Blob Storage Integration):</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Bucket Name</td><td style="padding:2px 4px; border:1px solid #334155;">Azure Blob container name for import/export operations.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Folder Path</td><td style="padding:2px 4px; border:1px solid #334155;">Path within the container (e.g., exports/2025/).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Account Key</td><td style="padding:2px 4px; border:1px solid #334155;">Azure Storage account access key.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Account URL</td><td style="padding:2px 4px; border:1px solid #334155;">Blob Storage endpoint URL (e.g., https://account.blob.core.windows.net).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes (if TARGET)</td></tr>
</table><br>

<br>

<b>Step-by-Step Instructions:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Enter Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Enter a unique Connection Name (e.g., Prod_Synapse_Analytics2025).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Fill Synapse Details:</b></td><td style="padding:4px; border: none; vertical-align: top;">Provide Username, Password, Server, Database, and Schema.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Enable TARGET (Optional):</b></td><td style="padding:4px; border: none; vertical-align: top;">If Blob Storage integration is needed, enable TARGET and provide Blob Storage details (Bucket Name, Folder Path, Account Key, Account URL).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test</b> to validate Synapse (and Blob Storage if TARGET enabled).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>5.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Save:</b></td><td style="padding:4px; border: none; vertical-align: top;">If the test succeeds, click <b>Save</b> to register the connection.</td></tr>
</table><br>

<br>

<b>Important Notes:</b>
<ul>
<li>Ensure that Azure Synapse is resumed before connecting/validating.</li>
</ul><br>

<b>Why and When to Use TARGET:</b><br>
Target credentials allow Synapse to read from and write to Azure Blob Storage. They are required when:
<ul>
<li>Exporting query results to Blob containers.</li>
<li>Importing datasets (CSV, Parquet) from Blob into Synapse.</li>
<li>Integrating ETL pipelines that exchange files with Blob.</li>
</ul><br>

<b>Enable TARGET only when:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Scenario</th>
<th style="padding:2px 4px; border:1px solid #334155;">Enable TARGET?</th>
<th style="padding:2px 4px; border:1px solid #334155;">Reason</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Query Synapse tables only</td><td style="padding:2px 4px; border:1px solid #334155;">No</td><td style="padding:2px 4px; border:1px solid #334155;">All queries remain within Synapse.</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Export query results to Blob</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td><td style="padding:2px 4px; border:1px solid #334155;">Blob credentials required for export.</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Import files from Blob</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td><td style="padding:2px 4px; border:1px solid #334155;">Needed to load external datasets.</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">ETL pipelines with Blob</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td><td style="padding:2px 4px; border:1px solid #334155;">Blob access is mandatory.</td></tr>
</table><br>

<b>Example Configuration – Without TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Prod_Synapse_Analytics2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">synapse_user</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Server</td><td style="padding:2px 4px; border:1px solid #334155;">synapse-workspace.sql.net</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">SALES_DB</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">dbo</td></tr>
</table><br>

<b>Example Configuration – With TARGET:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Prod_Synapse_Export_Target2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Username</td><td style="padding:2px 4px; border:1px solid #334155;">export_user</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Password</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Server</td><td style="padding:2px 4px; border:1px solid #334155;">synapse-workspace.sql.net</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database</td><td style="padding:2px 4px; border:1px solid #334155;">EXPORTS_DB</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Schema</td><td style="padding:2px 4px; border:1px solid #334155;">export_schema</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Bucket Name</td><td style="padding:2px 4px; border:1px solid #334155;">synapse-data-exports</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Folder Path</td><td style="padding:2px 4px; border:1px solid #334155;">exports/annual/2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Account Key</td><td style="padding:2px 4px; border:1px solid #334155;">q5vLgEXAMPLEKEY==</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Account URL</td><td style="padding:2px 4px; border:1px solid #334155;">https://myaccount.blob.core.windows.net</td></tr>
</table><br>

<br>

<b>Best Practices:</b>
<ul>
<li>Pause the Azure Synapse when not in use to reduce billing and usage of resources.</li>
<li>Use descriptive, unique names for each connection.</li>
<li>Rotate Account Keys periodically and keep them secure.</li>
<li>Apply least-privilege access for Blob containers.</li>
<li>Maintain separate containers/folders for projects.</li>
<li>Only enable TARGET when Blob integration is required.</li>
</ul><br>

<b>Troubleshooting Tips:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;">•</td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Duplicate Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Choose a unique Connection Name.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Authentication Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Verify Synapse credentials.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Network/Server Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Confirm SQL endpoint address.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Blob Access Failures:</b></td><td style="padding:4px; border: none; vertical-align: top;">Ensure container/folder exist and credentials are correct.</td></tr>
</table><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks Synapse and Blob credentials. 
Unique connection names are enforced. 
Always protect sensitive keys, use least-privilege principles, and rotate credentials regularly.<br><br>

<i>Use this guide to configure Azure Synapse connections with or without Blob integration 
for secure, enterprise-scale data validation workflows.</i>
"""
}
,

# ---------------------------------------     Databricks     ------------------------------------

"Databricks": {
    "title": "Databricks Database Connection",
    "description": """
<b>Databricks Connection - Help Guide</b><br><br>

This Databricks connection module enables secure integration with 
<b>Databricks Unified Data & AI Platform</b> for high-performance analytics, 
reporting, and data validation in the INFOFISCUS Data Validation Tool.<br><br>

<b>How to Navigate:</b>
<ol>
<li>Click <b>Connection</b> on the sidebar.</li>
<li>Double-click on the name or single-click on the dropdown arrow to open <b>Create Connection</b>.</li>
<li>Double-click on the name or single-click on the dropdown arrow to see the list of databases. <b>Database</b>.</li>
<li>Select <b>Databricks</b> from the list.</li>
</ol><br>

<b>Required Fields:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field Name</th>
<th style="padding:2px 4px; border:1px solid #334155;">Description</th>
<th style="padding:2px 4px; border:1px solid #334155;">Required</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">Unique name for this connection. Duplicate names not allowed.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Server Hostname</td><td style="padding:2px 4px; border:1px solid #334155;">Databricks workspace hostname (e.g., adb-12345.6.azuredatabricks.net).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Access Token</td><td style="padding:2px 4px; border:1px solid #334155;">Personal access token generated from Databricks (hidden).</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">HTTP Path</td><td style="padding:2px 4px; border:1px solid #334155;">Path for the target SQL Warehouse or Cluster.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Catalog</td><td style="padding:2px 4px; border:1px solid #334155;">Unity Catalog name for organizing schemas/databases.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database/Schema</td><td style="padding:2px 4px; border:1px solid #334155;">Schema under the catalog where target tables exist.</td><td style="padding:2px 4px; border:1px solid #334155;">Yes</td></tr>
</table><br>

<br>

<b>Step-by-Step Instructions:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Enter Connection Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Enter a unique Connection Name (e.g., DBX_Prod_Analytics2025).</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Fill Connection Details:</b></td><td style="padding:4px; border: none; vertical-align: top;">Fill Server Hostname, Access Token, HTTP Path, Catalog, Database/Schema.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test</b> to validate connection.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Save:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Save</b> once successful.</td></tr>
</table><br>


<br>

<b>Best Practices:</b>
<ul>
<li>Use descriptive, unique connection names.</li>
<li>Do not reuse connection names across environments.</li>
<li>Store access tokens securely; rotate regularly.</li>
<li>Apply least privilege when generating tokens.</li>
</ul><br>

<b>Troubleshooting Tips:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;">•</td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Duplicate Name:</b></td><td style="padding:4px; border: none; vertical-align: top;">Change the connection name.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Auth Errors:</b></td><td style="padding:4px; border: none; vertical-align: top;">Verify and regenerate token if needed.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Network Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Check server hostname & HTTP Path.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;">•</td><td style="padding:4px; border: none; vertical-align: top;"><b>Catalog/Schema Issues:</b></td><td style="padding:4px; border: none; vertical-align: top;">Confirm existence and permissions.</td></tr>
</table><br>

<br>

<b>Example Configuration:</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:2px 4px; border:1px solid #334155;">Field</th>
<th style="padding:2px 4px; border:1px solid #334155;">Example Value</th>
</tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Connection Name</td><td style="padding:2px 4px; border:1px solid #334155;">DBX_Prod_Analytics2025</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Server Hostname</td><td style="padding:2px 4px; border:1px solid #334155;">adb-12345.6.azuredatabricks.net</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Access Token</td><td style="padding:2px 4px; border:1px solid #334155;">****</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">HTTP Path</td><td style="padding:2px 4px; border:1px solid #334155;">/sql/1.0/warehouses/abcd1234</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Catalog</td><td style="padding:2px 4px; border:1px solid #334155;">main</td></tr>
<tr><td style="padding:2px 4px; border:1px solid #334155;">Database/Schema</td><td style="padding:2px 4px; border:1px solid #334155;">analytics</td></tr>
</table><br>


<br>

<b>Advanced Tips:</b>
<ul>
<li>Use Unity Catalog for centralized governance.</li>
<li>Scale SQL Warehouses dynamically for performance & cost efficiency.</li>
</ul><br>

<b>Security Reminder:</b><br>
INFOFISCUS masks access tokens and enforces unique connection names.<br><br>

<i>Use this guide to confidently configure, test, and manage Databricks connections securely at enterprise scale.</i>
"""
}

,


# -----------------------------------      Edit Databases   ---------------------

"Edit Database": {
    "title": "Edit Database Connection Parameters",
    "description": """
<b>Edit Database – Help Guide</b><br><br>

<b>Overview</b><br>
The Edit Database feature allows you to modify, update, or test the connection configuration for any supported database platform after initial setup. 
This ensures your data connections are always current, reflecting changes in credentials, database structure, or server information—without the need to create entirely new connections.<br><br>

<b>How Edit Database Works</b><br>

<b>Database Selection</b>
<ul>
  <li>At the top of the Edit Database section, you’ll find a dropdown menu labeled <b>Select Database</b>.</li>
  <li>Click this dropdown to view a list of all supported database types (such as Oracle, SQL Server, MySQL, StarRocks, PostgreSQL, Snowflake, Google BigQuery, Amazon RedShift, Azure Synapse, Databricks, etc.).</li>
  <li>Select the target database platform you want to edit. The form below will adapt to the chosen database, showing only relevant fields and options.</li>
</ul>

<b>Selecting the Connection to Edit</b>
<ul>
  <li>Under the database platform heading (e.g., Snowflake), you’ll see a labeled field such as <b>Connection Name</b> with a dropdown menu (Select Connection).</li>
  <li>Click this dropdown to view all the existing connections you have previously created for that specific database type.</li>
  <li>Choose the desired connection to load its current configuration.</li>
</ul>

<b>Review and Edit Connection Details</b>
<ul>
  <li>After selecting a connection, all configuration fields (such as Username, Password, Host, Port, Account ID, Warehouse, Database, Schema, Role—depending on your selected database type) will populate with existing stored values.</li>
  <li>Carefully review current details.</li>
  <li>Make any necessary changes:
    <ul>
      <li>Update credentials if passwords, usernames, or key files have rotated or expired.</li>
      <li>Edit connection properties (host, port, database, relevant GCS/S3 or warehouse settings) in response to infrastructure changes, migrations, or upgrades.</li>
      <li>If you do not wish to change anything, you can simply refresh and validate the connection as-is.</li>
    </ul>
  </li>
</ul>

<br>

<b>Test and Save</b>
<ul>
  <li>Once all required changes are made, or if you simply want to refresh/revalidate the connection to sync new metadata, click the <b>Test and Save</b> button at the bottom.</li>
  <li>The system will:
    <ul>
      <li>Attempt to establish a connection with the new or existing settings.</li>
      <li>Validate credentials, host reachability, permissions, and (if applicable) pull updated schema or object information.</li>
      <li>If any problems are detected, you will be prompted to revise and fix the inputs.</li>
    </ul>
  </li>
</ul>

<br>

<b>Update Other Connections</b>
<ul>
  <li>To edit another database type or different connection:
    <ul>
      <li>Return to the <b>Select Database</b> dropdown and choose another platform.</li>
      <li>Repeat the process—select the connection, review/edit credentials/settings, and use Test and Save.</li>
    </ul>
  </li>
</ul>

<br>

<br>

<b>Use Cases and Benefits</b>
<ul>
  <li><b>Schema Changes:</b> If new tables, columns, or changes in structure have been made in your data source, updating preserves all test case mapping and avoids duplication.</li>
  <li><b>Credential Updates:</b> Handle password rotations, updated access keys or authentication parameters securely.</li>
  <li><b>Infrastructure Migration:</b> Migrate connections seamlessly if servers or cloud endpoints change, keeping all test cases and results intact.</li>
  <li><b>Centralized Management:</b> Avoids proliferation of redundant connections, supporting streamlined maintenance and auditability.</li>
  <li><b>Non-Disruptive Updates:</b> Edits are applied in-place, keeping associated test cases linked and valid.</li>
</ul>

<br>

<b>Detailed Steps</b>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border: none;">
<tr><td style="padding:4px; border: none; vertical-align: top; width: 20px;"><b>1.</b></td><td style="padding:4px; border: none; vertical-align: top; width: 180px;"><b>Access Edit Database:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click Edit Database in the sidebar menu.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>2.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Database Platform Selection:</b></td><td style="padding:4px; border: none; vertical-align: top;">Use the top dropdown to select from available database platforms.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>3.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Select Existing Connection:</b></td><td style="padding:4px; border: none; vertical-align: top;">In the Connection Name dropdown, select the specific connection you wish to modify.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>4.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Edit or Review Parameters:</b></td><td style="padding:4px; border: none; vertical-align: top;">All current connection details are loaded into editable form fields. Update any field as required: Username or password (for changed credentials), Host or port (for infrastructure changes), Special platform fields (like Warehouse, Account ID, Role for Snowflake), Any other relevant settings for your platform.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>5.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Credential Security:</b></td><td style="padding:4px; border: none; vertical-align: top;">Password fields are masked. Use <b>Show Password</b> if you need to reveal input. JSON/key uploads (if present) should be chosen with care and removed once no longer needed.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>6.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Test and Save:</b></td><td style="padding:4px; border: none; vertical-align: top;">Click <b>Test and Save</b> to validate. If successful, the connection updates and any linked tests or jobs will immediately use the new configuration. If there are errors, the form will display messages—correct and retry as needed.</td></tr>
<tr><td style="padding:4px; border: none; vertical-align: top;"><b>7.</b></td><td style="padding:4px; border: none; vertical-align: top;"><b>Repeat for Other Connections/Platforms:</b></td><td style="padding:4px; border: none; vertical-align: top;">Easily switch databases from the dropdown and repeat the process as your environment evolves.</td></tr>
</table>

<br>
<br>

<b>Best Practices</b>
<ul>
  <li>Always use Test and Save to ensure new settings work before deploying to production workflows.</li>
  <li>Update connections routinely after planned changes in your data environment.</li>
  <li>Use clear, unique connection names and document changes for audit purposes.</li>
  <li>Remove obsolete connections to maintain security hygiene.</li>
</ul>

<br>

<b>Security & Audit</b>
<ul>
  <li>All modifications (who, what, when) are logged for security and compliance.</li>
  <li>Passwords and key files are handled with enterprise-grade encryption and never stored in plain text.</li>
  <li>Only authorized users can perform connection edits.</li>
</ul>

<br>
<i>Edit Database lets you keep every data integration up-to-date, secure, and connected—supporting agile data operations without the complexity of rebuilding connections or workflows.</i>
"""
}


}