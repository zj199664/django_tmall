'''
1.语法格式
2.内置过滤器
3.自定义过滤器
  在app下新建一个tamplatetags的文件夹
  在该文件夹下创建一个py文件
  实例化注册器：register=template.Library()
  声明过滤器（过滤器的本质是一个函数）
  注册过滤器
  可以在模板中使用
'''
from django import template

# 实例化注册器（固定格式）
register = template.Library()


# value|multiply:params
@register.filter
def multiply(value, params):
    return value * params
