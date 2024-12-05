import os
from utils_asr import record_auto, speech_recognition
from utils_agent import AGENT_SYS_PROMPT
from utils_llm import llm_yi

def test_speech_agent():
    # 确保temp文件夹存在
    if not os.path.exists('temp'):
        os.makedirs('temp')
    
    print("\n请说出指令，比如：'帮我把红色方块放在小猪佩奇上'")
    print("(说完后保持安静几秒钟，系统会自动停止录音)")
    
    # 使用默认设备录音
    record_auto(MIC_INDEX=0)
    
    # 进行语音识别
    speech_result = speech_recognition()
    print("\n语音识别结果：", speech_result)
    
    # 构建完整的提示词
    full_prompt = AGENT_SYS_PROMPT + speech_result
    
    # 调用LLM获取Agent规划
    print("\n正在规划动作...")
    agent_response = llm_yi(full_prompt)
    print("\nAgent规划结果：", agent_response)

if __name__ == "__main__":
    test_speech_agent() 