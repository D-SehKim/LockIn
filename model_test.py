import create_data_from_image

def model_testing(file_path_to_folder, model):
    y_pred = model.predict(create_data_from_image.load_images(file_path_to_folder), verbose=0)
    if y_pred[0][0] < y_pred[0][1]:
        return 1
    else: 
        return 0

