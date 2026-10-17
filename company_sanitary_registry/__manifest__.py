# Copyright 2023 Tecnativa - Carlos Roca
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Sanitary Registry",
    "version": "20.0.1.0.0",
    "depends": ["stock"],
    "data": [
        "templates/sanitary_registry_template.xml",
        "views/res_company_view.xml",
        "views/sanitary_registry_view.xml",
        "views/sanitary_registry_warehouse_category_views.xml",
        "security/ir.access.csv",
    ],
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/community-data-files",
    "license": "AGPL-3",
    "installable": True,
}
