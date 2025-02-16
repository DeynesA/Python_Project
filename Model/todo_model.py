class ToDoModel:
    def __init__(self, dateipfad):
        """
        Initialisiert das Model mit dem Pfad zur Datei, in der die Aufgaben gespeichert werden.
        """
        self.dateipfad = dateipfad
        self.aufgaben = self.lade_aufgaben()

    def lade_aufgaben(self):
        """
        Lädt die Aufgaben aus der Datei.
        """
        try:
            with open(self.dateipfad, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []

    def speichere_aufgaben(self):
        """
        Speichert die Aufgaben in der Datei.
        """
        with open(self.dateipfad, 'w') as file:
            for aufgabe in self.aufgaben:
                file.write(f"{aufgabe}\n")

    def aufgabe_hinzufuegen(self, aufgabe):
        """
        Fügt eine neue Aufgabe hinzu und speichert sie.
        """
        self.aufgaben.append(aufgabe)
        self.speichere_aufgaben()

    def aufgaben_anzeigen(self):
        """
        Gibt die Liste der Aufgaben zurück.
        """
        return self.aufgaben

    def aufgabe_als_erledigt_markieren(self, task_numbers):
        """
        Markiert die angegebenen Aufgaben als erledigt.
        """
        for number in task_numbers:
            if 0 <= number < len(self.aufgaben):
                self.aufgaben[number] += " (erledigt)"
        self.speichere_aufgaben()

    def aufgabe_loeschen(self, task_numbers):
        """
        Löscht die angegebenen Aufgaben.
        """
        self.aufgaben = [task for i, task in enumerate(self.aufgaben) if i not in task_numbers]
        self.speichere_aufgaben()