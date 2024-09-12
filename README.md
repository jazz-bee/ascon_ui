# Ascon UI: First Educational Tool for Cryptography Algorithm ASCON

An interactive desktop application to visualize and experiment with the [Ascon lightweight cryptography algorithm](https://ascon.iaik.tugraz.at/specification.html). This project provides a graphical interface for users to input parameters and see real-time encryption and decryption results.

## Features

- Visualize Ascon encryption and decryption results
- Supports different versions of the Ascon algorithm
- Adjustable parameters (e.g., key, nonce, associated data)
- Easy-to-use graphical interface (built with Tkinter and CustomTkinter)

## Setup
### 1) Create a local environment

Make sure you are running the commands INSIDE source code directory
Virtualenv modules installation 
(Unix based systems)
```
$ virtualenv env
$ source env/bin/activate
```
 (Windows based systems)
 ```
$ # virtualenv env
$ # .\env\Scripts\activate
$
```
(Mac based systems)
```
$# python3 -m venv venv
$# source venv/bin/activate
```

### 2) Install dependencies
```
pip3 install -r requirements.txt 
```
### 3) Run the application
```
python3 main.py
```
### 3) Tests
```
python3 -m unittest
```

## Usage

1. Launch the app using the instructions above.
2. Enter the parameters (key, nonce, plaintext, associated data(optional), variant) for encryption.
3. Click "Encrypt" to see the encrypted output.
4. Use the "Decrypt" option to reverse the encryption process.
5. Switch between different Ascon algorithm versions using the UI toggle.

## Project Structure for Devs

- `/algorithms/`: Contains the Ascon algorithm implementation.
- `/controllers/`: Handles the business logic and interaction between the UI and the algorithm.
- `/view/`: Manages the graphical interface using Tkinter.
- `/utils/`: Contains utility functions used across the application.
- `/tests/`: Contains unit tests for different components.
- `main.py`: Entry point for running the application.
- `requirements.txt`: Lists the dependencies required to run the project.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! If you find a bug or want to improve the application:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## Contact

If you have any questions, feel free to reach out or open an issue in this repository.