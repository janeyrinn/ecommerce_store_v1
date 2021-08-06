from django.forms.widgets import ClearableFileInput
# Using 'as _" means we can now call gettext_lazy() using "_()"
from django.utils.translation import gettext_lazy as _


# creates our own custom class which inherits the built in one
class CustomClearableFileInput(ClearableFileInput):
    """ Override the clear checkbox label, the initial text, and 
    the template name with our own values  """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'