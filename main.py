import u_net

unet = u_net.U_Net()

model_path = r"weights/trained_by_Molin_175.h5" # the model we have trained
unet.test(model_path = model_path)     # test results are saved in folder evaluation

# unet.test1()  # test randomly
# save_path = 'weights/history'
# unet.train(epochs = 175, save_path = save_path)    # trainned model is saved in folder weights/history








