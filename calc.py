from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

# Load the external KV file
Builder.load_file('calculator.kv')

# Main app
class CalculatorApp(App):
    def build(self):
        self.operations = ""
        self.result = self.root.ids.result
        return

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

# Start app
if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
