from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ['Harry Potter', 'Ron Weasley', 'Hermione Granger']

    def build(self):
        """Build the Kivy GUI with creating labels from data."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.color = (1, 1, 0, 1)
            self.root.ids.name_labels.add_widget(temp_label)
        return self.root


DynamicLabelsApp().run()
