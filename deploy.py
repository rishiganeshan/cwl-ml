# ... (rest of the code)

if __name__ == "__main__":
    import sys
    model_path = sys.argv[1]
    x_random, y_pred = make_predictions(model_path)
    with open("predictions.txt", "w") as f:
        f.write("Random input data:\n")
        f.write(str(x_random))
        f.write("\nPredicted output data:\n")
        f.write(str(y_pred))
