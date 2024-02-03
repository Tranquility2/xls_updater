"""Module providing utils."""


def change_file_extension_with_string_methods(filename: str, new_extension: str) -> str:
    """Function updating the given filename string to a given extention."""
    # Note: replace with with_suffix() method
    if "." in filename:
        name, old_extension = filename.rsplit(".", 1)
        print(f"Replacing old '{old_extension}' with new '{new_extension}' extension")
        new_filename = name + "." + new_extension
    else:
        new_filename = filename + "." + new_extension
    return new_filename
