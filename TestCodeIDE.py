# def execute_python_code(code_str, n):
#     try:
#         # 创建一个空的字典用于存储函数中的局部变量
#         local_vars = {}
#         # 在字典中添加 n 变量
#         local_vars['n'] = n
#         # 执行输入的 Python 代码，并在局部变量中存储结果
#         exec(code_str, globals(), local_vars)
#
#         # 获取并执行函数
#         if 'your_function' in local_vars:
#             your_function = local_vars['your_function']
#             # 直接调用函数获取结果
#             result = your_function(n)
#             return f"函数从 0 到 {n} 的和为: {result}"
#         else:
#             return "未找到名为 'your_function' 的函数"
#     except Exception as e:
#         # 如果有错误，返回错误信息
#         return f"发生错误: {str(e)}"
#
# # 示例用法
# code_to_execute = """
# def your_function(n):
#     return sum(range(n + 1))
# """
# n_value = 5
# result = execute_python_code(code_to_execute, n_value)
# print(result)

def execute_python_code(code_str, *args):
    try:
        # 创建一个空的字典用于存储函数中的局部变量
        local_vars = {}
        # 在字典中添加参数
        for i, arg in enumerate(args):
            local_vars[f'arg_{i+1}'] = arg

        # 执行输入的 Python 代码，并在局部变量中存储结果
        exec(code_str, globals(), local_vars)

        # 获取并执行函数
        if 'your_function' in local_vars:
            your_function = local_vars['your_function']
            # 直接调用函数获取结果
            result = your_function(*args)
            return f"函数结果为: {result}"
        else:
            return "未找到名为 'your_function' 的函数"
    except Exception as e:
        # 如果有错误，返回错误信息
        return f"发生错误: {str(e)}"

# 示例用法
# 动态参数数量的代码
code_to_execute = """
def your_function(*args):
    x = args[0]
    y = args[1]
    # 必须包括这两行，如果有三个参数需要多赋值一个变量
    ls = [x,y]
    return sum(ls)
"""

# 存储格式：
# 0 题目ID INT
# 1 题目描述 STR
# 2 题目答案组 DICT{[Parama1,Parama2,...]:Ans}


# 执行方法
result_two_args = execute_python_code(code_to_execute, 3, 5)

print(result_two_args)

