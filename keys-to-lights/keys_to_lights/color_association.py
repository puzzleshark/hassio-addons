from enum import Enum

import numpy as np

class Note(Enum):
    C = 0
    G = 1
    D = 2
    A = 3
    E = 4
    B = 5
    H = 6
    K = 7
    P = 8
    T = 9
    V = 10
    F = 11


def circ(note):

    val = np.pi*(float(note.value) / 6.0)
    return np.array([np.cos(val), np.sin(val)])

start = np.array([1.0, 1.0, 1.0]) / 3.0

c_lin = (np.array([[1.0], [0.0], [0.0]]) - start.reshape((-1, 1))) @ circ(Note.C).reshape((1, -1))
e_c_com = (circ(Note.E) @ circ(Note.C)) * circ(Note.C)
e_c_orth_com = circ(Note.E) - e_c_com
e_ket = -(c_lin @ circ(Note.E)).reshape((-1, 1)) + np.array([[0.0], [1.0], [0.0]]) - start.reshape((-1, 1))
e_bra = e_c_orth_com.reshape((1, -1)) / np.linalg.norm(e_c_orth_com) ** 2
c_e_lin = c_lin + e_ket @ e_bra


def note_to_color(note: Note):
    return (c_e_lin @ circ(note) * 0.5 + start) * 1.5

def note_to_rgb(note: Note):
    return np.round(note_to_color(note) * 255)

def note_to_rgb2(note: Note):
    val = (c_e_lin @ circ(note) + start)
    min_val = np.min(val)
    floor = val - min_val
    max_val = np.max(floor)
    ok = floor/max_val
    return np.round(ok * 255)


def circle_of_fifths(note):
    value =  7.0 * note
    while value >= 12.0:
        value -= 12.0
    return value

def mapping(v):
    return 2 ** (v/12.0)

def rev_map(a):
    value = np.log2(a) * 12.0
    while value >= 12.0:
        value -= 12.0
    return value


if __name__ == "__main__":

    for note in Note:
        print(f"{note.name} => {note_to_rgb2(note)}")

