from engine.preprocessing.loader import load_image

image = load_image("data/samples/1.jpeg")

print(type(image))
print(image.shape)