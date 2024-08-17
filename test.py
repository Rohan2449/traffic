import traffic

images, labels = traffic.load_data("gtsrb")


for i in range(traffic.NUM_CATEGORIES):
    print("IMAGES")
    print(images)

    print(f"\nLABEL: {labels[i]}")


