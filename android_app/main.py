
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp


class JarvisApp(App):

    def build(self):
        self.title = "JARVIS"

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(20)
        )

        with layout.canvas.before:
            Color(0.02, 0.03, 0.06, 1)
            self.bg = Rectangle(
                pos=layout.pos,
                size=layout.size
            )

        layout.bind(
            pos=self.update_bg,
            size=self.update_bg
        )

        title = Label(
            text="[b]J.A.R.V.I.S[/b]",
            markup=True,
            font_size="36sp",
            color=(0, 0.85, 1, 1)
        )

        subtitle = Label(
            text="PERSONAL AI ASSISTANT",
            font_size="14sp",
            color=(0, 1, 0.5, 1)
        )

        self.status = Label(
            text="SYSTEM ONLINE",
            font_size="20sp",
            color=(0, 1, 0.4, 1)
        )

        button = Button(
            text="INITIALIZE JARVIS",
            font_size="18sp",
            background_normal="",
            background_color=(0, 0.45, 0.65, 1),
            size_hint=(1, 0.18)
        )

        button.bind(on_press=self.initialize)

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(self.status)
        layout.add_widget(button)

        return layout

    def update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def initialize(self, instance):
        self.status.text = "JARVIS IS READY"
        self.status.color = (0, 1, 0.5, 1)


if __name__ == "__main__":
    JarvisApp().run()

