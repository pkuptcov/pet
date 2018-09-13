from selenium.webdriver.common.by import By


class NotesControls:

    # Заметки
    notesEdit = (By.XPATH, "//textarea[@name='note']")
    notesSave = (By.XPATH, "//button[@type='submit']")