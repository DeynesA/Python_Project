class ToDoController:
    def __init__(self, model, view):
        """
        Initialisiert den Controller mit dem Model und der View.
        """
        self.model = model
        self.view = view

    def start(self):
        """
        Startet die Anwendung und verarbeitet die Benutzereingaben.
        """
        while True:
            self.view.display_menu()  # Zeigt das Hauptmenü an
            choice = self.view.get_user_choice()  # Holt die Auswahl des Benutzers
            if choice == '1':
                task = self.view.get_task_input()  # Holt die Eingabe für eine neue Aufgabe
                self.model.aufgabe_hinzufuegen(task)  # Fügt die Aufgabe hinzu
                print("Aufgabe erfolgreich hinzugefügt.")
            elif choice == '2':
                tasks = self.model.aufgaben_anzeigen()  # Liest alle Aufgaben aus der Datei
                self.view.display_tasks(tasks)  # Zeigt die Aufgaben an
            elif choice == '3':
                tasks = self.model.aufgaben_anzeigen()  # Liest alle Aufgaben aus der Datei
                self.view.display_tasks(tasks)  # Zeigt die Aufgaben an
                task_numbers = self.view.get_task_numbers()  # Holt die Nummern der Aufgaben, die bearbeitet werden sollen
                self.model.aufgabe_als_erledigt_markieren(task_numbers)  # Markiert die Aufgaben als erledigt
                print("Aufgaben als erledigt markiert.")
            elif choice == '4':
                tasks = self.model.aufgaben_anzeigen()  # Liest alle Aufgaben aus der Datei
                self.view.display_tasks(tasks)  # Zeigt die Aufgaben an
                task_numbers = self.view.get_task_numbers()  # Holt die Nummern der Aufgaben, die bearbeitet werden sollen
                self.model.aufgabe_loeschen(task_numbers)  # Löscht die Aufgaben
                print("Erledigte Aufgaben gelöscht.")
            elif choice == '5':
                print("Die To-Do-Liste wurde beendet.")
                break  # Beendet die Schleife und damit die Anwendung
            else:
                print("Ungültige Wahl. Gib eine Zahl zwischen 1 und 5 ein.")