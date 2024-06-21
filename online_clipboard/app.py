
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes_file_path = 'notes.txt'
if not os.path.exists(notes_file_path):
    with open(notes_file_path, 'w') as f:
        f.write('')


def read_notes_from_file():
    with open(notes_file_path, 'r') as f:
        notes = f.read().split('\n')
    return [note for note in notes if note]


def write_notes_to_file(notes):
    with open(notes_file_path, 'w') as f:
        f.write('\n'.join(notes))


@app.route('/')
def index():
    notes = read_notes_from_file()
    return render_template('index.html', notes=notes)


@app.route('/add_note', methods=['POST'])
def add_note():
    new_note = request.form.get('note')
    if new_note:
        notes = read_notes_from_file()
        notes.append(new_note)
        write_notes_to_file(notes)
    return redirect('/')


@app.route('/delete_note/<int:note_index>', methods=['GET'])
def delete_note(note_index):
    notes = read_notes_from_file()
    if 0 <= note_index < len(notes):
        del notes[note_index]
        write_notes_to_file(notes)
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7040, debug=True)
