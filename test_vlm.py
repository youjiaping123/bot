import os
from utils_vlm import yi_vision_api, post_processing_viz

def test_vlm():
    # 确保temp文件夹和visualizations文件夹存在
    if not os.path.exists('temp'):
        os.makedirs('temp')
    if not os.path.exists('visualizations'):
        os.makedirs('visualizations')
    
    # 测试图片路径
    img_path = 'temp/vl_now.jpg'
    
    # 测试指令
    test_prompt = "帮我把绿色方块放在摩托车上"
    print("\n测试指令：", test_prompt)
    
    try:
        # 调用视觉语言模型
        print("\n正在调用视觉语言模型...")
        result = yi_vision_api(PROMPT=test_prompt, img_path=img_path)
        print("\n模型输出结果：")
        print(f"起始物体：{result['start']}")
        print(f"起始物体坐标：{result['start_xyxy']}")
        print(f"目标物体：{result['end']}")
        print(f"目标物体坐标：{result['end_xyxy']}")
        
        # 可视化结果
        print("\n正在可视化结果...")
        start_x, start_y, end_x, end_y = post_processing_viz(result, img_path, check=True)
        print("\n物体中心点坐标：")
        print(f"起始物体中心点：({start_x}, {start_y})")
        print(f"目标物体中心点：({end_x}, {end_y})")
        
    except Exception as e:
        print(f"\n发生错误：{str(e)}")

if __name__ == "__main__":
    test_vlm() 