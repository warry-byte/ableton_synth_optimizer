import PySimpleGUI as sg

def main():
    # Define the layout of the GUI
    layout = [
        [sg.Slider(range=(0, 6), orientation='h', size=(20, 20), key='-SLIDER-', default_value=0)],
        [sg.Text('Chosen Number: '), sg.Text('', size=(5, 1), key='-OUTPUT-')]
    ]

    # Create the window
    window = sg.Window('Number Chooser', layout, finalize=True)

    # Initialize the chosen number to the default value
    chosen_number = 0

    while True:
        # Read events and values from the window
        event, values = window.read(timeout=100)  # Timeout added to make the GUI responsive

        # If the window is closed, break the loop
        if event == sg.WINDOW_CLOSED:
            break

        # Check if the slider value has changed
        if values['-SLIDER-'] != chosen_number:
            # Update the chosen number in the text element
            chosen_number = int(values['-SLIDER-'])
            window['-OUTPUT-'].update(chosen_number)

            # Perform the action with the chosen number (replace this with your actual action)
            perform_action(chosen_number)

    # Close the window
    window.close()

def perform_action(chosen_number):
    # Replace this with your actual action based on the chosen number
    print(f"Action performed with chosen number: {chosen_number}")

if __name__ == '__main__':
    main()
