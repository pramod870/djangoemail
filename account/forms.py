from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import UserMaster, DMFField, DMF, Sales


class UserForm(forms.ModelForm):
    class Meta:
        model = UserMaster
        fields = ('username', 'email', 'isauth', 'role')


class DMFFORM(forms.ModelForm):
    class Meta:
        model = DMFField
        fields = ('field_name',)


class DMFFIELD(forms.ModelForm):
    class Meta:
        model = DMF
        fields = ('form_name',)




class SaleForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields= ['name','Bill_Date','Invoice_No','Tally_MasterID','Total_Inventory_Amount','Total_GST','SGST_AMOUNT']


class CrispySaleForm(SaleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-7 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Bill_Date', css_class='form-group col-md-6 mb-0'),
                Column('Invoice_No', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('Tally_MasterID', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Total_Inventory_Amount', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Total_GST', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('SGST_AMOUNT', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )




from django import forms
from bootstrap_daterangepicker import widgets, fields


class DemoForm(forms.Form):
    # Date Picker Fields
    date_single_normal = fields.DateField()
    date_single_with_format = fields.DateField(
        input_formats=['%d/%m/%Y'],
        widget=widgets.DatePickerWidget(
            format='%d/%m/%Y'
        )
    )
    date_single_clearable = fields.DateField(required=False)

    # Date Range Fields
    date_range_normal = fields.DateRangeField()
    date_range_with_format = fields.DateRangeField(
        input_formats=['%d/%m/%Y'],
        widget=widgets.DateRangeWidget(
            format='%d/%m/%Y'
        )
    )
    date_range_clearable = fields.DateRangeField(required=False)

    # DateTime Range Fields
    datetime_range_normal = fields.DateTimeRangeField()
    datetime_range_with_format = fields.DateTimeRangeField(
        input_formats=['%d/%m/%Y (%I:%M:%S)'],
        widget=widgets.DateTimeRangeWidget(
            format='%d/%m/%Y (%I:%M:%S)'
        )
    )
    datetime_range_clearable = fields.DateTimeRangeField(required=False)