# feedback/forms.py
from django import forms
from .models import ProductFeedback

# Define your product options
PRODUCT_CHOICES = [
    ('iPhone 15', 'iPhone 15'),
    ('Samsung Galaxy S24', 'Samsung Galaxy S24'),
    ('OnePlus 12', 'OnePlus 12'),
    ('MacBook Air M2', 'MacBook Air M2'),
    ('MacBook Pro M2', 'MacBook Pro M2'),
    ('Dell XPS 13', 'Dell XPS 13'),
    ('Dell XPS 15', 'Dell XPS 15'),
    ('HP Spectre x360', 'HP Spectre x360'),
    ('Lenovo ThinkPad X1 Carbon', 'Lenovo ThinkPad X1 Carbon'),
    ('Apple Watch Series 9', 'Apple Watch Series 9'),
    ('Samsung Galaxy Watch 6', 'Samsung Galaxy Watch 6'),
    ('Bose QuietComfort 45', 'Bose QuietComfort 45'),
    ('Sony WH-1000XM5', 'Sony WH-1000XM5'),
    ('JBL Flip 7', 'JBL Flip 7'),
    ('Nintendo Switch OLED', 'Nintendo Switch OLED'),
    ('PlayStation 5', 'PlayStation 5'),
    ('Xbox Series X', 'Xbox Series X'),
    ('Kindle Paperwhite', 'Kindle Paperwhite'),
    ('GoPro Hero 12', 'GoPro Hero 12'),
    ('DJI Mavic 3', 'DJI Mavic 3'),
    ('Google Pixel 9', 'Google Pixel 9'),
    ('Amazon Echo Dot', 'Amazon Echo Dot'),
    ('Apple iPad Air', 'Apple iPad Air'),
    ('Samsung Galaxy Tab S9', 'Samsung Galaxy Tab S9'),
    ('Logitech MX Master 3', 'Logitech MX Master 3'),
    ('Razer DeathAdder V3', 'Razer DeathAdder V3'),
    ('Corsair K95 Keyboard', 'Corsair K95 Keyboard'),
    ('NVIDIA RTX 4090', 'NVIDIA RTX 4090'),
    ('AMD Radeon RX 7900 XT', 'AMD Radeon RX 7900 XT'),
]

class ProductFeedbackForm(forms.ModelForm):
    product_name = forms.ChoiceField(choices=PRODUCT_CHOICES)  # Dropdown

    class Meta:
        model = ProductFeedback
        fields = ['name', 'product_name', 'rating', 'comments']
