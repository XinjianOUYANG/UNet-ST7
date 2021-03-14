import u_net

unet = u_net.U_Net()
# model_path = r"weights/best_model.h5" # the model we have trained
# unet.test(model_path)     # test results are saved in folder evaluation

# unet.test1()  # test randomly

unet.train(epochs = 5)    # trainned model is saved in foplder weights/history








