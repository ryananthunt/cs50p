file = input('File name: ')

image_extensions = ['.gif', 'jpg', '.jpeg', '.png']
applications_extensions = ['.pdf', '.txt', '.zip']

if any(ext in file for ext in image_extensions):
    file = 'image' + file.replace('.', '/')
    print(file)

elif any(ext in file for ext in applications_extensions):
    file = 'application' + file.replace('.', '/')

else:
    print('application/octet-stream')
