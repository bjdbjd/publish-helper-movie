import requests


def get_pt_gen_description(pt_gen_api_url, resource_url):
    try:
        # 设置一个合理的超时时间，例如10秒
        response = requests.get(f"{pt_gen_api_url}?url={resource_url}", timeout=12)

        # 检查响应是否成功
        if response.status_code != 200:
            print("请求失败，状态码:", response.status_code)
            return False, f"PT-Gen接口请求失败，状态码: {str(response.status_code)}"

        # 尝试解析JSON响应
        try:
            data = response.json()
        except ValueError:
            print("响应不是有效的JSON格式")
            return False, "PT-Gen接口响应不是有效的JSON格式，请检查PT-Gen接口是否正常"

        # 根据响应结构获取format字段
        format_data = data.get("format") if "format" in data else data.get("data", {}).get("format", "")

        # 返回处理后的format字段
        # print(format_data)
        format_data += '\n'
        if format_data != '\n':
            format_data = format_data.replace('img1', 'img2')
            return True, format_data
        else:
            return False, "获取到的PT-Gen简介为空，可能是资源链接有误或PT-Gen接口出错，请检查后重试"

    except requests.Timeout:
        # 处理超时异常
        print("请求超时")
        return False, "PT-Gen接口请求超时"

    except requests.RequestException as e:
        # 处理请求过程中的其他异常
        print(f"请求发生错误: {e}")
        return False, f"PT-Gen接口请求发生错误: {e}"
