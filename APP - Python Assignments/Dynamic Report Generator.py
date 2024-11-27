#Dynamic Report Generator.
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.formatted_content = content

    def __str__(self):
        return f"Title: {self.title}\n\n{self.formatted_content}"

    def __call__(self, formatter):
        self.formatted_content = formatter(self.content)
        return self

    @classmethod
    def create_template(cls, template_name):
        if template_name == "simple":
            return cls("Simple Report", "This is a Program of experiment 2 of APP")
        elif template_name == "detailed":
            return cls("Detailed Report", "This is a detailed report with more sections.")
        else:
            return cls("Custom Report", "Custom report content.")

    def apply_formatting(self, formatting_func):
        self.formatted_content = formatting_func(self.content)

def bold_format(content):
    return f"**{content}**"

def italic_format(content):
    return f"*{content}*"

report = Report("APP Experiment Report", "This is the content of the APP experiment report.")
print(report)

formatted_report = report(bold_format)
print(formatted_report)

template_report = Report.create_template("simple")
template_report.apply_formatting(italic_format)
print(template_report)
