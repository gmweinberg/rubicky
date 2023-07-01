#!/usr/bin/env python

"""Cube class represents the current sate of the cube. The cube is represented as a list
   where the index indicates the position (face, y, x) and the value indicates the 'color' 0-5."""

def get_td(color, index):
    """Return td  element from the int color."""
    colors = ["red", "orange", "yellow", "dodgerblue", "springgreen", "silver", "white"]
    return '<td style="background-color:{}" width=20 height=20>{}</td>'.format(colors[color], index)


class Cube:
    def __init__(self, size=3):
        """Create a cube with the given size."""
        self.size = size
        self.squares = [0] * 6 * size * size
        for face in range(6):
            for ii in range(size):
                for iii in range(size):
                    self.squares[face * size * size + ii * size + iii] = face

    def get_ords(self, index):
        """return a tuple face, y, x from the index."""
        face = int(index / (self.size * self.size))
        y = int((index - face * self.size * self.size) / self.size)
        x = index - face * self.size * self.size - y * self.size
        return (face, y, x)

    def get_index(self, ords):
        face = ords[0]
        y = ords[1]
        x = ords[2]
        """inverse of get_ords"""
        return face * self.size * self.size + y * self.size + x

    def html_dump(self):
        """Create a crappy html page of the unfolded cube."""
        # we will make face 0 the "front", 1 - 3 looping around, 4 = right, 5 = left
        # so face 3 is at the top
        # We boldly ignore the the advice against using tables for display :-)
        page = ''
        page += '<html><head><title>A cube?</title></head>'
        page += '<table>\n'
        # show the top
        face = 3
        for ii in range(self.size):
            page += '<tr>'
            for iii in range(self.size):
                page += get_td(6, '')
            for iii in range(self.size):
                index = face * self.size * self.size + ii * self.size + iii
                color = self.squares[index]
                page +=  get_td(color, index)
            for iii in range(self.size):
                page += get_td(6, '')

        # todo show the left and right correctly
        for ii in range(self.size):
            page += '<tr>'
            face = 4
            for iii in range(self.size):
                index = face * self.size * self.size + iii * self.size + ii
                color = self.squares[index]
                page += get_td(color, index)
            face = 0
            for iii in range(self.size):
                index = ii * self.size + iii
                color = self.squares[index]
                page += get_td(color, index)
            face = 5
            for iii in range(self.size):
                index = face * self.size * self.size + self.size * (self.size - (iii + 1)) + ii
                color = self.squares[index]
                page += get_td(color, index)
            page += '</tr>\n'

        face = 1
        for ii in range(self.size):
            page += '<tr>'
            for iii in range(self.size):
                page += get_td(6, '')
            for iii in range(self.size):
                index = face * self.size * self.size + ii * self.size + iii
                color = self.squares[index]
                page +=  get_td(color, index)
            for iii in range(self.size):
                page += get_td(6, '')
        face = 2
        for ii in range(self.size):
            page += '<tr>'
            for iii in range(self.size):
                page += get_td(6, '')
            for iii in range(self.size):
                index = face * self.size * self.size + ii * self.size + iii
                color = self.squares[index]
                page +=  get_td(color, index)
            for iii in range(self.size):
                page += get_td(6, '')
        page += '</table>'
        page += ('</body></html>')
        return page

if __name__ == '__main__':
    cube = Cube(4)
    if False:
        for ii in range(6 * 9):
            ords = cube.get_ords(ii)
            print(ii, ords, cube.get_index(ords))
    with open('cube.html', 'w') as f:
        f.write(cube.html_dump())


