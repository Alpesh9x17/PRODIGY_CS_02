from PIL import Image

def encrypt_decrypt_image(input_path, output_path, key, mode):
    """
    Encrypts or decrypts an image using pixel-wise XOR with the key.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the encrypted/decrypted image.
    :param key: Integer key for XOR operation (0-255).
    :param mode: 'encrypt' or 'decrypt'.
    """
    img = Image.open(input_path)
    img = img.convert("RGB")
    encrypted_img = Image.new("RGB", img.size)
    pixels = img.load()
    encrypted_pixels = encrypted_img.load()

    for i in range(img.size[0]):
        for j in range(img.size):
            r, g, b = pixels[i, j]
            if mode in ["encrypt", "decrypt"]:
                # XOR with key (encryption and decryption are the same operation for XOR)
                encrypted_pixels[i, j] = (r ^ key, g ^ key, b ^ key)
            else:
                print("Invalid mode (choose 'encrypt' or 'decrypt').")
                return

    encrypted_img.save(output_path)
    print(f"Image saved as {output_path}")

def main():
    print("=== Image Encryption Tool ===")
    input_path = input("Enter input image path (e.g., test.png): ")
    output_path = input("Enter output image path (e.g., out.png): ")
    key = int(input("Enter encryption key (0-255): "))
    mode = input("Encrypt or decrypt? ").strip().lower()

    encrypt_decrypt_image(input_path, output_path, key, mode)

if __name__ == "__main__":
    main()
