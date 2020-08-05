from django import forms


class SelecioneIdade(forms.Form):
    MY_CHOICES = (
        ('0', 'Adulto'),
        ('1', 'Idoso'),
        ('2', 'Jovem'),
    )
    idade = forms.ChoiceField(
        label='Selecione a idade',
        choices=MY_CHOICES,
        widget=forms.Select(
            attrs={'class': 'styled-select yellow rounded'}))


class GrauRisco(forms.Form):
    MY_CHOICES = (
        ('0', 'Aventureiro'),
        ('1', 'Cauteloso'),
        ('2', 'Ousado'),
        ('3', 'Normal')
    )
    risco = forms.ChoiceField(
        label='Estilo de Uso',
        choices=MY_CHOICES,
        widget=forms.Select(
            attrs={'class': 'styled-select yellow rounded'}))


class ModeloVeiculo(forms.Form):
    MY_CHOICES = (
        ('0', 'Economico'),
        ('1', 'Sedan'),
        ('2', 'Carro Esportivo'),
        ('3', 'Luxo'),
        ('4', 'Super Luxo')
    )
    veiculo = forms.ChoiceField(
        label='Modelo do Veiculo',
        choices=MY_CHOICES,
        widget=forms.Select(
            attrs={'class': 'styled-select yellow rounded'}))
