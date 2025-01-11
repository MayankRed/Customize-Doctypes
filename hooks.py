app_name = "customerpnext"
app_title = "Custom ErpNext"
app_publisher = "Mayank Nandwani"
app_description = "This is custom ErpNext app"
app_email = "nandwanimayank16d@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []
fixtures = [{
        "dt": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Sales Invoice-custom_terms_of_delivery",
                    "Sales Invoice-custom_freight",
                    "Sales Invoice-custom_vehicle",
                    "Sales Invoice-custom_transport"
                ]
            ]
        ]
    }, "Client Script",
    ]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "customhelp",
# 		"logo": "/assets/customhelp/logo.png",
# 		"title": "Custom Help",
# 		"route": "/customhelp",
# 		"has_permission": "customhelp.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/customhelp/css/customhelp.css"
# app_include_js = "/assets/customhelp/js/customhelp.js"

# include js, css files in header of web template
# web_include_css = "/assets/customhelp/css/customhelp.css"
# web_include_js = "/assets/customhelp/js/customhelp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "customhelp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "customhelp/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "customhelp.utils.jinja_methods",
# 	"filters": "customhelp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "customhelp.install.before_install"
# after_install = "customhelp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "customhelp.uninstall.before_uninstall"
# after_uninstall = "customhelp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "customhelp.utils.before_app_install"
# after_app_install = "customhelp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "customhelp.utils.before_app_uninstall"
# after_app_uninstall = "customhelp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "customhelp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"customhelp.tasks.all"
# 	],
# 	"daily": [
# 		"customhelp.tasks.daily"
# 	],
# 	"hourly": [
# 		"customhelp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"customhelp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"customhelp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "customhelp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "customhelp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "customhelp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["customhelp.utils.before_request"]
# after_request = ["customhelp.utils.after_request"]

# Job Events
# ----------
# before_job = ["customhelp.utils.before_job"]
# after_job = ["customhelp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"customhelp.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

