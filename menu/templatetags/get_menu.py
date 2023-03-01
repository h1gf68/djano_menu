from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context, **kwargs):
    menu = MenuItem.objects.filter(
        menu__name=kwargs['main'],
        menu__visible=True,
        visible=True,
    ).order_by('position')

    if menu:
        css_class = menu[0].menu.css_class
        css_class = css_class if css_class else ''

        full_menu = {}
        for item in menu:
            if full_menu.get(item.id):
                full_menu[item.id]['item'] = item
            else:
                full_menu[item.id] = {'item': item}

            p = item.parent
            full_menu[item.id]['parent'] = p

            if p:
                if full_menu.get(p.id):
                    if full_menu.get(p.id).get('child'):
                        full_menu[p.id]['child'].append(item.id)
                    else:
                        full_menu[p.id]['child'] = [item.id]
                else:
                    full_menu[p.id] = {'child': [item.id]}

        return {
            'menu': full_menu,
            'request': context['request'],
            'menu_class': css_class
            }
    else:
        msg = 'Did not match any of the menu item!'
        raise template.TemplateSyntaxError(msg)


@register.inclusion_tag('submenu.html', takes_context=True)
def show_submenu(context, submenu_ids, menu):
    submenu = [menu.get(i) for i in submenu_ids]

    return {
        'submenu': submenu,
        'menu': menu,
        'request': context['request'],
    }


@register.simple_tag
def define(val=None):
    return val

@register.simple_tag
def concat(val1, val2):
    return str(val1)+str(val2)