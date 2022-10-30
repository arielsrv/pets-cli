import click
import questionary
from prompt_toolkit.styles import Style


class MultipleOptions(click.Option):
    def __init__(self, param_decls=None, **attrs):
        click.Option.__init__(self, param_decls, **attrs)
        if not isinstance(self.type, click.Choice):
            raise Exception('ChoiceOption type arg must be click.Choice')

    def prompt_for_value(self, ctx):
        custom_style_fancy = Style(
            [
                ("separator", "fg:#cc5454"),
                ("qmark", "fg:#673ab7 bold"),
                ("question", ""),
                ("selected", "fg:#cc5454"),
                ("pointer", "fg:#673ab7 bold"),
                ("highlighted", "fg:#673ab7 bold"),
                ("answer", "fg:#f44336 bold"),
                ("text", "fg:#FBE9E7"),
                ("disabled", "fg:#858585 italic"),
            ]
        )

        val = questionary.autocomplete(self.prompt, choices=self.type.choices, style=custom_style_fancy).unsafe_ask()
        return val
