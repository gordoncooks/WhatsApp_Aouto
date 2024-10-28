import customtkinter as ctk
import time

class WhatsAppAutomationGUI:

    def __init__(self):
        # Initial loading window setup
        self.mainWindow = ctk.CTk()
        self.mainWindow.geometry("400x200")
        self.mainWindow.title("WhatsApp Auto - Loading")

        # Create a custom font with a specific size (e.g., 20 for large text)
        self.custom_font_heading1 = ctk.CTkFont(size=30, underline=True, weight='bold')  # You can also specify 'family' and 'weight' if needed
        
        # Add main program name to loading screen
        self.heading = ctk.CTkLabel(self.mainWindow, width=25, text="WhatsApp Auto", height=0, font=self.custom_font_heading1)
        self.heading.pack(pady=40)
        

        # Add Progress Bar to mainWindow
        self.progress_bar = ctk.CTkProgressBar(self.mainWindow, width=300, height=20)
        self.progress_bar.pack(pady=0)
        self.progress_bar.set(0)  # Initialize the progress bar to 0%

        # Automatically start the progress bar when the window is created
        self.mainWindow.after(100, self.runStart)

    def runStart(self):
        total_time = 3  # 15 seconds loading time
        increment = 0.01  # Update progress bar by this increment
        steps = total_time / increment  # Number of steps for progress completion

        # Update progress bar progressively over 15 seconds
        for i in range(int(steps)):
            progress = (i + 1) / steps
            self.progress_bar.set(progress)  # Update progress
            self.mainWindow.update()  # Refresh the GUI window
            time.sleep(increment)  # Delay for incremental loading

        # Once loading is complete, switch to the main window
        self.switchToMainWindow()

    def switchToMainWindow(self):
        # Remove all widgets from the initial window (clear out the loading screen)
        for widget in self.mainWindow.winfo_children():
            widget.destroy()

        # Change the window's size and title
        self.mainWindow.geometry("600x600")
        self.mainWindow.title("WhatsApp Auto : Main")

        # Add other widgets or functionality for the main window here
        main_label = ctk.CTkLabel(self.mainWindow, text="Welcome to WhatsApp Automation!")
        main_label.pack(pady=20)

        

    

    def run(self):
        self.mainWindow.mainloop()  # Start the GUI loop