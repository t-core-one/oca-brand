# Copyright (C) 2019 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale Brand",
    "summary": "Send branded sales orders",
    "version": "15.0.1.0.4",
    "category": "Sales Management",
    "website": "https://github.com/OCA/brand",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["sale", "brand", "account_brand", "analytic_brand"],
    "data": [
        "views/sale_views.xml",
        "views/crm_team_views.xml",
        "views/res_brand.xml",
    ],
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["osi-scampbell", "sbejaoui"],
}
