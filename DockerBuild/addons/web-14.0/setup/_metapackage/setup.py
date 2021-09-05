import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-web",
    description="Meta package for oca-web Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-web_access_rule_buttons',
        'odoo14-addon-web_advanced_search',
        'odoo14-addon-web_company_color',
        'odoo14-addon-web_copy_confirm',
        'odoo14-addon-web_decimal_numpad_dot',
        'odoo14-addon-web_dialog_size',
        'odoo14-addon-web_domain_field',
        'odoo14-addon-web_drop_target',
        'odoo14-addon-web_environment_ribbon',
        'odoo14-addon-web_group_expand',
        'odoo14-addon-web_ir_actions_act_multi',
        'odoo14-addon-web_ir_actions_act_view_reload',
        'odoo14-addon-web_listview_range_select',
        'odoo14-addon-web_m2x_options',
        'odoo14-addon-web_no_bubble',
        'odoo14-addon-web_notify',
        'odoo14-addon-web_refresher',
        'odoo14-addon-web_responsive',
        'odoo14-addon-web_sheet_full_width',
        'odoo14-addon-web_timeline',
        'odoo14-addon-web_tree_dynamic_colored_field',
        'odoo14-addon-web_tree_image_tooltip',
        'odoo14-addon-web_tree_many2one_clickable',
        'odoo14-addon-web_widget_bokeh_chart',
        'odoo14-addon-web_widget_dropdown_dynamic',
        'odoo14-addon-web_widget_url_advanced',
        'odoo14-addon-web_widget_x2many_2d_matrix',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
