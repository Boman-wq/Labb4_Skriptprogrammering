from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, RadioField, SelectField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField

class RegisterForm(FlaskForm):
    """Klass för att hantera formulär"""
    Betalsatt = SelectField("Korttyp", choices=[('visa', 'VISA'), ('mastercard', 'MasterCard'), ('americanexpress', 'AMERICAN EXPRESS')])
    Fornamn = StringField("Förnamn:")
    Efternamn = StringField("Efternamn:")
    Adress = StringField("Adress:")
    Postnummer = StringField("Postnummer")
    Ort = StringField(" och ort:")
    Mobil = IntegerField("Mobil:")
    E_post = EmailField("E-post:")
    Losenord = PasswordField("Password:")
    Erbjudandedn_via_e_post = BooleanField("Erbjudanden via e-post:")
    E_postformat = RadioField("E-postformat:", choices=[('HTML','HTML'),('text','Text')])
    Kommentarer = TextAreaField("Dina kommentarer:", render_kw={"rows": 8, "cols": 70})