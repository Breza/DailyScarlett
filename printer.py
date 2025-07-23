from escpos.printer import Usb


def print_receipt(receipt_message: str, cut_receipt: bool = True, vendor_id: int = 0x0416, product_id: int = 0x5011,
        out_endpoint: int = 0x03) -> None:
    """Initializes a connection to a USB ESC/POS thermal printer, prints a
    message, and safely closes the connection.

    This function encapsulates the entire printer lifecycle for a single print job.
    It finds the printer by its Vendor and Product ID, sends text to it,
    cuts the paper, and ensures the USB device is properly released so it can be
    used again by subsequent calls.

    Args:
        receipt_message (str): The primary text content to be printed on the receipt.
        cut_receipt (bool, optional): If True, the printer will cut the paper
            after printing. Defaults to True.
        vendor_id (int, optional): The USB Vendor ID of the printer. Defaults to
            the value for a common 58mm thermal printer (0x0416).
        product_id (int, optional): The USB Product ID of the printer. Defaults
            to the value for a common 58mm thermal printer (0x5011).
        out_endpoint (int, optional): The USB OUT endpoint address for the printer.
            This value often needs to be discovered through diagnostics.
            Defaults to a commonly found value (0x03).

    Raises:
        This function catches all exceptions from the underlying libraries
        (e.g., usb.core.USBError, escpos.exceptions.DeviceNotFoundError)
        and prints a friendly error message. A user might expect errors
        related to device permissions, connection issues, or incorrect IDs.

    Example:
        >>> from printer import print_receipt
        >>>
        >>> morning_greeting = "Good Morning, Scarlett!\\nHave a wonderful day!"
        >>> print_receipt(morning_greeting)
    """
    printer_instance: Usb | None = None
    try:
        printer_instance = Usb(idVendor=vendor_id, idProduct=product_id, out_ep=out_endpoint)
        print("Printer connection successful.")

        # You can customize the printing style here
        printer_instance.set(align='left', font='a', text_type='normal')
        printer_instance.text(receipt_message + "\n\n")

        # It's good form to cut the receipt when done printing
        if cut_receipt:
            printer_instance.cut()

        print("Print job sent successfully.")

    except Exception as receipt_exception:
        print(f"An error occurred during printing: {receipt_exception}")

    finally:
        # This block ensures the printer connection is closed, even if an error occurred.
        # Releasing the device is crucial for subsequent print jobs to work.
        if printer_instance:
            printer_instance.close()
            print("Printer connection closed.")
