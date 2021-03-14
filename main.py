import u_net

unet = u_net.U_Net()
model_path = r"weights/best_model.h5"
unet.test(model_path)     # 评价测试集并检测测试集肿瘤分割结果

# unet.test1()  # test randomly

#unet.train(epochs = 100)    # trainning a model 








