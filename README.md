# Custom Hooks for ERPNext Doctype Customization  

This repository contains a sample `hooks.py` file designed to help you customize Doctypes in ERPNext using **Custom Apps** while keeping the core system untouched.  

By following the steps below, you can easily add custom fields, configure their behavior, and export fixtures for a seamless upgrade-safe customization experience.  

---

## How to Use  

### Step 1: Add Fields in Doctype Using Customize Doctype  
1. Log in to your ERPNext instance.  
2. Navigate to **Customize Form** in the settings.  
3. Select the Doctype you wish to customize (e.g., Sales Invoice).  
4. Add your required fields, such as **Transport Details** or **Terms of Delivery**, with their respective labels, data types, etc.  

---

### Step 2: Update Field Names in `hooks.py`  
1. Copy the field names you just created from the **Customize Form** page.  
2. Open the `hooks.py` file in this repository.  
3. Locate the relevant section for custom fields and paste your field names as specified in the comments.  

   Example:  
   ```python
   # Custom fields for Sales Invoice
   fixtures = [
       {
           "doctype": "Custom Field",
           "filters": [["name", "in", ["transport_details", "terms_of_delivery"]]]
       }
   ]

# Custom Hooks for ERPNext Doctype Customization  

This repository contains a sample `hooks.py` file designed to help you customize Doctypes in ERPNext using **Custom Apps** while keeping the core system untouched.  

By following the steps below, you can easily configure your customizations and export fixtures for a seamless upgrade-safe experience.  

---

## How to Use  

### Step 3: Export the Fixtures  
1. Once you have updated the field names in the `hooks.py` file, navigate to your local development environment where your custom app is installed.  
2. Run the following command to export the fixtures:  
   ```bash
   bench export-fixtures
   ```
3. The fixtures will be saved in your custom app directory under the `/fixtures` folder.  

---

## Why Use This Approach?  
- Keeps ERPNext's core system intact, enabling smooth upgrades.  
- Ensures your customizations are modular and maintainable.  
- Simplifies collaboration by maintaining a clean separation of customizations.  

---

## Contribute  
Feel free to fork this repository and make improvements or suggestions!  

---

For more details, refer to the example in this repository 
