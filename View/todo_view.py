class ToDoView:
    def display_menu(self):
        """
        Zeigt das Hauptmenü der Anwendung an.
        """
        print("\nTo-Do-Liste Menü:")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe als erledigt markieren")
        print("4. Aufgabe löschen")
        print("5. Beenden")

    def get_user_choice(self):
        """
        Holt die Auswahl des Benutzers.
        """
        return input("Wähle 1-5 aus: ")

    def get_task_input(self):
        """
        Holt die Eingabe für eine neue Aufgabe.
        """
        return input("Gib die Aufgabe ein: ")

    def display_tasks(self, tasks):
        """
        Zeigt die Aufgaben an.
        """
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Keine Aufgaben gefunden.")

    def get_task_numbers(self):
        """
        Holt die Nummern der Aufgaben, die bearbeitet werden sollen.
        """
        try:
            task_numbers = input("Gib die Nummern der Aufgaben ein (z.B. 1,3,5): ")
            return [int(n) for n in task_numbers.split(',')]
        except ValueError:
            print("Ungültige Eingabe! Gib eine gültige Zahl ein.")
            return []
