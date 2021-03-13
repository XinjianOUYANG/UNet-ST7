import u_net





unet = u_net.U_Net()
# model_path = r"weights/best_model.h5"
# picture_path = r"./prediction/test_picture/"
#  unet.prediction(picture_path ,model_path)



unet.train(epochs = 10)    # 开始训练网络
unet.test()     # 评价测试集并检测测试集肿瘤分割结果
# unet.test1()  # 随机显示








