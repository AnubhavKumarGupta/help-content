import sys
import os
# Add help_content directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
help_content_dir = os.path.join(current_dir, 'help_content')
sys.path.insert(0, help_content_dir)

# Try PyQt6 first, fallback to PyQt5
try:
    from PyQt6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout,
        QTreeWidget, QTreeWidgetItem, QLabel, QHBoxLayout,
        QStyledItemDelegate, QStyleOptionViewItem, QStyle,
        QScrollArea, QFrame
    )
    from PyQt6.QtGui import QIcon, QBrush, QColor, QFont, QPainter, QPalette, QScreen
    from PyQt6.QtCore import Qt, QRect
    PYQT6 = True
except ImportError:
    from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout,
        QTreeWidget, QTreeWidgetItem, QLabel, QHBoxLayout,
        QStyledItemDelegate, QStyleOptionViewItem, QStyle,
        QScrollArea, QFrame
    )
    from PyQt5.QtGui import QIcon, QBrush, QColor, QFont, QPainter, QPalette
    from PyQt5.QtCore import Qt, QRect
    PYQT6 = False

# Import updated help content manager
from help_manager import HelpContentManager

# =============================================================================
# CONFIGURATION MODULE - Change sizes here
# =============================================================================
class UIConfig:
    """Centralized configuration for all UI elements"""
    
    # Base font sizes (will be scaled based on screen DPI)
    BASE_SIDEBAR_TEXT_SIZE = 13      # Sidebar navigation text
    BASE_TITLE_SIZE = 20             # Main heading/title
    BASE_DESCRIPTION_SIZE = 12       # Description text
    BASE_DESCRIPTION_HEADING_SIZE = 16  # Sub-headings in descriptions
    
    # Panel sizes
    SIDEBAR_WIDTH = 300              # Left navigation panel width
    
    # Get screen scale factor for responsive design
    @staticmethod
    def get_scale_factor():
        """Get screen scale factor for responsive fonts"""
        try:
            if PYQT6:
                screen = QApplication.primaryScreen()
                return screen.logicalDotsPerInch() / 96.0  # 96 DPI is standard
            else:
                # PyQt5 fallback
                desktop = QApplication.desktop()
                return desktop.logicalDpiX() / 96.0
        except:
            return 1.0  # Fallback to no scaling
    
    @classmethod
    def get_scaled_font_size(cls, base_size):
        """Get font size scaled for current screen"""
        scale = cls.get_scale_factor()
        return int(base_size * scale)
    
    @classmethod
    def get_sidebar_font_size(cls):
        """Get scaled sidebar text font size"""
        return cls.get_scaled_font_size(cls.BASE_SIDEBAR_TEXT_SIZE)
    
    @classmethod
    def get_title_font_size(cls):
        """Get scaled title font size"""
        return cls.get_scaled_font_size(cls.BASE_TITLE_SIZE)
    
    @classmethod
    def get_description_font_size(cls):
        """Get scaled description font size"""
        return cls.get_scaled_font_size(cls.BASE_DESCRIPTION_SIZE)
    
    @classmethod
    def get_description_heading_font_size(cls):
        """Get scaled description heading font size"""
        return cls.get_scaled_font_size(cls.BASE_DESCRIPTION_HEADING_SIZE)
    
    @classmethod
    def get_scaled_sidebar_width(cls):
        """Get scaled sidebar width"""
        scale = cls.get_scale_factor()
        return int(cls.SIDEBAR_WIDTH * scale)

# =============================================================================
# FONT MANAGEMENT MODULE
# =============================================================================
class FontManager:
    """Centralized font management"""
    
    @staticmethod
    def create_sidebar_font():
        """Create font for sidebar navigation"""
        font = QFont('Roboto', UIConfig.get_sidebar_font_size())
        font.setFamily('Roboto, Open Sans, Arial, Helvetica, sans-serif')
        return font
    
    @staticmethod
    def create_title_font():
        """Create font for main titles"""
        font = QFont()
        font.setPointSize(UIConfig.get_title_font_size())
        font.setBold(True)
        return font
    
    @staticmethod
    def create_description_font():
        """Create font for description text"""
        font = QFont()
        font.setPointSizeF(UIConfig.get_description_font_size())
        return font
    
    @staticmethod
    def create_description_heading_font():
        """Create font for description headings/subheadings"""
        font = QFont()
        font.setPointSize(UIConfig.get_description_heading_font_size())
        font.setBold(True)
        return font

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================
def align_center():
    return Qt.AlignmentFlag.AlignCenter if PYQT6 else Qt.AlignCenter

def align_left():
    return Qt.AlignmentFlag.AlignLeft if PYQT6 else Qt.AlignLeft

def run_app(app):
    sys.exit(app.exec() if PYQT6 else app.exec_())

def get_icon_path(icon_filename):
    """Get the full path to an icon file"""
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "icons", icon_filename)
    return icon_path

def create_icon(icon_filename):
    """Create a QIcon from an icon filename"""
    icon_path = get_icon_path(icon_filename)
    return QIcon(icon_path)

# -------- Delegate: draw bg only where we want (icon + text) ----------
class IconTextHighlightDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hover_sel_color = QColor("#068293")   # teal for normal items
        self.logout_color = QColor("#d55534")      # red for logout
        self.text_white = QColor("white")
        self.radius = 5
        self.hpad = 8
        self.vpad = 4
        self.State_Selected = QStyle.StateFlag.State_Selected
        self.State_MouseOver = QStyle.StateFlag.State_MouseOver
        self.SE_Text = QStyle.SubElement.SE_ItemViewItemText
        self.SE_Icon = QStyle.SubElement.SE_ItemViewItemDecoration

    def _content_rect(self, opt, style):
        """Union of icon + text rect => we highlight exactly this area."""
        text_rect = style.subElementRect(self.SE_Text, opt, opt.widget)
        icon_rect = style.subElementRect(self.SE_Icon, opt, opt.widget)
        combined = text_rect.united(icon_rect)
        return QRect(
            combined.left() - self.hpad,
            combined.top() - self.vpad,
            combined.width() + 2 * self.hpad,
            combined.height() + 2 * self.vpad,
        )

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index):
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)
        style = opt.widget.style() if opt.widget else QApplication.style()
        label = str(index.data()) if index.data() is not None else ""
        is_logout = label.strip().lower() == "logout"
        is_selected = bool(opt.state & self.State_Selected)
        is_hover = bool(opt.state & self.State_MouseOver)
        content_rect = self._content_rect(opt, style)

        # ---- draw background (rounded) ----
        paint_bg = is_logout or is_selected or is_hover
        bg_color = self.logout_color if is_logout else self.hover_sel_color if is_selected or is_hover else None
        if paint_bg:
            painter.save()
            painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
            painter.setBrush(bg_color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRoundedRect(content_rect, self.radius, self.radius)
            painter.restore()
            # ensure text is white on top of colored bg
            pal = opt.palette
            pal.setColor(QPalette.ColorRole.Text, self.text_white)
            pal.setColor(QPalette.ColorRole.HighlightedText, self.text_white)
            opt.palette = pal

        # stop default full-row highlight
        orig_state = opt.state
        if is_selected:
            opt.state &= ~self.State_Selected
        if is_hover:
            opt.state &= ~self.State_MouseOver

        # normal paint (icon + text)
        super().paint(painter, opt, index)
        opt.state = orig_state

# -------- Help Content Widget ----------
class HelpContentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Create scroll area for long content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Content widget inside scroll area
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(15)
        self.content_widget.setStyleSheet("background-color: #182334; color: white;")
        
        # Title label - using FontManager for consistent styling
        self.title_label = QLabel()
        self.title_label.setAlignment(align_center())
        self.title_label.setWordWrap(True)
        self.title_label.setFont(FontManager.create_title_font())
        self.title_label.setStyleSheet("color: #068293; margin-bottom: 10px;")
        
        # Description label - using FontManager for consistent styling
        self.description_label = QLabel()
        self.description_label.setAlignment(align_left())
        self.description_label.setWordWrap(True)
        self.description_label.setFont(FontManager.create_description_font())
        self.description_label.setStyleSheet(f"""
                color: white;
                line-height: 1.6;
                padding: 10px;
                background-color: #182334;
                border-radius: 0;
            """)
        
        # Add labels to content layout
        self.content_layout.addWidget(self.title_label)
        self.content_layout.addWidget(self.description_label)
        self.content_layout.addStretch()
        
        # Set content widget to scroll area
        scroll.setWidget(self.content_widget)
        layout.addWidget(scroll)
        
    def update_content(self, title, description):
        """Update the help content dynamically"""
        self.title_label.setText(title)
        # Enable rich text formatting and apply heading styles
        formatted_description = self.apply_heading_styles(description)
        self.description_label.setTextFormat(Qt.TextFormat.RichText)
        self.description_label.setText(formatted_description)
    
    def apply_heading_styles(self, text):
        """Apply consistent heading styles to description text"""
        # You can customize this to match your content format
        # Example: Replace markdown-style headers with styled HTML
        heading_size = UIConfig.get_description_heading_font_size()
        
        # Replace ### with styled headings
        text = text.replace('### ', f'<h3 style="font-size: {heading_size}px; color: #068293; font-weight: bold; margin-top: 15px; margin-bottom: 10px;">')
        text = text.replace('## ', f'<h2 style="font-size: {heading_size + 2}px; color: #068293; font-weight: bold; margin-top: 20px; margin-bottom: 10px;">')
        text = text.replace('# ', f'<h1 style="font-size: {heading_size + 4}px; color: #068293; font-weight: bold; margin-top: 25px; margin-bottom: 15px;">')
        
        # Close any unclosed heading tags (basic implementation)
        for tag in ['h1', 'h2', 'h3']:
            if f'<{tag} style=' in text and f'</{tag}>' not in text:
                # Find line breaks after headings and close tags
                import re
                pattern = f'(<{tag} style="[^"]*">)([^<\n]*?)(\n|$)'
                text = re.sub(pattern, f'\\1\\2</{tag}>\\3', text)
        
        return text

# -------- Main Window with Modular Help System ----------
class MainWindowHelp(QMainWindow):
    def __init__(self, page_key=None):
        super().__init__()
        self.setWindowTitle("INFOFISCUS DATA VALIDATION TOOL")
        
        # Set window icon using proper path resolution
        window_icon_path = get_icon_path("infometry.png")
        self.setWindowIcon(QIcon(window_icon_path))
        
        self.resize(1200, 700)
        
        # Initialize help content manager with all modules
        self.help_manager = HelpContentManager()
        
        # Updated page map to include all database types
        self.page_map = {
            "home": ["Home"],
            "con": ["Connection"],
            "con_cc": ["Connection", "Create Connection"],
            "con_cc_db": ["Connection", "Create Connection", "Database"],
            "con_cc_db_or": ["Connection", "Create Connection", "Database", "Oracle"],
            "con_cc_db_ss": ["Connection", "Create Connection", "Database", "SQL Server"],
            "con_cc_db_ms": ["Connection", "Create Connection", "Database", "MySQL"],
            "con_cc_db_sr": ["Connection", "Create Connection", "Database", "StarRocks"],
            "con_cc_db_pg": ["Connection", "Create Connection", "Database", "PostgreSQL"],
            "con_cc_db_sf": ["Connection", "Create Connection", "Database", "Snowflake"],
            "con_cc_db_gbq": ["Connection", "Create Connection", "Database", "Google BigQuery"],
            "con_cc_db_ar": ["Connection", "Create Connection", "Database", "Amazon RedShift"],
            "con_cc_db_as": ["Connection", "Create Connection", "Database", "Azure Synapse"],
            "con_cc_db_dbks": ["Connection", "Create Connection", "Database", "Databricks"],
            "con_ec": ["Connection", "Edit Connection"],
            "con_ec_ed": ["Connection", "Edit Connection", "Edit Database"],
            "con_dc": ["Connection", "Delete Connection"],
            "ctc": ["Create Test Case"],
            "stc": ["Show Test Case"],
            "str": ["Show Test Results"],
            "adm": ["Admin"],
            "adm_cnu": ["Admin", "Create New User"],
            "adm_eu": ["Admin", "Edit User"],
            "adm_ult": ["Admin", "Update Logout Time"],
            "adm_pr": ["Admin", "Password Reset"],
            "chg_pwd": ["Change Password"],
            "sch": ["Schedule"],
            "sh_sch": ["Show Scheduled Jobs"],
            "logout": ["Logout"]
        }
        
        self.init_ui(page_key)

    def init_ui(self, page_key):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        
        self.sidebar = self.create_sidebar()
        self.help_widget = HelpContentWidget()
        
        # Apply styling to help widget
        self.help_widget.setStyleSheet("background-color: #182334; color: white;")
        
        # Set initial help content (Home page)
        home_content = self.help_manager.get_help_content("Home")
        self.help_widget.update_content(home_content["title"], home_content["description"])
        
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.help_widget, 1)  # Give help widget more space
        
        self.apply_custom_theme()
        
        if page_key in self.page_map:
            self.select_item_by_text(self.page_map[page_key])

    def create_sidebar(self):
        tree = QTreeWidget()
        tree.setHeaderHidden(True)
        tree.setFixedWidth(UIConfig.get_scaled_sidebar_width())  # Using scaled width
        tree.setMouseTracking(True)
        
        # Apply font to the entire tree widget
        tree.setFont(FontManager.create_sidebar_font())
        
        self.tree_items = {}
        tree.setItemDelegate(IconTextHighlightDelegate(tree))

        def add_item(parent, label, icon_file):
            item = QTreeWidgetItem([label])
            item.setIcon(0, create_icon(icon_file))
            parent.addChild(item)
            self.tree_items[label] = item
            return item

        def add_top(label, icon_file):
            item = QTreeWidgetItem([label])
            item.setIcon(0, create_icon(icon_file))
            self.tree_items[label] = item
            tree.addTopLevelItem(item)
            return item

        # Sidebar structure with all databases
        add_top("Home", "home.png")
        connection = add_top("Connection", "connection.png")
        create_conn = add_item(connection, "Create Connection", "create_connection.png")
        db = add_item(create_conn, "Database", "database.png")
        
        # All supported database types
        db_types = [
            ("Oracle", "oracle.png"),
            ("SQL Server", "sql_server.png"),
            ("MySQL", "mysql.png"),
            ("StarRocks", "starrocks.png"),
            ("PostgreSQL", "postgresql.png"),
            ("Snowflake", "snowflake.png"),
            ("Google BigQuery", "bigquery.png"),
            ("Amazon RedShift", "redshift.png"),
            ("Azure Synapse", "synapse.png"),
            ("Databricks", "databricks.png")
        ]
        
        for db_type, icon_file in db_types:
            add_item(db, db_type, icon_file)

        edit_conn = add_item(connection, "Edit Connection", "edit_connection.png")
        add_item(edit_conn, "Edit Database", "edit_database.png")
        add_item(connection, "Delete Connection", "delete_connection.png")

        # Test Case Management
        add_top("Create Test Case", "create_test_case.png")
        add_top("Show Test Case", "show_test_case.png")
        add_top("Show Test Results", "show_test_results.png")

        # Administration
        admin = add_top("Admin", "admin.png")
        admin_items = [
            ("Create New User", "create_user.png"),
            ("Edit User", "edit_user.png"),
            ("Update Logout Time", "logout_time.png"),
            ("Password Reset", "password_reset.png")
        ]
        for label, icon_file in admin_items:
            add_item(admin, label, icon_file)

        # Account Management
        add_top("Change Password", "change_password.png")
        
        # Scheduling
        add_top("Schedule", "schedule.png")
        add_top("Show Scheduled Jobs", "show_jobs.png")
        
        # Logout
        logout = add_top("Logout", "logout.png")
        logout.setForeground(0, QBrush(QColor("white")))
        logout_font = FontManager.create_sidebar_font()
        logout_font.setBold(True)
        logout.setFont(0, logout_font)

        tree.itemClicked.connect(self.handle_click)
        return tree

    def handle_click(self, item, column):
        """Handle menu item clicks and update help content"""
        label = item.text(0)
        content = self.help_manager.get_help_content(label)
        self.help_widget.update_content(content["title"], content["description"])

    def select_item_by_text(self, path_list):
        parent = None
        item = None
        for label in path_list:
            item = self.tree_items.get(label)
            if item:
                if parent:
                    parent.setExpanded(True)
                parent = item
        if item:
            self.sidebar.setCurrentItem(item)
            # Update help content for selected item
            final_label = path_list[-1]
            content = self.help_manager.get_help_content(final_label)
            self.help_widget.update_content(content["title"], content["description"])

    def add_custom_help_content(self, item_name, title, description):
        """Method to add new help content dynamically"""
        self.help_manager.add_help_content(item_name, title, description)

    def get_help_statistics(self):
        """Get help content statistics for debugging"""
        return self.help_manager.get_content_statistics()

    def validate_help_content(self):
        """Validate help content structure"""
        return self.help_manager.validate_content_structure()

    def apply_custom_theme(self):
        # Get scaled font size for dynamic CSS
        sidebar_font_size = UIConfig.get_sidebar_font_size()
        
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: #182334;
                color: white;
            }}
            QTreeWidget {{
                background-color: #182334;
                border-right: 1px solid #333;
                color: white;
                font-size: {sidebar_font_size}px;
                font-family: 'Roboto', 'Open Sans', Arial, Helvetica, sans-serif
            }}
            QScrollArea {{
                background-color: #182334;
                border: 1px solid #333;
                border-radius: 8px;
            }}
            QScrollArea > QWidget > QWidget {{
                background-color: #182334;
            }}
            QScrollBar:vertical {{
                background-color: #182334;
                width: 12px;
                border-radius: 6px;
            }}
            QScrollBar::handle:vertical {{
                background-color: #182334;
                border-radius: 6px;
                min-height: 20px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: #182334;
            }}
            QTreeWidget::item {{
                padding: 5px;
            }}
        """)

if __name__ == "__main__":
    page_key = sys.argv[1] if len(sys.argv) > 1 else None
    app = QApplication(sys.argv)
    
    # Validate help content on startup (optional debugging)
    window = MainWindowHelp(page_key=page_key)
    is_valid, issues = window.validate_help_content()
    if not is_valid:
        print("Help content validation issues found:")
        for issue in issues:
            print(f"  - {issue}")
    
    # Print current scaling info for debugging
    scale_factor = UIConfig.get_scale_factor()
    print(f"Screen scale factor: {scale_factor:.2f}")
    print(f"Scaled font sizes - Sidebar: {UIConfig.get_sidebar_font_size()}px, Title: {UIConfig.get_title_font_size()}px")
    
    window.show()
    run_app(app)