# Ultimate Translator Hub

Welcome to the **Ultimate Translator Hub**! This is a Python-based graphical user interface (GUI) application built using the `customtkinter` and `tkinter` modules. The application provides a user-friendly interface for translating text between various languages using the Google Translator API from the `deep_translator` module.

## Features

- **Text Translation**: Enter text and translate it into your chosen language.
- **Language Selection**: Choose from a wide range of languages for translation.
- **User Feedback**: Rate the application and view information about the creator.
- **Placeholder Text**: Placeholder text in the input box that disappears when you start typing.

## Installation

To run this application, you need to have Python installed on your machine along with the required libraries. Follow these steps to set up the environment:

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/ultimate-translator-hub.git
    cd ultimate-translator-hub
    ```

2. **Install Dependencies**

    Create a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    Install the required Python packages:

    ```sh
    pip install customtkinter tkinter deep-translator
    ```

3. **Run the Application**

    Execute the main script:

    ```sh
    python main.py
    ```

## Usage

- **Text Entry**: Type or paste the text you want to translate into the text box.
- **Language Selection**: Choose the target language from the dropdown menu.
- **Translation**: The translated text will appear in the result box once you select a language.
- **Rate Us**: Click on the "Help" menu and select "Rate Us" to provide feedback.
- **About Us**: Click on the "Help" menu and select "About Us" to learn more about the application.

## Code Overview

- **GUI Layout**: Uses `customtkinter` to create a modern, customizable interface with frames, labels, and buttons.
- **Translation Functionality**: The `optionmenu_callback_translating` function handles the translation using the `GoogleTranslator` class from the `deep_translator` module.
- **Help Menu**: Contains options to rate the application and view information about the developer.

## Screenshots
![Screenshot 2024-08-18 190935](https://github.com/user-attachments/assets/8312b4de-65d1-4d57-a9e5-66ed4d12cfe6)

![Screenshot 2024-08-18 190957](https://github.com/user-attachments/assets/dc905fb3-758a-440b-a2dd-388704911909)

![Screenshot 2024-08-18 191136](https://github.com/user-attachments/assets/c42cbf45-fecc-497a-951b-57fcfdc3a9d6)

![Screenshot 2024-08-18 191210](https://github.com/user-attachments/assets/a9c5070c-27cb-42a1-955b-15b0b797a25f)

![Screenshot 2024-08-18 191240](https://github.com/user-attachments/assets/14380925-5818-40ea-b087-fac5aff57720)

![Screenshot 2024-08-18 191303](https://github.com/user-attachments/assets/5a211719-5e86-4ba4-a3e7-e0709a00a5f8)
![Screenshot 2024-08-18 191317](https://github.com/user-attachments/assets/5f9c2581-8a31-4d8c-a523-e7a65bbf623c)
![Screenshot 2024-08-18 191333](https://github.com/user-attachments/assets/c4c31a3a-58f1-4e39-bdf7-c683f0847fe1)

## Troubleshooting

If you encounter any issues, make sure:
- You have installed all required dependencies.
- The `deep_translator` module is correctly installed and accessible.
- The icon file path in the code is correctly specified. You might need to update it to match your system's path.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

- [customtkinter](https://github.com/pepperoni456/customtkinter) for providing a modern GUI toolkit.
- [deep_translator](https://pypi.org/project/deep-translator/) for translation services.

Feel free to reach out with any questions or feedback. Enjoy using the Ultimate Translator Hub!
