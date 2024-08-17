from traffic import *


print(tf.keras.__version__)

images, labels = load_data("gtsrb")

print(len(images))

# for i in range(traffic.NUM_CATEGORIES):
#     print("IMAGES")
#     print(images)

#     print(f"\nLABEL: {labels[i]}")


