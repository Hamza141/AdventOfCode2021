from copy import copy, deepcopy
from collections import Counter

class Grid:
    # Map of cardinal directions to (i,j) index offsets for a 2D grid.
    _GRID_DIRS = {
        'n': (-1, 0),
        's': (1, 0),
        'w': (0, -1),
        'e': (0, 1),
        'nw': (-1, -1),
        'ne': (-1, 1),
        'sw': (1, -1),
        'se': (1, 1)
    }
    
    def __init__(self, rows=None, cols=None):
        """Initialize a Grid object. Only one of rows or cols must be set.
        
        Args:
            rows - A list of rows that represent this grid.
            cols - A list of cols that represent this grid.
        """
        assert rows is not None or cols is not None
        if rows is not None:
            assert cols is None, "Only one of rows OR cols can be set."
            assert isinstance(rows, list)
            assert len(rows) > 0
            assert isinstance(rows[0], list)
            m = len(rows[0])
            self._grid = []
            for i, row in enumerate(rows):
                assert isinstance(row, list)
                assert len(row) == m
                self._grid.append(row)
        elif cols is  not None:
            assert isinstance(cols, list)
            assert len(cols) > 0
            assert isinstance(cols[0], list)
            n = len(cols[0])
            self._grid = [[] for i in range(n)]
            for col in cols:
                assert isinstance(col, list)
                assert len(col) == n
                for i, val in enumerate(col):
                    self._grid[i].append(val)
            
    @property
    def n(self):
        return len(self._grid)
        
    @property
    def m(self):
        return len(self._grid[0])

    @property
    def size(self):
        return self.n * self.m
        
    @property
    def dimensions(self):
        return (self.n, self.m)
    
    def __getitem__(self, indices):
        """
        The __getitem__ and __setitem__ functions below allow read and writing to
        the grid by indexing, rather than by using a helper function.
        
        Valid examples:
            a = grid[i][j]  # calls grid.__getitem__(i)
            b = grid[i]     # calls grid.__getitem__(i)
            c = grid[i, j]  # calls grid.__getitem__((i, j))
            grid[i][j] = a  # calls grid.__getitem__(i)
            grid[i, j] = b  # calls grid.__setitem__((i, j))
        Invalid examples:
            grid[i] = a     # __setitem__(i) is not supported
        """
        if isinstance(indices, tuple):
            assert len(indices) == 2, "Only 1 or 2 indices allowed"
            i, j = indices
            if isinstance(i, slice):
                rows = []
                for s in self._grid[i]:
                    rows.append(s[j])
                if isinstance(j, slice):
                    return Grid(rows)
                else:
                    return rows
            else:
                assert isinstance(i, int)
                return self._grid[i][j]
        elif isinstance(indices, slice):
            return Grid(self._grid[indices])
        else:
            assert isinstance(indices, int), "Index must be an int."
            return self._grid[indices]
            
    def __setitem__(self, indices, value):
        assert isinstance(indices, tuple)
        assert len(indices) == 2, "Only 2 indices allowed"
        i, j = indices
        self._grid[i][j] = value
        
    def __iter__(self):
        for row in self._grid:
            yield row

    def __reversed__(self):
        for row in reversed(self._grid):
            yield row
            
    def __contains__(self, item):
        for row in self._grid:
            if item in row:
                return True
        return False
        
    def __str__(self):
        val_length = 0
        for row in self._grid:
            for val in row:
                val_length = max(len(str(val)), val_length)
        s = ''
        for row in self._grid:
            s += ','.join([str(val).rjust(val_length) for val in row])
            s += '\n'
        return s
        
    def copy(self):
        """Returns a deepcopy of this Grid object."""
        return Grid(deepcopy(self._grid))
    
    def encode(self, val_sep=',', row_sep='\\'):
        """Encodes the grid as a string, see decode().
        
        Args:
            val_sep - Separator for the values within the row.
            row_sep - Separator for the rows within the grid.
        Returns:
            String representation of the grid.
        """
        s = row_sep.join(
                [val_sep.join(
                    [str(val) for val in row]) for row in self._grid])
        return s
    
    def decode(grid, val_sep=',', row_sep='\\', str_map=int):
        """Decodes the grid from a string, see encode() and parse().
        
        Args:
            grid    - String encoding representing a grid object.
            val_sep - Separator for the values within the row.
            row_sep - Separator for the rows within the grid.
            str_map - Function to apply on values before creating the grid.
        Returns:
            Grid object constructed from the grid string.
        """
        return Grid.parse(grid.split(row_sep), val_sep, str_map)
    
    def parse(lines, sep=None, str_map=int):
        """Parse the grid from a list of input lines.
        
        Args:
            lines   - List of rows, each row represented by a string.
            sep     - Separator for the values within the row.
            str_map - Function to apply on values before creating the grid.
        Returns:
            Grid object constructed from the row strings.
        
        Example:
            grid = Grid.parse(['a,b,c', 'd,e,f', 'g,h,i'], sep=',', str_map=str)
            print(grid._grid)
            > [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        Example:
            grid = Grid.parse(['123', '456', '789'], str_map=int)
            print(grid._grid)
            > [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        """
        grid = []
        for line in lines:
            if sep is not None and sep != '':
                line = line.split(sep)
            grid.append([str_map(val) for val in line if len(val) > 0])
        return Grid(grid)
    
    def make_grid(n, m, default):
        """Create an NxM grid with default values.
        
        Args:
            n       - Number of rows in the grid.
            m       - Number of columsn in the grid.
            default - Either a default value or a function which take (i,j) as
                      parameters and returns a value.
        Returns:
            Grid object constructed from the specified input.
        
        Example:
            print(Grid.make_grid(2, 3, default=7))
            > 7,7,7
            > 7,7,7
        Example:
            print(Grid.make_grid(3, 2, default=lambda i,j: i+j))
            > 0,1
            > 1,2
            > 2,3
        """
        val_f = default if callable(default) else (lambda i,j: default)
        grid = [[val_f(i,j) for j in range(m)] for i in range(n)]
        return Grid(grid)
    
    def add_border(self, val=0, width=1):
        """Generate a new grid with a border of specified width and value.
        
        Args:
            val   - Default value to use for the border values.
            width - Width of the border.
        Returns:
            Grid object representing this grid with a border added to it.
        
        Example:
            print(grid)
            > 1,2,3
            > 4,5,6
            > 7,8,9
            print(grid.add_border(0,1))
            > 0,0,0,0,0
            > 0,1,2,3,0
            > 0,4,5,6,0
            > 0,7,8,9,0
            > 0,0,0,0,0
        """
        new_grid = []
        for i in range((2 * width) + self.n):
            new_grid.append([val for j in range(2 * width + self.m)])
        for i in range(self.n):
            for j in range(self.m):
                new_grid[width + i][width + j] = self._grid[i][j]
        return Grid(new_grid)
            
    def get_valid_dirs():
        """Return the list of valid cardinal directions for this grid."""
        return list(Grid._GRID_DIRS.keys())
            
    def get_dir(self, i, j, dir, coords=False):
        """Get neighbor of (i, j) according to the cardinal direction specified.

        Args:
            i      - Row index of node whose neighbor we want.
            j      - Column index of node whose neighbor we want.
            dir    - One of ['n', 's', 'e', 'w', 'nw', 'ne', 'sw', 'se']
            coords - If True, will return a coordinate tuple (i', j') of the
                     neighbor and otherwise will return the neighbor's value. 
        Returns:
            Value of the neighbor of a tuple of coordinates if coords=True.
        
        Example:
            print(grid)
            > 1,2,3
            > 4,5,6
            > 7,8,9
            print(grid.get_dir_neighbor(1, 1, 'w'))
            > 4
            print(grid.get_dir_neighbor(1, 1, 'w', coords=True))
            > (1, 0)
        """
        dir = dir.lower()
        assert dir in Grid._GRID_DIRS.keys()
        
        add_i, add_j = Grid._GRID_DIRS[dir]
        new_i, new_j = i + add_i, j + add_j    
        if new_i < 0 or new_i >= self.n or new_j < 0 or new_j >= self.m:
            if coords:
                return (None, None)
            else:
                return None
        if coords:
            return (new_i, new_j)
        else:
            return self._grid[new_i][new_j]
            
    def enumerate(self, i0=0, j0=0, i1=None, j1=None):
        """Enumerates the grid with index / value tuples.

        Args:
            i0 - Row index to start the enumeration (inclusive).
            j0 - Column index to start the enumeration (inclusive).
            i1 - Row index to stop the enumeration (exclusive).
            j1 - Column index to stop the enumeration (exclusive).
        Returns:
            List of (i, j, value) tuples.
        
        Example:
            print(grid)
            > 1,2,3
            > 4,5,6
            > 7,8,9
            print(grid.enumerate(1, 1))
            > [(1, 1, 5), (1, 2, 6), (2, 1, 8), (2, 2, 9)]
        """
        if i1 is None:
            i1 = self.n
        if j1 is None:
            j1 = self.m
        vals = []
        for i, row in enumerate(self._grid[i0:i1], start=i0):
            for j, val in enumerate(row[j0:j1], start=j0):
                if i >= i0 and j >= j0 and i < i1 and j < j1:
                    vals.append((i, j, val))
        return vals
        
    def get_matches(self, matcher, coords=False):
        """Get the values matching the matcher function.

        Args:
            matcher - Function that takes in a grid value and returns a bool.
            coords  - If False, will return the count of values for which
                      matcher(val) returns True. If True, will return a list of
                      coordinate tuples for which matcher(val) returns True. 
        Returns:
            Count of matched values, or list of coordinates.
        
        Example:
            print(grid)
            > 1,2,3
            > 4,5,6
            > 7,8,9
            print(grid.get_matches(lambda v: v % 2 == 0))
            > 4
            print(grid.get_matches(lambda v: v % 2 == 0, coords=True))
            > [(0, 1), (1, 0), (1, 2), (2, 1)]
        """
        assert matcher is not None
        
        coordinates = []
        total = 0
        for (i, j, val) in self.enumerate():
            if matcher(val):
                total += 1
                if coords:
                    coordinates.append((i, j))
        if coords:
            return coordinates
        else:
            return total
            
    def map(self, mapper):
        """Apply mapper function to all grid values and return a new grid.

        Args:
            mapper - Function to apply on all grid values.
        Returns:
            New Grid with mapper function applied to all values.
        
        Example:
            print(grid)
            > 1,2,3
            > 4,5,6
            > 7,8,9
            print(grid.map(lambda v: v % 2)
            > 1,0,1
            > 0,1,0
            > 1,0,1
        """
        assert mapper is not None
        
        new_grid = self.copy()
        for i, j, val in new_grid.enumerate():
            new_grid[i][j] = mapper(val)
        return new_grid
        
    def get_counter(self, i0=0, j0=0, i1=None, j1=None):
        """Get Counter of values in the grid.

        Args:
            i0 - Row index to start the enumeration (inclusive).
            j0 - Column index to start the enumeration (inclusive).
            i1 - Row index to stop the enumeration (exclusive).
            j1 - Column index to stop the enumeration (exclusive).
        Returns:
            Counter object of values in the grid.
        """
        counts = Counter()
        for _, _, val in self.enumerate(i0, j0, i1, j1):
            counts[val] += 1
        return counts
        
    def get_counter_for_row(self, i, j0=0, j1=None):
        """Get Counter of values in row i of the grid.

        Args:
            i - Row index to get counter for.
            j0 - Column index to start the enumeration (inclusive).
            j1 - Column index to stop the enumeration (exclusive).
        Returns:
            Counter object of values in the row.
        """
        if j1 is None:
            j1 = self.m
        return Counter(self._grid[i][j0:j1])
        
    def get_counter_for_col(self, j, i0=0, i1=None):
        """Get Counter of values in col j of the grid.

        Args:
            j - Col index to get counter for.
            i0 - Row index to start the enumeration (inclusive).
            i1 - Row index to stop the enumeration (exclusive).
        Returns:
            Counter object of values in the col.
        """
        if i1 is None:
            i1 = self.n
        return Counter(self.__getitem__((slice(i0, i1, 1), j)))
        
    def most_common(self, i0=0, j0=0, i1=None, j1=None, keyf=None):
        """Get most common value in the specified range.

        Args:
            i0   - Row index to start the enumeration (inclusive).
            j0   - Column index to start the enumeration (inclusive).
            i1   - Row index to stop the enumeration (exclusive).
            j1   - Column index to stop the enumeration (exclusive).
            keyf - Key function to be used for tie breakers in .sort().
        Returns:
            Tuple of most common value and its count.
        
        Example:
            print(grid)
            > 1,2,3
            > 4,5,5
            > 7,8,9
            print(grid.most_common())
            > (5, 2)
        """
        counts = self.get_counter(i0, j0, i1, j1)
        commons = counts.most_common()
        max_vals = []
        for i, val in enumerate(commons):
            if val[1] != commons[0][1]:
                break
            max_vals.append(val)
        if len(max_vals) == 1:
            return max_vals[0]
        assert keyf is not None, "Tie breaker mustn't be None"
        max_vals.sort(key=lambda x: keyf(x[0]))
        return max_vals[0]
        
    def most_common_per_row(self, i0=0, i1=None, keyf=None):
        """Get most common value per row.

        Args:
            i0   - Row index to start the enumeration (inclusive).
            i1   - Row index to stop the enumeration (exclusive).
            keyf - Key function to be used for tie breakers in .sort().
        Returns:
            List of most common values per row.
        
        Example:
            print(grid)
            > 1,2,3,1
            > 4,5,5,5
            > 7,8,9,9
            print(grid.most_common_per_row())
            > [1, 5, 9]
        """
        if i1 is None:
            i1 = self.n
        vals = []
        for row in self._grid[i0:i1]:
            counts = Counter(row)
            commons = counts.most_common()
            max_vals = []
            for i, val in enumerate(commons):
                if val[1] != commons[0][1]:
                    break
                max_vals.append(val)
            if len(max_vals) == 1:
                vals.append(max_vals[0][0])
            else:
                assert keyf is not None, "Tie breaker mustn't be None"
                max_vals.sort(key=lambda x: keyf(x[0]))
                vals.append(max_vals[0][0])
        return vals
        
    def most_common_per_col(self, j0=0, j1=None, keyf=None):
        """Get most common value per col.

        Args:
            j0   - Column index to start the enumeration (inclusive).
            j1   - Column index to stop the enumeration (exclusive).
            keyf - Key function to be used for tie breakers in .sort().
        Returns:
            List of most common values per col.
        
        Example:
            print(grid)
            > 1,2,3,1
            > 4,5,5,5
            > 7,8,5,9
            > 4,2,5,5
            print(grid.most_common_per_col())
            > [4, 2, 5, 5]
        """
        if j1 is None:
            j1 = self.m
        vals = []
        for j in range(j0, j1):
            counts = Counter(self.__getitem__((slice(0, self.n, 1), j)))
            commons = counts.most_common()
            max_vals = []
            for i, val in enumerate(commons):
                if val[1] != commons[0][1]:
                    break
                max_vals.append(val)
            if len(max_vals) == 1:
                vals.append(max_vals[0][0])
            else:
                assert keyf is not None, "Tie breaker mustn't be None"
                max_vals.sort(key=lambda x: keyf(x[0]))
                vals.append(max_vals[0][0])
        return vals
        
    def subset_cols(self, cols=[]):
        """Create a new Grid object with just the specified columns.

        Args:
            cols - A list of column indices to include.
        Returns:
            New Grid object with only the specified cols.
        
        Example:
            print(grid)
            > 1,2,3,1
            > 4,5,5,5
            print(grid.subset_cols([1,3]))
            > 2,1
            > 5,5
        """
        new_rows = []
        for i, row in enumerate(self._grid):
            new_rows.append([self._grid[i][j] for j in cols])
        return Grid(new_rows)
        
    def subset_rows(self, rows=[]):
        """Create a new Grid object with just the specified rows.

        Args:
            rows - A list of row indices to include.
        Returns:
            New Grid object with only the specified rows.
        
        Example:
            print(grid)
            > 1,2,3
            > 4,5,5
            > 7,5,6
            print(grid.subset_rows([0,2]))
            > 1,2,3
            > 7,5,6
        """
        return Grid([self._grid[i] for i in rows])

    def get_neighbors(self, i, j, diags=True, coords=True, depth=1, include_self=False):
        """Get neighbors for a specified index within this grid. 

        Args:
            i      - Row index of node whose neighbors we want.
            j      - Column index of node whose neighbors we want.
            diags  - If True, will include diagonal neighbors.
            coords - If True, will return a list of coordinate tuples (i', j')
                     and otherwise will return a list of the nieghbors' values.
            depth  - The depth (away from the current node) we want to search
                     for neighbors.
            include_self - If True, will include the node itself in neighbors.
        Returns:
            List of coordinate tuples if coords=True, else neighbors' values.
        
        Example:
            print(grid)
            > 1,2,3
            > 4,5,6
            > 7,8,9
            print(grid.get_neighbors(0, 1))
            > [(0,0), (0,2), (1,0), (1,1), (1,2)]
            print(grid.get_neighbors(0, 1, coords=False))
            > [1, 3, 4, 5, 6]
        """
        potential_neighbors = []
        for add_i in range(0 - depth, depth + 1):
            for add_j in range(0 - depth, depth + 1):
                if not diags:
                    if add_i != 0 and add_j != 0:
                        continue
                if not include_self:
                    if (add_i, add_j) == (0, 0):
                        continue
                potential_neighbors.append((i + add_i, j + add_j))
        neighbors = []
        for (new_i, new_j) in potential_neighbors:
            if new_i >= 0 and new_i < self.n and new_j >= 0 and new_j < self.m:
                neighbors.append((new_i, new_j))
        if coords:
            return neighbors
        else:
            return [self._grid[x][y] for (x,y) in neighbors]    
            
    def flip_vertical(self):
        """Return a new grid with the ordering of rows inverted.
        
        Example:
            print(grid)
            > 1,2,3
            > 4,5,6
            > 7,8,9
            print(grid.flip_vertical())
            > 7,8,9
            > 4,5,6
            > 1,2,3
        """
        return Grid([row for row in reversed(self._grid)])
        
    def flip_horizontal(self):
        """Return a new grid with the ordering of columns inverted.
        
        Example:
            print(grid)
            > 1,2,3
            > 4,5,6
            > 7,8,9
            print(grid.flip_vertical())
            > 3,2,1
            > 6,5,4
            > 9,8,7
        """
        return Grid([list(reversed(row)) for row in self._grid])
        
    def merge(self, to_merge, merge_fn, default=None, anchor=(0,0)):
        """Get neighbors for a specified index within this grid. 

        Args:
            to_merge - Grid object to merge with this grid.
            merge_fn - Function to be applied on the two values from each grid.
                       The result will be stored in the merged cell.
            default  - Default value to use when new cells are generated
            anchor   - If the grid dimensions are not equivalent then the anchor
                       coordinates are where `to_merge` will begin being merged.
        Returns:
            Grid object representing the merged result.
        
        Example:
            print(grid1)
            > 1,1
            > 1,1
            > 1,1
            print(grid2)
            > 2,2,2
            > 2,2,2
            print(grid1.merge(grid2, merge_fn=lambda a, b: a+b, default=0))
            > 3,3,2
            > 3,3,2
            > 1,1,0
            print(grid1.merge(
                    grid2, merge_fn=lambda a, b: a+b, default=0, anchor=(2,2)))
            > 1,1,0,0,0
            > 1,1,0,0,0
            > 1,1,2,2,2
            > 0,0,2,2,2
        """
        anchor_i, anchor_j = anchor
        new_n = max(self.n, to_merge.n + anchor_i)
        new_m = max(self.m, to_merge.m + anchor_j)
        
        new_grid = Grid.make_grid(new_n, new_m, default=None)
        for i, j, _ in new_grid.enumerate():
            self_in_bounds = (i < self.n and j < self.m)
            to_merge_in_bounds = (
                    i >= anchor_i and i < anchor_i + to_merge.n
                    and j >= anchor_j and j < anchor_j + to_merge.m
                )
            if self_in_bounds:
                if to_merge_in_bounds:
                    new_grid[i][j] = merge_fn(
                        self._grid[i][j], to_merge[i - anchor_i][j - anchor_j])
                else:
                    new_grid[i][j] = self._grid[i][j]
            else:
                if to_merge_in_bounds:
                    new_grid[i][j] = to_merge[i - anchor_i][j - anchor_j]
                else:
                    assert default is not None
                    new_grid[i][j] = default
        return new_grid
        
    def concat_below(self, to_concat):
        """Append rows of `to_concat` to current grid.

        Args:
            to_concat - Grid object to append.
        Returns:
            Grid object representing the merged grids.
        
        Example:
            print(grid1)
            > 1,1
            > 1,1
            > 1,1
            print(grid2)
            > 2,2
            > 2,2
            print(grid1.concat_below(grid2))
            > 1,1
            > 1,1
            > 1,1
            > 2,2
            > 2,2
        """
        assert self.m == to_concat.m
        new_grid = deepcopy(self._grid)
        for row in to_concat:
            new_grid.append(row)
        return Grid(new_grid)
        
    def concat_right(self, to_concat):
        """Append columns of `to_concat` to current grid.

        Args:
            to_concat - Grid object to append.
        Returns:
            Grid object representing the merged grids.
        
        Example:
            print(grid1)
            > 1,1
            > 1,1
            print(grid2)
            > 2,2,2
            > 2,2,2
            print(grid1.concat_below(grid2))
            > 1,1,2,2,2
            > 1,1,2,2,2
        """
        assert self.n == to_concat.n
        new_grid = []
        for i in range(self.n):
            new_row = deepcopy(self._grid[i])
            new_row.extend(to_concat[i])
            new_grid.append(new_row)
        return Grid(new_grid)
        
    def split_vertical(self, j, include_col=True):
        """Split the grid on column j and return two grids.

        Args:
            j           - Column to split grid on.
            include_col - If True, the j column will be included as the first
                          column of the second grid. See examples below.
        Returns:
            Tuple of two grid objects representing the resulting split grids.
        
        Example:
            print(grid)
            > 1,1,2,3,3
            > 5,5,6,7,7
            grid1, grid2 = grid.split(2)
            print(grid1)
            > 1,1
            > 5,5
            print(grid2)
            > 2,3,3
            > 6,7,7
        Example:
            print(grid)
            > 1,1,2,3,3
            > 5,5,6,7,7
            grid1, grid2 = grid.split(2, include_col=False)
            print(grid1)
            > 1,1
            > 5,5
            print(grid2)
            > 3,3
            > 7,7
        """
        assert j > 0 and j < self.m
        rows1, rows2 = [], []
        for row in self._grid:
            rows1.append(row[0:j])
            if include_col:
                rows2.append(row[j:self.m])
            else:
                assert j < self.m - 1
                rows2.append(row[(j+1):self.m])
        return Grid(rows1), Grid(rows2)
        
    def split_horizontal(self, i, include_row=True):
        """Split the grid on row j and return two grids.

        Args:
            i           - Row to split grid on.
            include_row - If True, the i row will be included as the first row
                          of the second grid. See examples below.
        Returns:
            Tuple of two grid objects representing the resulting split grids.
        
        Example:
            print(grid)
            > 1,1
            > 2,2
            > 3,3
            > 4,4
            grid1, grid2 = grid.split(2)
            print(grid1)
            > 1,1
            > 2,2
            print(grid2)
            > 3,3
            > 4,4
        Example:
            print(grid)
            > 1,1
            > 2,2
            > 3,3
            > 4,4
            grid1, grid2 = grid.split(2, include_col=False)
            print(grid1)
            > 1,1
            > 2,2
            print(grid2)
            > 4,4
        """
        assert i > 0 and i < self.n
        grid1 = Grid(self._grid[0:i])
        if include_row:
            grid2 = Grid(self._grid[i:self.n])
        else:
            assert i < self.n - 1
            grid2 = Grid(self._grid[(i+1):self.n])
        return grid1, grid2
    
    def rotate(self, degrees):
        """Rotate the grid by the amount of degrees specified.

        Args:
            degrees - The amount of degrees to rotate the grid.
        Returns:
            Grid object with the applied rotation.
        
        Example:
            print(grid)
            > 1,2
            > 3,4
            print(grid.rotate(90))
            > 4,1
            > 3,2
            print(grid.rotate(180))
            > 3,4
            > 2,1
        """
        degrees = degrees % 360
        assert degrees in [0, 90, 180, 270]
        if degrees == 0:
            return self.copy()
        elif degrees == 90 or degrees == 270:
            new_grid = [[None for i in range(self.n)] for j in range(self.m)]
            if degrees == 90:
                for i,j,v in self.enumerate():
                    new_grid[j][(self.n - 1) - i] = v
            else:
                for i,j,v in self.enumerate():
                    new_grid[(self.m - 1) - j][i] = v
        else:
            new_grid = [[None for j in range(self.m)] for i in range(self.n)]
            for i,j,v in self.enumerate():
                new_grid[(self.n - 1) - i][(self.m - 1) -j] = v
        return Grid(new_grid)
    
    def transpose(self):
        """Transpose the current grid.
        
        Example:
            print(grid)
            > 1,2
            > 3,4
            print(grid.transpose())
            > 1,3
            > 2,4
        """
        return Grid(cols=self._grid)
        
    # TODO: get diagonal (w/ wrapping)    
    # TODO: split 4-way
    # TODO: push_row, pop_row, push_col, pop_col, insert row/col, delete row/col
    # TODO: flip col/row, swap row/col
        