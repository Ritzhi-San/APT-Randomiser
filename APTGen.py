import tkinter as tk
import random
import string

class DNASequenceGenerator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("DNA Sequence Generator")
        self.master.geometry("700x700")
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)

        # Create GUI elements
        self.length_label = tk.Label(self, text="Sequence Length [Use Between 30 and 80]:")
        self.length_label.grid(row=0, column=0)
        self.length_entry = tk.Entry(self)
        self.length_entry.grid(row=0, column=1)

        self.gc_label = tk.Label(self, text="GC Content (%) [Use Between 1% and 100%]:")
        self.gc_label.grid(row=1, column=0)
        self.gc_entry = tk.Entry(self)
        self.gc_entry.grid(row=1, column=1)

        self.repeat_label = tk.Label(self, text="Repeat Frequency [0 for no repeats, > 1 for random repetitions]:")
        self.repeat_label.grid(row=2, column=0)
        self.repeat_entry = tk.Entry(self)
        self.repeat_entry.grid(row=2, column=1)

        self.num_seq_label = tk.Label(self, text="Number of Sequences [Use Between 1 to 1000]:")
        self.num_seq_label.grid(row=3, column=0)
        self.num_seq_entry = tk.Entry(self)
        self.num_seq_entry.grid(row=3, column=1)

        self.dna_radio = tk.Radiobutton(self, text="DNA", variable=tk.StringVar(), value="DNA")
        self.dna_radio.grid(row=4, column=0)

        self.rna_radio = tk.Radiobutton(self, text="RNA", variable=tk.StringVar(), value="RNA")
        self.rna_radio.grid(row=4, column=1)

        self.generate_button = tk.Button(self, text="Generate", command=self.generate_sequences)
        self.generate_button.grid(row=5, column=0)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=6, column=2, sticky=tk.N+tk.S)

        self.sequence_text = tk.Text(self, yscrollcommand=self.scrollbar.set)
        self.sequence_text.grid(row=6, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.sequence_text.config(state=tk.DISABLED)

        self.download_button = tk.Button(self, text="Download", command=self.download_sequences)
        self.download_button.grid(row=7, column=0)

        self.quit_button = tk.Button(self, text="Quit", command=self.master.quit)
        self.quit_button.grid(row=7, column=1)

    def generate_sequences(self):
        length = int(self.length_entry.get())
        gc_content = int(self.gc_entry.get())
        repeat_freq = int(self.repeat_entry.get())
        num_seqs = int(self.num_seq_entry.get())
        base_pairs = ["A", "T", "C", "G"] if self.dna_radio.cget("value") == "DNA" else ["A", "U", "C", "G"]
        sequences = []

        for i in range(num_seqs):
            sequence = ""
            for j in range(length):
                if random.randint(1, 100) <= gc_content:
                    sequence += random.choice(["C", "G"])
                else:
                    sequence += random.choice(["A", "T"] if self.dna_radio.cget("value") == "DNA" else ["A", "U"])
            sequences.append(sequence)

        if repeat_freq > 0:
            for i in range(repeat_freq):
                repeat_length = random.randint(2, 5)
                repeat_seq = "".join([random.choice(base_pairs) for _ in range(repeat_length)])
                for j in range(num_seqs):
                    repeat_pos = random.randint(0, length-repeat_length)
                    sequences[j] = sequences[j][:repeat_pos] + repeat_seq + sequences[j][repeat_pos+repeat_length:]

        # Update the text widget with the generated sequences
        self.sequence_text.config(state=tk.NORMAL)
        self.sequence_text.delete("1.0", tk.END)
        for sequence in sequences:
            self.sequence_text.insert(tk.END, sequence + "\n")
        self.sequence_text.config(state=tk.DISABLED)

    def download_sequences(self):
        filename = "sequences.txt"
        with open(filename, "w") as f:
            f.write(self.sequence_text.get("1.0", tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    app = DNASequenceGenerator(master=root)
    app.mainloop()
