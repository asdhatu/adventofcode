class TextGridConverter:
    def __init__(self, file_path):
        # set up the text file as a grid
        self.grid = self._convert_to_grid(file_path)
        # initiate the height and length
        self.height = len(self.grid)
        self.length = len(self.grid[0]) if self.grid else 0

    def _convert_to_grid(self, file_path):
        # attempt to read file and store grid in a list of lists
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                return [list(line.strip()) for line in lines]
        except FileNotFoundError:
            print("File not found. Please check the file path.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def display_grid_dimensions(self):
        print(f"Length: {self.length}, Height: {self.height}")

    def print_grid(self):
        for row in self.grid:
            print(''.join([str(char) if char is not None else '.' for char in row]))

    def adjacency_check(self, y, x):
        # iterate over adjacent squares and check if they contain symbols
        adj_elements = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,1),(1,0),(1,-1)]
        for adj in adj_elements:
            if self.is_symbol_at(y+adj[1],x+adj[0]):
                return True
        
    def make_snake(self, y, x, form = ''):
        # creates 'snake' with coordinate inputs if start is number
        # and returns all numbers adjacent and to the right
        # also checks if there is an adjacent symbol to any square
        ## initialize the adjacent symbol flag
        symbol_found = False
        # establish that the entry is not a number (base case)
        if not self.is_number_at( y, x):
            return form, symbol_found
        # check for adjacency and update the form and flag
        else:
            if self.adjacency_check(y,x):
                symbol_found = True
            next_form, next_flag = self.make_snake(y, x+1, form)
            form = str(self.grid[y][x]) + str(next_form)
            # update symbol based on current or next checks
            symbol_found = symbol_found or next_flag
        return form, symbol_found
            
        
    def iterate(self):
        # check the entire file for numbers with adjacent symbols
        total = 0
        x = 0
        y = 0
        # loop over all y entries
        while y < self.height:
            # reset x to 0
            x = 0
            while x < self.length:
                # loop over all x entries
                # create a snake if entry is a number
                if self.is_number_at(y,x):
                    form, symbol_found = self.make_snake(y,x)
                    if symbol_found:
                        # add snake to total sum if its number is adjacent to a symbol
                        total += int(form)
                        x += len(form)
                    else:
                        # otherwise add snake to x to avoid repeating process
                        x+= len(form)
                else:
                    # otherwise move stepwise left to right
                    x += 1
            y+=1
        return total
                
    def is_number_at(self, y, x):
        # check if coordinates are within the grid boundaries
        if 0 <= x < self.length and 0 <= y < self.height:
            # check if element is a digit
            element = self.grid[y][x]
            if  element.isdigit():
                return True
        else:
            print("Coordinates are outside the grid boundaries.")
            return False

    def is_symbol_at(self, y, x):
        # check if coordinates are within the grid boundaries
        if 0 <= x < self.length and 0 <= y < self.height:
            # check if element is a symbol that is not 'x'
            element = self.grid[y][x]
            if element is None or element.isdigit() or element == '.':
                return False
            return True
        else:
            print('woring!')
            print("Coordinates are outside the grid boundaries.")
            return False

# process to initialize the grid
example = "filepath.txt"
# initialize the class
converter = TextGridConverter(example)

# Displaying new dimensions of the grid
print(converter.iterate())
