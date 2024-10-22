# WebP to PNG Converter

A lightweight Python script that automatically monitors a folder for WebP files and converts them to PNG format. The script runs continuously in the background, converting both existing WebP files and new ones as they appear.

## Features

- 🔄 Real-time folder monitoring
- 🖼️ Automatic WebP to PNG conversion
- 🚀 Handles both new and modified files
- 🗑️ Automatic cleanup of original WebP files
- ⚡ Lightweight and efficient
- 🛡️ Error handling and file locking protection

## Prerequisites

```bash
pip install watchdog Pillow
```

## Usage

1. Clone or download the script
2. Modify the `folder` path in the script to your desired watch folder:
   ```python
   folder = r"C:\Your\Path\Here"
   ```
3. Run the script:
   ```bash
   python webp_converter.py
   ```
4. The script will run continuously until you press Ctrl+C to stop it

## How It Works

The script uses:
- `watchdog` for real-time folder monitoring
- `Pillow (PIL)` for image conversion
- A file processing queue to prevent duplicate conversions
- Error handling for incomplete or corrupted files

## Example Output

```
Monitoring: C:\Users\Example\Downloads
Converted: image1.webp
Converted: image2.webp
```

## Error Handling

The script handles common errors such as:
- Files being in use
- Incomplete file transfers
- Corrupted WebP files
- Permission issues

## Limitations

- Only monitors a single folder (non-recursive)
- Only converts WebP to PNG format
- Requires the folder to be writable

## Contributing

Feel free to fork the repository and submit pull requests for any improvements.

## License

This project is licensed under the MIT License - feel free to use it in your own projects.
