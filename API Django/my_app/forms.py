from django import forms


class PredForm(forms.Form):
    Age = forms.FloatField(label='Age')
    family_history_with_overweight = forms.BooleanField(initial=False, required=False,
                                                        label='family_history_with_overweight')
    FAVC = forms.BooleanField(initial=False, required=False, label='FAVC')
    FCVC = forms.FloatField(label='FCVC')
    NCP = forms.FloatField(label='NCP')
    CAEC = forms.IntegerField(label='CAEC')
    SMOKE = forms.BooleanField(initial=False, required=False, label='SMOKE')
    CH2O = forms.FloatField(initial=False, required=False, label='CH2O')
    SCC = forms.BooleanField(initial=False, required=False, label='SCC')
    FAF = forms.FloatField(label='FAF')
    TUE = forms.FloatField(label='TUE')
    CALC = forms.IntegerField(label='CALC')
    Male = forms.IntegerField(label='Male')
    Female = forms.IntegerField(label='Female')
    Public_Transportation = forms.IntegerField(
        label='Public_Transportation')
    Automobile = forms.IntegerField(label='Automobile')
    Motorbike = forms.IntegerField(label='Motorbike')
    Bike = forms.IntegerField(label='Bike')
    Walking = forms.IntegerField(label='Walking')
