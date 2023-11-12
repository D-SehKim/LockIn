import create_data_from_image

def model_testing(file_path_to_folder, model):
    y_pred = model.predict(create_data_from_image.load_images(file_path_to_folder))
    print(y_pred)
    if y_pred[0][0] > y_pred[0][1]:
        print('eye"s Closed')
    else: 
        print("eye's opened")