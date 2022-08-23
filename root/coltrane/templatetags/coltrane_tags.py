from django import template
from coltrane.models import Entry
from django.db.models import get_model


# def do_latest_entries(parser, token):
#     return LatestEntriesNode()

# class LatestEntriesNode(template.Node):
#     def render(self, context):
#         context['latest_entries'] = Entry.live.all()[:5]
#         return ''

# register = template.Library()
# register.tag('get_latest_entries', do_latest_entries)

def do_latest_content(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise template.TemplateSyntaxError("'get_latest_content' tag takes exactly four arguements")
    model_args = bits[1].split('.')
    if len(model_args) != 2:
        raise template.TemplateSyntaxError("First arguemnet to 'get_latest_content' must be an 'application name '.'model name' string")
        model = get_model(*model_args)
        if model is None:
            raise template.TemplateSyntaxError("'get_latest_content' tag got an invalid model: %s" % bits[1])
    model = get_model(model_args[0], model_args[1])
    return LatestContentNode(bits[1], bits[2], bits[4])

class LatestContentNode:
    def __init__(self, model, num, varname):
        self.model = model
        self.num = int(num)
        self.varname = varname

    def render(self, context):
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''

register = template.Library()
register.tag('get_latest_content', do_latest_content)


from django import template
from markdown import markdown

def safe_markdown(value):
    return markdown(value, safe_mode=True)

register = template.Library()
register.filter(safe_markdown)

