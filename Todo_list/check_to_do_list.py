import os

# Pfad zur Datei
pfad = os.path.join(".", "todo_list.txt")

# Funktion zum Hinzufügen einer Aufgabe
def add_task():
    """
    Diese Methode ermöglicht es dem Benutzer, eine neue Aufgabe hinzuzufügen.
    Die Aufgabe wird in der Datei gespeichert.
    """
    try:
        task = input("Gib die Aufgabe ein: ")
        with open(pfad, 'a') as file:
            file.write(f"{task}\n")
        print("Aufgabe erfolgreich hinzugefügt.")
    except Exception as e:
        print(f"Fehler beim Hinzufügen der Aufgabe: {e}")

# Funktion zum Anzeigen aller Aufgaben
def show_tasks():
    """
    Diese Methode zeigt alle Aufgaben aus der Datei an.
    Jede Aufgabe wird auf einer neuen Zeile angezeigt.
    """
    try:
        with open(pfad, 'r') as file:
            tasks = file.readlines()
        if tasks:
            for i, task in enumerate(tasks, 1):  # Zeigt die Aufgaben an.
                print(f"{i}. {task.strip()}")
        else:
            print("Keine Aufgaben gefunden.")
    except FileNotFoundError:
        print("Keine Aufgaben gefunden.")
    except Exception as e:
        print(f"Fehler beim Anzeigen der Aufgaben: {e}")

# Funktion zum Markieren von Aufgaben als erledigt
def mark_task_done():
    """
    Diese Methode ermöglicht es dem Benutzer, mehrere Aufgaben als erledigt zu markieren.
    Die entsprechenden Zeilen in der Datei werden mit einem "X" markiert.
    """
    show_tasks()
    try:
        task_numbers = input("Gib die Nummern der Aufgaben ein, um sie als erledigt zu markieren (z.B. 1,3,5): ")
        task_numbers = [int(n) for n in task_numbers.split(',')]
        with open(pfad, 'r') as file:
            tasks = file.readlines()
        for number in sorted(task_numbers, reverse=True):
            if 0 < number <= len(tasks):
                tasks[number - 1] = "X " + tasks[number - 1]
        with open(pfad, 'w') as file:
            file.writelines(tasks)
        print("Aufgaben als erledigt markiert.")
    except ValueError:
        print("Ungültige Eingabe! Gib eine gültige Zahl ein.")
    except FileNotFoundError:
        print("Keine Aufgaben gefunden.")
    except Exception as e:
        print(f"Fehler beim Markieren der Aufgaben: {e}")

# Funktion zum Löschen von Aufgaben
def delete_task():
    """
    Diese Methode ermöglicht es dem Benutzer, mehrere erledigte Aufgaben zu löschen.
    Die entsprechenden Zeilen werden aus der Datei entfernt.
    """
    show_tasks()
    try:
        task_numbers = input("Gib die Nummern der erledigten Aufgaben ein, die gelöscht werden sollen (z.B. 1,3,5): ")
        task_numbers = [int(n) for n in task_numbers.split(',')]
        with open(pfad, 'r') as file:
            tasks = file.readlines()
        for number in sorted(task_numbers, reverse=True):
            if 0 < number <= len(tasks):
                del tasks[number - 1]
            else:
                print(f"Nummer {number} ist ungültig. Bitte gib eine gültige Zahl ein.")
        with open(pfad, 'w') as file:
            file.writelines(tasks)
        print("Erledigte Aufgaben gelöscht.")
    except ValueError:
        print("Ungültige Eingabe! Gib eine gültige Zahl ein.")
    except FileNotFoundError:
        print("Keine erledigten Aufgaben gefunden.")
    except Exception as e:
        print(f"Fehler beim Löschen der erledigten Aufgaben: {e}")

# Hauptmenüfunktion
def menu():
    """
    Diese Methode zeigt das Hauptmenü der Anwendung an und verarbeitet die Benutzereingaben.
    Der Benutzer kann zwischen verschiedenen Optionen zur Verwaltung der Aufgaben wählen.
    """
    while True:
        print("\nTo-Do-Liste Menü:")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe als erledigt markieren")
        print("4. Aufgabe löschen")
        print("5. Beenden")
        
        choice = input("Wähle 1-5 aus: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Die To-Do-Liste wurde beendet.")
            break
        else:
            print("Ungültige Wahl. Gib eine Zahl zwischen 1 und 5 ein.")

# Menü direkt aufrufen
menu()