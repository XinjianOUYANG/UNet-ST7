import u_net

unet = u_net.U_Net()
model_path = r"weights/best_model.h5" # the model we have trained
unet.test(model_path)     # test

# unet.test1()  # test randomly

#unet.train(epochs = 100)    # trainning a model 








