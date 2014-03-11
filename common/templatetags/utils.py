from django.template import Library

register = Library()

@register.filter
def get_range(value):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return range( value )

@register.filter
def in_range(value):
    vars = value.split(',')
    min = int(vars[0])
    max = int(vars[1]) + 1
    return range(min, max)

@register.filter
def multiply(value, arg):
    return value*int(arg)

@register.filter
def divide(value, arg):
    return (value + int(arg) -1)/int(arg)

@register.filter
def split_list(value, arg):
    arg = int(arg)
    ret = []
    sub_list = []
    for i in value:
        sub_list.append(i)
        if len(sub_list) == arg:
            ret.append(sub_list)
            sub_list = []

    if len(sub_list):
        ret.append(sub_list)

    return ret
