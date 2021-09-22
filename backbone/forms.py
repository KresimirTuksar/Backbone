from django import forms
from django.db.models import fields
from django.core.exceptions import ValidationError
from django.forms.models import ModelForm
from .models import *

class MjestoForm(forms.ModelForm):

    class Meta:
        model = Mjesto
        fields = ['naziv']
        

class PodrucjeForm(forms.ModelForm):

    class Meta:
        model = Podrucje
        fields = ['naziv', 'dc']




class OdkForm(forms.ModelForm):

    class Meta:
        model = Odk
        fields = ['naziv']


class DionicaForm(forms.ModelForm):

    class Meta:
        model = Dionica
        fields = ['rb', 'naziv', 'duzina']

class DionicaEditForm(forms.ModelForm):

    class Meta:
        model = Dionica
        fields = ['rb', 'naziv']


class KabelForm(forms.ModelForm):

    class Meta:
        model = Kabel
        fields = ['segment','odk','broj_niti','napomena']

class KabelEditForm(forms.ModelForm):

    class Meta:
        model = Kabel
        exclude = ['rijeseno','radna_duzina','azurirao']
        

class BiljeskaForm(forms.ModelForm):

    class Meta:
        model = Biljeska
        fields = ['sadrzaj']



class IzvrsavanjeForm(forms.ModelForm):

    class Meta:
        model = Kabel
        fields = ['status', 'pocetna', 'zavrsna']

    def clean(self):
        super(IzvrsavanjeForm, self).clean()
        # dohvacanje vrijednosti u poljima
        status = self.cleaned_data.get('status')
        pocetna = self.cleaned_data.get('pocetna')
        zavrsna = self.cleaned_data.get('zavrsna')
        radna_duzina = self.cleaned_data.get('radna_duzina')

        if status == 'Riješeno':
            if not pocetna:
                self._errors['pocetna'] = self.error_class(['Ovo polje je obavezno'])
            if not zavrsna:
                self._errors['zavrsna'] = self.error_class(['Ovo polje je obavezno'])
            
            if pocetna and zavrsna:
                if abs(pocetna - zavrsna)<1:
                    raise ValidationError(
                        "Početna i završna stacionaža ne mogu biti jednake vrijednosti"
                    )
                    self._errors['pocetna'] = self.error_class([''])
                    self._errors['pocetna'] = self.error_class([''])
        

        return self.cleaned_data


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class KabelSearchForm(forms.ModelForm):

    class Meta:
        model = Kabel
        fields = ['segment','dionica','odk', 'status']