import jinja2


class Renderer:
    def __init__(self):
        self._jinja = jinja2.Environment(
            loader=jinja2.PackageLoader("qutelaunch", "templates")
        )

    def render(self, template_file_name, **kwargs):
        template = self._jinja.get_template(template_file_name)
        result = template.render(**kwargs)
        return result
