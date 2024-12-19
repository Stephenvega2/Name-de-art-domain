from kivy.app import App
from kivy.uix.image import Image as KivyImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from art_generator import generate_art

class ArtApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.image = KivyImage(source='art.png')
        layout.add_widget(self.image)

        self.file_name_input = TextInput(hint_text='Enter file name', multiline=False)
        layout.add_widget(self.file_name_input)

        self.domain_name_input = TextInput(hint_text='Enter domain name', multiline=False)
        layout.add_widget(self.domain_name_input)

        btn = Button(text='Generate Art')
        btn.bind(on_press=self.update_image)
        layout.add_widget(btn)

        return layout

    def update_image(self, instance):
        file_name = self.file_name_input.text
        domain_name = self.domain_name_input.text
        if file_name and domain_name:
            unique_link = generate_art(file_name, domain_name)
            self.image.source = f'{file_name}.png'
            self.image.reload()
            print(f'Art saved as {file_name}.png with link: {unique_link}')
        else:
            print('Please enter both a file name and a domain name.')
