import pandas as pd
from generation_utils import describe_dataframe, generate_transformation_sequence, apply_transformations, load_dataframe_from_file, save_dataframe_to_file

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file: ")

    try:
        df = load_dataframe_from_file(file_path)
    except FileNotFoundError as e:
        print(e)
        exit(1)

    df_description = describe_dataframe(df)

    # User inputs the transformation prompt
    user_prompt = input("What transformations would you like to perform?: ")

    # Generate the sequence of transformations
    user_transformations, transformations = generate_transformation_sequence(user_prompt, df_description)

    if user_transformations:
        print("Transformations:")
        print(*user_transformations, sep="\n", end=".\n")

        # User confirmation
        confirm = input("Apply these transformations? (y/n): ").strip().lower()
        if confirm == "y":
            # Apply transformations
            transformed_df = apply_transformations(df, transformations)
            print("Result:")
            print(transformed_df)

            # Confirmation to save changes
            save_confirm = input("Save changes to the file? (y/n): ").strip().lower()
            if save_confirm == "y":
                save_dataframe_to_file(transformed_df, file_path)  # Save to original file
            else:
                print("Changes not saved.")
        else:
            print("Transformations canceled.")
    else:
        print("Failed to generate transformations.")
