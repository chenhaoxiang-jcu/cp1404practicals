from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main program - Kivy app to demo box layout."""

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Display a greeting message."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_text(self):
        """Clear texts of input box and output label."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


BoxLayoutDemo().run()
