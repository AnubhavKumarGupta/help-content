# help_content/help_manager.py

from home_help import get_home_content
from connection_help import get_connection_content
from database_help import get_database_content
from admin_help import get_admin_content
from testcase_help import get_testcase_content
from schedule_help import get_schedule_content
from account_help import get_account_content


class HelpContentManager:
    """Central manager for all help content across the application"""

    def __init__(self):
        self.help_content = {}
        self.load_all_content()

    def load_all_content(self):
        """Load all help content from different modules"""
        # Load content from all help modules
        self.help_content.update(get_home_content())
        self.help_content.update(get_connection_content())
        self.help_content.update(get_database_content())
        self.help_content.update(get_admin_content())
        self.help_content.update(get_testcase_content())
        self.help_content.update(get_schedule_content())
        self.help_content.update(get_account_content())

    def add_help_content(self, item_name, title, description):
        """Add new help content dynamically"""
        self.help_content[item_name] = {
            "title": title,
            "description": description
        }

    def update_help_content(self, item_name, title=None, description=None):
        """Update existing help content"""
        if item_name in self.help_content:
            if title:
                self.help_content[item_name]["title"] = title
            if description:
                self.help_content[item_name]["description"] = description

    def get_all_items(self):
        """Get list of all available help items"""
        return list(self.help_content.keys())

    def search_content(self, search_term):
        """Search help content by title or description"""
        results = {}
        search_term = search_term.lower()

        for item_name, content in self.help_content.items():
            title = content["title"].lower()
            description = content["description"].lower()

            if search_term in title or search_term in description:
                results[item_name] = content

        return results

    def get_category_items(self, category):
        """Get items belonging to a specific category"""
        category_map = {
            "connection": ["Connection", "Create Connection", "Edit Connection", "Delete Connection"],
            "database": ["Database", "Oracle", "SQL Server", "MySQL", "PostgreSQL", "Snowflake",
                        "Google BigQuery", "Amazon RedShift", "Azure Synapse", "Databricks", "StarRocks", "Edit Database"],
            "admin": ["Admin", "Create New User", "Edit User", "Update Logout Time", "Password Reset"],
            "testcase": ["Create Test Case", "Show Test Case", "Show Test Results"],
            "schedule": ["Schedule", "Show Scheduled Jobs"],
            "account": ["Change Password", "Logout"],
            "home": ["Home"]
        }

        items = {}
        if category.lower() in category_map:
            for item_name in category_map[category.lower()]:
                if item_name in self.help_content:
                    items[item_name] = self.help_content[item_name]

        return items

    def get_help_content(self, item_name):
        """Get help content for a specific menu item"""
        if item_name in self.help_content:
            return self.help_content[item_name]
        else:
            # Return default content for undefined items
            return {
                "title": f"{item_name} - Help Content",
                "description": f"""
<b>Help for {item_name}</b>

This section is part of the INFOFISCUS Data Validation Tool.

<b>Content Status:</b>
The detailed help content for '{item_name}' is currently being prepared
and will be available soon.

<b>General Information:</b>
This feature is part of the comprehensive data validation workflow
that helps ensure data quality and integrity across your organization's
database systems.

<b>Support:</b>
For immediate assistance with '{item_name}', please contact your
system administrator or refer to the user documentation.

<b>Common Features:</b>
Most sections in INFOFISCUS provide:
• Step-by-step guidance for operations
• Best practices and recommendations
• Security and compliance information
• Troubleshooting and error resolution

<b>Navigation Tip:</b>
Try exploring related menu items or parent sections for additional
context and information about this feature.

Current selection: <b>{item_name}</b>
"""
            }

    def validate_content_structure(self):
        """Validate that all help content follows the expected structure"""
        valid_structure = True
        issues = []

        for item_name, content in self.help_content.items():
            if not isinstance(content, dict):
                issues.append(f"Content for '{item_name}' is not a dictionary")
                valid_structure = False
                continue

            if "title" not in content:
                issues.append(f"Content for '{item_name}' missing 'title' field")
                valid_structure = False

            if "description" not in content:
                issues.append(f"Content for '{item_name}' missing 'description' field")
                valid_structure = False

            if "title" in content and not isinstance(content["title"], str):
                issues.append(f"Title for '{item_name}' is not a string")
                valid_structure = False

            if "description" in content and not isinstance(content["description"], str):
                issues.append(f"Description for '{item_name}' is not a string")
                valid_structure = False

        return valid_structure, issues

    def get_content_statistics(self):
        """Get statistics about the help content"""
        stats = {
            "total_items": len(self.help_content),
            "categories": {},
            "average_description_length": 0,
            "items_with_html": 0
        }

        # Calculate category counts
        category_map = {
            "connection": ["Connection", "Create Connection", "Edit Connection", "Delete Connection"],
            "database": ["Database", "Oracle", "SQL Server", "MySQL", "PostgreSQL", "Snowflake",
                        "Google BigQuery", "Amazon RedShift", "Azure Synapse", "Databricks", "StarRocks", "Edit Database"],
            "admin": ["Admin", "Create New User", "Edit User", "Update Logout Time", "Password Reset"],
            "testcase": ["Create Test Case", "Show Test Case", "Show Test Results"],
            "schedule": ["Schedule", "Show Scheduled Jobs"],
            "account": ["Change Password", "Logout"],
            "home": ["Home"]
        }

        for category, items in category_map.items():
            stats["categories"][category] = len([item for item in items if item in self.help_content])

        # Calculate description statistics
        total_length = 0
        html_count = 0
        
        for content in self.help_content.values():
            desc_length = len(content.get("description", ""))
            total_length += desc_length
            
            if "<" in content.get("description", "") and ">" in content.get("description", ""):
                html_count += 1

        stats["average_description_length"] = total_length // len(self.help_content) if self.help_content else 0
        stats["items_with_html"] = html_count

        return stats