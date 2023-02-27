import random
import tkinter as tk
from tkinter import filedialog

def generate_random_dna(length, gc_content):
    """Generate a random DNA sequence of the specified length and GC content."""
    
    # Calculate the number of GC and AT base pairs required based on the GC content
    gc_count = int(length * gc_content)
    at_count = length - gc_count
    
    # Generate the random sequence of GC and AT base pairs
    seq = ""
    for i in range(gc_count):
        seq += random.choice("GC")
    for i in range(at_count):
        seq += random.choice("AT")
    
    # Shuffle the sequence to make it truly random
    seq_list = list(seq)
    random.shuffle(seq_list)
    seq = "".join(seq_list)
    
    return seq

def save_sequence_to_file(seq, filename):
    """Save the DNA sequence to a file."""
    
    with open(filename, "w") as f:
        f.write(seq)

def generate_sequence():
    """Generate a random DNA sequence and save it to a file."""
    
    # Get the desired length and GC content from the user
    length = int(length_entry.get())
    gc_content = float(gc_content_entry.get())
    
    # Generate the random DNA sequence
    seq = generate_random_dna(length, gc_content)
    
    # Get the filename to save the sequence to
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    
    # Save the sequence to the file
    save_sequence_to_file(seq, filename)
    
    # Show a message box indicating that the sequence was saved
    message = f"DNA sequence of length {length} and GC content {gc_content} saved to {filename}."
    tk.messagebox.showinfo("Sequence generated", message)

# Create the main window
root = tk.Tk()
root.title("Random DNA Sequence Generator")

# Create the length label and entry box
length_label = tk.Label(root, text="Enter length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Create the GC content label and entry box
gc_content_label = tk.Label(root, text="Enter GC content (between 0 and 1):")
gc_content_label.pack()
gc_content_entry = tk.Entry(root)
gc_content_entry.pack()

# Create the generate button
generate_button = tk.Button(root, text="Generate Sequence", command=generate_sequence)
generate_button.pack()

# Start the main event loop
root.mainloop()
