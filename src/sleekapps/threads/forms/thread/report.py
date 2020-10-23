from violation.forms.violation import ViolationForm


class ThreadReportForm(ViolationForm):
    categories = ['forum']

    def save(self, commit=True):
        report = super().save(commit=False)
        report.violator = self.object.starter
        if commit:
            report.save()
        return report
