import pyaudio

def check_audio_devices():
    p = pyaudio.PyAudio()
    default_input = p.get_default_input_device_info()
    
    print("\n=== 系统默认输入设备 ===")
    print(f"设备索引: {default_input['index']}")
    print(f"设备名称: {default_input['name']}")
    print(f"输入通道数: {default_input['maxInputChannels']}")
    
    print("\n=== 所有可用的输入设备 ===")
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if dev['maxInputChannels'] > 0:  # 只显示输入设备
            print(f"\n设备索引 {i}:")
            print(f"  名称: {dev['name']}")
            print(f"  输入通道数: {dev['maxInputChannels']}")
            print(f"  默认采样率: {dev['defaultSampleRate']}")
    
    p.terminate()

if __name__ == "__main__":
    check_audio_devices() 