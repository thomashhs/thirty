from django import template
register = template.Library()

from django.utils.html import format_html
@register.simple_tag
def circle_page(curr_page,loop_page,num_pages,search_name=""):
    if search_name:
        href_1 = '<li class="active"><a href="?q='+search_name+'&page=%s">%s</a></li>'
        href_2 = '<li><a href="?q='+search_name+'&page=%s">%s</a></li>'
    else:
        href_1 = '<li class="active"><a href="?page=%s">%s</a></li>'
        href_2 = '<li><a href="?page=%s">%s</a></li>'

    offset = abs(curr_page - loop_page)

    if curr_page==1 or curr_page==num_pages:
        if offset < 5:
            if curr_page == loop_page:
                page_ele = href_1 % (loop_page, loop_page)
            else:
                page_ele = href_2 % (loop_page, loop_page)
            return format_html(page_ele)
        else:
            return ''
    elif curr_page==2 or curr_page==num_pages-1:
        if offset < 4:
            if curr_page == loop_page:
                page_ele = href_1 % (loop_page, loop_page)
            else:
                page_ele = href_2 % (loop_page, loop_page)
            return format_html(page_ele)
        else:
            return ''
    else:
        if offset < 3:
            if curr_page == loop_page:
                page_ele = href_1 %(loop_page,loop_page)
            else:
                page_ele = href_2 %(loop_page,loop_page)
            return format_html(page_ele)
        else:
            return ''