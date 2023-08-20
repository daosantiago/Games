from django import forms
from .models import Evaluation, Game, Console


class EvaluationForm(forms.ModelForm):
    console = forms.ModelChoiceField(queryset=Console.objects.all())

    class Meta:
        model = Evaluation
        fields = ("title", "platform", "game")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["game"].queryset = Game.objects.none()

        if "console" in self.data:
            try:
                console_id = int(self.data.get("console"))
                self.fields["game"].queryset = Game.objects.filter(
                    id_console=console_id
                )
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields["game"].queryset = self.instance.game
