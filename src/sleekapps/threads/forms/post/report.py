from violation.forms.violation import ViolationForm


class PostReportForm(ViolationForm):
    categories = ['post']

    def save(self, commit=True):
        report = super().save(commit=False)
        report.violator = self.object.user
        if commit:
            report.save()
        return report
