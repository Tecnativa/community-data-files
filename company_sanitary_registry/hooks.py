from openupgradelib import openupgrade

from odoo.tools import config


def pre_init_hook(cr):
    if config["test_enable"]:
        return
    openupgrade.logged_query(
        cr,
        """
        CREATE TABLE IF NOT EXISTS sanitary_registry (id serial primary key, name varchar)
        """,
    )
    # Create sanitary.registry records for values set on company
    openupgrade.logged_query(
        cr,
        """
        INSERT INTO sanitary_registry (name)
        SELECT sanitary_registry
        FROM res_company
        WHERE sanitary_registry IS NOT NULL;
        """,
    )
    openupgrade.logged_query(
        cr,
        """
        ALTER TABLE res_company ADD COLUMN IF NOT EXISTS sanitary_registry_id integer
        """,
    )
    # Assign the sanitary.registry record to res.company
    openupgrade.logged_query(
        cr,
        """
        UPDATE res_company rc
        SET sanitary_registry_id = sr.id FROM sanitary_registry sr
        WHERE sr.name = rc.sanitary_registry
        """,
    )
