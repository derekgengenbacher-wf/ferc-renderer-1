from ferc_renderer.render import FERCRenderException, get_fact_by_local_name

TEMPLATE_SET_LOCATIONS = {
    '1': 'https://github.com/ferc_rendering_templates/Form_1.zip',
    '1F': 'https://github.com/ferc_rendering_templates/Form_1F.zip',
    '1/3-Q': 'https://github.com/ferc_rendering_templates/Form_3Q_Electric.zip',
    '2': 'https://github.com/ferc_rendering_templates/Form_2.zip',
    '2A': 'https://github.com/ferc_rendering_templates/Form_2A.zip',
    '2/3-Q': 'https://github.com/ferc_rendering_templates/Form_3Q_Gas.zip',
    '6': 'https://github.com/ferc_rendering_templates/Form_6.zip',
    '6Q': 'https://github.com/ferc_rendering_templates/Form_6Q.zip',
    '60': 'https://github.com/ferc_rendering_templates/Form_60.zip',
    '714': 'https://github.com/ferc_rendering_templates/Form_714.zip'
}

CSS_FILE_LOCATION = 'https://github.com/ferc_rendering_css/form-template.css'


def determine_template(modelXbrl):
    """"
    Determine the correct template to use based on the FormType from the model xbrl

    :param modelXbrl: The model from which to get form type
    :type modelXbrl: :class: `~arelle.ModelXbrl.ModelXbrl`
    :return: The location of the rendering template to use
    :rtype: str
    """
    form_type_fact = get_fact_by_local_name(modelXbrl, 'FormType')
    if form_type_fact is not None:
        template_set_location = TEMPLATE_SET_LOCATIONS.get(str(form_type_fact.value))
        if template_set_location is not None:
            return template_set_location
    raise FERCRenderException(
        'Cannot find the correct form template for form: //{}//'.format(
            form_type_fact.value if form_type_fact is not None else None
        )
    )
