from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operations = ""
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout = GridLayout(cols=4, spacing=2)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        for button in buttons:
            button_widget = Button(text=button, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            button_widget.bind(on_press=self.on_button_press)
            layout.add_widget(button_widget)
        
        clear_button = Button(text="Clear", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        clear_button.bind(on_press=self.on_clear_press)
        layout.add_widget(clear_button)
        
        equals_button = Button(text="=", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)

        layout.add_widget(self.result)

        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ""
        else:
            new_text = current + button_text
            self.result.text = new_text

    def on_clear_press(self, instance):
        self.result.text = ""

    def on_solution(self, instance):
        try:
            self.result.text = str(eval(self.result.text))
        except Exception:
            self.result.text = "Error"

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
