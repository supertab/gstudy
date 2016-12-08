processor:
stage 1: 使用先验知识确定识别区域（路标的颜色，位置）使路标限制在设定的识别区域中(region of interest(ROI))
    a. down-sampling, 低采样？
    b. 通过先验知识定位,确定图像的中间位置（通过色调，饱和度）
    c. 

stage 2: 在ROI中搜索可能的三角形或圆形区域
stage 3: 与模板做匹配识别图像
