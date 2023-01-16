import datetime
import sys

# Store the next available id
last_id = 0


class Note:
    """Represent a note in the notebook. Match against a string in searches
    and store tags for each note"""
    def __init__(self, memo, tags=''):
        """Create a note containing a memo and optional space-separated tags. Automatically
        set the creation date and id of the note"""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, string):
        """Determine if the string is in the note"""
        return string in self.memo or string in self.tags


class Notebook:
    """Represent a collection of Note classes. Modify a note's memo or tags. Search for a string
    in all notes"""
    def __init__(self):
        """Initialize a notebook with an empty list"""
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list"""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Search for the note with the given id and change its memo"""
        # self.notes[note_id].memo = memo #could not work because the note indexes
        # start from 1 but the list starts from 0

        # for note in self.notes:
        #     if note.id == note_id:
        #         note.memo = memo #We did not have the _find_note method then
        #
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        """Search for the note with the given id and change its tags"""
        # self.notes[note_id].tags = tags #could not work because the note indexes
        # start from 1 but the list starts from 0

        # for note in self.notes:
        #     if note.id == note_id:
        #         note.memo = tags #We did not have the _find_note method then
        self._find_note(note_id).tags = tags

    def search(self, string):
        """Find all notes that match a given string and return a list of them"""
        # matching_notes = []
        # for note in self.notes:
        #     if note.match(string):
        #         matching_notes.append(note)
        # return matching_notes #if you don't know list comprehension
        return [note for note in self.notes if note.match(string)]

    def _find_note(self, note_id):
        """Find note with a specific id"""
        for note in self.notes:
            if note.id == note_id:
                return note
        return None


class Menu:
    """Display a menu and respond to choices when run"""
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    # noinspection PyMethodMayBeStatic
    def display_menu(self):
        """Display all menu options"""
        print("""
Notebook Menu
1. Show all notes
2. Search notes
3. Add note
4. Modify note
5. Quit
        """)

    def run(self):
        """Show the menu and respond to choices"""
        while True:
            self.display_menu()
            choice = input("Enter an option:")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("It is not a valid choice")

    def show_notes(self, notes=None):
        """Print all notes"""
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("%i: %s\n%s" % (note.id, note.tags, note.memo))

    def search_notes(self):
        """Find all notes that match a given string and return a list of them"""
        string = input("Looking for:")
        notes = self.notebook.search(string)
        self.show_notes(notes)

    def add_note(self):
        """Create a new note and add it to the list of notes in the notebook class"""
        memo = input("Enter the memo:")
        tags = input("Enter the tags:")
        self.notebook.new_note(memo, tags)

    def modify_note(self):
        """Rewrite memo and tags of a note by id. To not change an attribute, enter an empty string"""
        id = int(input("Enter a note id:"))
        memo = input("Enter a memo:")
        tags = input("Enter tags:")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        """Close the menu and leave the program"""
        print("Thank you for using your notebook today")
        sys.exit(0)


if __name__ == "__main__":
    menu = Menu()
    menu.run()

